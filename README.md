# AI Development Workflow

这是一个面向“主要依靠 AI 进行软件开发和二次开发”的个人开发工作流。

它解决的不是“怎么写一个更厉害的 Prompt”，而是：

- 不依赖 ChatGPT、Codex 或 Gemini 的长期记忆；
- 用 Git 保存长期事实、项目规则和关键决策；
- 明确 ChatGPT、Codex 与 Gemini 之间的职责边界；
- 让风险、证据、审查和跨 AI / 跨 Conversation 交接成为可重复流程；
- 尽量减少零代码用户手工搬运上下文、判断技术路由和做技术裁决的负担。

当前版本：**v1**。

## 使用入口

任何新的 ChatGPT 项目或对话，都从 [`START-HERE.md`](./START-HERE.md) 开始。

推荐的新项目启动语：

> 这是一个新的开发项目。请读取这个仓库的 `START-HERE.md`，按照我的 AI 开发流程执行。现在不要写代码，也不要生成 Codex Task，先进入 Project Discovery。我是零代码基础用户，请由你判断 Project Tier、Conversation Topology、Task Risk、Codex 模型与是否需要 Gemini Review。

新项目的初始 Project Discovery 对话默认成为 **Primary Conversation**。如果项目需要多个长期工作流或多个 Repo，由 Primary Conversation 决定是否建立 Child Conversation，并直接生成用户可复制的新对话启动消息。用户不需要自己判断“这个需求属于 API、Web 还是架构”。

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

- Git 是长期事实锚点，但“代码正在运行”不等于“代码天然正确”；
- Project Memory 是辅助，不是正式事实同步机制；
- 高风险任务必须提供更强的可验证证据；
- 跨 AI / 跨 Conversation 不存在“魔法箭头”，必须有明确上下文与 Handoff；
- 用户负责产品目标和最终上线决定，不负责底层技术争论、Conversation / Repo 路由与验证实验设计；
- Codex 的模型选择需要考虑额度与实现复杂度，因此正式 Codex Task 必须给出模型与推理强度建议。

## 文档导航

- [`START-HERE.md`](./START-HERE.md)：唯一入口与场景路由
- [`WORKFLOW.md`](./WORKFLOW.md)：正常开发循环、AI 职责、Conversation Orchestration 与验证原则
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
