#!/usr/bin/env python3
from __future__ import annotations

import subprocess
import tempfile
import unittest
import zipfile
from pathlib import Path

TOOL = Path(__file__).with_name("generate_review_pack.py")


def run(cmd, cwd=None, check=True):
    return subprocess.run(
        cmd,
        cwd=cwd,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=check,
    )


class ReviewPackTests(unittest.TestCase):
    def make_repo(self) -> Path:
        td = tempfile.TemporaryDirectory()
        self.addCleanup(td.cleanup)
        repo = Path(td.name)
        run(["git", "init", "-q"], cwd=repo)
        run(["git", "config", "user.email", "test@example.com"], cwd=repo)
        run(["git", "config", "user.name", "test"], cwd=repo)
        return repo

    def commit(self, repo: Path, message: str) -> str:
        run(["git", "add", "-A"], cwd=repo)
        run(["git", "commit", "-qm", message], cwd=repo)
        return run(["git", "rev-parse", "HEAD"], cwd=repo).stdout.strip()

    def test_safe_change_creates_pack(self):
        repo = self.make_repo()
        (repo / "app.py").write_text('print("hello")\n', encoding="utf-8")
        base = self.commit(repo, "init")
        (repo / "app.py").write_text('print("hello world")\n', encoding="utf-8")
        self.commit(repo, "change")

        out = repo / "pack.zip"
        p = run(
            ["python3", str(TOOL), "--repo", str(repo), "--base", base, "--output", str(out)]
        )
        self.assertEqual(p.returncode, 0)
        self.assertTrue(out.exists())

        with zipfile.ZipFile(out) as zf:
            patch = zf.read("review-pack/diff.patch").decode()
            manifest = zf.read("review-pack/MANIFEST.md").decode()
            self.assertIn('print("hello world")', patch)
            self.assertIn("app.py", manifest)
            self.assertIn("review-pack/context/changed/app.py", zf.namelist())

    def test_denied_env_is_not_present_in_patch(self):
        repo = self.make_repo()
        (repo / ".env").write_text("SAFE=1\n", encoding="utf-8")
        base = self.commit(repo, "init")
        (repo / ".env").write_text("FOO=bar\n", encoding="utf-8")
        self.commit(repo, "change")

        out = repo / "pack.zip"
        run(
            ["python3", str(TOOL), "--repo", str(repo), "--base", base, "--output", str(out)]
        )

        with zipfile.ZipFile(out) as zf:
            patch = zf.read("review-pack/diff.patch").decode()
            manifest = zf.read("review-pack/MANIFEST.md").decode()
            self.assertNotIn("FOO=bar", patch)
            self.assertNotIn("diff --git a/.env", patch)
            self.assertIn(".env", manifest)
            self.assertIn("policy-denied", manifest)

    def test_env_example_is_allowlisted(self):
        repo = self.make_repo()
        (repo / ".env.example").write_text("API_URL=https://example.invalid\n", encoding="utf-8")
        base = self.commit(repo, "init")
        (repo / ".env.example").write_text("API_URL=https://api.example.invalid\n", encoding="utf-8")
        self.commit(repo, "change")

        out = repo / "pack.zip"
        run(
            ["python3", str(TOOL), "--repo", str(repo), "--base", base, "--output", str(out)]
        )

        with zipfile.ZipFile(out) as zf:
            patch = zf.read("review-pack/diff.patch").decode()
            self.assertIn(".env.example", patch)

    def test_possible_secret_aborts(self):
        repo = self.make_repo()
        (repo / "app.py").write_text("x = 1\n", encoding="utf-8")
        base = self.commit(repo, "init")
        (repo / "app.py").write_text('api_key = "abcdefghijklmnop"\n', encoding="utf-8")
        self.commit(repo, "change")

        out = repo / "pack.zip"
        p = run(
            ["python3", str(TOOL), "--repo", str(repo), "--base", base, "--output", str(out)],
            check=False,
        )
        self.assertEqual(p.returncode, 3)
        self.assertFalse(out.exists())
        self.assertIn("possible secrets detected", p.stderr)

    def test_dirty_worktree_aborts_by_default(self):
        repo = self.make_repo()
        (repo / "app.py").write_text("x = 1\n", encoding="utf-8")
        base = self.commit(repo, "init")
        (repo / "app.py").write_text("x = 2\n", encoding="utf-8")

        out = repo / "pack.zip"
        p = run(
            ["python3", str(TOOL), "--repo", str(repo), "--base", base, "--output", str(out)],
            check=False,
        )
        self.assertEqual(p.returncode, 4)
        self.assertFalse(out.exists())
        self.assertIn("working tree is dirty", p.stderr)

    def test_allow_dirty_records_but_does_not_silently_include_worktree(self):
        repo = self.make_repo()
        (repo / "app.py").write_text("x = 1\n", encoding="utf-8")
        base = self.commit(repo, "init")
        (repo / "note.txt").write_text("unrelated local note\n", encoding="utf-8")

        out = repo / "pack.zip"
        p = run(
            [
                "python3",
                str(TOOL),
                "--repo",
                str(repo),
                "--base",
                base,
                "--output",
                str(out),
                "--allow-dirty",
            ]
        )
        self.assertEqual(p.returncode, 0)

        with zipfile.ZipFile(out) as zf:
            patch = zf.read("review-pack/diff.patch").decode()
            manifest = zf.read("review-pack/MANIFEST.md").decode()
            self.assertEqual(patch, "")
            self.assertIn("?? note.txt", manifest)


if __name__ == "__main__":
    unittest.main()
