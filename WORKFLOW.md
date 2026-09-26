# WORKFLOW

## 1. Identity Model

长期协作严格区分：

- **Role Mask**：Project Manager / Product Manager / Engineer / UI Designer / Independent Reviewer
- **Conversation Position**：Primary / Child / External
- **Runtime / Model**：ChatGPT / Codex / WebCodex / Gemini / Claude

Runtime 不是 Role；Primary / Child 也不是 Role。

## 2. Project Entry

Project Manager：

```text
Role Bootstrap
→ Project Onboarding
→ Project Baseline
→ Project Work
```

其他角色：

```text
Role Bootstrap
→ 第一份完整上位任务 / Handoff
→ Project Context + Work
```

不为了形式增加重复 Project Bind。

## 3. Normal Work Routing

不固定单一路线。

常见路径：

```text
Owner / Project Direction
↓
Project Manager / Product Manager
↓
Research（需要时）
↓
Engineer：Coherent Work Unit
↓
Implement → Embedded Review → Validate → Evidence
↓
上游验收
↓
Formal Independent Review（有实际价值 / 高风险时）
↓
Finding 返回真正负责的角色
```

Routing 遵守：

- Fewest Necessary Agents
- Fewest Necessary Handoffs
- Correct Failure Routing

## 4. Research-Assisted Problem Solving

复杂、未知、第三方相关问题，优先使用：

- 官方文档；
- GitHub upstream；
- Issues / Discussions；
- 类似开源实现；
- Web Research；
- 最小针对性实验。

先建立有依据的 Hypothesis，再验证。

外部实现是 Reference，不是项目 SSOT。

## 5. Coherent Work Unit

Engineer Task 默认按一个完整 Outcome 派发。

一个 Task 可以内部包含：

- inspect
- plan
- research
- implement
- debug
- embedded review
- test
- validate
- commit
- report

这些是 Engineer 内部步骤，不是 Owner Relay Gate。

只有真实 Gate 才拆：关键 PoC、跨 Repo Contract、不可逆动作、前序结果决定后续方向、真正并行、上下文失控或风险明显不同。

## 6. Embedded Review

Engineer 可以在有意义节点调用第二模型 Review，无需 Owner 逐次转发。

默认原则：

- Review at meaningful checkpoints, not every step.
- Embedded Review 是内部质量控制。
- 不自动替代所有 Formal Independent Review。
- Reviewer 意见是 Evidence / Input，不自动成为正确答案。

## 7. Dynamic Review Routing

Independent Reviewer 可审核：

- Product
- Architecture
- Code
- Security
- Data
- UI / UX
- Cross-repo Integration

Finding 回到真正负责的角色：

- Product → Product Manager
- Architecture / Project Boundary → Project Manager
- Engineering Defect → Engineer
- UI / UX → UI Designer / Product Manager
- Business Decision → Owner

工程缺陷可以直接 Engineer → Fix → Reviewer Verify，不机械绕路。

## 8. Owner Boundary

Owner 负责：

- 产品方向；
- 商业规则；
- 核心用户结果；
- 重大优先级；
- 上线 / 停止；
- 只有 Owner 才知道的业务事实。

AI 负责：

- 技术调查；
- 架构与实现方案；
- Repo / Conversation 路由；
- 测试与验证；
- 普通产品细节；
- 代码 / Git；
- Review / Evidence。

不要把技术选择转嫁给 Owner。

## 9. Truth Layers

```text
Git / Runtime / Tests / Evidence
= 技术事实

Notion
= Owner-facing Project / Product Memory

Conversation / PDF
= Working Context / Discussion History
```

讨论过 ≠ 决定了。

发生冲突时执行 Ground Truth Verification，不自动相信任何一层。

## 10. Handoff

跨 Conversation / Runtime 不存在 Magic Arrow。

发送方负责生成完整、自包含、可直接复制的 Prompt。

Owner 是 Relay Transport，不是 Relay Editor。

正式 Prompt 必须明确：

- 发给谁
- 发送方
- 项目
- Recipient Code（启用时）
- Goal / Scope / Non-goals
- Required Context
- Expected Return
- Escalation Boundary

只有发给 Engineer 的 Task 需要包含推荐 Model / Reasoning：

- Model 只允许 GPT-6 Luna（`gpt-6-luna`）或 GPT-6 Sol（`gpt-6-sol`）；
- Reasoning 只允许 `none` / `low` / `medium` / `high` / `xhigh` / `max`；
- 因此 Engineer 固定从 12 种 Model × Reasoning 组合中选择；
- 普通清晰任务优先 Luna；大上下文、跨模块、复杂 Debug、架构敏感、高复杂度 / 高风险任务优先 Sol；
- Reasoning 使用最低充分档位，不机械默认高强度；
- 其他 ChatGPT 网页端角色 Handoff 不携带模型推荐字段，Owner 默认使用最高可用 ChatGPT 档位。

Engineer 内部调用 agy / Antigravity Reviewer 的模型选择是独立机制，按 `roles/ENGINEER.md` 执行。

## 11. Evidence

Agent 的“已完成 / 已修复 / 没问题”属于 Claim。

Evidence 包括：

- tests / build / lint / typecheck；
- runtime / HTTP / integration；
- CI；
- screenshot / preview；
- diff / commit；
- migration dry-run；
- other reproducible verification。

任务风险越高，对独立、可重复 Evidence 的要求越高。

## 12. Ground Truth Verification

事实冲突时：

```text
STOP affected mutation
→ 明确冲突
→ 收集证据
→ 判断哪一方过时 / 错误
→ 修正真正错误的一方
```

如果冲突会改变产品 / 商业结果，再交 Owner 决定。

纯技术事实由 AI 基于 Evidence 处理。

## 13. Git / PR

Known State > Clean State。

不得覆盖未知修改，不执行无依据 destructive Git 操作。

PR 不是默认步骤。只有仓库规则、Owner 明确要求、正式 Review 需要或具体风险确实值得时使用。

## 14. Completion

完成不等于“代码写完”。

至少按任务适用范围确认：

- Outcome 达成；
- Validation 完成；
- Evidence 可追踪；
- Git anchor 清楚；
- 未验证项明确；
- 必要 Review 已完成；
- 长期 Project / Product Memory 是否需要更新。

不因普通小改机械更新 Notion / 长期文档。
