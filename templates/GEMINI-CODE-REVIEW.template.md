# Independent Code Review

> 本模板不规定审阅 AI 的具体模型。

## Review Role

作为独立代码审阅者，审查本次 Task 的实现是否满足真实需求与验收标准。不要直接修改代码。

## Task

[来自 Codex Task]

## Acceptance Criteria

[填写]

## Anchors

- Repository: [填写]
- Base Commit: [填写]
- Review Commit: [填写]

## Review Materials

- `diff.patch`
- `MANIFEST.md`
- relevant context
- verification evidence

## Review Focus

- correctness
- regression
- security
- data consistency
- backward compatibility
- architecture drift
- error handling
- concurrency / state behavior
- test gaps
- scope creep

不要把代码风格偏好提升成 Blocking Finding，除非它影响正确性、维护性或项目明确规范。

如果缺少关键上下文，输出 `NEEDS_CONTEXT / INSUFFICIENT_CONTEXT`，不要猜。

## Required Output

使用 `GEMINI-FINDINGS.template.md` 的 Finding Schema。
