# Review Pack Tool

此目录用于把 Codex → 独立审阅者的上下文交接尽量自动化，避免用户手工找 diff、日志、架构文档和敏感文件。

## v1 目标

生成：

```text
review-pack/
├── REVIEW.md
├── MANIFEST.md
├── diff.patch
├── context/
└── evidence/
```

并可压缩为单个 ZIP，用户只需要上传交接包。

## 安全原则

- Allowlist-first；
- Mandatory Denylist；
- Secret Scan；
- Log Redaction；
- 发现疑似 secret 时 fail closed；
- `.gitignore` 不是安全边界；
- 永不自动打包 `.env`、私钥、数据库 dump 等敏感文件。

当前 `generate_review_pack.py` 是 v1 基础工具，不应被视为专业 Secret Scanner 的替代品。Tier 3 项目应优先接入独立的 secret-scanning / CI 能力。
