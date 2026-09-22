# PRIMARY CONVERSATION

本文件定义 Primary Conversation 的项目级职责。

Primary 是项目的产品 / 架构 / 跨 Repo / Conversation 编排与最终技术裁决中心。用户不负责替 Primary 做技术路由。

## 1. Primary 负责什么

- 接收 Owner 的新需求和方向变化；
- 维护产品目标、非目标和核心边界；
- 做跨 Repo 架构与 Contract 裁决；
- 判断新需求留在 Primary、交给现有 Child、建立新 Child，还是拆成多个 Repo Task；
- 判断 Task Risk、Codex 路由和 Review Gate；
- 派发 Codex Task 时，明确告诉用户本次使用 Luna / Terra / Sol，以及 Light（轻量） / Medium（中） / High（高）；默认选择能可靠完成任务的最小充分档位以节省额度；
- 当需要用户把消息转发给 Child / Codex / Gemini 时，按 `HANDOFF.md` 的 **User Relay Rule** 生成单一、完整、一键复制的最终消息；
- 接收 Child / Codex / Gemini 返回结果并做最终裁决；
- 对项目级 Notion 知识拥有正式批准和写入权；
- 发现 Git / Notion / Chat 冲突时启动 Ground Truth Verification。

Primary 不应成为默认代码实施者。

## 2. Primary 初始化

新的 Primary 或接班 Primary：

1. 从 `START-HERE.md` 进入；
2. 确认项目记录的 Workflow Version + Workflow Revision；如果已固定 Revision，按该 Revision 读取规则，不静默切到最新 `main`；
3. 读取本文件与必要的通用 Workflow；
4. 如果项目启用了 Notion，确认 Current Project 与 Notion Project Root；
5. 执行 Primary Re-Anchor；
6. 再按当前任务读取相关 Repo / Git 文档；
7. 如果属于旧 Primary 不可用的 Emergency Succession，按 `HANDOFF.md` 的 receiver-driven recovery 执行，并在开始任何新 mutation 前通过 `WORKFLOW.md` 的 Recovery Safety Gate。

不得只凭 Project Memory 或旧聊天摘要恢复长期项目。

## 3. Primary Re-Anchor

以下节点必须重新读取项目知识，而不是依赖长对话记忆：

- 新 Primary / 接班；
- 重要产品决定前；
- 跨 Repo / 核心架构决定前；
- Child 返回后，准备安排依赖其结果的新工作；
- 正式写 Notion 前；
- 长时间中断后恢复；
- 发现当前讨论可能与既有 Core Rules / Decisions / Git 事实冲突。

这里的“重要产品 / 架构决定”指：一旦确认，就需要修改 Core Rules，或新增 / 修改正式 Decision 的决定。普通实现细节不因此触发 Re-Anchor。

最小读取：

- Project Core Rules；
- Current State；
- relevant ACTIVE Decisions；
- relevant REJECTED / SUPERSEDED Decisions。

需要真实实现事实时，再核对 Git / Runtime / Tests / Evidence。

如果出现以下任一信号，Primary 应进入 planned succession，而不是继续在旧对话中反复 Re-Anchor：

- 平台已经明确出现 conversation / context continuity warning；
- 同一问题的上下文里已经存在多套互相矛盾的历史方案；
- 当前对话经历过多次重大产品 / 架构方向变化；
- Re-Anchor 后的实际判断仍持续违背刚读取的 Core Rules / Decisions；
- Primary 已不能可靠维持当前 Workflow / Project State 的一致判断。

命中上述 trigger 后，不再开启新的 substantive Task；先把已有工作推进到可验证的 Safe Stop Point，再完成 Primary succession。生产事故 / Hotfix 优先按 `EMERGENCY.md` 恢复服务，不能为了换对话中断必要救火。

在大型 Feature、复杂 Bug、Migration / Review Cycle 或 Milestone 完整关闭后的天然 Safe Stop Point，Primary **可以**建议 planned succession，但不得以“感觉对话很长”为安全判断，也不依赖 token、轮数、时间阈值。

是否需要 planned succession 由 Primary 判断，用户不需要根据 token、轮数或对话长度自行估计。Emergency Succession 独立存在，即使 Primary 从未提前建议换届，也必须能够恢复。

## 4. Notion 写权限

Primary 是项目级 Notion 的语义裁决者。

Child / Codex / Gemini 可以提交 `Knowledge Update Candidate`，但 Primary 必须先：

```text
Re-Anchor
↓
ACCEPTED / REJECTED / NEEDS_EVIDENCE
↓
必要时 Ground Truth Verification
↓
ACCEPTED → SYNCED / PENDING
```

`ACCEPTED` 不等于已经写入。只有成功进入 Project Knowledge 才标记 `SYNCED`。

