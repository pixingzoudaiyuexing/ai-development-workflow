# KNOWLEDGE MANAGEMENT

目标：解决长期项目中的对话过长、换新对话后的状态偏差、核心定位漂移，以及已经否定的方案被重新引入。

本文件定义 Notion 在 Workflow 中的最小职责。它不是聊天全文归档，也不是 Git 的替代品。

## 1. 三层职责

```text
GitHub Workflow
= AI 应该怎么工作、Primary / Child 各自有什么职责

Notion
= 当前项目现在是怎么定的

Git / Runtime / Tests
= 代码现在实际上是什么样、验证结果是什么
```

Chat / Project Memory 只用于讨论和辅助上下文，不作为长期项目事实的唯一来源。

## 2. Notion 最小内容

长期复杂项目的 Project Root 至少建议维护：

```text
<Project>｜Core Rules
<Project>｜Current State
<Project>｜Decisions
```

### Core Rules

只记录以后新对话不能忘记的项目级原则，例如：

- 项目到底解决什么问题；
- 每个 Repo / 组件负责什么；
- 明确的职责边界和禁止事项；
- 不应随着普通实现任务随意改变的核心定位。

不要复制整个 Workflow。页面顶部只需要记录当前 Workflow Source、Workflow Version 与 **Workflow Revision（具体 commit SHA）**。项目默认固定到该 Revision；除非 Primary 明确执行升级，不把 `main` 的后续变化静默当作当前项目规则。

### Current State

保持短，只记录：

- Current Phase；
- 当前主要目标；
- 重要 Repo / Feature 当前状态；
- Blockers；
- Next Step；
- Last Updated / Last Verified。

它不是日报。

### Decisions

只记录已经正式裁决、以后可能被重新讨论的重要决定。

最小状态：

- `ACTIVE`：当前有效；
- `REJECTED`：讨论过并明确否定；
- `SUPERSEDED`：曾经有效，但已经被新决定替代。

`SUPERSEDED` 必须指出替代它的新 Decision。不要删除旧决定，否则未来 AI 可能把旧方案重新当成新方案提出。

## 3. Project Knowledge Isolation

一个 Notion 账号可以包含很多项目，但每个项目必须有独立 Project Root。

任何 Primary / Child 都必须知道：

```text
Current Project: <project>
Notion Project Root: <project root>
```

默认规则：

- 只在当前 Project Root 内读取和搜索项目知识；
- 不把 workspace-wide 搜索结果直接当作当前项目事实；
- 不因页面名称相似就跨项目引用；
- Archived Project 默认不读取；
- 跨项目知识只有在 Primary 明确声明 Cross-Project Context 时才允许引入，并必须保留来源。

## 4. 写权限

项目级 Notion 的正式写入权属于 Primary Conversation。

```text
Primary
= Read + Approve + Write

Child
= Read + Propose

Codex
= Propose through Report / Evidence

Gemini
= Propose through Findings / Review
```

Child、Codex、Gemini 不得自行把建议宣布成项目级新事实。

它们通过 `Knowledge Update Candidate` 把可能需要长期保存的变化交给 Primary。Primary 负责接受、拒绝或要求进一步验证。

Primary 能直接写 Notion 时，完成校准后直接写入；如果当前环境不能直接写，不得只说“请更新 Notion”，而应生成：

- 要更新的具体页面；
- 完整可复制 / 可替换文本；
- 必须保留的旧内容或 pointer；
- 更新完成后应看到的目标状态。

用户只负责执行最小复制粘贴，不负责重新总结或决定写什么。

## 4.1 Primary Continuity Pointer（接班索引，不是项目事实库）

对已启用 Notion 且可写的长期项目，Primary 可以在**同一个 Project Root** 下维护一份可覆盖更新的 `<Project>｜Primary Continuity` 短页。它只回答“接班时先去哪里核查、哪些执行风险尚未解除”，**不取代** Core Rules / Current State / Decisions，也不镜像 Git / runtime 事实。

最小内容：

```text
Last Updated / Last Verified:
Active External Work: None / Child、Codex、Gemini、CI 或生产操作的任务位置和已知状态
Pending Formal Delta: None / ACCEPTED + Knowledge Sync: PENDING 的简述与原始证据指针
Recovery Risks: None / 已知 dirty workspace、运行中或未知的部署 / 迁移、UNRECONCILED HOTFIX
Next Safe Action:
Known Gaps:
```

仅在外部任务已派发且可能继续独立运行、已 ACCEPTED 的重要知识仍 PENDING、出现影响接班的执行风险，或这些项目的状态发生实质变化时刷新。**不是每轮聊天、每个普通 Task 或每日备份**；只覆盖最新内容，不存全文 Task、聊天、Git diff、日志或完整报告。Pointer 的“None”必须来自已知事实，无法确认时写 Unknown，绝不能猜成 None。

Primary 有直接写入权限时自行更新；没有直接写入权限时，沿用本文件原有的“完整替换文本 + 最小粘贴”机制，但**不得**把每次普通工作中的人工更新变成项目运行的硬性前置条件。若无法将 Pointer 实际写入，明确记为 unavailable / stale，不得宣称已持久化；继续使用现有可访问的 Git、项目文档、任务记录及 Handoff。任何执行状态不明的范围均遵循 `WORKFLOW.md` 的 Recovery Safety Gate。

