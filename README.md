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

v0.2.0-dev 不再把所有任务固定成同一条流水线。默认采用：

```text
Owner / Project Direction
        ↓
Project Manager / Product Manager
        ↓
Research-assisted analysis（需要时）
        ↓
Engineer：一个 Coherent Work Unit
        ↓
Research → Implement → Embedded Review → Validate → Evidence
        ↓
上游验收
        ↓
Formal Independent Review（仅在有价值 / 高风险时）
        ↓
Finding 按性质返回正确角色
```

同时遵循：

- **Role Stable**：长期职业身份不被普通 Task 静默改变；
- **Routing First**：先判断谁最适合做，不机械经过全部角色；
- **Fewest Necessary Agents / Handoffs**：在不降低正确性和必要控制的前提下减少 Owner 搬运；
- **Research-Assisted Problem Solving**：复杂 / 未知 / 第三方相关问题先借助官方资料、GitHub、同类项目建立可靠假设，避免长时间 Blind Trial-and-Error；
- **Coherent Work Unit**：Engineer Task 以完整可交付结果为单位，内部步骤由 Engineer 自行完成；
- **Embedded Review**：Engineer 可在有意义节点自动调用第二模型审查，不要求 Owner 逐次转发；
- **Dynamic Review Routing**：正式 Reviewer 可介入产品、架构、代码、安全、数据、UI；Finding 返回真正负责的角色；
- **Git / Runtime / Tests / Evidence** 保存技术事实；Notion（启用时）面向 Owner 保存项目进度与产品记忆；
- Project Memory 是辅助，不是正式事实同步机制；
- 旧项目固定到自己的 Workflow Version + Revision，不因 `main` 变化静默迁移。

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

Workflow 使用 SemVer 风格的 0.x 版本进行演进：

- `v0.1.0`：第一份稳定快照；
- `v0.2.0-dev`：当前 `main` 的 Role-First / Owner-visible 工作流重构阶段；
- 完成并验证后再发布正式 `v0.2.0`。

每个项目应同时记录：

```text
Workflow Version: <release / dev version>
Workflow Revision: <exact commit SHA>
```

Version 方便 Owner 识别工作流代际；Revision 用于 AI 精确读取规则。

旧项目不会因为 Workflow 升级自动迁移。
