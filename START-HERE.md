# START HERE

这是 AI Development Workflow 的唯一入口。

先读取 `VERSION` 确认当前 Workflow 版本，再判断当前场景，然后只读取需要的文档；不要一次性把所有规则加载进上下文。

## 1. 新项目

读取：

1. `BOOTSTRAP.md`
2. `WORKFLOW.md`
3. 必要时 `RISK-GATES.md`
4. 需要跨 AI 审查时再读取 `HANDOFF.md`

在 Project Discovery 完成前：

- 不写代码；
- 不生成正式 Codex Task；
- 不预设项目架构；
- 先确认项目目标、边界、现状、约束和非目标。

## 2. 正常开发

读取：

1. 当前项目根目录 `AGENTS.md`
2. 与任务相关的项目文档
3. `WORKFLOW.md`
4. `RISK-GATES.md`

然后完成 Task Risk 判断，再决定是否进入 Codex 或先做 Gemini Design Review。

## 3. 跨 AI 交接 / Gemini 独立审查

读取：

- `HANDOFF.md`

禁止假设另一个 AI 自动拥有当前对话、仓库、工作树、日志或私有文件。

## 4. 生产事故 / 紧急修复

读取：

- `EMERGENCY.md`

Hotfix 可以延后部分流程，但不能永久跳过流程。

## 5. 项目暂停、恢复或文档维护

读取：

- `DOCUMENTATION.md`
- 项目 `STATUS.md`（如果存在）
- 项目根 `AGENTS.md`

恢复长期休眠项目时，先做 Repository Reality Check 与 baseline verification，再相信旧文档。

## 6. 核心不变量

- ChatGPT：产品、需求、架构、任务拆解、风险判断、技术裁决。
- Codex：默认唯一代码实施者，负责代码、测试、构建、Git 与证据收集。
- Gemini：默认独立审阅者，按 Risk Gate 做 Design/Code Review，默认不直接改代码。
- 用户：定义“我要什么”和“是否上线”，不负责技术争议裁决。
- 发生重大 AI 分歧时，进入 Evidence Gate，不继续无限理论争论。
- 任何跨 AI 箭头都必须有 Handoff。
