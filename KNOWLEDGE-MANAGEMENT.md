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

不要复制整个 Workflow。页面顶部只需要记录当前 Workflow 来源与版本。

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

## 5. Re-Anchor：用 Notion 给长对话重新校准

Notion 不只是知识存储，也是长期对话的 Re-Anchor 点。

### Primary 必须 Re-Anchor 的时机

- 新 Primary / 接班 Primary 启动；
- 准备做重要产品或跨 Repo 架构决定；
- Child 返回后，准备安排依赖该结果的下一阶段；
- 准备正式更新 Notion；
- 长时间中断后恢复；
- 发现当前讨论与既有规则、Decision 或 Git 事实可能冲突。

Primary Re-Anchor 至少读取：

- Core Rules；
- Current State；
- relevant ACTIVE Decisions；
- relevant REJECTED / SUPERSEDED Decisions；
- 必要时再核对相关 Git / Runtime / Evidence。

### Child 必须 Re-Anchor 的时机

- 新 Child 第一次启动；
- 开始新的 Feature / 新阶段；
- 准备生成一个新的非简单 Codex Task；
- 发现需求可能改变 Repo Scope、Contract、核心架构或项目规则；
- 发现当前方案可能与 Core Rules / Decision 冲突；
- 准备 Return to Primary；
- 长时间中断后恢复；
- 出现明显漂移信号，例如重复讨论旧问题、重新提出已否定方案、开始持续讨论本 Repo 之外的职责。

Child 每次只读取 Minimum Sufficient Knowledge：

- Core Rules；
- Current State；
- 与本 Child 相关的 ACTIVE Decisions；
- 与当前问题相关的 REJECTED / SUPERSEDED Decisions。

不要因为 Re-Anchor 就读取整个 Notion 项目知识库。

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

## 7. 更新前先校准

Primary 准备写 Notion 前必须：

1. 重新读取当前 Project Root 的 Core Rules / Current State；
2. 读取与本次更新有关的 ACTIVE / REJECTED / SUPERSEDED Decisions；
3. 检查新内容是否与当前规则冲突；
4. 如有冲突，先做 Ground Truth Verification 或明确产品裁决；
5. 再更新 Notion。

这样可以防止长对话在已经漂移后把错误状态写进知识库。

## 8. Git 与 Notion 冲突

不要简单规定“Git 永远高于 Notion”或“Notion 永远高于 Git”。

先判断冲突是什么：

- 实现是否偏离了已批准的项目规则；
- Notion 是否过期；
- Git 文档是否过期；
- 产品要求是否真的改变；
- Runtime 是否与 Repo 不一致。

然后进入 `WORKFLOW.md` 的 Ground Truth Verification，修正真正错误或过期的一方。

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

把 `Knowledge Update Candidate` 保留在 Return Package / Handoff 中。Primary 在后续依赖这些新知识继续编排前，应优先完成同步或把 Pending Candidate 明确带入下一次 Handoff。
