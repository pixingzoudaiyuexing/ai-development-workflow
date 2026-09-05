# CROSS-CONTEXT HANDOFF PROTOCOL

## 1. No Magic Arrows

任何 AI → AI、Conversation → Conversation 的交接都必须回答：

- 传什么；
- 谁生成；
- 什么格式；
- 从哪里取得；
- 接收方是否能访问；
- 访问不了怎么办；
- 是否包含足够但不过量的上下文；
- 是否完成脱敏；
- 如何确认交接完整；
- 结果如何返回并可追踪。

不要假设另一个 AI 或同一 Project 中的另一个对话自动拥有当前会话、本地仓库、私有 GitHub、工作树、日志、附件或工具权限。

Project Memory 可以辅助上下文恢复，但不是正式 Handoff 的替代品。

在当前个人开发流程中，Gemini 是默认独立审阅者。

## 2. Handoff Readiness Gate

交接前检查：

1. 接收方角色和目标是否明确；
2. 当前 Project / Repo / branch / base commit 是否按场景明确；
3. Task / Scope / Non-goals / Acceptance Criteria 是否明确；
4. 相关 Architecture / Decision 是否已选择；
5. 需要的 Diff / Patch / Changed Files 是否准备；
6. Evidence 与 Unverified Gaps 是否准备；
7. 跨 AI Pack 是否经过敏感信息过滤；
8. 上下文是否在接收方可处理范围内；
9. 接收方如果不能直接访问 Repo，是否已有替代材料；
10. 结果返回格式与返回位置是否明确。

Gate 的目标是防止断链，不要求每次由用户手工打勾。

## 3. Primary Conversation → Child Conversation

当 Primary Conversation 判断需要新建子对话时，必须生成用户可直接复制的 Conversation Handoff，而不是让用户自己描述技术职责。

使用 `templates/CONVERSATION-HANDOFF.template.md`，至少包含：

- Suggested Conversation Name
- Parent / Primary Conversation
- Project
- Purpose
- Repository / Domain
- Workflow Source
- Workflow Docs to Read
- Project Docs to Read
- Current Task
- Scope
- Non-goals
- Escalation Triggers
- Expected Return Package

启动消息应明确要求新对话先从 Workflow `START-HERE.md` 建立规则上下文，再按给定 Repo / 项目文档恢复事实上下文。

如果 Project / Repo 文档尚未建立，必须明确说明当前哪些事实来自 Primary Conversation Handoff、哪些仍待写入 Git；不要假装 Git 中已经存在。

### Escalation Triggers

Child Conversation 发现以下情况时应返回 Primary Conversation，而不是自行扩大决策范围：

- 需求改变产品目标、非目标或核心业务规则；
- 需要修改另一个 Repo；
- 需要改变跨 Repo Contract / API Contract；
- 需要改变核心架构或安全边界；
- 当前 Task 与 Handoff Scope 明显冲突；
- 发现一个会影响其他工作流的重要长期决定。

### Child Conversation → Primary Conversation

完成阶段性工作或触发升级时，返回包至少包含：

- 当前任务结果摘要；
- 相关 Repo / branch / commit（若发生代码变更）；
- 已验证 Evidence / 未验证项；
- 新形成或需要确认的长期决定；
- 对其他 Repo / 产品边界的影响；
- Blockers / 下一步建议。

用户只负责把结果带回主对话，不负责重新整理或技术裁决。

## 4. ChatGPT → Codex

最小 Task 包：

- Goal
- Background
- Scope
- Non-goals
- Relevant Context / 文档指针
- Acceptance Criteria + Evidence Expectations
- Task Risk
- Git / Preflight 要求
- Recommended Codex Model
- Recommended Reasoning Level
- Selection Reason
- Review / Stop Point

对于已有仓库，尽量附：

- expected repo
- expected branch（若已知）
- base commit（若已知且稳定）

如果重要决定仍只存在于聊天、尚未进入 Git，应先将其整理为当前 Task 的明确 Context，必要时在完成后按 `DOCUMENTATION.md` 沉淀。

## 5. Codex → ChatGPT

最小结果包：

- Implementation Report
- Changed Files
- Git diff summary / commit
- Tests / build / lint / typecheck 实际执行情况
- Verifiable Evidence
- Unverified Gaps
- Risk Assessment
- 是否建议独立 Review 及原因

报告中的文字判断是 Claim；命令输出、CI、runtime 结果等才是 Evidence。

