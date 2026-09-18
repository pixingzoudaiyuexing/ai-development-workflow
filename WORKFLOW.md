# WORKFLOW

## 1. AI 角色

### ChatGPT

负责：

- 项目发现与需求澄清；
- 产品与架构设计；
- 任务拆解；
- Task Risk 判断；
- Codex Task 生成；
- 综合 Codex 证据与 Gemini 审查意见；
- 技术裁决；
- 必要时设计 Evidence Gate 的最小可证伪实验；
- 在长期项目中承担 Conversation Orchestration，决定是否需要子对话以及如何交接。

默认不作为主代码修改者。

### Codex

负责：

- 读取真实仓库与项目规则；
- 实施代码；
- 调试；
- 测试、构建、lint、typecheck 等项目适用验证；
- Git 状态、diff、commit；
- Implementation Report；
- Claims 与 Verifiable Evidence；
- 生成跨 AI Review Pack（需要时）。

除非明确要求，Codex 是默认唯一代码实施者。

### Gemini

负责：

- Design Review；
- Code Review；
- Security / Failure Mode Review；
- 独立第二意见；
- 明确指出缺失上下文，而不是基于未知实现强行推理。

Gemini 默认不直接修改项目代码。

## 2. 标准开发循环

```text
需求
↓
ChatGPT：分析 / 设计 / Task Risk
↓
必要时：Gemini Design Review
↓
ChatGPT：最终方案
↓
Codex Task
↓
Codex：Preflight → 实现 → 验证 → Evidence → Report
↓
ChatGPT：核对验收与 Risk Gate
↓
High Risk：Gemini Code Review
↓
ChatGPT：Accepted / Rejected / Needs Evidence
↓
必要时 Codex Fix
↓
最终验证
↓
验收 / 发布
↓
仅在 DOCUMENTATION.md 触发条件成立时更新长期文档
```

## 3. ChatGPT Project 与 Conversation Orchestration

### 3.1 一个产品，一个 ChatGPT Project

一个长期产品原则上使用一个 ChatGPT Project。一个产品可以包含多个 Git Repo，也可以包含多个职责明确的 ChatGPT 对话。

Project Memory 可以帮助同一 Project 内的对话引用相关历史，但不得把它当作完整、确定、永久同步的事实数据库。

长期复杂、多 Repo 或多 Conversation 项目可以启用 Notion 作为 **Project Knowledge Layer**，专门保存项目 Core Rules、Current State 和正式 Decisions。它不替代 Git，也不保存完整聊天。

Repo 内技术事实仍以项目 Git 文档、真实代码、Runtime 与 Evidence 为锚点，例如：

- `AGENTS.md`
- `docs/PROJECT.md`
- `docs/ARCHITECTURE.md`
- `docs/DECISIONS.md` / `docs/adr/`
- `docs/ROADMAP.md`
- `docs/STATUS.md`（checkpoint only）

原则：

```text
GitHub Workflow = AI 应该怎么工作
Notion           = 项目现在怎么定（启用时）
Git / Runtime    = 技术上现在实际是什么
Chat / Memory    = 讨论与临时上下文
```

发生冲突时不凭优先级猜测，进入 Ground Truth Verification。

### 3.2 Primary Conversation

新项目的初始 Project Discovery 对话默认成为 **Primary Conversation（主对话）**。详细角色边界见 `PRIMARY-CONVERSATION.md`.

主对话负责：

- 接收用户新增需求与方向变化；
- 产品、架构、跨 Repo 边界设计；
- 判断需求属于局部任务还是跨领域任务；
- 决定是否需要创建、复用或结束 Child Conversation；
- 生成子对话可直接复制的启动消息；
- 指定子对话需要读取的 Workflow 文档、项目文档、Repo 与当前任务；
- 接收子对话返回结果并决定下一步；
- 项目启用 Notion 时，负责项目级 Knowledge Re-Anchor、正式批准与写入。

用户不负责判断“应该开几个对话、属于前端还是后端、是否跨 Repo”。这些属于主对话的编排职责。

凡是 ChatGPT 需要用户把消息转发给另一个 Conversation、Codex 或 Gemini，必须按 `HANDOFF.md` 的 **User Relay Rule** 输出一个单一、完整、自包含的一键复制 Transfer Block。用户只负责搬运，不负责从解释正文中挑选、拼接或修改技术内容。

### 3.3 Child Conversation

Child Conversation（子对话）是有明确工作边界的长期或阶段性工作区。详细角色边界与 Re-Anchor 规则见 `CHILD-CONVERSATION.md`。例如：

- Backend / API
- Frontend / Web
- Client
- Deployment / Operations
- 某个长期独立模块

子对话不重新拥有整个产品的架构裁决权。它应优先处理自己的 Repo / Scope；如果发现当前需求影响产品规则、核心架构、其他 Repo 或既有 Contract，应暂停扩大范围并返回 Primary Conversation。

子对话可以长期存在，也可以只是某个阶段的专项对话。是否创建新子对话由 Primary Conversation 根据复杂度、持续时间、Repo 边界和上下文隔离收益决定，不由用户提前猜测。

