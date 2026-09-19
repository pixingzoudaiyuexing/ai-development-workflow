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

**应急接班例外**：旧 Primary 已无法回复时，不要求其先生成 Handoff；由新的 Primary 按本文件的 **Emergency Succession** 从可访问证据反向恢复。此例外不解除恢复核验、User Relay Rule 或后续正常交接要求。

### User Relay Rule — 用户只负责搬运，不负责编辑

当 **ChatGPT** 要求用户把内容转发给另一个 ChatGPT Conversation、Codex 或 Gemini 时，必须输出一个**独立、完整、可一键复制的最终 Transfer Block**。

核心规则：

1. **一个转发动作，只给一个最终可发送块。** 需要用户转发的全部内容必须放在同一个 fenced code block 中；代码块外的解释默认只给用户看，不需要转发。
2. **用户不负责挑选、拼接、删减或补写技术内容。** 禁止使用“把上面几段发过去”“再补发这一句”“把第 2、4、6 点一起复制”等要求。
3. **Transfer Block 必须自包含。** 假设接收方完全看不到发送方当前对话；所有必要的 Project、Role、Workflow Revision、Repo / branch / commit、Task、Scope、Non-goals、Decision、Evidence、Stop / Escalation 条件、Expected Return 等，由 ChatGPT 按场景补齐。
4. **有补充或修正时，重新生成完整新版。** 如果旧版尚未发送，必须明确写“上一版作废，请只发送下面完整新版”；不得让用户手工把增量拼进旧版。
5. **给用户看的解释与给接收方的消息必须明显分离。** ChatGPT 应在 Transfer Block 前明确写“下面整块直接发送给 <目标>，不要修改”；用户应能仅凭这一标记判断需要搬运的边界。
6. **用户是 Relay Transport，不是 Relay Editor。** 任何因为转发完整性而需要技术判断的工作，都属于 ChatGPT 的职责。

适用范围重点包括：

- Primary → Child；
- Child → Primary；
- Primary / Child → Codex；
- Primary / Child → Gemini；
- Primary → 已存在 Child 的 Update Handoff；
- 其他任何由 ChatGPT 要求用户人工搬运的任务包或上下文。

本规则**不要求** Codex / Gemini 的返回消息额外拆成 Transfer Block；当用户可以直接“复制整条返回”带回 ChatGPT 时，保持完整原始返回即可。

## 2. Handoff Readiness Gate

交接前检查：

1. 接收方角色和目标是否明确；
2. 当前 Workflow Version + **Workflow Revision（具体 commit SHA）**、Project / Repo / branch / base commit 是否按场景明确；
3. Task / Scope / Non-goals / Acceptance Criteria 是否明确；
4. 相关 Architecture / Decision 是否已选择；
5. 需要的 Diff / Patch / Changed Files 是否准备；
6. Evidence 与 Unverified Gaps 是否准备；
7. 跨 AI Pack 是否经过敏感信息过滤；
8. 上下文是否在接收方可处理范围内；
9. 接收方如果不能直接访问 Repo，是否已有替代材料；
10. 结果返回格式与返回位置是否明确；
11. 项目启用 Notion 时，Current Project / Project Root / Required Knowledge / Re-Anchor Scope 是否明确。

Gate 的目标是防止断链，不要求每次由用户手工打勾。

如果本次交接需要用户人工转发，Gate 还必须确认：ChatGPT 已按 **User Relay Rule** 输出单一、完整、自包含的一键复制 Transfer Block。

## 3. Primary Conversation → Child Conversation

当 Primary Conversation 判断需要新建子对话时，必须生成用户可直接复制的 Conversation Handoff，而不是让用户自己描述技术职责。

使用 `templates/CONVERSATION-HANDOFF.template.md`，至少包含：

- Suggested Conversation Name
- Parent / Primary Conversation
- Project
- Purpose
- Repository / Domain
- Workflow Source + Workflow Version + exact Workflow Revision
- Workflow Docs to Read
- Project Docs to Read
- Project Knowledge Root（如启用 Notion）
- Notion Knowledge to Read（如启用）
- Re-Anchor Scope / Triggers
- Context Budget / Do Not Preload
- Current Task
- Scope
- Non-goals
- Escalation Triggers
- Expected Return Package

启动消息应明确要求新对话先从 Workflow `START-HERE.md` 建立规则上下文，再按给定 Repo / 项目文档恢复事实上下文。

