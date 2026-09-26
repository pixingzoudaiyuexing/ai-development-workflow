# DOCUMENTATION RULES

## 1. Git 文档负责技术长期事实

常见：

- `AGENTS.md`：开发 / 测试 / 构建规则
- `docs/PROJECT.md`：Repo-local What / Why
- `docs/ARCHITECTURE.md`：当前真实架构
- `docs/DECISIONS.md` / `docs/adr/`：重要技术决定
- `docs/ROADMAP.md`：技术 / Repo 路线
- `docs/STATUS.md`：低频 Save Point

不要把未来愿望写成当前实现。

## 2. Notion 与 Git 不重复

Notion：

- Owner-facing Project / Product Memory
- Project Progress / Current State
- Product Intent / Feature Memory
- Project-level Decision 状态

Git：

- code
- architecture
- API / schema / protocol
- build / test
- implementation consequence
- runtime / evidence anchors

同一个信息只在最合适的层保留完整正文，另一层使用摘要 / pointer。

## 3. 更新触发

只有长期事实发生变化时更新长期文档。

普通 Bug、CSS 微调、小 Feature、一次性调试默认不更新，除非它们真正改变架构、项目规则或长期产品行为。

## 4. 冲突

Git / Notion / Runtime 冲突时执行 Ground Truth Verification。

## 5. Resume

长期项目恢复时：

1. 先确认 Role / Project；
2. 读取 Minimum Sufficient Project Memory；
3. 检查相关 Git / Runtime / Evidence；
4. 只恢复当前工作需要的技术事实；
5. 再开始新的 mutation。

# END
