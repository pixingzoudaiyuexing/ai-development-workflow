# BOOTSTRAP

## 1. 新项目初始化原则

Project Discovery 完成前，不生成正式 Codex Task，不开始写代码。

先确认：

- 这个项目是什么；
- 为谁解决什么问题；
- 核心目标；
- 非目标；
- 已有代码还是从零开始；
- 现有技术 / 运行环境；
- 必须兼容什么；
- 商业、安全、部署等重要约束；
- 用户当前最希望先解决什么。

不要为了填模板而虚构未知事实。未知项明确写“待确认”。

初始 Project Discovery 对话默认承担 Primary Conversation（主对话）职责。用户只需要描述产品和需求，不需要预先判断应该建立几个子对话、哪些属于前端 / 后端 / 运维或是否跨 Repo。

## 2. Project Tier

### Tier 0 — 临时实验

适用：一次性脚本、快速验证、短期实验。

最低要求：

- 无需完整项目文档；
- 仍遵守基本 Git 安全与 Evidence 原则。

### Tier 1 — 小型长期项目

默认建立：

```text
AGENTS.md
docs/PROJECT.md
docs/STATUS.md
```

其中 `STATUS.md` 仍按 checkpoint 使用，不作为日报。

### Tier 2 — 正式长期项目

默认建立：

```text
AGENTS.md
docs/PROJECT.md
docs/ARCHITECTURE.md
docs/ROADMAP.md
docs/STATUS.md      # checkpoint only
```

在出现长期重要决定时增加：

```text
docs/DECISIONS.md
```

### Tier 3 — 商业 / 核心 / 高风险长期项目

默认建立：

```text
AGENTS.md
docs/PROJECT.md
docs/ARCHITECTURE.md
docs/ROADMAP.md
docs/STATUS.md
docs/adr/           # 出现重要架构决策时一事一记
```

并默认要求存在独立于 Codex 自述之外的自动化验证能力。具体 CI/CD 平台不由本 Workflow 指定；若不适用，必须在项目规则或 ADR 中记录 Waiver 原因。

## 3. 初始化文档边界

### AGENTS.md

只写当前项目的“如何开发”：

- 项目适用规则；
- 构建 / 测试 / baseline verification；
- 禁止事项；
- 特殊风险模块；
- 需要优先阅读的项目文档。

不要复制全局 Codex 个性化规则。

### PROJECT.md

只写 What & Why：

- 产品定位；
- 用户；
- 目标；
- 非目标；
- 业务边界；
- 重要约束。

### ARCHITECTURE.md

只描述当前真实架构或已经明确批准、准备立即实现的初始架构。

不要把未来愿望伪装成现状。

### DECISIONS / ADR

只记录未来很可能重新讨论的重要长期决定。

### ROADMAP.md

记录阶段 / Milestone / 暂缓 / 放弃的计划，不作为每日任务清单。

### STATUS.md

是 Save Point，不是开发日志。

## 4. Conversation Topology Gate

Project Discovery 基本完成后，Primary Conversation 判断是否需要多个长期或阶段性对话。

判断依据包括：

- 是否存在多个 Git Repo；
- 是否存在长期独立的工作流（API、Web、Client、Ops 等）；
- 是否需要明显的上下文隔离；
- 是否会长期并行推进；
- 单一对话是否会因为职责混杂而增加错误路由或上下文污染。

不要为了“结构看起来完整”机械创建很多对话。简单项目可以只有 Primary Conversation。

如果需要 Child Conversation，Primary Conversation 必须主动给出：

```text
建议对话数量
每个对话名称
用途
负责 Repo / Domain
第一个任务
需要读取的 Workflow / Project 文档
何时返回主对话
可直接复制的启动消息
```

使用 `templates/CONVERSATION-HANDOFF.template.md`。用户不负责自行编写这些启动消息。

Conversation Topology 可以随着项目演进由 Primary Conversation 调整；新增需求不要求用户提前预测未来会出现哪些工作流。

## 5. Project Ready Gate

进入第一个正式 Codex Task 前确认：

- 项目目标与非目标已足够清晰；
- Project Tier 已确定；
- 对应 Tier 的默认基础文档已建立；
- 项目 `AGENTS.md` 已定义 baseline verification；
- 真实仓库 / 分支已确认；
- 未知事项不会阻止第一个 Task；
- 当前第一个 Task 有明确 Acceptance Criteria；
- 如果项目需要多个对话，Conversation Topology 已由 Primary Conversation 给出，必要的 Child Conversation Handoff 已准备。

满足后才进入正常 `WORKFLOW.md`。
