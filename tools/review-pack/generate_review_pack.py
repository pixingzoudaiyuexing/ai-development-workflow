#!/usr/bin/env python3
"""Generate a small/medium cross-AI code review pack.

Safe-by-default baseline helper for Workflow v1.
It is NOT a replacement for a dedicated secret scanner.
"""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

SAFE_SUFFIXES = {
    ".c", ".cc", ".cpp", ".cs", ".css", ".go", ".h", ".hpp", ".html",
    ".java", ".js", ".json", ".jsx", ".kt", ".md", ".php", ".py", ".rb",
    ".rs", ".scss", ".sh", ".sql", ".swift", ".toml", ".ts", ".tsx",
    ".txt", ".xml", ".yaml", ".yml",
}

DENY_NAMES = {
    ".env", ".git", "node_modules", "id_rsa", "id_ed25519",
}
DENY_SUFFIXES = {".key", ".pem", ".p12", ".pfx", ".dump", ".sql.gz"}

SECRET_PATTERNS = [
    re.compile(r"AKIA[0-9A-Z]{16}"),
    re.compile(r"(?i)(api[_-]?key|secret|password|passwd|token)\s*[:=]\s*['\"]?[^\s'\"]{8,}"),
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    re.compile(r"(?i)(postgres|mysql|mongodb(?:\+srv)?)://[^\s:@]+:[^\s@]+@"),
]


def run(repo: Path, *args: str) -> str:
    p = subprocess.run(
        ["git", "-C", str(repo), *args],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if p.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)} failed:\n{p.stderr}")
    return p.stdout


def denied(path: Path) -> bool:
    parts = set(path.parts)
    if parts & DENY_NAMES:
        return True
    name = path.name.lower()
    if name == ".env" or name.startswith(".env."):
        return True
    return any(name.endswith(s) for s in DENY_SUFFIXES)


def scan_text(label: str, text: str) -> list[str]:
    hits = []
    for pattern in SECRET_PATTERNS:
        if pattern.search(text):
            hits.append(f"{label}: matched {pattern.pattern}")
    return hits


def copy_safe_text(repo: Path, rel: Path, dest: Path, findings: list[str]) -> bool:
    if denied(rel) or rel.suffix.lower() not in SAFE_SUFFIXES:
        return False
    src = (repo / rel).resolve()
    try:
        src.relative_to(repo.resolve())
    except ValueError:
        return False
    if not src.is_file() or src.stat().st_size > 300_000:
        return False
    try:
        text = src.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return False
    findings.extend(scan_text(str(rel), text))
    target = dest / rel
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text, encoding="utf-8")
    return True


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=".")
    ap.add_argument("--base", required=True, help="Base commit/ref")
    ap.add_argument("--head", default="HEAD", help="Review commit/ref")
    ap.add_argument("--output", default="review-pack.zip")
    ap.add_argument("--context", action="append", default=[], help="Extra safe context file")
    ap.add_argument("--evidence", action="append", default=[], help="Evidence text file")
    ns = ap.parse_args()

    repo = Path(ns.repo).resolve()
    if not (repo / ".git").exists():
        print("ERROR: --repo must be a Git working tree", file=sys.stderr)
        return 2

    base_sha = run(repo, "rev-parse", ns.base).strip()
    head_sha = run(repo, "rev-parse", ns.head).strip()
    branch = run(repo, "branch", "--show-current").strip()
    status = run(repo, "status", "--short")
    changed = [Path(p) for p in run(repo, "diff", "--name-only", base_sha, head_sha).splitlines() if p.strip()]
    patch = run(repo, "diff", "--no-ext-diff", "--binary", base_sha, head_sha)

    findings = scan_text("diff.patch", patch)

    with tempfile.TemporaryDirectory(prefix="review-pack-") as td:
        root = Path(td) / "review-pack"
        context_dir = root / "context"
        evidence_dir = root / "evidence"
        context_dir.mkdir(parents=True)
        evidence_dir.mkdir(parents=True)

        included = []
        excluded = []

        for rel in changed:
            if copy_safe_text(repo, rel, context_dir / "changed", findings):
                included.append(str(rel))
            else:
                excluded.append(str(rel))

        for raw in ns.context:
            rel = Path(raw)
            if copy_safe_text(repo, rel, context_dir / "extra", findings):
                included.append(f"context:{rel}")
            else:
                excluded.append(f"context:{rel}")

        for raw in ns.evidence:
            rel = Path(raw)
            src = (repo / rel).resolve()
            try:
                src.relative_to(repo)
            except ValueError:
                excluded.append(f"evidence:{rel}")
                continue
            if denied(rel) or not src.is_file() or src.stat().st_size > 1_000_000:
                excluded.append(f"evidence:{rel}")
                continue
            try:
                text = src.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                excluded.append(f"evidence:{rel}")
                continue
            findings.extend(scan_text(f"evidence:{rel}", text))
            target = evidence_dir / rel.name
            target.write_text(text, encoding="utf-8")
            included.append(f"evidence:{rel}")

        if findings:
            print("ERROR: possible secrets detected; review pack generation aborted.", file=sys.stderr)
            for hit in findings:
                print(f" - {hit}", file=sys.stderr)
            return 3

        (root / "diff.patch").write_text(patch, encoding="utf-8")
        (root / "REVIEW.md").write_text(
            "# Review Pack\n\n"
            "Fill in or have Codex fill in: Task, Acceptance Criteria, Task Risk, Review Focus, and Known Gaps.\n",
            encoding="utf-8",
        )
        (root / "MANIFEST.md").write_text(
            "# Manifest\n\n"
            f"- Branch: `{branch or '(detached)'}`\n"
            f"- Base: `{base_sha}`\n"
            f"- Head: `{head_sha}`\n"
            f"- Working tree short status at packaging time:\n\n```text\n{status or '(clean)'}\n```\n\n"
            "## Included\n" + "\n".join(f"- `{x}`" for x in included) +
            "\n\n## Excluded / Not Copied\n" + "\n".join(f"- `{x}`" for x in excluded) + "\n",
            encoding="utf-8",
        )

        out = Path(ns.output).resolve()
        out.parent.mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as zf:
            for p in root.rglob("*"):
                if p.is_file():
                    zf.write(p, p.relative_to(root.parent))

    print(f"Created {Path(ns.output).resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