如果 Project / Repo 文档尚未建立，必须明确说明当前哪些事实来自 Primary Conversation Handoff、哪些仍待写入 Git；不要假装 Git 中已经存在。

项目启用 Notion 时，Handoff 必须绑定明确的 Current Project 与 Notion Project Root；隔离和写权限按 `KNOWLEDGE-MANAGEMENT.md` 执行。

### Context Truncation

Conversation Handoff 遵循 **Minimum Sufficient Context**：

- Primary 只指定当前 Child 真正需要读取的 Workflow / 项目文档；
- 不要因为“以后可能有用”而预加载整个项目知识库；
- 对明显无关的领域或文档，Primary 应在 Handoff 中明确写入 `Do Not Preload`；
- 如果 Child 后续缺少关键上下文，应请求具体文件 / Contract / Evidence，而不是自动扩大到全项目读取。

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
- 本次更新或影响到的 Git 核心文档列表（没有则写 None）；
- 新形成或需要确认的长期决定；
- 对其他 Repo / 产品边界的影响；
- Blockers / 下一步建议；
- Knowledge Update Candidate：`NONE` 或 `PROPOSED`，如为 PROPOSED 列出需要 Primary 检查的 Core Rule / State / Decision / Superseded 信息。

用户只负责把结果带回主对话，不负责重新整理或技术裁决。

Primary 收到返回包后，如果下一步任务依赖该 Child 的真实实现、架构、Contract 或长期文档变化，必须先执行 Re-Sync：读取返回的 commit anchor 和受影响 Git 文档，再进行下一次 Task 编排。

项目启用 Notion 且 Knowledge Update Candidate = PROPOSED 时，Primary 在正式写入前必须先按 `KNOWLEDGE-MANAGEMENT.md` 执行 Re-Anchor，再做 ACCEPT / REJECT / NEEDS_EVIDENCE。

如果 Primary 无法直接访问对应 Repo，不得要求零代码用户手工寻找 diff / 文档；应让 Child / Codex 输出精确文件内容、diff 或结构化返回包。

### Primary → 已存在 Child 的 Update Handoff

当 Primary 批准了会影响已经存在 Child 的 shared Contract、Core Rule、project-level Decision 或 Scope 变化时，不允许假设对方会自动知道。

Primary 生成最小 Update Handoff：

```text
Project:
Affected Child:
Workflow Revision:
What Changed:
Relevant Decision / Core Rule:
Git / Contract Anchor:
Required Re-Anchor:
Required Re-Sync:
Before Continuing Related Work:
```

只发送给真正受影响的 Active Child。接收方在继续相关工作前完成 Re-Anchor / Re-Sync；无关 Child 不机械刷新。

## 3.1 Primary → New Primary（正常换届）

由旧 Primary 在安全停止点生成**一个完整、自包含的一键复制块**，用户只需原样发送给新的 Primary，不负责重新整理历史。

内容至少包含：Project / Current Project Root、Workflow Source + Version + pinned Revision、产品目标与相关正式决定的定位指针、Current State 的定位和新旧核验时间、受影响 Repo / branch / last known commit（明确只是锚点）、Active Child / Codex / Gemini / CI / production work 的位置与已知执行状态、Pending Formal Delta（ACCEPTED + Knowledge Sync: PENDING）及证据位置、存在的 dirty / Hotfix / destructive-operation 风险、已验证事项、缺失或冲突事项、下一步安全动作与禁止重复执行项。

旧 Primary 在交接前只做能够安全完成的状态收尾；存在正在运行的外部任务时如实登记，不自行重派、取消或声称已经完成。新 Primary 按 `PRIMARY-CONVERSATION.md` 初始化，并按 `WORKFLOW.md` 的 Recovery Safety Gate 核验后再派新任务。不能把旧 Handoff 中的 last known commit 直接当成最新技术事实。

## 3.2 Emergency Succession — Old Primary Unavailable

当旧 Primary 因平台限制或其他原因无法继续回复、无法生成最终 Handoff 时，用户可直接开启新 Primary 并说明“旧 Primary 无法回复，请执行 Emergency Succession”。**不得要求用户先返回无法使用的旧 Primary 取得 Handoff**。

新 Primary 的恢复顺序：

