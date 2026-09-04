# AI 学习助手 Skill

[English](README.md) | **简体中文**

> 一份真实性优先、基于证据判断学习状态、选择合适表达形式并让 Agent 执行可复核的行为 Skill。

## 当前正式状态

| 字段 | 当前值 |
| --- | --- |
| 当前稳定版本 | `v0.6` |
| 当前行为基线 | Candidate 04 — Failure-Aware Degradation |
| 基线状态 | `FROZEN` |
| 基线角色 | `CURRENT_BASELINE` |
| 冻结来源提交 | `164c4d9` |
| 唯一运行入口 | `SKILL.md` |
| 当前诊断 | Candidate 05 — Learner Evidence Conflict |
| Candidate 05 状态 | `DIAGNOSTIC` |

Candidate 05 尚未接受、尚未验证，也不是正式基线行为。它没有行为规则文件。下一步是运行 Clean R0，再对结果进行失败分类。

Agent 或维护者应先读 [STATUS.md](STATUS.md)，再按 [AGENTS.md](AGENTS.md) 的最小读取顺序工作。

## Skill 解决什么问题

它帮助 Agent：

- 区分已验证事实、基于证据的推断和未验证内容；
- 根据具体 Topic 的学习证据调整解释，而不是给用户贴全局能力等级；
- 根据真实信息需求选择文字、步骤、表格、流程或总览图；
- 在工具或证据不可用时安全降级，同时保持真实性边界；
- 区分已经完成、已经验证和仍未验证的执行结果；
- 用户请求完成后停止，不默认追加学习路线或行动号召。

## 使用方式

运行时只使用根目录 `SKILL.md`。它应始终与 `project/baseline-manifest.json` 中记录的 Candidate 04 冻结源逐字节一致。

在另一个 Agent 环境中使用前，先从仓库根目录运行：

```bash
python scripts/validate_repo.py
python scripts/verify_baseline.py
python scripts/lint_eval_prompts.py
git diff --check
```

验证通过后，把 `SKILL.md` 作为该 Agent 的 Skill 指令。不同宿主如何安装或加载由宿主决定；本仓库定义行为与治理，不绑定某一种安装器。

## Candidate 生命周期

Candidate 的生命周期状态与项目角色分开记录。合法状态、终止状态和 Promotion Gate 见 `docs/candidate-lifecycle.md`。

诊断可以以 `CLOSED_NO_CHANGE` 结束；出现新编号不代表一定增加规则。任何失败必须先分类，只有经过验证的 `SKILL_RULE_GAP` 才能成为新行为 Candidate 的依据，而且不能原地修改当前冻结基线。

## 评测系统

- Executor 只能看到场景事实、中性用户 Prompt 和必要上下文。
- Expected invariants、禁止行为和 Judge rubric 只提供给 Judge。
- 每次真实运行保存完整原始输出和真实模型、环境、日期、上下文信息。
- Markdown 人类记录与 `evals/results.jsonl` 的机器记录必须一致。
- 真正的私有 Holdout 必须在仓库外或未来 AgentOS Verifier 存储中，不能放在 Builder 可读的仓库里。

详见 `docs/evaluation-protocol.md`、`docs/failure-taxonomy.md` 与 `evals/schemas/`。

## 与 Liu AgentOS 的关系

这个仓库正在被标准化为未来 Liu AgentOS 可以接管的治理单元。`STATUS.md`、项目 manifest、Candidate 生命周期、评测 schema 和验证命令，让一个没有聊天历史的新 Agent 也能识别正式基线、当前诊断、冻结范围和下一步。

本仓库目前不包含 AgentOS 运行时、私有 Verifier 存储或自动多模型执行器。本轮是项目标准化，不是新增 Skill 行为。

## 仓库结构

- `SKILL.md` — 唯一正式运行入口。
- `STATUS.md` — 当前人类可读状态。
- `AGENTS.md` — 读取顺序、冻结范围、修改边界与验证命令。
- `project/` — 基线与 Candidate 状态 manifest。
- `docs/` — 设计历史、生命周期、评测协议与失败分类。
- `tests/` — 公开开发、回归与诊断证据。
- `evals/` — schema、公开运行记录与机器可读结果。
- `scripts/` — 零依赖仓库校验。

## License

本项目基于 [Apache License 2.0](LICENSE)（`Apache-2.0`）发布。
