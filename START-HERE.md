# START HERE

这是 AI Development Workflow 的入口。

## 1. 先建立职业身份

所有长期 AI 对话都由 Owner 先发送对应 Role Bootstrap：

- `roles/PROJECT-MANAGER.md`
- `roles/PRODUCT-MANAGER.md`
- `roles/ENGINEER.md`
- `roles/UI-DESIGNER.md`
- `roles/INDEPENDENT-REVIEWER.md`

Role Mask、Conversation Position、Runtime 是三件不同的事。普通 Task 不得静默改变长期 Role。

## 2. Project Manager 的第二步

Project Manager 完成 Role Bootstrap 后，不要求 Owner 填技术型 PROJECT BIND。

进入：

`PROJECT-ONBOARDING.md`

流程是：

```text
Owner Role Bootstrap
→ Project Onboarding
→ PM 自主调查 + 引导 Owner
→ Project Baseline
→ Normal Project Work
```

Owner 负责产品意图；Project Manager 负责理解技术结构、项目边界和推进方式。

## 3. 其他角色

Product Manager / Engineer / UI Designer / Independent Reviewer 不单独增加 Project Bind。

```text
Owner Role Bootstrap
→ 第一份完整的上位 Handoff / Task / Review / Design Prompt
→ 建立 Project Context + 开始工作
```

第一份正式提示词必须携带当前任务所需的最小 Project Context。

## 4. Small Project Mode

小型项目可以由同一个 Project Manager 同时承担 Product Manager 的必要职责，不新增第六个 Role Mask。

启动：

- `SMALL-PROJECT-ONBOARDING.md`

当项目长期出现多 Feature / 多 Repo / 产品讨论明显复杂化时，再拆出独立 Product Manager。

## 5. 长对话接班

Project Manager：

- `templates/succession/PROJECT-MANAGER-SUCCESSION.md`

Product Manager：

- `templates/succession/PRODUCT-MANAGER-SUCCESSION.md`

Small Project Mode：

- `templates/succession/SMALL-PROJECT-SUCCESSION.md`

Owner 同时提供上一任对话 PDF。新对话采用 Tail First → Expand Backward as Needed 恢复最近工作现场。

PDF 是 Conversation History，不替代 Git / Notion / Formal Decision。

## 6. 核心协作原则

- Role Stable
- Routing First
- Fewest Necessary Agents
- Fewest Necessary Handoffs
- Research-Assisted Problem Solving
- Coherent Work Unit
- Embedded Review at Meaningful Checkpoints
- Dynamic Review Routing
- Evidence over Agent Claims
- Git Technical Truth
- Notion Owner-facing Project / Product Memory
- Conversation PDF = Working Context / Succession Source

## 7. 常用文档

- `roles/ROLE-SYSTEM.md`：角色系统
- `PROJECT-ONBOARDING.md`：项目经理项目接入流程
- `SMALL-PROJECT-ONBOARDING.md`：小型项目 Project Manager + Product Manager 模式
- `WORKFLOW.md`：整体协作规则
- `HANDOFF.md`：跨角色交接
- `KNOWLEDGE-MANAGEMENT.md`：Notion / 长期知识
- `RISK-GATES.md`：风险与审查
- `EMERGENCY.md`：生产事故
- `DOCUMENTATION.md`：Git 文档边界

旧项目如果 pinned 到旧 Workflow Revision，不因 `main` 更新自动迁移。
