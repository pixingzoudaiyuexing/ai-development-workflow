# KNOWLEDGE MANAGEMENT

## 1. Notion 定位

Notion 是：

**Owner-facing Project / Product Memory Layer**

不是技术 SSOT，也不是聊天全文归档。

它回答：

- 项目现在做到哪里；
- 我们为什么这样定；
- 哪些方向已经确认；
- 哪些方向已经否定；
- 当前下一步是什么；
- Owner 是否需要决定什么。

Git / Runtime / Tests / Evidence 回答技术上实际发生了什么。

Conversation / PDF 保存讨论现场和接班历史。

## 2. Role Ownership

### Project + Product Manager

当 Owner 选择合并身份时，该角色同时维护下面 Project Manager + Product Manager 两层 Owner-facing Memory，但不重复写两份相同内容。

### Project Manager

主要维护：

- Owner Dashboard
- Project Progress
- Roadmap / Milestones
- Current Project State
- Role / Conversation Topology
- Project-level Decisions
- Workflow Version / Revision
- Owner Action Required
- Project-level Blocker / Continuity

### Product Manager

主要维护：

- Feature Memory
- Owner Intent
- Confirmed Direction
- Must Have / Must Not
- Delegated Space
- Open Questions
- Implemented Behavior
- AI-added Improvements
- Important Deviations
- Feature Change History

### Engineer / UI Designer / Independent Reviewer

提供真实 Evidence / Behavior / Finding / Design delta，供对应 Role 判断是否值得沉淀。

Primary / Child 是位置，不改变上述语义 Ownership。

## 3. 不记录每句话

Notion 不保存完整聊天。

默认不进入 Notion：

- 对话 transcript；
- AI 中间推理；
- 普通 brainstorming；
- terminal / CI 全量日志；
- source code / diff；
- 普通 Bug 调试过程；
- 每次 commit 流水账；
- 无长期价值的失败尝试。

只有“未来新的 Project Manager / Product Manager 不知道这件事就可能做错方向”的内容才值得沉淀。

## 4. Important Record

重要记录建议使用：

`YYYY-MM-DD HH:mm GMT±X`

并区分：

- Confirmed
- Rejected
- Superseded
- Candidate / Open Question

讨论过不等于决定了。

## 5. Project Isolation

每个项目有自己的 Project Root。

默认只在当前 Project Root 内读取 / 写入，不因为页面名相似跨项目引用。

跨项目上下文必须明确标记来源。

## 6. Git 与 Notion

```text
Notion
= Owner-facing project / product memory

Git / Runtime / Tests / Evidence
= technical truth
```

不要把完整技术实现复制到 Notion。

重要项目决定如果有技术细节：

- Notion 保存 Owner-facing 结论和状态；
- Git ADR / docs 保存技术理由、Evidence 和实现后果。

## 7. Update Timing

适合更新的时机：

- Owner 确认重要方向；
- 正式 Decision 变化；
- Feature / Milestone 关闭；
- 实际实现与原产品方向出现重要差异；
- 当前阶段 / 下一阶段发生实质变化；
- Rejected / Superseded 方向需要长期防止复活。

普通小任务不机械更新。

## 8. Conflict

Notion 与 Git / Runtime 冲突时，不自动相信任何一方。

按 `WORKFLOW.md` 的 Ground Truth Verification 核实。

## 9. Notion 不可用

Notion 暂不可用不阻塞安全的技术工作。

需要长期沉淀的内容可以先保留在完整 Return / Handoff 中，等具备写入能力后再同步。

不要因此建立第二套复杂状态系统。

# END
