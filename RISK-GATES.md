# RISK GATES

Risk Gate 用于决定 Evidence 和 Review 强度，不用于制造固定流水线。

上游在派发正式 Engineer Task 时必须明确 Task Risk 与 Formal Independent Review 状态：

- REQUIRED
- NOT REQUIRED
- CONDITIONAL

Engineer 不负责替上游静默补一个“默认 NOT REQUIRED”；如果实际工程调查发现风险升级或命中本文件的默认 Formal Review 条件，应触发 Review Requirement Mismatch 并返回上游。

## 1. Low

典型：

- 范围小；
- 行为明确；
- 易回退；
- 验证简单。

默认：

Engineer → Evidence → 上游验收。

Formal Independent Review 通常不需要。

## 2. Medium

典型：

- 普通新功能；
- 跨多个文件 / 模块；
- 有一定状态 / 回归 / 兼容风险。

要求更完整的验证。

是否 Formal Review 由上游根据实际风险和 Embedded Review 结果决定。

## 3. High

典型：

- auth / permission / security boundary；
- payment / billing；
- important data migration / deletion；
- irreversible infrastructure change；
- core protocol incompatibility；
- complex concurrency / state consistency；
- high-impact failure recovery；
- 明显可能造成数据损失 / 长时间服务中断。

High 要求：

- 更强 Acceptance Evidence；
- 更明确 rollback / recovery；
- 更严格 diff / runtime validation；
- 对安全、支付、重要数据迁移、不可逆高影响变化，默认需要 Formal Independent Review。

其他 High-complexity 情况由上游角色判断 Formal Review 是否提供实际独立价值，不为形式机械增加 Owner Relay。

## 4. Design Review

只有当设计选择本身存在真实高风险权衡时才在实现前增加 Design Review。

如果现有规范 / 架构已经把方案限定得很清楚，不机械增加。

## 5. Embedded Review

Engineer Embedded Review 是内部质量控制。

它可以减少低 / 中风险任务对 Formal Review 的需要，但不能自动替代需要独立性的高风险审查。

## 6. Risk ≠ Model

Task Risk 衡量做错后的影响。

Model / Reasoning 选择考虑实现难度、上下文、调试复杂度和可靠性。

两者不是一一对应。

# END
