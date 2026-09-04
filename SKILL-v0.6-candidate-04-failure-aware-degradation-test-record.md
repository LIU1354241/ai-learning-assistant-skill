# v0.6 Candidate 04 — Failure-Aware Degradation Test Record

日期：2026-09-04  
状态：Formal Freeze  
最终建议：`FREEZE R3`

本记录仅汇总已经存在的 Candidate 04 测试、Failure Analysis、跨模型审查与 targeted retest 证据，不重新执行测试，也不重新发明结论。

---

## Baseline

- Frozen baseline：`SKILL-v0.6-candidate-03-question-representation.md`
- Candidate 03 SHA-256：`db4cd684ae27659b109e85b239afd1b70943c57248bc18764e3d1fb3f26493aa`
- Candidate 03 在 Candidate 04 设计、测试、复测与本次 Freeze 全程保持 zero diff。
- Candidate 03 不进入本次 staged diff。

---

## Candidate 04 Evolution

| 版本 | 文件 | SHA-256 | 证据定位 |
|---|---|---|---|
| R1 | `SKILL-v0.6-candidate-04-failure-degradation-test.md` | `08c77c4cdc3ed77c0e4a8289b90857e9f86bda350a96708957ba28752df5dc7b` | 原始 Failure-Aware Degradation candidate |
| R2 | `SKILL-v0.6-candidate-04-failure-degradation-test-r2.md` | `67a85c4b3eaf813b262b586fadece0ee1ac0e213773f3765352f68f2296a5e2f` | 针对 RT-04-002 的最小确认边界修订 |
| R3 | `SKILL-v0.6-candidate-04-failure-degradation-test-r3.md` | `c41bd7d50fdbecf4fc9b16aabd613f16f0fdc8bf5a01c7d3f32e2b4aeaac37fa` | 最终 frozen source |

R3 的 final SHA-256 已在 Freeze 开始前重新计算，并与预期值完全一致。

---

## Kimi Evidence

证据文件：

- `tests/candidate-04/test-cases.md`
- `tests/candidate-04/expected-behavior.md`
- `tests/candidate-04/harness.md`
- `tests/candidate-04/results.md`
- `tests/candidate-04/failure-analysis.md`
- `tests/candidate-04/regression-summary.md`
- `tests/candidate-04/r3-targeted-retest.md`

### 原 27 项 Behavior Tests

- T01–T06：5 PASS + 1 PARTIAL。T06 在 Cross-model Review 中按一致标准由原 PASS 修正为 PARTIAL。
- A01–A16：15 PASS + 1 PARTIAL。A04 为 PARTIAL（RT-04-001）。
- REG-01–05：5/5 PASS。
- 最终合计：25 PASS + 2 PARTIAL；无 FAIL。

### R3 Targeted Retest

- R3-01 Confirmation：PASS
- R3-02 Stable Knowledge：PASS
- R3-03 Explicit Candidate：PASS
- R3-04 Agent Transparency Guard：PASS
- 合计：Kimi 4/4 PASS。

---

## Cross-model Evidence

来源说明：以下 final cross-model 结果来自本次 Freeze 前已经完成并由用户提供的 Final Cross-model Review；`tests/candidate-04/cross-model-review.md` 保留此前各阶段的详细 review 与 Model Compatibility Finding provenance。

### Gemini

- Confirmation：PASS。

### DeepSeek

- Confirmation：FAIL。
- Stable Knowledge：PARTIAL。
- Explicit Candidate：PASS。

### 豆包

- Confirmation：FAIL。
- Stable Knowledge：PARTIAL。
- Explicit Candidate：PASS。

DeepSeek / 豆包的剩余失败统一归类为：

`Model Compatibility / Instruction-following Boundary`

这些结果保留为跨模型指令遵循兼容性边界，不记为 Candidate 04 unresolved rule defect，不触发 R4。

---

## Regression and Preservation

- Candidate 03 与 R3 的 exact logical diff 仅为 24 行新增的 Failure-Aware Degradation 内容，分布在 `真实第一`、`失败感知与安全降级`、`Failure Awareness` 三处。
- Hard Overview Gate：未变化。
- Completion / Request Completion Gate：未变化。
- Visual Truth：未变化。
- Learner State：未变化。
- Explicit Delta：未变化。
- REG-01–05 全部 PASS。
- Candidate 03 保持 zero diff。

---

## Public Repository Safety

- Candidate 04 准备提交的 Skill、测试、fixture 与 provenance 文件已检查本机绝对路径。
- `tests/candidate-04/harness.md` 中唯一的本机绝对路径已泛化为相对于 `repository root` 的路径。
- R1 / R2 / R3 Skill 正文未因路径清理而修改。
- 对 token、password、API key、email、secret 与 Bearer credential 样式进行扫描，未发现真正敏感信息。
- Public repo safety check：PASS。

---

## Final Decision

- Candidate-04 specific unresolved Finding：`0`
- R4 blocker：`NONE`
- Final recommendation：`FREEZE R3`
- Frozen source：`SKILL-v0.6-candidate-04-failure-degradation-test-r3.md`
- Formal Candidate：`SKILL-v0.6-candidate-04-failure-aware-degradation.md`

**CLOSE: v0.6 Candidate 04 Failure-Aware Degradation FROZEN**
