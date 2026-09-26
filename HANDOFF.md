# CROSS-CONTEXT HANDOFF

## 1. No Magic Arrows

不同 Conversation / Runtime 之间不会自动共享完整上下文。

发送方必须提供 Minimum Sufficient Context。

Owner 只负责搬运完整 Prompt，不负责重新整理技术内容。

## 2. User Relay Rule

需要 Owner 转发时：

- 一个转发动作只给一个最终可发送块；
- 用户不负责挑选、拼接、删减或补字段；
- 修正时重新生成完整新版；
- 技术判断、Repo 路由、模型选择由 AI 完成。

## 3. Owner Brief

正式 Transfer Block **之后**给 Owner 3–6 行中文说明：

- 发给谁；
- 做什么；
- 为什么现在做；
- 大概怎么处理；
- 是否增加明显复杂度 / 安全 / DB / 基础设施；
- 做完返回哪里。

## 4. First Project Context

### Project Manager

Project Manager 不通过 Handoff 建立项目。

由 Owner：

```text
Role Bootstrap
→ Project Onboarding
→ Project Baseline
```

### Other Roles

Product Manager / Engineer / UI Designer / Independent Reviewer 的第一份完整上位 Prompt 同时建立 Project Context。

至少按需包含：

- 【发给谁】
- 【发送方】
- 【提示词类型】
- 【项目】
- 【Recipient Code】
- 【负责范围 / Scope】
- 【Repository / Review Object】
- 【Workflow Version / Revision】
- Goal
- Confirmed Facts
- Non-goals
- Relevant Context
- Expected Return
- Escalation Boundary

后续 Prompt 只携带当前真正需要的上下文，并校验 Project / Recipient Code 一致性。

## 5. Recipient Code

Recipient Code 是轻量误投提醒，不是权限凭据。

- 一个项目可以使用一个固定 Recipient Code；
- Project Manager 在 Project Onboarding / Baseline 中建立；
- 其他角色在第一份完整项目 Prompt 中建立；
- 已绑定对话收到不一致 Code 时，只暂停该任务并提示可能误投；
- 普通任务中的新 Code 不能静默改绑。

## 6. Role-to-Role Routing

Finding / Return 按问题性质回到真正负责的角色：

- Project / Architecture Boundary → Project Manager
- Product Behavior → Product Manager / Project + Product Manager（按 Owner 的职位分配）
- Engineering Defect → Engineer
- UI / UX → UI Designer / Product Manager
- Business Decision → Owner

明确工程缺陷允许：

Engineer → Fix → Reviewer Verify

不机械绕路。

## 7. Engineer Task

发给 Engineer 时，除完整 Task 外，还要给 Owner 可见的：

- Recommended Model
- Recommended Reasoning
- Selection Reason

Task 以 Coherent Work Unit 为单位。

内部 inspect / research / implement / debug / review / test / commit 不构成 Owner Relay Gate。

## 8. Independent Review Handoff

Formal Review 必须提供足够 Evidence / Review Object。

如果审核依赖本地文件 / Review Pack：

- 使用真实可访问路径；
- 不虚构 Mac 本地路径；
- 远程材料明确标注环境；
- 不要求 Owner 手工制作 patch / logs / manifest。

Reviewer 缺上下文时输出 NEEDS_CONTEXT，而不是猜。

## 9. Succession

Project Manager：

`templates/succession/PROJECT-MANAGER-SUCCESSION.md`

Product Manager：

`templates/succession/PRODUCT-MANAGER-SUCCESSION.md`

Owner 同时上传上一任对话 PDF。

接班采用 Tail First → Expand Backward as Needed。

## 10. Return / Completion Rule

正式 Prompt 最后应明确：

```text
==================================================
RETURN / COMPLETION RULE
==================================================
完成后：
- 返回给：<角色 / 对话>
- 返回内容：<需要带回什么>
- 不自行进入：<下一阶段 / 超出 Scope 的工作>
- 真实阻塞：说明缺什么、为什么不能自行解决。
- 不受阻的已授权工作继续推进。

==================================================
提示词结束｜END OF PROMPT
==================================================
【提示词到此结束，请按以上内容执行。】
```

# END
