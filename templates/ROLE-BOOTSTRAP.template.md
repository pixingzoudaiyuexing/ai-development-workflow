# Role Bootstrap Template — DEPRECATED ON main

> `main` 已进入 v0.2.0-dev。
> 旧的“由发送方 AI 填写一份 Role Bootstrap 模板”方式已停止作为新工作流入口。

Owner 新建长期对话时，直接让接收方读取对应的 canonical Role Bootstrap：

- Project Manager: `roles/PROJECT-MANAGER.md`
- Product Manager: `roles/PRODUCT-MANAGER.md`
- Engineer: `roles/ENGINEER.md`
- UI Designer: `roles/UI-DESIGNER.md`
- Independent Reviewer: `roles/INDEPENDENT-REVIEWER.md`

固定顺序：

```text
Owner → Role Bootstrap
→ ROLE CONFIRMATION
→ Owner → PROJECT BIND
→ Task / Handoff
```

旧项目如 pinned 到 v0.1.0 / 旧 Revision，继续按其固定版本执行。
