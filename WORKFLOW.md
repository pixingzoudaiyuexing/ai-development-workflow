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

长期事实仍以项目 Git 文档为锚点，例如：

- `AGENTS.md`
- `docs/PROJECT.md`
- `docs/ARCHITECTURE.md`
- `docs/DECISIONS.md` / `docs/adr/`
- `docs/ROADMAP.md`
- `docs/STATUS.md`（checkpoint only）

原则：**对话负责讨论与执行上下文，Git 文档负责长期事实。**

### 3.2 Primary Conversation

新项目的初始 Project Discovery 对话默认成为 **Primary Conversation（主对话）**。

主对话负责：

- 接收用户新增需求与方向变化；
- 产品、架构、跨 Repo 边界设计；
- 判断需求属于局部任务还是跨领域任务；
- 决定是否需要创建、复用或结束 Child Conversation；
- 生成子对话可直接复制的启动消息；
- 指定子对话需要读取的 Workflow 文档、项目文档、Repo 与当前任务；
- 接收子对话返回结果并决定下一步。

用户不负责判断“应该开几个对话、属于前端还是后端、是否跨 Repo”。这些属于主对话的编排职责。

### 3.3 Child Conversation

Child Conversation（子对话）是有明确工作边界的长期或阶段性工作区，例如：

- Backend / API
- Frontend / Web
- Client
- Deployment / Operations
- 某个长期独立模块

子对话不重新拥有整个产品的架构裁决权。它应优先处理自己的 Repo / Scope；如果发现当前需求影响产品规则、核心架构、其他 Repo 或既有 Contract，应暂停扩大范围并返回 Primary Conversation。

子对话可以长期存在，也可以只是某个阶段的专项对话。是否创建新子对话由 Primary Conversation 根据复杂度、持续时间、Repo 边界和上下文隔离收益决定，不由用户提前猜测。

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

不要要求零代码用户充当人工路由器。

### 3.6 Primary Re-Sync Gate

Child Conversation 返回结果后，Primary Conversation 不得只依赖历史 Project Memory 或文字摘要继续编排。

如果下一步任务依赖该 Child 的真实代码状态、架构变化、Contract 变化或长期文档变化，Primary 必须先刷新相关 Git 事实：

1. 读取返回包中的 Repo / branch / commit anchor；
2. 读取本次明确受影响或已更新的核心 Git 文档；
3. 必要时核对相关 diff / Implementation Report / Evidence；
4. 然后才生成依赖这些变化的下一项 Task。

`STATUS.md` 只在它本来就属于当前 checkpoint、被更新或恢复流程需要时读取；不要为了 Re-Sync 强迫每个 Task 更新 STATUS。

如果 Primary 无法直接访问对应 Repo / 文档，应让 Child / Codex 提供精确的文件内容、diff 或结构化 Handoff；不得把“去 Git 里自己找这些文件”变成零代码用户的任务。

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
- 必要的 Review / Evidence Gate 完成。
