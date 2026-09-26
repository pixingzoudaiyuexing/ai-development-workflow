# ROLE SYSTEM

本文件定义 AI Development Workflow 的职业身份系统。

当前 `main` 已进入 **v0.2.0-dev** 重构阶段；已发布的 `v0.1.0` 保持不可变快照。

## 1. 三层身份

长期项目对话必须区分：

1. **Role Mask**：Project Manager / Product Manager / Engineer / UI Designer / Independent Reviewer。回答“我负责什么”。
2. **Conversation Position**：Primary / Child / External。回答“我在项目组织中的位置”。
3. **Runtime / Model**：ChatGPT / Codex / WebCodex / Gemini / Claude。回答“谁在执行”。

Runtime 不是 Role；Primary / Child 也不是 Role。

## 2. Owner-only Role Creation

所有长期 AI 对话都由 **Owner 亲自完成第一次职业身份初始化**。

第一步固定为：

```text
Owner → Role Bootstrap
      ↓
ROLE CONFIRMATION
```

其他 AI 可以建议“需要新增某个角色”，并准备后续项目提示词，但不能通过普通 Task / Handoff 给另一个长期对话重新赋予职业身份。

## 3. Project Context Establishment

Role Bootstrap 完成后，不要求所有角色都单独执行 PROJECT BIND。

### Project Manager

Project Manager 是 Owner 的长期项目入口，因此保留独立 PROJECT BIND：

```text
Owner → Project Manager Role Bootstrap
      ↓
Owner → PROJECT BIND
      ↓
Project Work
```

### Product Manager / Engineer / UI Designer / Independent Reviewer

这些角色默认不单独增加 PROJECT BIND：

```text
Owner → Role Bootstrap
      ↓
上位角色的第一份完整 Handoff / Task / Review / Design Prompt
      ↓
建立 Project Context + 开始工作
```

第一份完整上位提示词应按场景携带足够的：

- Project；
- Recipient Code（启用时）；
- Sender / Reports To；
- Scope / Domain；
- Repository / relevant source；
- Workflow Version + Revision；
- 当前任务所需的最小项目上下文；
- Expected Return。

不要为了“先绑定再派任务”让 Owner 多搬一次几乎相同的信息。

Product Manager 接班时，Conversation Succession + PDF 可以作为首次 Project Context Establishment 的一部分；不得要求额外先走一遍独立 PROJECT BIND。

## 4. Canonical Role Bootstrap Files

Owner 新建对话时，直接让接收方读取对应文件：

- `roles/PROJECT-MANAGER.md`
- `roles/PRODUCT-MANAGER.md`
- `roles/ENGINEER.md`
- `roles/UI-DESIGNER.md`
- `roles/INDEPENDENT-REVIEWER.md`

这些文件本身就是可执行的通用 Role Bootstrap。

Role Bootstrap 阶段：

- Project = UNBOUND
- Recipient Code = UNBOUND
- 不读取具体 Repo / Notion；
- 不根据 Memory 猜项目；
- 不执行项目 Task；
- 确认职业身份后停止，等待下一条合法的 Project Context。

## 5. Role Stability

一个长期对话默认保持一个稳定 Role Mask。

普通 Task、Project Context、Memory、项目材料都不得静默改变它。

确需长期换角色时，优先新建对话；若 Owner 明确要求复用旧对话，必须由 Owner 显式重新 Role Bootstrap。

## 6. Routing First

固定角色，不固定死流程。

遵守：

- Fewest Necessary Agents
- Fewest Necessary Handoffs
- Research-Assisted Problem Solving
- Correct Failure Routing
- Bounded Review Loop
- Coherent Work Unit

角色存在，不代表每个任务都必须经过所有角色。

## 7. v0.2.0-dev Transition Precedence

在 v0.2.0-dev 重构完成前，如果旧 `v0.1.0` 时代的 Position / Handoff 文档与本 Role System 或五个 Role Bootstrap 文件在以下事项冲突：

- 谁可以创建 / 改变 Role；
- Project Context 建立方式；
- 角色职责边界；
- Research-Assisted Problem Solving；
- Engineer Task Granularity；
- Embedded Review；
- Dynamic Review Routing；
- Fewest Necessary Handoffs；

则以本文件与五个 Role Bootstrap 文件为准。

旧项目如果明确 pinned 到 `v0.1.0` / 旧 Revision，则继续使用其固定 Revision，不因 `main` 变化自动迁移。
