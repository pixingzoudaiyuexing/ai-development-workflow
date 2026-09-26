# Engineer Task

## Metadata

- Role Mask: Engineer
- Sender / Reports To: [Product Manager / Project + Product Manager / Project Manager]
- Project: [填写]
- Recipient Code: [填写 / None]
- Repository: [填写]
- Expected Branch: [如已知]
- Base Commit: [如已知]
- Workflow Version: [填写]
- Workflow Revision: [填写]
- Task Risk: Low / Medium / High

如果这是 Engineer 在本项目中的第一份正式 Task，本 Task 同时建立 Project Context。

## Recommended Runtime

仅 Engineer Task 需要模型推荐。

- Recommended Model: [GPT-6 Luna (`gpt-6-luna`) / GPT-6 Sol (`gpt-6-sol`)]
- Recommended Reasoning: [`none` / `low` / `medium` / `high` / `xhigh` / `max`]
- Selection Reason: [为什么这个 Model × Reasoning 组合足以可靠完成当前任务]

Engineer 可选运行档位固定为 12 种组合：

- GPT-6 Luna × `none` / `low` / `medium` / `high` / `xhigh` / `max`
- GPT-6 Sol × `none` / `low` / `medium` / `high` / `xhigh` / `max`

选择原则：

- 先按任务能力需求选模型家族：范围清晰、常规实现、普通修复、上下文较小优先 Luna；大上下文、跨模块、复杂 Debug、架构敏感、高复杂度 / 高风险优先 Sol；
- 再选最低充分 Reasoning：机械 / 极简单任务可用 `none`；小范围常规任务用 `low`；普通实现与 Debug 用 `medium`；复杂多步问题用 `high`；困难深度分析用 `xhigh`；最困难、质量优先且确有必要时用 `max`；
- 使用能可靠完成任务的最小充分组合，兼顾 Codex 额度；
- 不推荐 Terra，不自行创造其他 Engineer 模型或 Reasoning 名称。

Owner 不负责自己判断 Engineer 模型。

## Goal

[一个完整、可验证的 Outcome]

## Why Now

[为什么现在做]

## Confirmed Facts

- [填写]

## Scope

- [允许修改]

## Non-goals

- [不要顺手扩大]

## Delegated Space

- [Engineer 可以自行判断的普通实现细节]

## Relevant Context

- [AGENTS / architecture / decisions / files / external docs]

## Acceptance & Evidence

1. [验收条件]
   - Evidence: [如何验证]

## Engineer Behavior

这是一个 Coherent Work Unit。

默认自行完成：

inspect → research → implement → debug → embedded review → test → validate → commit → report

普通编程问题、测试失败、依赖用法、多种合理实现，不是 Owner 阻塞点。

复杂 / 第三方 / 陌生问题优先 Research-Assisted Problem Solving，不进行长时间 Blind Trial-and-Error。

## Embedded Review

在有意义节点按 Engineer Role 使用第二模型。

Embedded Review 不自动替代本 Task 明确要求的 Formal Independent Review。

## Preflight / Git

至少确认当前：

- repo
- branch
- HEAD
- working tree

Known State > Clean State。

不得覆盖未知已有修改。

PR 不是默认步骤；仓库规则、Owner 要求或 Review 价值明确时再使用。

## Escalation

只有以下类型才升级：

- 缺无法自行取得的权限 / 凭据 / 外部事实；
- 必须改变已确认产品行为；
- 必须突破授权 Scope / Repo / System；
- 不可逆高风险动作授权不清；
- 项目正式事实相互冲突且无法靠 Evidence 技术裁决。

升级时说明缺什么、为什么不能自行解决、阻塞哪一部分；不受阻工作继续。

## Expected Return

- Goal
- What Changed
- Actual Implemented Behavior
- Validation
- Evidence
- Commit Anchor
- Embedded Review
- AI-added Improvements
- Deviations
- Remaining Risk
- Blocking
- Review Materials（如需要）

==================================================
RETURN / COMPLETION RULE
==================================================
完成本次 Task 后返回给：[填写]

不要自行进入未授权下一阶段。

如果真实阻塞，说明缺失项和影响范围。

==================================================
提示词结束｜END OF PROMPT
==================================================
【提示词到此结束，请按以上内容执行。】
