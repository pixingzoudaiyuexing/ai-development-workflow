# START HERE

这是 AI Development Workflow 的入口。

## 1. 先建立职业身份

所有长期 AI 对话都由 Owner 先发送对应 Role Bootstrap：

- `roles/PROJECT-PRODUCT-MANAGER.md`（项目兼产品经理：新对话一份提示词即可）
- `roles/PROJECT-MANAGER.md`
- `roles/PRODUCT-MANAGER.md`
- `roles/ENGINEER.md`
- `roles/UI-DESIGNER.md`
- `roles/INDEPENDENT-REVIEWER.md`

Role Mask、Conversation Position、Runtime 是三件不同的事。普通 Task 不得静默改变长期 Role。

## 2. Project + Product Manager

如果 Owner 选择 **项目兼产品经理**，直接使用：

`roles/PROJECT-PRODUCT-MANAGER.md`

这一个文件已经包含 Role Bootstrap + Project Onboarding，不需要第二个 Onboarding 链接。

接班只使用：

`templates/succession/PROJECT-PRODUCT-MANAGER-SUCCESSION.md`

+ 上一任对话 PDF。

## 3. Project Manager 项目接入

Project Manager 不要求 Owner 填技术型 PROJECT BIND，也不需要第二份 Project Onboarding 文件。

`roles/PROJECT-MANAGER.md` 已内置 Role Bootstrap + Project Onboarding。

流程是：

```text
Owner
→ roles/PROJECT-MANAGER.md
→ Role Bootstrap + Embedded Project Onboarding
→ PM 自主调查 + 引导 Owner
→ Project Baseline
→ Normal Project Work
```

Owner 负责产品意图；Project Manager 负责理解技术结构、项目边界和推进方式。

## 4. 其他角色

Product Manager / Engineer / UI Designer / Independent Reviewer 不单独增加 Project Bind。

```text
Owner Role Bootstrap
→ 第一份完整的上位 Handoff / Task / Review / Design Prompt
→ 建立 Project Context + 开始工作
```

第一份正式提示词必须携带当前任务所需的最小 Project Context。

## 5. 长对话接班

Project + Product Manager：

- `templates/succession/PROJECT-PRODUCT-MANAGER-SUCCESSION.md`

Project Manager：

- `templates/succession/PROJECT-MANAGER-SUCCESSION.md`

Product Manager：

- `templates/succession/PRODUCT-MANAGER-SUCCESSION.md`

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
- `roles/PROJECT-MANAGER.md`：项目经理身份 + 项目接入流程
- `WORKFLOW.md`：整体协作规则
- `HANDOFF.md`：跨角色交接
- `KNOWLEDGE-MANAGEMENT.md`：Notion / 长期知识
- `RISK-GATES.md`：风险与审查
- `EMERGENCY.md`：生产事故
- `DOCUMENTATION.md`：Git 文档边界

旧项目如果 pinned 到旧 Workflow Revision，不因 `main` 更新自动迁移。
