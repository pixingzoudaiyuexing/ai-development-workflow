# AGENTS.md

> AI Workflow: v1  
> Workflow Source: https://github.com/pixingzoudaiyuexing/ai-development-workflow

## 项目规则入口

在执行中型及以上开发任务前，先阅读与当前任务直接相关的项目文档。

如果需要恢复完整 AI 协作制度，以 `Workflow Source` 对应版本的 `START-HERE.md` 为入口，不依赖 ChatGPT / Codex 的长期记忆。

## 项目概况

- Project: [填写]
- Repository: [填写]
- Primary stack: [填写]

## 开发规则

- [项目特有规则]
- [禁止事项]
- [兼容性边界]

## Baseline Verification

项目恢复或重大修改前用于确认基线：

```text
[填写真实命令，例如 build / test / lint / smoke test]
```

## High-Risk Areas

以下项目模块属于本项目特有高风险区域：

- [填写]

命中时结合全局 `RISK-GATES.md` 判断 Task Risk。

## 文档

- `docs/PROJECT.md`
- `docs/ARCHITECTURE.md`（若适用）
- `docs/ROADMAP.md`（若适用）
- `docs/DECISIONS.md` 或 `docs/adr/`（若适用）
- `docs/STATUS.md`（checkpoint only）

## 其他

如果项目文档、测试、源码与实际运行行为冲突，不要自行选择一方当作真理；先报告并触发 Ground Truth Verification。