项目启用 Notion 时，Child 可以读取 Primary 指定的项目知识用于校准，但不得直接修改项目级正式知识；需要变化时提交 Knowledge Update Candidate 并返回 Primary。

### 3.4 Conversation Topology 与 Context Budget

Project Discovery 后，如果项目存在多个长期工作流或多个 Repo，Primary Conversation 应主动给出建议的 Conversation Topology，例如：

```text
Project: CloudGap
│
├── Primary：产品 / 需求 / 架构 / 调度
├── Child：CloudGap API
└── Child：CloudGap Web
```

每个建议的 Child Conversation 必须同时给出：

- 建议名称；
- 为什么需要；
- 负责的 Repo / Domain；
- 需要读取的 Workflow 文档；
- 需要读取的项目 Git 文档；
- 当前第一个任务；
- Scope / Non-goals；
- 什么时候必须返回主对话；
- 完成后需要带回什么结果；
- 一段用户可直接复制到新对话的启动消息。

上下文遵循 **Minimum Sufficient Context**：

- 只预加载当前职责和任务需要的 Workflow / 项目文档；
- 不因为“可能以后有用”就把整个项目文档集塞进 Child Conversation；
- Primary 应明确当前不需要预加载的明显无关领域 / 文档；
- Child 如果后续被真实问题阻塞，再请求补充具体上下文，而不是一开始全量加载。

使用 `templates/CONVERSATION-HANDOFF.template.md`。

### 3.5 新需求如何路由

用户可以始终先把新需求告诉 Primary Conversation。

Primary Conversation 负责选择：

```text
留在主对话分析
或
交给现有子对话
或
创建新的子对话
或
拆成多个有顺序的 Repo Task
```

如果用户已经处于某个子对话，并且需求明显属于该子对话的既有 Scope，可以直接处理；一旦发现跨产品 / 架构 / Repo 边界，再升级回 Primary Conversation。

不要要求零代码用户充当人工路由器，也不要要求用户充当 Handoff 编辑器。任何需要用户转发的 ChatGPT 消息都必须由发送方 ChatGPT 整理成最终可发送版本。

### 3.6 Primary Re-Sync Gate

Child Conversation 返回结果后，Primary Conversation 不得只依赖历史 Project Memory 或文字摘要继续编排。

如果下一步任务依赖该 Child 的真实代码状态、架构变化、Contract 变化或长期文档变化，Primary 必须先刷新相关 Git 事实：

1. 读取返回包中的 Repo / branch / commit anchor；
2. 读取本次明确受影响或已更新的核心 Git 文档；
3. 必要时核对相关 diff / Implementation Report / Evidence；
4. 然后才生成依赖这些变化的下一项 Task。

`STATUS.md` 只在它本来就属于当前 checkpoint、被更新或恢复流程需要时读取；不要为了 Re-Sync 强迫每个 Task 更新 STATUS。

如果 Primary 无法直接访问对应 Repo / 文档，应让 Child / Codex 提供精确的文件内容、diff 或结构化 Handoff；不得把“去 Git 里自己找这些文件”变成零代码用户的任务。

### 3.7 Project Knowledge Re-Anchor

项目启用 Notion 时，长期对话不得只靠历史聊天或 Memory 维持项目规则。

Re-Anchor 的 canonical Trigger：

- Primary → `PRIMARY-CONVERSATION.md`
- Child → `CHILD-CONVERSATION.md`

Project Root 隔离、Notion 写权限、Knowledge Update Candidate 与 Minimum Sufficient Knowledge 的 canonical 规则统一见 `KNOWLEDGE-MANAGEMENT.md`。

本文件只定义它属于标准开发流程，不复制角色 Trigger，避免同一规则在多个文件独立演化。

### 3.8 Affected Active Children 传播

Notion / Git 被正确更新，并不代表已经存在的长期 Child Conversation 会自动知道变化。

当 Primary 批准的变化影响以下任一内容时：

- shared / cross-repo Contract；
- Project Core Rule；
- project-level Decision；
- 另一个 Child 的 Repo / Domain Scope 或关键假设；

Primary 必须明确列出：

```text
Affected Active Children:
- <Child name>

Before continuing related work:
- Re-Anchor: <Core Rules / Decision IDs / Current State>
- Re-Sync: <Git docs / contract / commit anchors, if needed>
```

受影响 Child 在继续**依赖该变化的相关工作**前，必须先收到最小 Update Handoff 并完成 Re-Anchor / 必要的 Git Re-Sync。

不受影响的 Child 不需要机械同步。不要建立实时广播系统；遵守 `HANDOFF.md` 的 No Magic Arrows。

## 4. Codex Preflight

开始非简单任务前至少确认：

```text
git status
git branch --show-current
git rev-parse HEAD
```

原则是 **Known state > Clean state**。

工作树不要求永远 clean，但：

- 不覆盖未知已有修改；
- 不擅自 reset；
- 不删除不属于当前任务的文件；
- 如果已有修改与当前任务冲突或难以区分，暂停并明确报告。

Remote Sync Check（例如 `git fetch`）是条件式操作：仅在存在远端依赖、网络与权限可用且当前任务需要确认远端状态时执行。

