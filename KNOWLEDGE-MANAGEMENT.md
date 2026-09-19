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

## 10. Primary Continuity Pointer

对于启用了 Notion Project Knowledge 的长期项目，可以维护一个单页、覆盖更新、非历史化的：

```text
<Project>｜Primary Continuity
```

它是 **Recovery Index，不是新的 truth source，也不是第四套项目数据库**。

最小字段：

```text
Last Updated / Last Verified:

Active External Work:
- None
- or <Child / Codex / Gemini / deploy / migration pointer>

Pending Formal Delta:
- None
- or <ACCEPTED + Knowledge Sync: PENDING + short statement + evidence/reference pointer>

Recovery Risks:
- None
- or <dirty workspace / unknown execution / deployment / migration / UNRECONCILED HOTFIX>

Next Safe Action:

Known Gaps:
- None
- or <what remains unverified>
```

不要保存：

- 完整 Task / Report；
- 聊天 transcript；
- source code / diff / logs；
- brainstorming；
- 完整 Decision 正文；
- Git implementation 的镜像。

Pointer 只在下列事件发生实质变化时覆盖更新：

1. 派发一个可能在 Primary 之外继续运行、且接班者需要知道的 Child / Codex / production operation；
2. 出现 `ACCEPTED + Knowledge Sync: PENDING`；
3. 出现需要 successor 知道的 dirty / unknown execution / Hotfix / destructive-operation 风险；
4. 上述 active / pending / risk 状态结束或发生实质变化；
5. planned Primary succession 前。

普通讨论、普通问答、没有 continuity 影响的小任务不更新。

Pointer 只告诉 successor “去哪里检查”和“现在不能做什么”；Git / Workspace / Runtime / Tests 仍需重新验证，Pointer 不能覆盖真实 Evidence。

如果 Primary 不能直接写 Notion，沿用本文件现有规则：生成完整替换文本，用户最多执行一次复制粘贴，不要求用户总结或判断字段。

如果项目没有启用 Notion，**不要为此单独引入第二套数据库**。Emergency Succession 仍可从 Git / Runtime / task records / Handoff Evidence 做 best-effort recovery；未知执行状态按 `WORKFLOW.md` 的 Recovery Safety Gate 处理。

### PENDING successor semantics

`ACCEPTED + Knowledge Sync: PENDING` 如果被 Continuity Pointer / Return Package / Handoff 发现：

- 不能因为旧 Notion 仍是旧值就自动撤销该决定；
- successor 应先寻找 Evidence / user confirmation / Return Package；
- 能验证则恢复该 Pending Delta 并完成同步；
- 无法验证则标记 `UNVERIFIED`；
- 如果下一动作依赖它，则 STOP mutation 并继续核验；
- 无关工作可以继续。

## 11. Notion 暂时不可用

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
