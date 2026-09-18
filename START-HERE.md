# START HERE

这是 AI Development Workflow 的唯一入口。

先读取 `VERSION` 确认当前 Workflow 版本，并记录当前项目采用的 **Workflow Revision（具体 commit SHA）**。项目默认固定到已记录的 Revision；除非 Primary 明确执行 Workflow 升级，不得因为仓库 `main` 继续变化而静默切换规则。然后再判断当前场景，只读取需要的文档；不要一次性把所有规则加载进上下文。

## 1. 新项目 / Primary Conversation

读取：

1. `BOOTSTRAP.md`
2. `WORKFLOW.md`
3. `PRIMARY-CONVERSATION.md`
4. 项目启用 Notion Project Knowledge 时读取 `KNOWLEDGE-MANAGEMENT.md`
5. 必要时 `RISK-GATES.md`
6. 需要跨上下文交接或独立审查时再读取 `HANDOFF.md`

在 Project Discovery 完成前：

- 不写代码；
- 不生成正式 Codex Task；
- 不预设项目架构；
- 先确认项目目标、边界、现状、约束和非目标。

初始 Project Discovery 对话默认作为 Primary Conversation。Project Discovery 基本完成后，由 Primary Conversation 判断是否需要 Child Conversation，并直接生成 Conversation Topology 与可复制启动消息；不要让零代码用户自己决定前端 / 后端 / Repo 路由。

对于长期复杂、多 Repo 或多 Conversation 项目，Primary 同时按 `BOOTSTRAP.md` 的 Project Knowledge Gate 判断是否启用 Notion Project Knowledge。启用后的隔离、写权限与 Re-Anchor 规则统一读取 `KNOWLEDGE-MANAGEMENT.md`。

## 2. Primary Conversation 创建或调度 Child Conversation

读取：

1. `PRIMARY-CONVERSATION.md`
2. `WORKFLOW.md` 的 Conversation Orchestration
3. `HANDOFF.md` 的 Conversation Handoff
4. `templates/CONVERSATION-HANDOFF.template.md`
5. 项目启用 Notion 时读取 `KNOWLEDGE-MANAGEMENT.md`
6. 当前项目相关 Git 文档

Primary Conversation 负责决定：复用现有子对话、新建子对话、留在主对话分析，还是拆成多个有顺序的任务。

## 3. Child Conversation / 正常开发

先读取 Primary Conversation 提供的 Handoff，然后按 Handoff 指定内容读取：

1. `CHILD-CONVERSATION.md`
2. 项目启用 Notion 时，读取 Handoff 指定的 Project Root / Core Rules / Current State / relevant Decisions
3. 当前项目根目录 `AGENTS.md`
4. 与任务相关的项目文档
5. `WORKFLOW.md`
6. `RISK-GATES.md`

然后完成 Task Risk 判断，再决定是否进入 Codex 或先做 Gemini Design Review。

Child Conversation 不应自行扩大产品 / 架构 / 跨 Repo 决策范围；命中 Handoff 中的 Escalation Trigger 时返回 Primary Conversation。

项目启用 Notion 时，Child 的 Re-Anchor 与项目知识权限以 `CHILD-CONVERSATION.md` 和 `KNOWLEDGE-MANAGEMENT.md` 为准；本入口不重复维护 Trigger 列表。

## 4. 跨 AI 交接 / Gemini 独立审查

读取：

- `HANDOFF.md`

禁止假设另一个 AI 自动拥有当前对话、仓库、工作树、日志或私有文件。

## 5. 生产事故 / 紧急修复

读取：

- `EMERGENCY.md`

Hotfix 可以延后部分流程，但不能永久跳过流程。

## 6. 项目暂停、恢复或文档维护

读取：

- `DOCUMENTATION.md`
- 项目 `STATUS.md`（如果存在）
- 项目根 `AGENTS.md`

恢复长期休眠项目时，先做 Repository Reality Check 与 baseline verification，再相信旧文档。

## 7. 核心不变量

- ChatGPT：产品、需求、架构、任务拆解、风险判断、技术裁决与 Conversation Orchestration。
- Primary Conversation：项目级需求入口与调度中心，决定是否创建 / 复用 Child Conversation，并负责上下文交接。
- Child Conversation：在明确 Scope / Repo 内工作，跨边界时返回 Primary Conversation。
- Codex：默认唯一代码实施者，负责代码、测试、构建、Git 与证据收集。
- Gemini：默认独立审阅者，按 Risk Gate 做 Design/Code Review，默认不直接改代码。
- 用户：定义“我要什么”和“是否上线”，不负责技术争议裁决、Conversation 路由或 Repo 路由。
- Project Memory 只作为辅助；不得用它替代正式恢复流程。
- GitHub Workflow 定义“AI 应该怎么工作”；项目使用 `Workflow Version + Workflow Revision` 锚定实际规则版本，避免同一个 `v1` 随 `main` 漂移。
- 启用 Notion 时，Notion 保存项目级长期产品真相与决定状态；Git / Runtime / Tests 保存 Repo 技术现实。两者默认 ownership 见 `DOCUMENTATION.md`。
- 项目级 Notion 正式写入由 Primary 裁决；Child / Codex / Gemini 只提交 Knowledge Update Candidate。
- 同一 Notion 账号可包含多个项目，但 Primary / Child 默认只能在当前 Project Root 内读取和搜索。
- 发生重大 AI 分歧时，进入 Evidence Gate，不继续无限理论争论。
- 任何跨 AI / 跨 Conversation 箭头都必须有 Handoff。
