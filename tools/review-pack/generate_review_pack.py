#!/usr/bin/env python3
"""Generate a small/medium cross-AI code review pack.

Safe-by-default baseline helper for Workflow v1.
It is not a replacement for a dedicated secret scanner.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

SAFE_SUFFIXES = {
    ".c", ".cc", ".conf", ".cpp", ".cs", ".css", ".go", ".gql", ".graphql",
    ".gradle", ".h", ".hpp", ".html", ".ini", ".java", ".js", ".json", ".jsx",
    ".kt", ".kts", ".lock", ".md", ".mod", ".php", ".properties", ".proto", ".py",
    ".rb", ".rs", ".scss", ".sh", ".sql", ".sum", ".swift", ".toml", ".ts", ".tsx",
    ".txt", ".xml", ".yaml", ".yml",
}

SAFE_FILENAMES = {
    ".env.example", ".env.sample", ".env.template",
    "Dockerfile", "Makefile", "Procfile",
    "Cargo.lock", "Cargo.toml", "go.mod", "go.sum",
    "package-lock.json", "pnpm-lock.yaml", "yarn.lock",
}

DENY_DIR_NAMES = {
    ".git", ".terraform", ".venv", "node_modules", "vendor",
}
DENY_EXACT_NAMES = {
    ".env", "id_rsa", "id_ed25519",
}
DENY_SUFFIXES = {
    ".dump", ".key", ".p12", ".pem", ".pfx", ".sql.gz",
}

SECRET_PATTERNS = [
    re.compile(r"AKIA[0-9A-Z]{16}"),
    re.compile(r"(?i)(api[_-]?key|secret|password|passwd|token)\s*[:=]\s*['\"]?[^\s'\"]{8,}"),
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    re.compile(r"(?i)(postgres|mysql|mongodb(?:\+srv)?)://[^\s:@]+:[^\s@]+@"),
]

MAX_CONTEXT_FILE_BYTES = 300_000
MAX_EVIDENCE_FILE_BYTES = 1_000_000
MAX_PATCH_BYTES = 1_500_000
MAX_CHANGED_FILES = 200


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
    lower_parts = {part.lower() for part in path.parts}
    if lower_parts & DENY_DIR_NAMES:
        return True

    name = path.name
    lower_name = name.lower()

    if name in SAFE_FILENAMES:
        return False

    if lower_name in DENY_EXACT_NAMES:
        return True
    if lower_name.startswith(".env."):
        return True
    return any(lower_name.endswith(suffix) for suffix in DENY_SUFFIXES)


def allowed_text_path(path: Path) -> bool:
    if denied(path):
        return False
    if path.name in SAFE_FILENAMES:
        return True
    return path.suffix.lower() in SAFE_SUFFIXES


def scan_text(label: str, text: str) -> list[str]:
    hits: list[str] = []
    for pattern in SECRET_PATTERNS:
        if pattern.search(text):
            hits.append(f"{label}: matched {pattern.pattern}")
    return hits


def safe_source(repo: Path, rel: Path) -> Path | None:
    src = (repo / rel).resolve()
    try:
        src.relative_to(repo.resolve())
    except ValueError:
        return None
    return src


def copy_context_file(
    repo: Path,
    rel: Path,
    dest: Path,
    findings: list[str],
) -> tuple[bool, str]:
    if not allowed_text_path(rel):
        return False, "policy-denied-or-not-allowlisted"

    src = safe_source(repo, rel)
    if src is None or not src.is_file():
        return False, "missing-or-deleted"
    if src.stat().st_size > MAX_CONTEXT_FILE_BYTES:
        return False, "too-large"

    try:
        text = src.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return False, "not-utf8-text"

    findings.extend(scan_text(str(rel), text))
    target = dest / rel
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text, encoding="utf-8")
    return True, "included"


def copy_evidence_file(
    repo: Path,
    rel: Path,
    dest: Path,
    findings: list[str],
) -> tuple[bool, str]:
    if denied(rel):
        return False, "policy-denied"

    src = safe_source(repo, rel)
    if src is None or not src.is_file():
        return False, "missing"
    if src.stat().st_size > MAX_EVIDENCE_FILE_BYTES:
        return False, "too-large"

    try:
        text = src.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return False, "not-utf8-text"

    findings.extend(scan_text(f"evidence:{rel}", text))
    target = dest / rel
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text, encoding="utf-8")
    return True, "included"


def copy_plain_review_file(
    repo: Path,
    rel: Path,
    target: Path,
    findings: list[str],
) -> tuple[bool, str]:
    if denied(rel):
        return False, "policy-denied"
    src = safe_source(repo, rel)
    if src is None or not src.is_file():
        return False, "missing"
    if src.stat().st_size > MAX_CONTEXT_FILE_BYTES:
        return False, "too-large"
    try:
        text = src.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return False, "not-utf8-text"
    findings.extend(scan_text(str(rel), text))
    target.write_text(text, encoding="utf-8")
    return True, "included"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=".")
    ap.add_argument("--base", required=True, help="Base commit/ref")
    ap.add_argument("--head", default="HEAD", help="Review commit/ref")
    ap.add_argument("--output", default="review-pack.zip")
    ap.add_argument("--context", action="append", default=[], help="Extra safe context file")
    ap.add_argument("--evidence", action="append", default=[], help="Evidence text file")
    ap.add_argument("--review", help="Prepared REVIEW.md source file")
    ap.add_argument("--report", help="Codex implementation report file")
    ap.add_argument(
        "--allow-dirty",
        action="store_true",
        help="Allow unrelated working-tree changes; they are recorded but not included",
    )
    ns = ap.parse_args()

    repo = Path(ns.repo).resolve()
    if not (repo / ".git").exists():
        print("ERROR: --repo must be a Git working tree", file=sys.stderr)
        return 2

    base_sha = run(repo, "rev-parse", ns.base).strip()
    head_sha = run(repo, "rev-parse", ns.head).strip()
    branch = run(repo, "branch", "--show-current").strip()
    status = run(repo, "status", "--short")

    if status and not ns.allow_dirty:
        print(
            "ERROR: working tree is dirty. This tool is commit-anchored and does not "
            "silently include worktree changes. Commit/stash task changes, or use "
            "--allow-dirty only when the remaining dirty state is known and unrelated.",
            file=sys.stderr,
        )
        return 4

    changed = [
        Path(p)
        for p in run(
            repo,
            "diff",
            "--name-only",
            "--diff-filter=ACMRTD",
            base_sha,
            head_sha,
        ).splitlines()
        if p.strip()
    ]

    if len(changed) > MAX_CHANGED_FILES:
        print(
            f"ERROR: {len(changed)} changed files exceed the small/medium pack limit "
            f"({MAX_CHANGED_FILES}). Split the review or use a PR / multi-part review.",
            file=sys.stderr,
        )
        return 5

    allowed_changed = [rel for rel in changed if allowed_text_path(rel)]
    excluded_changed = [
        (rel, "policy-denied-or-not-allowlisted")
        for rel in changed
        if rel not in allowed_changed
    ]

    patch = ""
    if allowed_changed:
        patch = run(
            repo,
            "diff",
            "--no-ext-diff",
            "--no-textconv",
            base_sha,
            head_sha,
            "--",
            *(str(rel) for rel in allowed_changed),
        )

    if len(patch.encode("utf-8")) > MAX_PATCH_BYTES:
        print(
            "ERROR: filtered patch is too large for the baseline Review Pack. "
            "Split the review, use a PR, or use a multi-part review.",
            file=sys.stderr,
        )
        return 6

    findings = scan_text("diff.patch", patch)

    with tempfile.TemporaryDirectory(prefix="review-pack-") as td:
        root = Path(td) / "review-pack"
        context_dir = root / "context"
        evidence_dir = root / "evidence"
        context_dir.mkdir(parents=True)
        evidence_dir.mkdir(parents=True)

        included: list[str] = []
        excluded: list[str] = [f"{rel} — {reason}" for rel, reason in excluded_changed]

        for rel in allowed_changed:
            ok, reason = copy_context_file(
                repo, rel, context_dir / "changed", findings
            )
            if ok:
                included.append(str(rel))
            else:
                excluded.append(f"{rel} — {reason}")

        for raw in ns.context:
            rel = Path(raw)
            ok, reason = copy_context_file(
                repo, rel, context_dir / "extra", findings
            )
            if ok:
                included.append(f"context:{rel}")
            else:
                excluded.append(f"context:{rel} — {reason}")

        for raw in ns.evidence:
            rel = Path(raw)
            ok, reason = copy_evidence_file(repo, rel, evidence_dir, findings)
            if ok:
                included.append(f"evidence:{rel}")
            else:
                excluded.append(f"evidence:{rel} — {reason}")

        if ns.review:
            rel = Path(ns.review)
            ok, reason = copy_plain_review_file(
                repo, rel, root / "REVIEW.md", findings
            )
            if ok:
                included.append(f"review:{rel}")
            else:
                print(f"ERROR: could not include review file: {reason}", file=sys.stderr)
                return 7
        else:
            (root / "REVIEW.md").write_text(
                "# Review Pack\n\n"
                "Codex must fill in: Task, Acceptance Criteria, Task Risk, "
                "Review Focus, and Known Gaps before handing this pack to a reviewer.\n",
                encoding="utf-8",
            )

        if ns.report:
            rel = Path(ns.report)
            ok, reason = copy_plain_review_file(
                repo, rel, root / "CODEX-REPORT.md", findings
            )
            if ok:
                included.append(f"report:{rel}")
            else:
                print(f"ERROR: could not include report file: {reason}", file=sys.stderr)
                return 8

        if findings:
            print(
                "ERROR: possible secrets detected; Review Pack generation aborted.",
                file=sys.stderr,
            )
            for hit in findings:
                print(f" - {hit}", file=sys.stderr)
            return 3

        (root / "diff.patch").write_text(patch, encoding="utf-8")
        (root / "MANIFEST.md").write_text(
            "# Manifest\n\n"
            f"- Branch: `{branch or '(detached)'}`\n"
            f"- Base: `{base_sha}`\n"
            f"- Head: `{head_sha}`\n"
            "- Diff scope: commit-to-commit, allowlisted text paths only\n"
            f"- Working tree short status at packaging time:\n\n```text\n{status or '(clean)'}\n```\n\n"
            "## Included\n"
            + ("\n".join(f"- `{x}`" for x in included) or "- (none)")
            + "\n\n## Excluded / Not Copied\n"
            + ("\n".join(f"- `{x}`" for x in excluded) or "- (none)")
            + "\n\n"
            "Excluded paths are intentionally visible so the reviewer can request "
            "missing context instead of assuming the pack is complete.\n",
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
