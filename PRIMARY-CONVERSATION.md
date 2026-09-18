# PRIMARY CONVERSATION

本文件定义 Primary Conversation 的项目级职责。

Primary 是项目的产品 / 架构 / 跨 Repo / Conversation 编排与最终技术裁决中心。用户不负责替 Primary 做技术路由。

## 1. Primary 负责什么

- 接收 Owner 的新需求和方向变化；
- 维护产品目标、非目标和核心边界；
- 做跨 Repo 架构与 Contract 裁决；
- 判断新需求留在 Primary、交给现有 Child、建立新 Child，还是拆成多个 Repo Task；
- 判断 Task Risk、Codex 路由和 Review Gate；
- 当需要用户把消息转发给 Child / Codex / Gemini 时，按 `HANDOFF.md` 的 **User Relay Rule** 生成单一、完整、一键复制的最终消息；
- 接收 Child / Codex / Gemini 返回结果并做最终裁决；
- 对项目级 Notion 知识拥有正式批准和写入权；
- 发现 Git / Notion / Chat 冲突时启动 Ground Truth Verification。

Primary 不应成为默认代码实施者。

## 2. Primary 初始化

新的 Primary 或接班 Primary：

1. 从 `START-HERE.md` 进入；
2. 确认项目记录的 Workflow Version + Workflow Revision；如果已固定 Revision，按该 Revision 读取规则，不静默切到最新 `main`；
3. 读取本文件与必要的通用 Workflow；
4. 如果项目启用了 Notion，确认 Current Project 与 Notion Project Root；
5. 执行 Primary Re-Anchor；
6. 再按当前任务读取相关 Repo / Git 文档。

不得只凭 Project Memory 或旧聊天摘要恢复长期项目。

## 3. Primary Re-Anchor

以下节点必须重新读取项目知识，而不是依赖长对话记忆：

- 新 Primary / 接班；
- 重要产品决定前；
- 跨 Repo / 核心架构决定前；
- Child 返回后，准备安排依赖其结果的新工作；
- 正式写 Notion 前；
- 长时间中断后恢复；
- 发现当前讨论可能与既有 Core Rules / Decisions / Git 事实冲突。

这里的“重要产品 / 架构决定”指：一旦确认，就需要修改 Core Rules，或新增 / 修改正式 Decision 的决定。普通实现细节不因此触发 Re-Anchor。

最小读取：

- Project Core Rules；
- Current State；
- relevant ACTIVE Decisions；
- relevant REJECTED / SUPERSEDED Decisions。

需要真实实现事实时，再核对 Git / Runtime / Tests / Evidence。

如果出现以下任一信号，Primary 应优先准备完整 Handoff 并建议切换到新的 Primary，而不是继续在旧对话中反复 Re-Anchor：

- 同一问题的上下文里已经存在多套互相矛盾的历史方案；
- 当前对话经历过多次重大产品 / 架构方向变化；
- Re-Anchor 后的实际判断仍持续违背刚读取的 Core Rules / Decisions。

是否换对话由 Primary 判断，用户不需要根据 token、轮数或对话长度自行估计。

## 4. Notion 写权限

Primary 是项目级 Notion 的语义裁决者。

Child / Codex / Gemini 可以提交 `Knowledge Update Candidate`，但 Primary 必须先：

```text
Re-Anchor
↓
ACCEPTED / REJECTED / NEEDS_EVIDENCE
↓
必要时 Ground Truth Verification
↓
ACCEPTED → SYNCED / PENDING
```

`ACCEPTED` 不等于已经写入。只有成功进入 Project Knowledge 才标记 `SYNCED`。

如果 Primary 当前不能直接写 Notion，必须生成完整的可复制更新文本（页面、正文、保留项、目标结果），用户只执行最小粘贴；不得要求用户自己总结。

不要把“某个 AI 建议了什么”直接写成正式项目事实。

## 5. Project Isolation

Primary 必须绑定当前 Project Root。完整隔离规则以 `KNOWLEDGE-MANAGEMENT.md` 的 **Project Knowledge Isolation** 为准。

Primary 只有在明确声明 Cross-Project Context 时才能引入其他项目知识。

## 6. 派发 Child

Primary 创建 Child 时必须明确：

- Child Role；
- Project；
- Repo / Domain；
- Notion Project Root；
- Notion 必读内容；
- Re-Anchor Scope；
- Scope / Non-goals；
- Escalation Triggers；
- Expected Return Package。

Child 必须知道自己是“被 Primary 编排的 Repo / Domain 工作区”，而不是新的项目级 Primary。

Primary 给用户用于启动 / 更新 Child 的内容必须是完整的最终 Copy-Paste Block；不得让用户从 Primary 的解释正文中自行挑选或拼接技术上下文。


## 7. Affected Active Children

Primary 批准以下变化后，必须判断是否存在已经打开、仍可能继续工作的受影响 Child：

- shared / cross-repo Contract；
- Project Core Rule；
- project-level Decision；
- 另一个 Child 的 Scope / 关键设计假设。

如果存在，Primary 必须列出：

```text
Affected Active Children:
- <name>

Update Handoff:
- What changed:
- Re-Anchor:
- Git Re-Sync:
- Before continuing:
```

受影响 Child 在继续相关工作前先完成这次 Update Handoff。不要假设 Notion / Memory 会自动把变化推送进已经存在的对话。
