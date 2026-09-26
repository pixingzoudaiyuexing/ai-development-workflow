# AI Development Workflow

面向个人开发者的 AI 多角色开发工作流。

当前 `main`：**v0.2.0-dev**  
已发布稳定快照：**v0.1.0**

## 核心结构

```text
Owner
↓
Role Bootstrap
↓
Project Manager：Project Onboarding → Project Baseline
↓
按需要路由 Product Manager / Engineer / UI Designer / Independent Reviewer
↓
Evidence / Review / Return
```

其他角色不单独执行 Project Bind；它们通过第一份完整上位任务建立 Project Context。

## 核心原则

- Role Stable
- Routing First
- Fewest Necessary Agents
- Fewest Necessary Handoffs
- Research-Assisted Problem Solving
- Coherent Work Unit
- Embedded Review at Meaningful Checkpoints
- Dynamic Review Routing
- Evidence over Claims
- Git = Technical Truth
- Notion = Owner-facing Project / Product Memory
- Conversation PDF = Succession / Working Context

## Owner 的职责

Owner 负责：

- 我想做什么；
- 为什么；
- 产品 / 商业结果；
- 什么不能改变；
- 重大优先级；
- 是否上线。

Owner 不负责：

- 框架选择；
- Repo 路由；
- 数据库设计；
- 普通架构 / 实现决策；
- 测试方案；
- AI 之间的技术争议裁决。

Project Manager 应主动调查并引导 Owner。

## 项目兼产品经理

如果 Owner 选择一个对话同时承担 Project Manager + Product Manager，只使用两份 canonical 提示词：

- 新对话：`roles/PROJECT-PRODUCT-MANAGER.md`
- 接班：`templates/succession/PROJECT-PRODUCT-MANAGER-SUCCESSION.md`

新对话文件已经包含 Role Bootstrap + Project Onboarding；接班文件已经包含 Role 恢复 + PDF Succession + 必要的项目校准。

不需要额外 Small Project Mode、额外 Onboarding 或额外接班提示词。

## 入口

- `START-HERE.md`
- `roles/ROLE-SYSTEM.md`
- `roles/PROJECT-MANAGER.md`
- `roles/PROJECT-PRODUCT-MANAGER.md`

## 角色

- `roles/PROJECT-PRODUCT-MANAGER.md`
- `roles/PROJECT-MANAGER.md`
- `roles/PRODUCT-MANAGER.md`
- `roles/ENGINEER.md`
- `roles/UI-DESIGNER.md`
- `roles/INDEPENDENT-REVIEWER.md`

## 接班

- `templates/succession/PROJECT-PRODUCT-MANAGER-SUCCESSION.md`
- `templates/succession/PROJECT-MANAGER-SUCCESSION.md`
- `templates/succession/PRODUCT-MANAGER-SUCCESSION.md`

## 其他

- `WORKFLOW.md`
- `HANDOFF.md`
- `KNOWLEDGE-MANAGEMENT.md`
- `RISK-GATES.md`
- `DOCUMENTATION.md`
- `EMERGENCY.md`

旧项目如果固定到旧 Workflow Version + Revision，不因 `main` 更新自动迁移。

## Version

```text
Workflow Version: v0.2.0-dev
Workflow Revision: <exact commit SHA>
```

正式整理和验证完成后发布 `v0.2.0`。
