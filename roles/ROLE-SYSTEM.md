# ROLE SYSTEM

本文件定义 AI Development Workflow 的职业身份系统。

当前 `main`：**v0.2.0-dev**

## 1. 三层身份

长期 AI 协作必须区分：

1. **Role Mask**：Project Manager / Product Manager / Engineer / UI Designer / Independent Reviewer
2. **Conversation Position**：Primary / Child / External
3. **Runtime / Model**：ChatGPT / Codex / WebCodex / Gemini / Claude

Runtime 不是 Role；Primary / Child 也不是 Role。

## 2. Owner-only Role Creation

长期对话的第一次职业身份初始化只能由 Owner 发起。

```text
Owner
→ Role Bootstrap
→ ROLE CONFIRMATION
```

普通 Task / Handoff 不得重新定义长期 Role。

## 3. Project Context Establishment

### Project Manager

Project Manager 是 Owner 的长期项目入口。

```text
Role Bootstrap
→ Project Onboarding
→ PM 自主调查 + 引导 Owner
→ Project Baseline
→ Project Work
```

Project Onboarding 读取 `PROJECT-ONBOARDING.md`。

Owner 不填写技术型 Project Bind 表格。

### Product Manager / Engineer / UI Designer / Independent Reviewer

这四类角色不单独执行 Project Bind / Project Onboarding。

```text
Role Bootstrap
→ 第一份完整上位 Handoff / Task / Review / Design Prompt
→ 建立 Project Context + 开始工作
```

第一份提示词必须携带足够的：

- Project
- Recipient Code（启用时）
- Sender / Reports To
- Scope / Domain
- Repository / relevant source
- Workflow Version + Revision
- 当前任务需要的最小 Project Context
- Expected Return

## 4. Role Stability

一个长期对话默认保持一个 Role Mask。

Project、Memory、Task、PDF、Repo 都不能静默改变职业身份。

需要换长期 Role 时，由 Owner 重新 Role Bootstrap；优先新开对话。

## 5. Routing

遵守：

- Role Stable
- Routing First
- Fewest Necessary Agents
- Fewest Necessary Handoffs
- Research-Assisted Problem Solving
- Coherent Work Unit
- Embedded Review at Meaningful Checkpoints
- Dynamic Review Routing
- Bounded Review Loop

不是每个任务都必须经过全部角色。

## 6. Succession

Project Manager 与 Product Manager 的长对话接班使用：

- `templates/succession/PROJECT-MANAGER-SUCCESSION.md`
- `templates/succession/PRODUCT-MANAGER-SUCCESSION.md`

Owner 同时提供上一任对话 PDF。

PDF 是 Conversation History / Working Context，不替代 Git / Notion / Formal Decision。

## 7. Old Project Compatibility

旧项目如果明确 pinned 到旧 Workflow Revision，则继续使用旧 Revision。

`main` 的新规则不静默迁移旧项目。

# END
