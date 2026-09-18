# DOCUMENTATION RULES

目标：既避免文档漂移，也避免每个小 Task 都机械修改大量文档。

## 1. 文件边界

### `AGENTS.md`

How：当前项目怎么开发、验证、构建，哪些规则和红线必须遵守。

### `docs/PROJECT.md`

What & Why：项目定位、用户、目标、非目标、业务边界、核心约束。

### `docs/ARCHITECTURE.md`

Current System：当前真实架构、组件关系、数据流、关键接口、部署结构与已知限制。

### `docs/DECISIONS.md` / `docs/adr/`

Why：长期重要技术决定及被拒绝方案。

Tier 2 可用单个 `DECISIONS.md`；Tier 3 或长期复杂项目优先使用 ADR 目录。

### `docs/ROADMAP.md`

Future：Milestone、阶段、优先级、暂缓 / 放弃计划。

### `docs/STATUS.md`

Save Point：低频项目恢复快照，不是日报。

## 2. Git 文档与 Notion 的边界

项目启用 Notion 时：

```text
Git / Repo Docs
= Repo-local 技术事实、实现 Contract、代码结构、API / schema、build / test 规则、技术 ADR

Notion
= 项目级 Core Rules、Current State、跨 Repo 产品边界、正式 Decisions、Rejected / Superseded 历史
```

不要把同一份大段内容复制到两边。需要两边都可发现时，一边保存 canonical 内容，另一边保存短摘要和指针。

Notion 不取代 `AGENTS.md`、`ARCHITECTURE.md`、ADR、真实代码或 Evidence；Git 也不需要承担所有 Conversation Topology、项目当前优先级和已否定产品方案的长期恢复职责。

发生 Git 与 Notion 冲突时，进入 `WORKFLOW.md` 的 Ground Truth Verification，不允许自动选择某一边。

## 3. 什么时候更新

```text
项目目标 / 非目标发生变化
→ PROJECT

当前真实架构发生变化
→ ARCHITECTURE

形成长期重要技术决定
→ DECISIONS / ADR

Milestone / 长期路线变化
→ ROADMAP

重大阶段完成 / 长期暂停 / 恢复 / 大版本 / 方向明显变化
→ STATUS

项目开发 / baseline verification 规则变化
→ AGENTS
```

普通 Bug、小 Feature、文案、UI 微调默认不修改长期文档，除非它们确实改变了上述长期事实。

## 4. STATUS 更新规则

只在以下时机考虑更新：

- Milestone / Stage 完成；
- 项目准备暂停较长时间；
- 长期休眠项目恢复；
- 重大版本发布前后；
- 项目方向显著改变。

保持短：

- 当前阶段；
- 稳定 commit（若适用）；
- 当前 blockers；
- 下一主要目标；
- 更新时间。

## 5. 文档与代码冲突

不要自动相信任何一方。

触发 `WORKFLOW.md` 的 Ground Truth Verification。

## 6. Resume / Reality Check

长期暂停后恢复项目：

1. 确认当前 Conversation Role；项目启用 Notion 时先按对应 Role 文件执行 Re-Anchor；
2. 读取根 `AGENTS.md`；
3. 检查 Git state / branch / HEAD / 近期历史；
4. 按项目 `AGENTS.md` 执行 baseline verification；
5. 读取 STATUS / PROJECT / ARCHITECTURE / 相关 ADR；
6. Codex 做 Repository Reality Check，报告明显 docs/code drift；
7. ChatGPT 比较 Notion（如启用）与 Git / Runtime 是否存在 State Drift；
8. ChatGPT 生成 Resumption Summary；
9. 再开始第一个新 Task。

不要在恢复时硬编码某一种语言或构建命令。
