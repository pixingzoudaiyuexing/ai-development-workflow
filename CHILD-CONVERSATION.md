# CHILD CONVERSATION

> Child 是 Conversation Position，不是职业角色。

Child 可以承载 Product Manager、UI Designer 或其他长期局部角色。其职责始终以 Role Mask 为准。

## 1. Initialization

新 Child：

```text
Owner → Role Bootstrap
→ 上位角色第一份完整 Handoff / Task
→ 建立 Project Context
→ Work
```

不单独执行 PROJECT BIND。

第一份 Handoff 必须提供完成当前工作所需的最小：

- Project
- Sender / Reports To
- Recipient Code（启用时）
- Scope / Domain
- Repo / relevant source
- Workflow Revision
- Goal
- Expected Return

## 2. Scope

Child 在自己的 Role + Scope 内自主工作。

如果需要改变：

- 项目方向；
- 核心产品规则；
- 另一个 Repo / Domain 的职责；
- 跨 Repo Contract；
- 已确认 Must Not；
- 未授权系统 / 资源；

则返回正确的上位角色，不自行扩大。

## 3. Context

遵守 Minimum Sufficient Context。

不因为“可能以后有用”一次加载整个 Notion / Repo / Workflow。

真实需要更多上下文时，再读取对应来源。

## 4. Return

返回上位角色时，按当前 Role 给出足够的：

- Result
- Actual Behavior / Findings
- Evidence
- Commit / Repo anchor（适用时）
- Deviations
- Blockers
- Cross-role impact
- Durable Knowledge Candidate（如有）

Owner 只负责搬运完整返回，不负责重新整理技术内容。

# END
