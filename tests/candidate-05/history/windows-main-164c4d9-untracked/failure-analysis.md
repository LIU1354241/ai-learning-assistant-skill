# Candidate 05 — R0 Failure Analysis

状态：EMPTY TEMPLATE

所有 PARTIAL / FAIL 均在此记录。一个模型失败不自动等于 Candidate 05 规则缺口。

## 强制分类问题

对每个 Finding，先回答：

> Candidate 04 是否已经清楚禁止这个行为？

- **YES**：首先归类为可能的回归 / 模型指令遵循失败；除非后续证据显示现有规则并不清楚，否则不得称为 Candidate 05 设计缺口。
- **NO / NOT CLEAR**：可暂列为潜在设计缺口，但必须检查可复现性、测试设计和环境因素。
- **TEST INVALID / CONTAMINATED**：输入歧义、隐藏上下文、平台冲突或判据问题；不得用来支持新增规则。

## Finding Template

### FA-C05-___

- Test ID:
- Model / platform version:
- Execution date:
- Fresh context confirmed:
- Full result reference:

#### Observed behavior

- Problematic verbatim excerpt:
- Observed behavior:
- Why it matters:

#### Evidence handling

- Prior evidence recognized:
- Current evidence recognized:
- Expected learner-state conclusion:
- Actual learner-state conclusion:
- Overclaiming / overgeneralization / unjustified update observed:

#### Existing Candidate 04 rule check

- Does Candidate 04 already clearly prohibit this behavior? (YES / NO / NOT CLEAR):
- Candidate 04 section and exact relevant text:
- Violated existing Candidate 04 rule, if any:
- Reasoning:

#### Classification

- Classification:
  - Possible regression / instruction-following failure
  - Genuine Candidate 05 design-gap candidate
  - Model variability
  - Test-design issue
  - Environment / context contamination
- Genuine rule gap vs model instruction-following issue:
- Confidence and unresolved ambiguity:

#### Reproducibility

- Same-model rerun required:
- Same-model rerun result:
- Cross-model evidence, if later available:
- Reproducibility conclusion:

#### Proposed next action

- Proposed next action:
- Why this action matches the classification:
- Rule change proposed now? (must remain NO during R0):
- Risk of premature rule change:

---

## R0 Classification Summary

| Finding ID | Test ID | Existing rule clear? | Classification | Reproducible? | Proposed next action |
|---|---|---|---|---|---|
|  |  |  |  |  |  |
