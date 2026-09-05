# Codex Task

## Task Metadata

- Project: [填写]
- Repository: [填写]
- Expected Branch: [如已知]
- Base Commit: [如已知]
- Task Risk: Low / Medium / High
- Review Gate: None / Design Review Completed / Code Review Required

## Recommended Codex Runtime

- Recommended Model: Luna / Terra / Sol
- Recommended Reasoning: Light / Medium / High
- Selection Reason: [说明实现复杂度、额度与风险权衡]

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
- [是否要求独立 commit]

## Stop Point

完成实现与验证后停止，输出 `CODEX-REPORT` 所需信息。不要未经要求进入下一阶段或额外重构。
