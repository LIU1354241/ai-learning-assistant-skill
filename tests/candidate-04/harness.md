# Candidate 04 测试执行 Harness

## 执行协议

Behavior Test = REAL EXECUTION。

- 每个测试由一个子代理在**全新上下文**中执行；
- 子代理首先读取被测 Skill 文件：
  `SKILL-v0.6-candidate-04-failure-degradation-test.md`（相对于 repository root）
  并将其作为自己的操作指令；
- 然后按该测试的 System Condition 与 User 输入作答；
- 子代理被指示不得修改任何文件、不得使用未被测试允许的工具；
- 子代理返回其会发给用户的**完整逐字回复**；
- 主代理按 expected-behavior.md 逐条判分 PASS / PARTIAL / FAIL。

## 模型与模式

- 实际模型：Kimi（与宿主 Agent 同模型，经子代理通道执行）
- 模式：子代理 / 全新上下文 / Skill 作为指令
- 执行性质：真实模型行为执行（非静态分析）

## Fixture

- `fixtures/webshop-app/`：含真实 `LICENSE`（MIT）与 `README.md`，
  用于 A03（本地等价证据）与 A12（执行模式拆分）的真实证据来源。

## 记录

- 输入、条件、完整输出与判定记录在 `results.md`；
- 失败分析记录在 `failure-analysis.md`；
- 回归结论记录在 `regression-summary.md`。