1. 确认 Project 身份及其已固定的 Workflow Version + Revision；若未知，从现有 Project Knowledge、Repo `AGENTS.md` 或可访问的 Handoff 查找，仍未知则标记待核实，不得默认按最新 `main` 覆盖既有项目规则。
2. 先暂停涉及受影响范围的新写入 / 部署 / 迁移；继续安全的只读恢复与核验。已有救火工作依 `EMERGENCY.md` 处理，不因为换对话自动结束 Hotfix。
3. 如启用且可访问，读取当前 Project Root 内的 Core Rules、Current State、相关 Decisions，以及最新的 Continuity Pointer（若存在）。Pointer 只用作查找线索，不作为已核验事实。
4. 从可直接访问的 Child / Codex / Gemini / PR / CI / workspace / runtime 等记录盘点活跃、已完成及**执行状态 UNKNOWN**的外部任务。**Git 无改动并不证明没有正在运行的任务**；远端 Git 不代表本地 working tree 或生产状态。
5. 对相关 Repo 核验 branch、HEAD、未提交修改和已有 Evidence；如需 Codex 协助，只派**只读 Recovery Preflight**，明确禁止修改文件、取消或重跑旧任务、reset、checkout 覆盖工作树、部署、迁移及其他外部副作用。若原 Codex 任务可能仍在同一 workspace 运行，应先查原任务状态，不能派第二个会干扰它的任务。
6. 将恢复材料逐项标为 `VERIFIED / UNVERIFIED / MISSING / CONFLICTING`（仅供本次恢复，不是永久状态机）。标明来源、时间 / commit 锚点和影响；按现有 Ground Truth Verification 处理冲突。注意已 ACCEPTED 但 PENDING 的决定可能不在旧 Notion 中：如找到线索，核验原用户确认、Return Package 或其他证据并同步；无法核实时不能自行撤销或重新裁决用户原有产品意图，后续依赖它的修改须暂停并请用户确认产品意图。
7. 只有关键材料无法直接访问时，才请用户**原样搬运具体一份已存在的完整消息或文件**；不得要求用户判断哪条 Commit 正确、哪个 Task 要重跑、哪个工作树可覆盖。
8. 进入 `WORKFLOW.md` 的 Recovery Safety Gate。执行状态不明时：**STOP mutation, continue verification**。受影响范围安全核验完成后，建立新的 Primary 并从现有进度继续；不重做已完成工作、不机械重建所有 Child。

即使缺少旧 Handoff、Notion 或 Continuity Pointer，也允许**启动只读恢复**；不能把缺失信息脑补为 None。实际无法找回且会影响下一步执行的事实，必须明确告知恢复缺口和当前安全边界，不得承诺百分之百无损接班。

## 4. ChatGPT → Codex

### Codex Runtime Banner

当 ChatGPT 要求用户把 Task 发送给 Codex 时，除了按 **User Relay Rule** 给出完整一键复制 Task Block，还必须在代码块**之前**单独告诉用户本次建议使用：

```text
Codex Model: Luna | Terra | Sol
Reasoning: Light（轻量） | Medium（中） | High（高）
Why: <一句话说明为什么这个档位足够>
```

这个 Banner 是给用户选择 Codex 运行档位看的，不要求用户自己根据技术内容判断模型。

默认采用 **Smallest Sufficient Runtime**：在能够可靠完成当前任务的前提下，优先选择更低的模型 / Reasoning 档位以节省额度；不要因为 Task Risk 高就机械使用 Sol / High，也不要为了省额度把明显高复杂度任务压到不足的档位。

同一份 Codex Task Block 内仍必须保留 Recommended Model / Recommended Reasoning / Selection Reason，确保任务本身也能独立理解推荐运行档位。

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

**Codex 是 Review Pack 的唯一默认生成责任方。**

当 ChatGPT 判定需要 Gemini Code Review 时，应先把“生成 Review Pack”作为当前 Codex Task 的 Stop Point / Handoff 要求，或单独生成一个 Review Pack Generation Task。Codex 负责：

- 运行 `tools/review-pack/` 工具；
- 生成 `diff.patch`；
- 收集允许进入 Pack 的测试 / build / CI / runtime Evidence；
- 执行既定脱敏与 Secret Scan；
- 输出最终 ZIP 或结构化 Markdown fallback。

用户只负责把最终产物交给 Gemini；不得要求零代码用户自己制作 patch、提取 exit code、整理 raw logs 或拼装 Review Pack。

如果 Codex 所在环境无法生成 Pack，应明确报告阻塞点并采用 `HANDOFF.md` 定义的 fallback，而不是把技术整理工作转嫁给用户。

Review Pack 至少包含：

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
