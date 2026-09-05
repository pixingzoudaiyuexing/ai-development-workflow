# EMERGENCY / HOTFIX LANE

Hotfix 的原则是：**Delay, don't skip.**

生产事故时优先恢复服务、阻止数据损失和安全扩大；可以延后部分设计审查与长期文档更新，但不能永久跳过。

## 1. 进入 Hotfix Lane

适用于：

- 生产不可用；
- 正在扩大影响的数据错误；
- 严重安全事件；
- 必须立即恢复的关键故障。

## 2. Hotfix 阶段

尽量：

- 先记录当前 production / commit / branch 状态；
- 建立最小可回滚点；
- 保留 logs / errors / health evidence；
- 做最小必要修改；
- 避免无关重构；
- 能 dry-run / staging 验证时优先使用。

## 3. UNRECONCILED HOTFIX

如果生产环境发生了尚未回填 Git 的手工修改，项目进入：

```text
UNRECONCILED HOTFIX
```

此状态允许：

- 继续恢复服务；
- 继续诊断；
- 完成必要紧急修复。

此状态禁止：

- 开始新的普通 Feature 开发。

必须先完成：

```text
Production actual state
→ Reconcile with Git
→ Diff
→ Test
→ Commit
→ Required Review（若命中 Risk Gate）
→ RECONCILED
```

## 4. 恢复服务后的补交流程

根据事故影响补：

- Root Cause Review；
- 回归测试；
- 独立 Review（High Risk）；
- Architecture / ADR 更新（若长期事实发生变化）；
- STATUS checkpoint（若达到重大阶段）；
- 确认生产与 Git 已重新一致。

Hotfix 不能成为绕过 Workflow 的长期后门。