## 6. Gemini Design Review Pack

Design Review 至少包含：

- 项目目标 / 非目标的相关部分；
- 当前架构相关部分；
- 相关 Decision / ADR；
- 当前 Task；
- ChatGPT 设计方案；
- 备选方案（若有）；
- 已知风险；
- 明确希望审查的问题。

不要无差别上传整个项目知识库。

## 7. Gemini Code Review Pack

至少包含：

```text
REVIEW.md
MANIFEST.md
diff.patch
context/
evidence/
```

`REVIEW.md`：Task、Acceptance、Risk、Review focus。

`MANIFEST.md`：base/review commit、changed files、included/excluded context、脱敏说明。

`diff.patch`：本任务审查差异。

`context/`：必要 Architecture / ADR / relevant source。

`evidence/`：tests、build、CI、runtime 等真实验证材料。

High Risk Code Review 优先使用明确的 **base commit → review commit** 锚点。任务改动不应只停留在未提交工作树中，否则 Review Pack 可能静默遗漏真正需要审查的变化。

一般开发允许 dirty working tree，但生成 commit-anchored Review Pack 时：

- 默认应先把本 Task 的修改形成可审查 commit；
- 如果仍存在已知且与本 Task 无关的 dirty state，可以由 Codex确认后显式允许；
- `MANIFEST.md` 必须记录打包时的 working tree state；
- 不得把“工作树是 dirty”与“Review Pack 已包含这些修改”混为一谈。

## 8. Context Selection

目标是 Minimum Sufficient Context。

Small Task：可使用一个 Markdown review dossier。

Medium Task：优先一个自动生成的 ZIP Review Pack。

Large Task：优先顺序：

1. 能安全拆分时拆为多个 Medium Review；
2. 平台支持可靠 PR Review 时使用 PR + Review Context；
3. 无法拆分时生成 Multi-Part Review Pack；
4. 单文件微观审查只能用于某个 Finding 的补充验证，不可替代整个 Large Change Review。

Relevant files 的选择应由 Codex / ChatGPT 依据 diff 与调用链完成，用户不负责手工理解依赖。

如果 changed path 因安全策略、大小或格式限制被排除，必须出现在 `MANIFEST.md` 中。Gemini 应把这种排除视为潜在缺失上下文，而不是默认认为未提供部分不存在问题。

## 9. Security / Redaction

Review Pack 使用：

```text
Allowlist + Mandatory Denylist + Secret Scan + Log Redaction
```

默认永不发送：

- `.env` / `.env.*`（允许明确作为 schema 的 `.env.example` / `.env.sample` / `.env.template`）；
- `*.pem` / `*.key` / `*.p12` / `*.pfx`；
- SSH private keys；
- database dumps；
- `.git/`；
- `node_modules/`；
- 明确的生产凭据文件；
- 无必要的大型 generated / vendor 文件。

`.gitignore` 不是 Secret Boundary。

需要说明环境变量时使用 `.env.example` 或生成脱敏 schema；不要修改真实 `.env` 后发送。

Secret Scan 失败或发现疑似凭据时，Pack 生成应 fail closed，并要求处理后重新生成。

当前 v1 helper 只提供基础 secret-pattern 检查，不应被视为专业 Secret / PII Scanner。敏感日志应在进入 Pack 前完成脱敏；Tier 3 项目优先使用独立 secret-scanning 能力。

## 10. Missing Context Declaration

Gemini 材料不足时必须允许输出：

```text
INSUFFICIENT_CONTEXT
```

或 Finding：

```text
Status: NEEDS_CONTEXT
Missing: <file / behavior / evidence>
Reason: <why it blocks reliable conclusion>
```

禁止基于未提供实现假装确定结论。

## 11. Finding Schema

推荐：

```text
Finding ID
Severity
Category
Claim
Evidence
Affected Files
Why It Matters
Recommendation
Confidence
Blocking: Yes/No
Missing Context: Yes/No
```

ChatGPT 裁决后保留 Finding ID：

```text
G-001 ACCEPTED
G-002 REJECTED
G-003 NEEDS_EVIDENCE
```

Codex Fix Task 必须携带对应 Finding ID，确保发现 → 裁决 → 修复 → 验证可追踪。

## 12. Multi-Repo Handoff

跨 Repo Task 至少记录：

- repo name
- branch
- commit anchor
- 本 Repo 的修改范围
- cross-repo contract

Review Pack 应在 MANIFEST 中明确多 Repo 边界。
