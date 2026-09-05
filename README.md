# AI Development Workflow

这是一个面向“主要依靠 AI 进行软件开发和二次开发”的个人开发工作流。

它解决的不是“怎么写一个更厉害的 Prompt”，而是：

- 不依赖 ChatGPT、Codex 或其他审阅 AI 的长期记忆；
- 用 Git 保存长期事实、项目规则和关键决策；
- 明确 ChatGPT、Codex 与独立审阅者之间的职责边界；
- 让风险、证据、审查和跨 AI 交接成为可重复流程；
- 尽量减少零代码用户手工搬运上下文和做技术裁决的负担。

当前版本：**v1**。

## 使用入口

任何新的 ChatGPT 对话或新的开发项目，都从 [`START-HERE.md`](./START-HERE.md) 开始。

推荐的新项目启动语：

> 这是一个新的开发项目。请读取这个仓库的 `START-HERE.md`，按照我的 AI 开发流程执行。现在不要写代码，也不要生成 Codex Task，先进入 Project Discovery。

## 核心原则

```text
ChatGPT 想
   ↓
Codex 做
   ↓
独立审阅者查（按风险 Gate）
   ↓
ChatGPT 裁
   ↓
Codex 修
```

同时遵循：

- Git 是长期事实锚点，但“代码正在运行”不等于“代码天然正确”；
- 高风险任务必须提供更强的可验证证据；
- 跨 AI 交接不存在“魔法箭头”，必须有明确上下文与交接包；
- 用户负责产品目标和最终上线决定，不负责底层技术争论与验证实验设计；
- Workflow 只管理真正需要管理的变量；Gemini 等独立审阅者的具体模型选择不属于本仓库职责；
- Codex 的模型选择需要考虑额度与实现复杂度，因此正式 Codex Task 必须给出模型与推理强度建议。

## 文档导航

- [`START-HERE.md`](./START-HERE.md)：唯一入口与路由
- [`WORKFLOW.md`](./WORKFLOW.md)：正常开发循环、AI 职责与验证原则
- [`BOOTSTRAP.md`](./BOOTSTRAP.md)：新项目初始化与 Tier 0–3
- [`RISK-GATES.md`](./RISK-GATES.md)：任务风险、Hard Risk Triggers、审查 Gate
- [`HANDOFF.md`](./HANDOFF.md)：跨 AI 上下文交接与 Review Pack
- [`EMERGENCY.md`](./EMERGENCY.md)：生产事故与 Hotfix Lane
- [`DOCUMENTATION.md`](./DOCUMENTATION.md)：长期项目文档边界与更新规则
- [`templates/`](./templates/)：项目文档、Codex Task/Report、独立审查模板
- [`tools/review-pack/`](./tools/review-pack/)：Review Pack 生成工具与安全规则

## 版本策略

Workflow 使用粗粒度版本：`v1`、`v2`、`v3`。

旧项目不会因为 Workflow 升级自动迁移。只有真实项目运行暴露出问题，或平台能力变化导致流程无法执行时，才进入下一版设计。
