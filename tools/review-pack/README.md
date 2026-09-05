# Review Pack Tool

此目录用于把 Codex → Gemini / 独立审阅者的上下文交接尽量自动化，避免用户手工找 diff、日志、架构文档和敏感文件。

## v1 目标

生成：

```text
review-pack/
├── REVIEW.md
├── MANIFEST.md
├── diff.patch
├── CODEX-REPORT.md      # 可选
├── context/
└── evidence/
```

并压缩为单个 ZIP，用户只需要上传交接包。

## 重要边界

当前工具是 **commit-to-commit** 的 small/medium Review Pack 生成器。

需要独立 Code Review 的任务，应优先形成清晰的 base commit / review commit 锚点，再生成 Review Pack。

为了保证 `diff.patch` 与 `context/changed/` 指向同一份代码：

- `--head` 必须等于当前实际 checkout 的 `HEAD`；
- 支持普通 Git clone 和 linked worktree；
- Reviewed code / `--context` 不能存在未提交覆盖；
- `--allow-dirty` 只允许已知、与审查代码和 context 无关的工作树修改；
- `--review`、`--report`、`--evidence` 和输出 ZIP 属于显式 Review Artifact，可以保持未提交，不要求为了生成 Pack 把这些临时文件提交进项目 Git。

工具不会静默把未提交源码修改混进 commit diff。所有工作树状态仍记录到 `MANIFEST.md`，供审阅者判断上下文完整性。

## 安全原则

- Allowlist-first；
- Mandatory Denylist；
- Secret Scan；
- 敏感日志应在进入 Pack 前脱敏；
- 发现疑似 secret 时 fail closed；
- `.gitignore` 不是安全边界；
- 永不自动打包 `.env`、私钥、数据库 dump 等敏感文件；
- 被排除的 changed path 仍会写进 `MANIFEST.md`，让审阅者知道上下文可能不完整。

当前 `generate_review_pack.py` 是 v1 基础工具，不应被视为专业 Secret Scanner 或 PII Scanner 的替代品。Tier 3 项目应优先接入独立的 secret-scanning / CI 能力。

## 基本使用

```bash
python3 tools/review-pack/generate_review_pack.py \
  --repo . \
  --base <BASE_COMMIT> \
  --head <REVIEW_COMMIT> \
  --review path/to/review.md \
  --report path/to/codex-report.md \
  --context docs/ARCHITECTURE.md \
  --evidence path/to/test-output.txt \
  --output review-pack.zip
```

`--context` 和 `--evidence` 可以重复使用。

如果 Pack 太大或变更范围超过工具基线限制，应按照 `HANDOFF.md`：优先拆分 Medium Review、使用可靠 PR Review，或生成 Multi-Part Review Pack，而不是只审一个孤立文件。

## 验证

仓库中的：

```bash
python3 tools/review-pack/test_generate_review_pack.py
```

覆盖基础安全与上下文完整性行为，包括：

- 普通文本变更可生成 Pack；
- `.env` 不进入 patch；
- `.env.example` 可作为安全 schema 示例；
- 疑似 secret 时 fail closed；
- 普通 dirty source 默认阻断；
- 显式允许 unrelated dirty 时记录但不混入 commit diff；
- dirty source 与 reviewed code/context 重叠时仍强制阻断；
- 临时 REVIEW / REPORT / evidence 文件无需提交即可打包；
- `--head` 与实际 checkout 不一致时阻断；
- linked Git worktree 可正常生成 Pack。
