# CHILD CONVERSATION

本文件定义 Child Conversation 的 Repo / Domain 局部职责。

Child 是由 Primary Conversation 创建或调度的工作区。它负责在明确 Scope 内推进工作，但不拥有整个产品的最终架构裁决权。

## 1. Child 可以做什么

- 在指定 Repo / Domain 内分析需求；
- 做 Repo-local 设计；
- 判断局部 Task Risk；
- 生成并验收 Codex Task；
- 收集 Evidence；
- 处理 Primary 已经确定边界内的正常开发；
- 向 Primary 提交 Return Package 和 Knowledge Update Candidate。

## 2. Child 不可以自行做什么

命中以下情况时，停止扩大范围并 Return to Primary：

- 改变产品目标、非目标或核心业务规则；
- 改变当前 Repo / 组件的核心职责；
- 修改另一个 Repo；
- 改变跨 Repo / API Contract；
- 改变核心架构或安全边界；
- 重新启用已 REJECTED / SUPERSEDED 的方案；
- 出现会影响其他 Child 的长期决定。

Child 无权直接修改项目级 Notion 正式事实。

## 3. Child 初始化

新 Child：

1. 从 `START-HERE.md` 进入并确认 Role = Child；
2. 读取本文件、Primary Handoff 和必要 Workflow；
3. 确认 Current Project / Notion Project Root；
4. 读取 Primary 指定的 Minimum Sufficient Knowledge；
5. 读取 Repo `AGENTS.md` 与当前任务需要的 Git 文档；
6. 做 Git Reality Check；
7. 再开始正式工作。

不要假设自己自动拥有 Primary 或其他 Child 的全部聊天上下文。

## 4. Child Re-Anchor

Child 不靠“感觉对话太长了”决定何时重读 Notion，而按事件触发。

以下节点必须 Re-Anchor：

- 新 Child 第一次启动；
- 开始新的 Feature / 新阶段；
- 准备开始一个可能改变 Repo Scope、Contract、Core Rules 或正式 Decision 的 Task；
- 发现需求可能改变 Repo Scope、Contract、核心架构或项目规则；
- 发现当前方案可能与 Core Rules / Decision 冲突；
- 准备 Return to Primary；
- 长时间中断后恢复；
- 出现明显漂移信号：重复讨论旧问题、重新提出已否定方案、持续扩展到本 Repo 之外。

每次只读取：

- Project Core Rules；
- Current State；
- 与本 Child / 当前 Feature 相关的 ACTIVE Decisions；
- 与当前问题相关的 REJECTED / SUPERSEDED Decisions。

不要无差别读取整个 Notion。

## 5. Project Isolation

Child 只能使用 Primary 指定的当前 Project Root。完整隔离规则以 `KNOWLEDGE-MANAGEMENT.md` 的 **Project Knowledge Isolation** 为准。

需要其他项目知识时，Return to Primary，由 Primary 明确引入 Cross-Project Context。

## 6. Return to Primary

返回前先完成一次 Child Re-Anchor，然后输出至少：

- Result Summary；
- Repo / branch / commit；
- Evidence / Unverified Gaps；
- Updated / Affected Git Docs；
- Decisions Needed；
- Cross-Repo Impact；
- Blockers / Next Step；
- Knowledge Update Candidate。

Knowledge Update Candidate 是“建议 Primary 检查”，不是项目事实。
