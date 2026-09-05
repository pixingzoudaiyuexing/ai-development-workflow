# START HERE

这是 AI Development Workflow 的唯一入口。

先读取 `VERSION` 确认当前 Workflow 版本，再判断当前场景，然后只读取需要的文档；不要一次性把所有规则加载进上下文。

## 1. 新项目 / Primary Conversation

读取：

1. `BOOTSTRAP.md`
2. `WORKFLOW.md`
3. 必要时 `RISK-GATES.md`
4. 需要跨上下文交接或独立审查时再读取 `HANDOFF.md`

在 Project Discovery 完成前：

- 不写代码；
- 不生成正式 Codex Task；
- 不预设项目架构；
- 先确认项目目标、边界、现状、约束和非目标。

初始 Project Discovery 对话默认作为 Primary Conversation。Project Discovery 基本完成后，由 Primary Conversation 判断是否需要 Child Conversation，并直接生成 Conversation Topology 与可复制启动消息；不要让零代码用户自己决定前端 / 后端 / Repo 路由。

## 2. Primary Conversation 创建或调度 Child Conversation

读取：

1. `WORKFLOW.md` 的 Conversation Orchestration
2. `HANDOFF.md` 的 Conversation Handoff
3. `templates/CONVERSATION-HANDOFF.template.md`
4. 当前项目相关 Git 文档

Primary Conversation 负责决定：复用现有子对话、新建子对话、留在主对话分析，还是拆成多个有顺序的任务。

## 3. Child Conversation / 正常开发

先读取 Primary Conversation 提供的 Handoff，然后按 Handoff 指定内容读取：

1. 当前项目根目录 `AGENTS.md`
2. 与任务相关的项目文档
3. `WORKFLOW.md`
4. `RISK-GATES.md`

然后完成 Task Risk 判断，再决定是否进入 Codex 或先做 Gemini Design Review。

Child Conversation 不应自行扩大产品 / 架构 / 跨 Repo 决策范围；命中 Handoff 中的 Escalation Trigger 时返回 Primary Conversation。

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
- Project Memory 只作为辅助；长期事实以 Git 文档为锚点。
- 发生重大 AI 分歧时，进入 Evidence Gate，不继续无限理论争论。
- 任何跨 AI / 跨 Conversation 箭头都必须有 Handoff。
