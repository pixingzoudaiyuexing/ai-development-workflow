# WORKFLOW

## 1. AI 角色

### ChatGPT

负责：

- 项目发现与需求澄清；
- 产品与架构设计；
- 任务拆解；
- Task Risk 判断；
- Codex Task 生成；
- 综合 Codex 证据与独立审查意见；
- 技术裁决；
- 必要时设计 Evidence Gate 的最小可证伪实验。

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

### 独立审阅者

负责：

- Design Review；
- Code Review；
- Security / Failure Mode Review；
- 独立第二意见；
- 明确指出缺失上下文，而不是基于未知实现强行推理。

Workflow 不管理独立审阅者使用哪一个具体模型。

## 2. 标准开发循环

```text
需求
↓
ChatGPT：分析 / 设计 / Task Risk
↓
必要时：Independent Design Review
↓
ChatGPT：最终方案
↓
Codex Task
↓
Codex：Preflight → 实现 → 验证 → Evidence → Report
↓
ChatGPT：核对验收与 Risk Gate
↓
High Risk：Independent Code Review
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

## 3. Codex Preflight

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

## 4. Codex Model Routing

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

## 5. Claims vs Evidence

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

## 6. Acceptance Evidence

每个正式 Task 的 Acceptance Criteria 应尽量对应可验证 Evidence。

示例：

```text
要求：/health 返回正常
证据：实际请求 → HTTP 200 → 预期响应体

要求：修复回归 Bug
证据：修复前测试失败 → 修复后测试通过 → 相关回归测试通过
```

没有实际运行的验证，不得写成“已通过”。

## 7. Ground Truth Verification

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

## 8. Evidence Gate

当 ChatGPT 与独立审阅者出现会影响实施方向的重大、无法靠已有材料解决的分歧时：

1. 停止观点争论；
2. ChatGPT 把争议转换成可证伪假设；
3. ChatGPT 生成 Verification Task；
4. Codex 执行安全、最小的验证；
5. 返回 tests / logs / benchmark / runtime behavior 等证据；
6. 再进行裁决。

零代码用户不负责设计验证实验。

如果实验需要生产环境、可能破坏数据或无法安全执行，必须先停下并改用安全的 staging、dry-run、只读验证或其他替代证据。

## 9. Multi-Repo 最小支持

一个产品可以对应多个 Git Repo，一个 ChatGPT Project 也可以讨论这个产品的多个 Repo。

但：

- 一个 Codex Task 默认只修改一个 Repo；
- 必须跨 Repo 时，Task 明确列出每个 Repo 的 branch / commit 锚点；
- 明确 cross-repo contract 与验收标准；
- v1 不做复杂的多仓库自动编排。

## 10. 完成定义

代码写完不等于任务完成。

中型及以上 Task 至少需要：

- 目标实现；
- 项目适用验证；
- diff 检查；
- 未验证内容说明；
- Implementation Report；
- Risk Assessment；
- 必要的 Review / Evidence Gate 完成。
