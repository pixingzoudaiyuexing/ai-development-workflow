#!/usr/bin/env python3
"""Generate a small/medium cross-AI code review pack.

Safe-by-default baseline helper for Workflow v1.
It is not a replacement for a dedicated secret or PII scanner.
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
    re.compile(r"gh[pousr]_[A-Za-z0-9]{30,}"),
    re.compile(r"github_pat_[A-Za-z0-9_]{30,}"),
    re.compile(r"sk-[A-Za-z0-9_-]{20,}"),
    re.compile(r"AIza[0-9A-Za-z_-]{35}"),
    re.compile(r"(?i)authorization\s*:\s*bearer\s+[A-Za-z0-9._~+/=-]{12,}"),
    re.compile(r"(?i)(api[_-]?key|secret|password|passwd|token)\s*[:=]\s*['\"]?[^\s'\"]{8,}"),
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    re.compile(r"(?i)(postgres|mysql|mongodb(?:\+srv)?)://[^\s:@]+:[^\s@]+@"),
]

MAX_CONTEXT_FILE_BYTES = 300_000
MAX_EVIDENCE_FILE_BYTES = 1_000_000
MAX_PATCH_BYTES = 1_500_000
MAX_CHANGED_FILES = 200


def git_proc(repo: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", "-C", str(repo), *args],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )


def run(repo: Path, *args: str) -> str:
    p = git_proc(repo, *args)
    if p.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)} failed:\n{p.stderr}")
    return p.stdout


def git_paths(repo: Path, *args: str) -> set[Path]:
    out = run(repo, *args, "-z")
    return {Path(item) for item in out.split("\0") if item}


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


def normalize_repo_path(repo: Path, raw: str | Path) -> Path | None:
    candidate = Path(raw)
    src = candidate if candidate.is_absolute() else repo / candidate
    try:
        resolved = src.resolve()
        rel = resolved.relative_to(repo.resolve())
    except (OSError, ValueError):
        return None
    if not rel.parts:
        return None
    return rel


def safe_source(repo: Path, rel: Path) -> Path | None:
    normalized = normalize_repo_path(repo, rel)
    if normalized is None or normalized != rel:
        return None
    src = (repo / rel).resolve()
    if src.is_symlink():
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
        return False, "missing-deleted-or-unsafe-path"
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
        return False, "missing-or-unsafe-path"
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
        return False, "missing-or-unsafe-path"
    if src.stat().st_size > MAX_CONTEXT_FILE_BYTES:
        return False, "too-large"

    try:
        text = src.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return False, "not-utf8-text"

    findings.extend(scan_text(str(rel), text))
    target.write_text(text, encoding="utf-8")
    return True, "included"


def normalized_arg_paths(repo: Path, values: list[str]) -> tuple[list[Path], list[str]]:
    good: list[Path] = []
    bad: list[str] = []
    for raw in values:
        rel = normalize_repo_path(repo, raw)
        if rel is None:
            bad.append(raw)
        else:
            good.append(rel)
    return good, bad


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=".")
    ap.add_argument("--base", required=True, help="Base commit/ref")
    ap.add_argument("--head", default="HEAD", help="Review commit/ref; must be checked out")
    ap.add_argument("--output", default="review-pack.zip")
    ap.add_argument("--context", action="append", default=[], help="Extra safe context file")
    ap.add_argument("--evidence", action="append", default=[], help="Evidence text file")
    ap.add_argument("--review", help="Prepared REVIEW.md source file")
    ap.add_argument("--report", help="Codex implementation report file")
    ap.add_argument(
        "--allow-dirty",
        action="store_true",
        help="Allow known unrelated working-tree changes; reviewed code/context must remain clean",
    )
    ns = ap.parse_args()

    repo = Path(ns.repo).resolve()
    probe = git_proc(repo, "rev-parse", "--is-inside-work-tree")
    if probe.returncode != 0 or probe.stdout.strip() != "true":
        print("ERROR: --repo must be a Git working tree", file=sys.stderr)
        return 2

    base_sha = run(repo, "rev-parse", ns.base).strip()
    head_sha = run(repo, "rev-parse", ns.head).strip()
    current_head = run(repo, "rev-parse", "HEAD").strip()
    branch = run(repo, "branch", "--show-current").strip()
    status = run(repo, "status", "--short")

    if head_sha != current_head:
        print(
            "ERROR: --head must match the currently checked-out HEAD. "
            "This keeps context files anchored to the same commit as diff.patch.",
            file=sys.stderr,
        )
        return 9

    context_paths, bad_context = normalized_arg_paths(repo, ns.context)
    evidence_paths, bad_evidence = normalized_arg_paths(repo, ns.evidence)
    if bad_context or bad_evidence:
        print(
            "ERROR: --context/--evidence paths must resolve inside the repository: "
            + ", ".join(bad_context + bad_evidence),
            file=sys.stderr,
        )
        return 11

    review_path: Path | None = None
    if ns.review:
        review_path = normalize_repo_path(repo, ns.review)
        if review_path is None:
            print("ERROR: --review must resolve inside the repository", file=sys.stderr)
            return 7

    report_path: Path | None = None
    if ns.report:
        report_path = normalize_repo_path(repo, ns.report)
        if report_path is None:
            print("ERROR: --report must resolve inside the repository", file=sys.stderr)
            return 8

    output_abs = Path(ns.output)
    if not output_abs.is_absolute():
        output_abs = (Path.cwd() / output_abs).resolve()
    else:
        output_abs = output_abs.resolve()
    output_rel = normalize_repo_path(repo, output_abs)

    changed = [
        Path(p)
        for p in run(
            repo,
            "diff",
            "--name-only",
            "--diff-filter=ACMRTD",
            "-z",
            base_sha,
            head_sha,
        ).split("\0")
        if p
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

    dirty_paths = (
        git_paths(repo, "diff", "--name-only")
        | git_paths(repo, "diff", "--cached", "--name-only")
        | git_paths(repo, "ls-files", "--others", "--exclude-standard")
    )

    intentional_artifacts = set(evidence_paths)
    if review_path is not None:
        intentional_artifacts.add(review_path)
    if report_path is not None:
        intentional_artifacts.add(report_path)
    if output_rel is not None:
        intentional_artifacts.add(output_rel)

    dirty_non_artifacts = dirty_paths - intentional_artifacts

    if dirty_non_artifacts and not ns.allow_dirty:
        print(
            "ERROR: working tree has non-artifact changes. This tool is commit-anchored "
            "and does not silently include worktree changes. Commit/stash task changes, "
            "or use --allow-dirty only when the remaining dirty state is known and unrelated.",
            file=sys.stderr,
        )
        return 4

    protected_paths = set(allowed_changed) | set(context_paths)
    overlap = dirty_non_artifacts & protected_paths
    if overlap:
        print(
            "ERROR: dirty paths overlap reviewed code/context, so the working-tree "
            "context could disagree with the commit-anchored diff: "
            + ", ".join(sorted(str(p) for p in overlap)),
            file=sys.stderr,
        )
        return 10

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

        for rel in context_paths:
            ok, reason = copy_context_file(
                repo, rel, context_dir / "extra", findings
            )
            if ok:
                included.append(f"context:{rel}")
            else:
                excluded.append(f"context:{rel} — {reason}")

        for rel in evidence_paths:
            ok, reason = copy_evidence_file(repo, rel, evidence_dir, findings)
            if ok:
                included.append(f"evidence:{rel}")
            else:
                excluded.append(f"evidence:{rel} — {reason}")

        if review_path is not None:
            ok, reason = copy_plain_review_file(
                repo, review_path, root / "REVIEW.md", findings
            )
            if ok:
                included.append(f"review:{review_path}")
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

        if report_path is not None:
            ok, reason = copy_plain_review_file(
                repo, report_path, root / "CODEX-REPORT.md", findings
            )
            if ok:
                included.append(f"report:{report_path}")
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

        out = output_abs
        out.parent.mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as zf:
            for p in root.rglob("*"):
                if p.is_file():
                    zf.write(p, p.relative_to(root.parent))

    print(f"Created {output_abs}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
