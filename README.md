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

## Small Project Mode

小型项目不必为了层级完整额外创建 Product Manager。

Owner 明确采用 Small Project Mode 时：

```text
Role Mask = Project Manager
Operational Mode = Project Manager + Product Manager responsibilities
```

启动：

- `SMALL-PROJECT-ONBOARDING.md`

项目复杂度长期上升后再拆出独立 Product Manager。

## 入口

- `START-HERE.md`
- `roles/ROLE-SYSTEM.md`
- `PROJECT-ONBOARDING.md`

## 角色

- `roles/PROJECT-MANAGER.md`
- `roles/PRODUCT-MANAGER.md`
- `roles/ENGINEER.md`
- `roles/UI-DESIGNER.md`
- `roles/INDEPENDENT-REVIEWER.md`

## 接班

- `templates/succession/PROJECT-MANAGER-SUCCESSION.md`
- `templates/succession/PRODUCT-MANAGER-SUCCESSION.md`
- `templates/succession/SMALL-PROJECT-SUCCESSION.md`

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
