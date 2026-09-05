# RISK GATES

风险路由使用两个维度：

```text
Project Tier + Current Task Risk
```

Project Tier 决定项目基础严格度；Task Risk 决定当前任务的审查强度。

## 1. Task Risk

### Low

典型特征：

- 范围小；
- 行为明确；
- 容易回退；
- 不影响关键边界；
- 验证简单。

默认流程：

```text
ChatGPT / 直接明确任务
→ Codex
→ Evidence
→ 验收
```

### Medium

典型特征：

- 跨多个文件或模块；
- 普通新功能；
- 有一定兼容 / 状态 / 回归风险；
- 但不命中 Hard Risk Trigger。

默认流程：

```text
ChatGPT
→ Codex
→ Evidence
→ ChatGPT 判断是否需要 Gemini 独立审查
```

### High

任何命中 Hard Risk Trigger 的任务自动 High，ChatGPT 不得因为“看起来不复杂”随意降级。

High 默认要求：

- 更强 Acceptance Evidence；
- Codex 完成后 Gemini Code Review；
- 必要时在 Codex 前做 Gemini Design Review。

## 2. Hard Risk Triggers

保持通用，不绑定具体项目。包括：

- 身份认证、权限模型或安全边界的重大变化；
- 重要数据迁移、不可逆数据修改或大范围删除；
- 核心支付 / 计费 / 资金逻辑变化；
- 对外 API / 协议出现重大不兼容变化；
- 核心架构替换或跨关键模块大规模重构；
- 复杂并发、状态一致性或故障恢复核心逻辑；
- 高影响、不可逆或难回滚的基础设施变化；
- 任何可能造成重大数据损失、安全问题或长时间服务中断的变更。

具体项目可在自己的 `AGENTS.md` 中补充“本项目哪些模块属于 High Risk”。

## 3. Design Review Gate

High 并不自动等于所有任务都需要 Design Review。

以下情况通常在 Codex 动工前做 Gemini Design Review：

- 命中 Hard Risk Trigger 且设计本身仍存在选择；
- 核心架构 / 安全边界正在改变；
- 错误设计会导致高昂返工或不可逆后果；
- 存在多个可行方案且权衡复杂。

如果设计已经由事实、规范或既有架构严格限定，可能只需要 High Risk Code Review。

## 4. Code Review Gate

所有 High Risk Task 在 Codex 完成并提供基本 Evidence 后，必须进入 Gemini Code Review。

Gemini 发现的问题回到 ChatGPT，由 ChatGPT标记：

- ACCEPTED
- PARTIALLY_ACCEPTED
- REJECTED
- NEEDS_EVIDENCE

出现重大分歧时进入 `WORKFLOW.md` 的 Evidence Gate。

## 5. Risk 与 Codex 模型不是同一维度

Task Risk 衡量“做错后影响多大”。

Codex 模型选择同时考虑“实现难度、上下文规模、调试难度、额度效率”。

因此 High Risk 不等于自动使用最强模型；Low Risk 也不等于技术上一定简单。