Pointer 只是可能过时的发现线索：新 Primary 必须重新核验活跃任务、本地工作树、远端 Git、运行环境和正式决定；Pointer 不具备覆盖这些来源的权威。未启用 Notion 的项目不强制新建 Notion 或额外状态数据库；其应急恢复可以少量缺失且必须如实声明。

`ACCEPTED + PENDING` 的原始决定不因旧 Primary 丢失而自动作废。新 Primary 找到相关指针时应核验原始用户确认 / Return Package；未能核实而后续工作依赖它时，暂停相关变更并向用户重新确认产品意图，不得擅自把旧 Notion 内容当成已否定该决定。

## 5. Re-Anchor：用 Notion 给长对话重新校准

Notion 不只是知识存储，也是长期对话的 Re-Anchor 点。

Re-Anchor 采用**事件触发**，不是按消息数量、时间间隔或 token 数量机械触发。

角色触发规则只在两个文件中维护：

- Primary：`PRIMARY-CONVERSATION.md` 的 **Primary Re-Anchor**；
- Child：`CHILD-CONVERSATION.md` 的 **Child Re-Anchor**。

本文件不重复维护两套 Trigger，避免 Workflow 自身出现规则漂移。

每次 Re-Anchor 都遵循 **Minimum Sufficient Knowledge**：只读取当前角色与当前问题需要的 Core Rules、Current State 和相关 Decisions，不因为 Re-Anchor 就加载整个 Notion 项目知识库。

Re-Anchor 是保护，不是无限延长旧对话的理由。如果同一问题已经出现多个互相矛盾的历史、对话经历多次重大方向变化，或 Re-Anchor 后行为仍与当前规则不一致，应优先使用**新 Conversation + 完整 Handoff**，而不是在旧对话中反复 Re-Anchor。具体角色判断见 `PRIMARY-CONVERSATION.md` / `CHILD-CONVERSATION.md`。

## 6. Knowledge Update Candidate

正式 Child / Codex Return Package 应回答：

```markdown
## Knowledge Update Candidate

Status: NONE | PROPOSED

### Core Rule / State Changes
- ...

### Decisions
- ...

### Superseded / Rejected Information
- ...

### Durable Risks / Limitations
- ...
```

普通 Bug、CSS 微调、无长期影响的小改动通常应为：

```text
Status: NONE
```

只有“以后新的 Primary / Child 必须知道”的变化才值得进入 Notion。

最简单的判断方法：

> 假设半年后换成一个全新的 Primary / Child，如果它不知道这件事，会不会因此做错产品、架构、Repo 职责或长期边界判断？

- 会 → `PROPOSED`
- 不会 → `NONE`

因此普通 Bug、CSS 微调、局部重构、一次性调试过程通常都应为 `NONE`。

Primary 对 `PROPOSED` 的裁决与同步状态分开记录：

```text
Primary Decision:
ACCEPTED | REJECTED | NEEDS_EVIDENCE

Knowledge Sync:
SYNCED | PENDING        # 仅 ACCEPTED 时需要
```

`ACCEPTED` 表示“这个长期知识变化成立”；`SYNCED` 才表示“它已经真正进入 Project Knowledge”。两者不得混为一谈。

## 7. 更新前先校准

Primary 准备写 Notion 前必须：

1. 重新读取当前 Project Root 的 Core Rules / Current State；
2. 读取与本次更新有关的 ACTIVE / REJECTED / SUPERSEDED Decisions；
3. 检查新内容是否与当前规则冲突；
4. 如有冲突，先做 Ground Truth Verification 或明确产品裁决；
5. 检查 Current State 的 `Last Updated / Last Verified` 是否明显落后于已知的最近长期裁决；如明显过时，先提示并核实；
6. 再更新 Notion，并更新相应的 `Last Updated / Last Verified`。

这样可以防止长对话在已经漂移后把错误状态写进知识库，也能被动发现“Primary 已经裁决，但知识库实际没有更新”的情况。

## 8. Git 与 Notion 冲突

Notion 与 Git / Runtime / Tests 出现冲突时，不自动相信任何一方。

统一进入 `WORKFLOW.md` 的 **Ground Truth Verification**；该节是冲突处理的 canonical 规则，本文件不再重复另一套流程。

简单记忆：

```text
Notion 记：我们现在决定怎么做。
Git 记：现在实际上做成什么样。
冲突时：先核实，不猜。
```

## 9. 不进入 Notion 的内容

默认不要同步：

- 完整 ChatGPT / Codex / Gemini 对话；
- AI 中间推理；
- brainstorming 和尚未裁决的猜测；
- 完整 terminal output；
- 完整 CI logs；
- 大段 source code / diff；
- 普通 Code Review nit；
- 无长期价值的失败尝试；
- 每次 commit 的流水账。

Notion 保存的是当前规则、当前状态、正式决定和必要的历史替代关系，而不是所有过程。

## 10. Notion 暂时不可用

Notion 不可用不能阻塞安全的技术完成、Hotfix 或必要发布。

如果本次确实产生了必须同步的长期知识：

```text
Technical work: complete
Knowledge Sync: PENDING
```

把 `Knowledge Update Candidate` 保留在 Return Package / Handoff 中，并明确 `Knowledge Sync: PENDING`。

- 与该 Pending 事实无关的工作可以继续；
- 任何设计、路由或后续 Task 如果依赖该事实，在继续前必须先完成同步，或由 Primary 显式重新验证并把完整事实带入 Handoff；
- 不允许多个依赖同一 Pending 事实的任务继续滚动，把“暂缓同步”变成永久丢失状态。
