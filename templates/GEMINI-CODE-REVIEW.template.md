# Gemini Code Review

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

- Review Directory (Mac-accessible absolute path): [由 ChatGPT 根据 Codex 核实结果直接填写；无法确认时明确说明，不得编造]
- Key Files (absolute paths): [由 ChatGPT 填入实际审核文件路径，如 REVIEW.md、MANIFEST.md、diff.patch；无本地路径则说明真实材料位置与访问方式]
- `diff.patch`
- `MANIFEST.md`
- relevant context
- verification evidence

请先读取上述实际可访问的审核目录 / 文件，再开展审查。不得要求 Owner 从其他消息手动补充路径。

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