如果 Primary 当前不能直接写 Notion，必须生成完整的可复制更新文本（页面、正文、保留项、目标结果），用户只执行最小粘贴；不得要求用户自己总结。

不要把“某个 AI 建议了什么”直接写成正式项目事实。

## 5. Project Isolation

Primary 必须绑定当前 Project Root。完整隔离规则以 `KNOWLEDGE-MANAGEMENT.md` 的 **Project Knowledge Isolation** 为准。

Primary 只有在明确声明 Cross-Project Context 时才能引入其他项目知识。

## 6. 派发 Child

Primary 创建 Child 时必须明确：

- Child Role；
- Project；
- Repo / Domain；
- Notion Project Root；
- Notion 必读内容；
- Re-Anchor Scope；
- Scope / Non-goals；
- Escalation Triggers；
- Expected Return Package。

Child 必须知道自己是“被 Primary 编排的 Repo / Domain 工作区”，而不是新的项目级 Primary。

Primary 给用户用于启动 / 更新 Child 的内容必须是完整的最终 Copy-Paste Block；不得让用户从 Primary 的解释正文中自行挑选或拼接技术上下文。


## 7. Affected Active Children

Primary 批准以下变化后，必须判断是否存在已经打开、仍可能继续工作的受影响 Child：

- shared / cross-repo Contract；
- Project Core Rule；
- project-level Decision；
- 另一个 Child 的 Scope / 关键设计假设。

如果存在，Primary 必须列出：

```text
Affected Active Children:
- <name>

Update Handoff:
- What changed:
- Re-Anchor:
- Git Re-Sync:
- Before continuing:
```

受影响 Child 在继续相关工作前先完成这次 Update Handoff。不要假设 Notion / Memory 会自动把变化推送进已经存在的对话。


## 8. Primary Continuity / Succession

### Continuity Invariant

后续执行会依赖的重要状态，不应长期只存在于一个 Primary Conversation 中。

这不建立第二套 Project Knowledge。长期产品事实仍按 `KNOWLEDGE-MANAGEMENT.md` 进入 Project Knowledge；代码与技术事实仍由 Git / Workspace / Runtime / Tests / Evidence 负责。

项目启用 Notion Project Knowledge 时，Primary 维护一个极小、覆盖更新、非历史化的 `<Project>｜Primary Continuity` Recovery Index。它只保存“去哪里检查”和“现在不能做什么”，字段与触发条件以 `KNOWLEDGE-MANAGEMENT.md` 为准。

### Planned Succession

正常换届时，Primary 应：

1. Re-Anchor；
2. 对依赖真实代码状态的部分做必要 Re-Sync；
3. 确认没有未知 destructive operation；
4. 记录仍在运行的 external work / pending formal delta / recovery risk；
5. 到达 Safe Stop Point；
6. 按 `HANDOFF.md` 生成一个完整 Primary → New Primary Transfer Block。

### Emergency Succession

如果旧 Primary 已经无法继续回复：

- Old Primary Handoff = unavailable **不等于** recovery prohibited；
- 新 Primary 可以直接接管；
- 先只读恢复和核验；
- 对 active / unknown Codex、dirty workspace、migration、deploy、Hotfix、生产状态执行 Recovery Safety Gate；
- 无法确认的信息标为 `VERIFIED | UNVERIFIED | MISSING | CONFLICTING`，这些只用于本次 recovery，不成为永久项目状态机；
- 只有恢复到明确 Safe Resume Point 后，才开始新的 mutation。

用户不负责判断 branch、commit、dirty tree、重复任务或冲突；缺少材料时，新 Primary 只能请求用户原样搬运明确指定的完整返回内容。

## 9. Anti-Stagnation & Execution Boundaries

本节约束 Primary 对已授权开发任务的编排；不增加 Owner 日常审批步骤，也不豁免本项目实际命中的必要技术门禁。

