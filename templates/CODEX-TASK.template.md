# Codex Task

## Task Metadata

- Project: [填写]
- Recipient Code: [本项目已启用时，自动填写目标接收对话的固定暗号；未启用写 None]
- Repository: [填写]
- Expected Branch: [如已知]
- Base Commit: [如已知]
- Task Risk: Low / Medium / High
- Review Gate: None / Design Review Completed / Code Review Required

## Recommended Codex Runtime

> ChatGPT 派发本 Task 给用户时，必须先在 Transfer Block 外明确显示：
> `Codex Model: <Luna/Terra/Sol> | Reasoning: <Light/Medium/High + 轻量/中/高>`
> 用户不负责自己判断档位。

- Recommended Model: Luna / Terra / Sol
- Recommended Reasoning: Light（轻量） / Medium（中） / High（高）
- Selection Reason: [说明为什么这是能可靠完成任务的最小充分档位，并兼顾额度]
- Runtime Principle: Smallest Sufficient Runtime

## Goal

[必须实现什么]

## Background

[当前现状和为什么做]

## Scope

- [允许修改]

## Non-goals

- [禁止顺手扩大范围]

## Relevant Context

- [AGENTS / PROJECT / ARCHITECTURE / ADR / 文件路径]

## Implementation Requirements

- [填写]

## Acceptance Criteria & Evidence

1. [条件]
   - Evidence: [如何客观验证]

## Preflight

至少确认：

```text
git status
git branch --show-current
git rev-parse HEAD
```

Known state > Clean state。不要覆盖未知修改。

## Validation

- [项目适用测试 / build / lint / smoke]

## Git Requirements

- 检查 diff；
- 不执行 destructive Git operation；
- PR 默认不是必选步骤；仅在仓库规则 / branch protection、Owner 明确要求、Review Gate 明确需要 PR，或 Primary 基于具体大型/高风险审查需要决定使用时创建 PR。其余情况下，在仓库允许时可完成验证后直接提交目标分支，不为形式机械增加 branch → PR → merge 链路；
- [是否要求独立 commit]

如果 `Review Gate = Code Review Required`：

- 优先把本 Task 修改形成清晰、可审查的 result commit；
- 保留明确的 base commit → review commit 锚点；
- 不得生成一个会静默遗漏未提交 Task 修改的 Review Pack；
- 若存在与当前 Task 无关的 dirty state，必须明确记录并确保不会混入审查范围；
- Codex 负责生成 Review Pack：运行 `tools/review-pack/`、收集允许的 Evidence、生成 patch / manifest / pack，并输出可直接交给独立审阅者的 ZIP 或结构化 Markdown fallback；
- 在 Review Handoff 中附审核材料目录及关键文件的真实绝对路径，说明路径所在环境与 Mac 本地 Gemini 是否可直接访问；若只有远程路径，须明确标注，不得虚构 Mac 路径。按 `HANDOFF.md` 的 Gemini 桌面客户端审核材料路径规则交接。
- 不得要求零代码用户自己制作 patch、提取 exit code、整理 raw logs 或手工拼装 Review Pack。

## Difficult Debugging / Early External Research

遇到非显而易见、可能已有外部先例的故障时，尽早向派发任务的 ChatGPT 返回精简 Diagnostic Return（准确错误、环境 / 版本、已尝试方法及结果、相关证据、Git / 未提交状态）。**即使常规调试持续产生新证据，也可以请求 ChatGPT 同步检索官方文档、GitHub Issues / Discussions 与同类项目**，无需等到失败若干次。对同一问题缺乏新依据的重复修改 / 重试应止损；不冲突的已授权工作可继续。ChatGPT 负责实际检索、核对适用条件，再派发有依据的下一步验证；不要让用户手工搜索、整理技术材料，亦不要直接照搬未核实的第三方脚本。遵循 `PRIMARY-CONVERSATION.md` 的 Difficult Debugging 规则。

## Stop Point

完成实现与验证后停止，输出 `CODEX-REPORT` 所需信息。若 Review Gate 要求独立 Code Review，同时输出 Review Pack 或明确说明无法生成的阻塞点。不要未经要求进入下一阶段或额外重构。

> **Anti-Stagnation / STOP 来源：** Primary 增设强制 STOP 时，须在条件旁简短注明其来源（Owner 明确要求、已生效项目约束、实际命中的 Workflow 技术门禁或有具体证据的真实技术阻断）。AI 的一般性担忧、无关外围核验失败及与当前独立测试无直接关系的生产级要求不得阻断任务。实际 STOP 时报告受影响范围；能独立安全完成的已授权工作继续推进，不要求 Owner 额外填表。
