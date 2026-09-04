# Candidate 04 Regression Summary

回归对象：Candidate 03 关键能力（Simple Query / Hard Overview Gate / Flow / State / Change-first + Explicit Delta）。

## R2 Gate 判定

- 全部 27 项测试中唯一非 PASS 项为 **A04（PARTIAL）**，对应唯一 Finding **RT-04-001**。
- RT-04-001 判定：**Candidate-04 specific = NO**（分类 C，模型措辞波动；Candidate 04 新增规则均未被违反，真实性边界已保留）。
- 因此 **R2 Gate = NOT MET**：不存在"Candidate-04 specific = YES 且值得修改规则"的 Finding，**不生成 R2**。
- 未对 `SKILL-v0.6-candidate-04-failure-degradation-test.md` 做任何修改。

## Baseline Regression 执行说明

测试集本身包含 REG-01–REG-05 作为 Candidate 03 关键能力的常态基线检查，故按 harness 正常执行（非"伪造 R2 回归"）：

| 测试 | 能力 | 判定 |
|---|---|---|
| REG-01 | Simple Query | PASS |
| REG-02 | Hard Overview Gate | PASS |
| REG-03 | Flow | PASS |
| REG-04 | State | PASS |
| REG-05 | Change-first + Explicit Delta | PASS |

结论：Candidate 04 在全部 5 项 Candidate 03 关键能力上无回退；新增"失败感知与安全降级"规则未污染常态行为（T01/A13/A14/REG-01 验证无故障尾巴）。

## R2 vs R1 回归

未生成 R2，无需执行。若未来生成 R2，需重跑：T01–T06、此前 FAIL/PARTIAL 的 A 测试、REG-01–05。
