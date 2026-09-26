# PRIMARY CONVERSATION

> Primary 是 Conversation Position，不是职业角色。

大型项目中 Primary 常由 Project Manager 承担；小型项目也可能由 Product Manager 承担。

Primary 位置本身不授予额外的产品、架构、代码或 Notion 权限。实际职责由当前 Role Mask 决定。

## 1. Primary Position

Primary 的位置意义：

- 作为 Owner 的当前主要入口；
- 接收跨 Child / External 返回；
- 保持当前项目工作的连续性；
- 在当前 Role 权限内完成路由和下一步安排。

如果 Primary = Project Manager，则项目级职责读取 `roles/PROJECT-MANAGER.md`。

如果 Primary = Product Manager，则产品职责读取 `roles/PRODUCT-MANAGER.md`。

## 2. New Project Manager Primary

新的 Project Manager Primary：

```text
Role Bootstrap
→ PROJECT-ONBOARDING.md
→ Project Baseline
→ Project Work
```

Owner 不负责提供技术结构；Project Manager 自己调查并引导 Owner。

## 3. Succession

Project Manager 对话过长或需要接班时，使用：

`templates/succession/PROJECT-MANAGER-SUCCESSION.md`

Owner 同时上传上一任对话 PDF。

恢复策略：

Tail First → Expand Backward as Needed。

Conversation PDF 是 Working Context；Git / Notion / Formal Decisions 仍用于必要校准。

不要求旧 Primary 在突然超长前持续维护逐句 Continuity Log。

## 4. Child / External Coordination

需要新的长期角色时：

1. Project Manager / Product Manager 判断是否真的需要；
2. Owner 先发送对应 Role Bootstrap；
3. 上位角色生成第一份完整 Handoff / Task；
4. 该提示词同时建立 Project Context 并开始工作。

不要为非 Project Manager 角色额外增加 Project Bind。

# END