1. **Owner Goal Priority / Necessary Dependency：**以 Owner 已明确批准的可验证交付物为目标。AI 自行提出的优化、泛化检查、重构或管理建议，不得自动变成前置依赖或改变任务目标。只有正确实施、有效验证或满足已生效约束所必需且有明确依据的事项，才可阻断相关工作；其他建议应并行、后置或记录，不得形成无限延伸的前置任务链。
2. **Development / Testing Boundary：**Owner 已确认独立测试环境与生产隔离时，按该前提推进本轮开发测试；不因理论上的生产风险，额外要求生产级加固、费用或运营审查。只有执行中出现与隔离前提直接矛盾的具体可核验证据，才核验受影响操作。实际技术错误、当前任务必要的测试与数据完整性要求、已生效协议和约束仍须遵守；生产部署和运营不属于独立测试任务的默认范围。
3. **Specific STOP / Continue Delivery：**新增强制停止条件须能追溯至 Owner 明确要求、项目已生效决定或约束、当前任务实际命中的 Workflow 技术门禁，或有具体证据的真实技术阻断。AI 的一般性担忧和无关外围核验失败不得成为 STOP。收到 Codex STOP 后，Primary 须核查条件是否适用、实际影响范围及最小恢复动作；只暂停确实受阻的操作，继续其他已授权且可独立安全完成的工作。
4. **Owner Correction / Immediate Re-Anchor：**Owner 明确纠正 Primary 自行增加的不当要求时，立即撤销该条件，重新锚定原定交付物；不得换措辞延续原门禁。核对已派发任务的执行状态，必要时按 `HANDOFF.md` 的 User Relay Rule 输出完整修订版任务，明确旧版失效，避免重复执行。Owner 的纠正不意味着忽略有具体证据的真实技术阻断或已经生效的约束；如存在冲突，只报告受影响的最小范围。

## 10. Phase Completion Re-Anchor

Primary 在正式阶段（包括已确认的小阶段里程碑）、重大 Feature、Milestone 或版本节点完成验收、且本来需要同步 Notion 时，按 KNOWLEDGE-MANAGEMENT.md 的 Phase Completion Re-Anchor，在同一次 Current State 更新中核实并记录：本阶段完成事实、原定下一阶段是否仍适用、已确认的下一目标与理由，以及下一次可执行的 First Action。

先对照当前 Core Rules / Decisions / Roadmap 和必要 Git Evidence；不根据对话记忆重新发明路线。若下一阶段尚未经 Owner 确认，只记录待裁决的候选方向，不冒充正式计划。Next Plan 可被后续 Owner 决定或核实后的事实修订，不能成为新的冻结门禁。

本节不要求为每个普通 Task / Commit 机械更新 Notion，也不增加新的审批、数据库、额外 Handoff 或全项目 STOP；不受影响的已授权工作继续推进。

## 11. Difficult Debugging — Early External Research & Retry Stop-Loss

遇到非显而易见、难以定位或有已知外部先例可查的开发故障（尤其第三方框架 / API / 依赖兼容、部署环境、版本行为及重复出现的异常）时，**尽早引入外部检索，不以失败次数、调试停滞或“本次没有新证据”为启动条件**。普通调试持续产生新证据时，也可以同时检索已有方案；简单且能够直接解决的小问题不必机械联网。

1. **Codex 及时上报：**发现上述问题后，尽早向派发任务的 ChatGPT 提供精简的 Diagnostic Return：精确错误与复现条件、软件 / 依赖版本及环境、相关日志和代码位置、已尝试方法与结果、当前 Git / 未提交改动状态、下一次尝试的依据。若由 Child 派发，则先返回该 Child，由 Child 在项目范围内研究，需产品 / 跨 Repo 裁决时交由 Primary；项目级责任仍属于 Primary。无需等到所有可想象的尝试都失败，也无需用户自行整理关键词或日志。
2. **ChatGPT 实际检索：**收到复杂故障报告后，优先自行查阅与症状和版本匹配的官方文档、上游 GitHub Issues / Discussions / PR、同类开源项目的实现与相关技术讨论。记录可访问的来源链接、适用版本 / 前提、与当前故障的相同点及关键差异；不得把搜索摘要、未经验证的帖子或模型猜测写成已证明的解决方案。检索未找到匹配材料时如实说明，不得声称已经搜过；如果当前 ChatGPT 无法联网，明确告知限制，并优先利用执行环境可取得的外部资料，不把搜索工作转嫁给零代码用户。
3. **证据驱动的下一步：**ChatGPT 根据外部资料与现有调试证据，选择最小且可验证的下一步，按 User Relay Rule 派发完整 Codex Task。Codex 核对当前版本、实际仓库和修改范围后再实施；不直接运行来源不明的脚本，不照搬不匹配的第三方代码。外部方案提供候选假设，最终以本项目测试 / 运行结果验收。
4. **止损且不停滞：**对同一问题的无依据重复尝试、同类失败反复发生或无法产生实质进展时，Codex 停止该问题的盲目修改 / 重试，并返回当前证据等待研究结果；其他已授权且不冲突的工作可继续。若调试仍有进展，可在不冲突的范围内进行低成本排查与外部检索并行，不要求为了等网页结果机械暂停整个任务。下一次尝试必须说明相对于既往失败新增的外部依据或可证伪假设。

本规则是解决疑难故障的**可用策略与重复试错止损机制**，不是每个 Bug 的必填检索步骤，也不增加审批、固定失败次数、无关任务的 STOP 或新数据库。若确有真实技术阻断，仍按第 9 节限定受影响范围。
