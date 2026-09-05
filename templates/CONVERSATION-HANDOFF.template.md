# Conversation Handoff

> 由 Primary Conversation 生成并交给用户复制到新的 Child Conversation。用户不需要自行补技术字段；未知项由 Primary Conversation 标记“待确认”。

## Suggested Conversation Name

[例如：CloudGap｜API 开发]

## Parent / Primary Conversation

[主对话名称或说明]

## Project

- Project: [填写]
- Project Tier: [如已确定]

## Purpose

[这个 Child Conversation 为什么存在，长期 / 阶段性职责是什么]

## Repository / Domain

- Repository: [URL / repo name / 本地仓库说明；如不绑定 Repo 写 None]
- Domain: [API / Web / Client / Ops / Module / Other]

## Workflow Source

- Repository: `https://github.com/pixingzoudaiyuexing/ai-development-workflow`
- Version: `v1`
- Entry: `START-HERE.md`

## Workflow Docs to Read

- `START-HERE.md`
- [按当前场景选择 `WORKFLOW.md` / `RISK-GATES.md` / `HANDOFF.md` 等]

## Project Docs to Read

- `AGENTS.md` [如存在]
- [相关 `docs/PROJECT.md` / `docs/ARCHITECTURE.md` / ADR / STATUS 等]

## Context Budget / Do Not Preload

- Required now: [当前任务真正需要的文档 / Contract / 文件]
- Do not preload: [明显无关的领域或文档，例如后端 DB ADR / Ops 文档；没有则写 None]

不要无差别读取所有文档，也不要因为“以后可能有用”预加载整个项目知识库。后续如果真实问题需要更多上下文，再请求具体文件。

## Current Task

[当前第一个任务 / 当前阶段目标]

## Scope

- [允许分析 / 修改 / 调用的范围]

## Non-goals

- [本对话不要自行扩大的范围]

## Escalation Triggers

遇到以下任一情况，暂停扩大范围并返回 Primary Conversation：

- 需要改变产品目标、非目标或核心业务规则；
- 需要修改另一个 Repo；
- 需要改变跨 Repo Contract / API Contract；
- 需要改变核心架构或安全边界；
- 当前任务与本 Handoff Scope 冲突；
- 出现会影响其他工作流的重要长期决定。

Primary Conversation 可按项目补充触发条件。

## Expected Return Package

完成当前阶段或触发升级时，返回 Primary Conversation：

- 结果摘要；
- Repo / branch / commit（如适用）；
- Evidence / Unverified Gaps；
- Updated / Affected Git Docs: [列出本次更新或影响到的核心项目文档；没有写 None]；
- 需要确认或沉淀的长期决定；
- 对其他 Repo / 产品边界的影响；
- Blockers / 下一步建议。

Primary 收到返回包后，如果下一步依赖本次真实实现、架构、Contract 或长期文档变化，应先按 commit anchor + Updated / Affected Git Docs 执行 Re-Sync，再继续编排。

## Copy-Paste Starter Message

Primary Conversation 最终必须把上述信息整理成下面这种**可直接复制**的启动消息，而不是要求用户自己拼接：

```text
这是当前项目中的一个 Child Conversation。

AI Development Workflow：
https://github.com/pixingzoudaiyuexing/ai-development-workflow

请从 START-HERE.md 开始，并按本 Handoff 指定的 Workflow / 项目文档建立上下文。
Project：[填写]
Primary Conversation：[填写]
本对话职责：[填写]
Repository / Domain：[填写]
当前任务：[填写]
Scope：[填写]
Non-goals：[填写]
Required Context：[填写]
Do Not Preload：[填写]

长期事实以项目 Git 文档为锚点，不要假设你自动拥有其他对话的全部上下文。
不要无差别加载整个项目文档；只有在真实问题需要时再请求额外上下文。
如果当前需求触发 Escalation Triggers，请停止扩大范围并明确告诉我需要把什么结果带回 Primary Conversation。

完成或升级返回时，请明确给出 Repo / branch / commit、Evidence / Unverified Gaps，以及 Updated / Affected Git Docs。

先恢复上下文并确认任务边界，不要默认开始修改代码。
```
