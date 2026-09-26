# AI Development Workflow

这是一个面向“主要依靠 AI 进行软件开发和二次开发”的个人开发工作流。

它解决的不是“怎么写一个更厉害的 Prompt”，而是：

- 不依赖 ChatGPT、Codex 或 Gemini 的长期记忆；
- 用 Git 保存 Repo 技术事实、代码、测试与 Evidence；
- 对长期复杂项目，可用 Notion 保存 Primary-approved 的项目 Core Rules、Current State 与 Decisions；
- 明确 ChatGPT、Codex 与 Gemini 之间的职责边界；
- 让风险、证据、审查和跨 AI / 跨 Conversation 交接成为可重复流程；
- 尽量减少零代码用户手工搬运上下文、判断技术路由和做技术裁决的负担。

当前 `main`：**v0.2.0-dev**。已发布稳定快照：**v0.1.0**。

## 使用入口

v0.2.0-dev 采用 **Owner Role First**。

新增长期 AI 对话时，Owner 先让接收方读取对应的通用 Role Bootstrap：

- [Project Manager](./roles/PROJECT-MANAGER.md)
- [Product Manager](./roles/PRODUCT-MANAGER.md)
- [Engineer](./roles/ENGINEER.md)
- [UI Designer](./roles/UI-DESIGNER.md)
- [Independent Reviewer](./roles/INDEPENDENT-REVIEWER.md)

Role 确认后停止，再由 Owner 发送 PROJECT BIND；完成项目绑定后才进入 Task / Handoff。

旧项目如果 pinned 到 v0.1.0 / 旧 Workflow Revision，不会因 `main` 更新自动迁移。

## 核心原则

```text
用户描述需求
   ↓
Primary Conversation：产品 / 架构 / 路由 / 任务拆分
   ↓
必要时 Child Conversation：在明确 Repo / Scope 内推进
   ↓
Codex 做
   ↓
Gemini 查（按风险 Gate）
   ↓
ChatGPT 裁
   ↓
Codex 修
```

同时遵循：

- GitHub Workflow 负责“AI 应该怎么工作”；Notion（启用时）负责“项目现在怎么定”；Git / Runtime / Tests 负责“技术上现在实际是什么”；
- Project Memory 是辅助，不是正式事实同步机制；
- 高风险任务必须提供更强的可验证证据；
- 跨 AI / 跨 Conversation 不存在“魔法箭头”，必须有明确上下文与 Handoff；
- 用户负责产品目标和最终上线决定，不负责底层技术争论、Conversation / Repo 路由与验证实验设计；
- Codex 的模型选择需要考虑额度与实现复杂度，因此正式 Codex Task 必须给出模型与推理强度建议。

## 文档导航

- [`START-HERE.md`](./START-HERE.md)：唯一入口与场景路由
- [`WORKFLOW.md`](./WORKFLOW.md)：正常开发循环、AI 职责、Conversation Orchestration 与验证原则
- [`PRIMARY-CONVERSATION.md`](./PRIMARY-CONVERSATION.md)：Primary 的主导职责、Re-Anchor 与 Notion 写权限
- [`CHILD-CONVERSATION.md`](./CHILD-CONVERSATION.md)：Child 的局部职责、Re-Anchor 与 Return to Primary
- [`KNOWLEDGE-MANAGEMENT.md`](./KNOWLEDGE-MANAGEMENT.md)：Notion 项目知识、项目隔离、Decision 历史与防漂移规则
- [`BOOTSTRAP.md`](./BOOTSTRAP.md)：新项目初始化、Tier 0–3 与 Conversation Topology Gate
- [`RISK-GATES.md`](./RISK-GATES.md)：任务风险、Hard Risk Triggers、审查 Gate
- [`HANDOFF.md`](./HANDOFF.md)：跨 Conversation / 跨 AI 上下文交接与 Review Pack
- [`EMERGENCY.md`](./EMERGENCY.md)：生产事故与 Hotfix Lane
- [`DOCUMENTATION.md`](./DOCUMENTATION.md)：长期项目文档边界与更新规则
- [`templates/`](./templates/)：项目文档、Conversation Handoff、Codex Task/Report、Gemini 审查模板
- [`tools/review-pack/`](./tools/review-pack/)：Review Pack 生成工具与安全规则

## 版本策略

Workflow 使用粗粒度版本：`v1`、`v2`、`v3`。

旧项目不会因为 Workflow 升级自动迁移。只有真实项目运行暴露出问题，或平台能力变化导致流程无法执行时，才进入下一版设计。
