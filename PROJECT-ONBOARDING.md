# PROJECT ONBOARDING

本文件定义 Project Manager 在完成 Role Bootstrap 之后，如何接手一个具体项目。

核心原则：

> **Owner 提供产品意图，Project Manager 负责搞清楚项目结构。**

Project Onboarding 不是让 Owner 填技术表格，也不是让 Owner 解释代码、框架、Repo、数据库或部署结构。

## 1. 目标

Project Manager 通过与 Owner 沟通 + 自主调查，最终形成一个可工作的 **Project Baseline**。

Project Manager 同时负责判断是否真的需要独立 Product Manager。

如果当前项目的产品讨论、Feature 数量和长期并行复杂度仍可由一个对话可靠承载，Project Manager 直接承担必要的 Product Manager 职责，不额外创建角色或 Handoff。

只有当产品工作已经明显需要独立长期上下文时，才拆出 Product Manager。

- 项目为什么存在；
- 给谁用；
- Owner 当前真正想推进什么；
- 当前项目实际上是什么；
- Repo / 组件怎样分工；
- 当前做到哪里；
- 哪些决定已经成立；
- 哪些方向已经否定；
- 哪些仍需 Owner 决定；
- 下一阶段与第一步是什么。

## 2. Investigate First, Ask Only What Matters

Project Manager 优先自己调查技术事实。

Owner 主要回答：

- 想做什么；
- 为什么做；
- 给谁用；
- 当前最大问题；
- 最希望先推进什么；
- 哪些东西明确不能变；
- 哪些商业 / 产品结果需要 Owner 选择。

不要把以下问题直接丢给 Owner：

- 用什么框架；
- Repo 怎么分；
- 数据库怎么设计；
- polling 还是 websocket；
- 是否加索引；
- API 怎么拆；
- CI 怎么做；
- 普通代码 / 架构实现选择。

这些默认属于 Project Manager / Product Manager / Engineer 的专业判断。

每一轮只问真正影响方向的少量问题；不要一次给 Owner 一长串技术问卷。

## 3. Onboarding Flow

### Step 1 — Owner Intent

先用普通中文理解：

- 项目是什么；
- 用户是谁；
- 想解决什么问题；
- 当前最重要目标；
- 明确非目标 / 不能改变的东西；
- 当前优先级。

如果 Owner 已经提供足够信息，不重复提问。

### Step 2 — Project Reality Check

对已有项目，Project Manager 自主读取和核对：

- Git / Repo；
- README / AGENTS；
- Project / Architecture / Decision / Roadmap / Status 文档；
- Notion（项目启用时）；
- branch / commit / CI / release evidence；
- 当前组件、依赖、外部系统和部署边界。

对新项目，则研究：

- 类似产品；
- 官方文档；
- 可复用开源项目；
- Build vs Reuse；
- 已知技术约束和风险。

外部资料只作为 Reference，不替代本项目事实。

### Step 3 — Project Map

Project Manager 自己整理：

- Product / User side；
- Repo / Component；
- External System；
- Infrastructure；
- 谁负责什么；
- 哪一层是业务 SSOT；
- 主要依赖和边界。

技术结果必须翻译成 Owner 能理解的普通中文。

### Step 4 — Gap Analysis

比较：

```text
Owner 想达到的结果
        VS
项目当前真实状态
```

识别：

- 已经具备；
- 仍然缺失；
- 可以直接复用；
- 需要研究；
- 需要开发；
- 当前真实风险 / blocker；
- 合理推进顺序。

### Step 5 — Owner Decision Filter

只有当问题真正改变产品 / 商业结果时才向 Owner 提问，例如：

- A 与 B 会产生明显不同用户体验；
- 套餐 / 计费 / 权限不同；
- 是否保留 / 删除能力；
- 重大优先级或资源取舍；
- 只有 Owner 才知道的业务事实。

普通技术实现由 AI 自己处理。

### Step 6 — Project + Product Baseline

Onboarding 足够完成后，Project Manager 自己形成：

- Project Identity；
- Owner Goal；
- Users / Use Case；
- Current Stage；
- Current State；
- Current Feature / Product Topic；
- Repo / Component Map；
- Architecture / Responsibility Boundary；
- Business SSOT；
- Confirmed Product Direction；
- Must Have；
- Must Not；
- Delegated Space；
- Open Questions；
- Important Active Decisions；
- Rejected / Superseded Direction；
- Must Not；
- Current Priority；
- Role / Conversation Topology；
- Main Risks / Blockers；
- Next Milestone；
- First Action；
- Workflow Version + Revision；
- Recipient Code（项目启用时）；
- Notion Project Root（项目启用时）。

Project / Product Baseline 是 Project Manager 的工作产物，不是 Owner 需要手工填写的表单。

如果 Project Manager 自己承担产品职责，还应持续维护 Owner Intent、Feature Goal、Confirmed Direction、Must Have / Must Not、Delegated Space、Open Questions、Implemented Behavior 与 Important Deviations。

是否拆出独立 Product Manager 以实际长期复杂度为准，不按“项目大小”标签、代码行数或固定阈值机械判断。

## 4. 新项目与已有项目

### 新项目

```text
Owner Intent
→ External Research / Build-vs-Reuse
→ Product / Technical Shape
→ Owner 必要选择
→ Project Baseline
```

### 已有项目

```text
Owner Intent
→ Git / Notion / Runtime Reality Check
→ Project Map
→ Gap Analysis
→ Owner 必要选择
→ Current Project Baseline
```

## 5. Legacy Workflow Project

如果这是从旧版 AI Development Workflow 迁移来的已有项目：

1. 保留旧 Notion / Git / Decision 中仍然有效的项目与产品事实；
2. 不因为旧页面使用了 Primary / Child / Project Bind 等旧术语就丢弃其中的真实业务结论；
3. 不继续执行已经被当前 `main` 替代的旧流程规则；
4. 旧 Notion 不要求 Owner 手工整体迁移；
5. Project Manager 自己读取、理解和映射旧结构，再形成当前 Project Baseline；
6. 后续按当前 Workflow 写入新的 Project / Product Memory，旧记录保留为历史来源；
7. 如果最近对话 PDF 与旧 Notion / Git 存在差异，先区分：
   - PDF = Recent Working Context / Owner recent correction；
   - Notion = Durable Project / Product Memory；
   - Git / Runtime / Tests / Evidence = Technical Truth；
   然后做 Minimum Necessary Re-Anchor，不以任何单一来源静默覆盖其他来源。

对于旧项目接班，推荐顺序：

```text
Role Bootstrap
→ Conversation Succession + PDF
→ Project Onboarding
→ Notion / Git / Runtime calibration
→ Current Project Baseline
→ Continue previous stopping point
```

接班 PDF 用来恢复“最近怎么讨论到这里”；Project Onboarding 用来恢复“项目当前正式状态是什么”。

## 6. 完成标准

Project Manager 不需要等到“所有未知都消失”才开始工作。

当以下内容已经足够可靠时即可进入正常项目管理：

- 项目目标和非目标足够清楚；
- 技术结构已经由 AI 自己恢复到可工作程度；
- 当前优先级明确；
- 没有阻止下一步的关键未知；
- 下一阶段和 First Action 可以明确。

如果仍有未知，但不影响当前工作，记录后继续。

# END OF PROJECT ONBOARDING
