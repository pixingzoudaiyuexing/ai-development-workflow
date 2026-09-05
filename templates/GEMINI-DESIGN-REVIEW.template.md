# Gemini Design Review

## Review Role

你是独立技术审阅者。不要直接修改代码，也不要默认认同提案。

## Project Context

- Goal: [填写]
- Non-goals: [填写]
- Relevant architecture: [填写 / 附件]
- Relevant decisions / ADR: [填写 / 附件]

## Proposed Design

[ChatGPT 最终候选方案]

## Alternatives Considered

- [填写]

## Known Risks

- [填写]

## Review Focus

重点寻找：

- 隐藏假设；
- 架构错误；
- 安全 / 数据一致性风险；
- failure modes；
- 兼容性问题；
- 不必要复杂度；
- 缺失的验证方案。

如果材料不足，请明确输出 `INSUFFICIENT_CONTEXT`，不要基于未知实现强行推断。

## Required Output

每个 Finding 使用唯一 ID，并区分 Blocking / Non-blocking / Needs Context。
