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

## 2. 什么时候更新

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

## 3. STATUS 更新规则

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

## 4. 文档与代码冲突

不要自动相信任何一方。

触发 `WORKFLOW.md` 的 Ground Truth Verification。

## 5. Resume / Reality Check

长期暂停后恢复项目：

1. 读取根 `AGENTS.md`；
2. 检查 Git state / branch / HEAD / 近期历史；
3. 按项目 `AGENTS.md` 执行 baseline verification；
4. 读取 STATUS / PROJECT / ARCHITECTURE / 相关 ADR；
5. Codex 做 Repository Reality Check，报告明显 docs/code drift；
6. ChatGPT 生成 Resumption Summary；
7. 再开始第一个新 Task。

不要在恢复时硬编码某一种语言或构建命令。