## 5. Codex Model Routing

正式 Codex Task 必须包含：

- Recommended Codex Model
- Recommended Reasoning Level
- Selection Reason

选择依据是：

- 实现复杂度；
- 上下文规模；
- 调试难度；
- Task Risk；
- 额度与效率。

默认指导：

- **Luna**：简单、边界明确、低复杂度的小改动；
- **Terra**：日常主力，普通功能、普通 Bug、跨若干文件的常规开发；
- **Sol**：高复杂度根因分析、核心架构实现、复杂跨模块逻辑或技术难度显著更高的任务。

Risk 与模型不是一一对应：高风险但机械的实现未必必须 Sol；低业务风险但极难调试的问题可能需要 Sol。

## 6. Claims vs Evidence

AI 的“我已经修复”“测试通过”“没有兼容问题”属于 Claim。

Evidence 可以包括：

- 实际命令与 exit code；
- 原始测试 / build 输出；
- 自动化测试；
- 独立 CI；
- staging / runtime 行为；
- HTTP response；
- 数据迁移 dry-run；
- UI 截图 / 预览；
- commit / diff。

统一原则：**任务风险越高，越必须依赖独立、可重复的验证，而不是 Agent 自述。**

## 7. Acceptance Evidence

每个正式 Task 的 Acceptance Criteria 应尽量对应可验证 Evidence。

示例：

```text
要求：/health 返回正常
证据：实际请求 → HTTP 200 → 预期响应体

要求：修复回归 Bug
证据：修复前测试失败 → 修复后测试通过 → 相关回归测试通过
```

没有实际运行的验证，不得写成“已通过”。

## 8. Ground Truth Verification

代码、文档、测试、运行行为、已确认产品要求和安全边界都只是事实来源的一部分。

发生冲突时：

```text
STOP
↓
明确冲突
↓
收集证据
↓
判断：代码错误 / 测试错误 / 文档过期 / 需求变化 / 环境异常
↓
修正真正错误的一方
```

禁止简单采用“代码永远正确”或“文档永远正确”。

裁决边界：

- 如果冲突是纯技术事实问题（代码 bug、测试与实现不一致、文档落后、环境异常等），由 Primary 基于 Evidence 做技术裁决；
- 如果冲突会改变用户已经明确确认的产品目标、业务规则、非目标或核心边界，Primary 必须先用非技术语言向用户说明冲突与可选方向，让用户确认“产品要 A 还是 B”；具体技术实现仍由 Primary 决定。

用户不负责判断代码、架构或验证方法，只负责确认真正的产品意图变化。

## 9. Evidence Gate

当 ChatGPT 与 Gemini 出现会影响实施方向的重大、无法靠已有材料解决的分歧时：

1. 停止观点争论；
2. ChatGPT 把争议转换成可证伪假设；
3. ChatGPT 生成 Verification Task；
4. Codex 执行安全、最小的验证；
5. 返回 tests / logs / benchmark / runtime behavior 等证据；
6. 再进行裁决。

零代码用户不负责设计验证实验。

如果实验需要生产环境、可能破坏数据或无法安全执行，必须先停下并改用安全的 staging、dry-run、只读验证或其他替代证据。

## 10. Multi-Repo 最小支持

一个产品可以对应多个 Git Repo，一个 ChatGPT Project 也可以讨论这个产品的多个 Repo。

但：

- 一个 Codex Task 默认只修改一个 Repo；
- 必须跨 Repo 时，Task 明确列出每个 Repo 的 branch / commit 锚点；
- 明确 cross-repo contract 与验收标准；
- v1 不做复杂的多仓库自动编排。

## 11. 完成定义

代码写完不等于任务完成。

中型及以上 Task 至少需要：

- 目标实现；
- 项目适用验证；
- diff 检查；
- 未验证内容说明；
- Implementation Report；
- Risk Assessment；
- 必要的 Review / Evidence Gate 完成；
- **Documentation Impact Check**：`NONE` 或命中 `DOCUMENTATION.md` 的具体更新项；
- **Knowledge Impact Check**：`NONE` 或 `Knowledge Update Candidate: PROPOSED`；
- 如果 Knowledge Candidate = `PROPOSED`，由 Primary 完成 `ACCEPTED / REJECTED / NEEDS_EVIDENCE`；
- 如果 Candidate = `ACCEPTED`，再明确 `Knowledge Sync: SYNCED | PENDING`。

正常任务命中 Git 长期文档 Trigger 时，应在关闭前同步相应 Git 文档；Hotfix 按 `EMERGENCY.md` 允许延后回填。

Notion 暂时不可用不阻塞安全的技术完成；允许 `Knowledge Sync: PENDING`。但任何后续设计、路由或 Task **如果依赖该 Pending 事实**，在继续前必须先完成同步，或由 Primary 显式重新验证该事实并把它完整带入 Handoff。无关工作可以继续。

如果 Primary 无法直接写 Notion，应生成“页面 + 完整可复制更新文本 + 更新后应看到的结果”，把用户操作降为粘贴 / 替换，而不是要求用户自己整理知识。
