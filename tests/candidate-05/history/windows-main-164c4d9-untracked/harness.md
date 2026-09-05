# Candidate 05 — R0 Manual Cross-Model Harness

状态：DIAGNOSTIC ONLY
冻结行为合约：`SKILL-v0.6-candidate-04-failure-aware-degradation.md`（commit `164c4d9`）

## 目的

在不添加 Candidate 05 规则的前提下，观察 Candidate 04 在学习者状态证据、证据冲突与结论范围方面的实际模型行为。

协议适用于：

- Kimi
- Doubao
- DeepSeek
- Gemini

R0 首轮只执行 Kimi。其他模型保留为后续交叉验证对象，不得在 R0 结果中假装已经执行。

## 测试材料

- 行为合约：repository root 下的 `SKILL-v0.6-candidate-04-failure-aware-degradation.md`
- 输入：`tests/candidate-05/test-cases.md`
- 判据：`tests/candidate-05/expected-behavior.md`
- 原始与判定记录：`tests/candidate-05/results.md`
- 失败分类：`tests/candidate-05/failure-analysis.md`

## 单次执行协议

对每个模型、每个案例或变体执行以下步骤：

1. 新建空白会话或等价的全新上下文。
2. 将冻结的 Candidate 04 文件完整内容作为 system / skill 行为指令提供给模型。
3. 不提供 Candidate 05 的预期行为、评分标准、其他案例输出或先前模型结果。
4. 只粘贴当前案例的“独立运行输入”。案例内已经包含全部允许使用的先前证据与当前证据。
5. 不启用或引用跨会话 Memory；若平台无法关闭 Memory，必须使用新账户、临时会话或明确确认该会话没有相关历史。无法保证时，在结果中记录污染风险。
6. 不追问、不提示、不纠正，保存模型第一次生成的完整逐字回复。
7. 按 `expected-behavior.md` 判为 PASS / PARTIAL / FAIL，并逐项写出证据。
8. 对任何 PARTIAL / FAIL，先执行 Candidate 04 既有规则检查，再决定失败分类。

## 独立运行单位

- C05-01、C05-02、C05-03、C05-05：各自一个全新会话。
- C05-04A、C05-04B、C05-04C：每个变体分别使用全新会话；不得在同一会话连续运行三个变体。
- 共 7 个独立执行单位。

输入中的“先前证据”是当前测试提示显式提供的测试事实，不是要求模型调用隐藏 Memory。模型若声称读取了输入外历史，应作为真实性或状态边界问题记录。

## R0 执行顺序

1. Kimi：C05-01
2. Kimi：C05-02
3. Kimi：C05-03
4. Kimi：C05-04A
5. Kimi：C05-04B
6. Kimi：C05-04C
7. Kimi：C05-05

R0 完成前不执行 Doubao、DeepSeek 或 Gemini。若后续进入 cross-model 阶段，各模型使用相同 Candidate 04 合约、相同输入文本和相同首答记录规则。

## 记录要求

每个执行单位记录：

- 模型与可见版本标识（若平台提供）；
- 执行日期；
- 是否为全新上下文；
- Candidate 04 文件与 commit；
- 完整输入；
- 完整逐字输出；
- PASS / PARTIAL / FAIL；
- 判定证据；
- 是否观察到隐藏 Memory 或上下文污染迹象。

不得只保存摘要后删除原始输出。判定者不得用“我认为模型本意是……”替代对实际措辞的检查。

## 失败分类 Gate

每个 PARTIAL / FAIL 必须按以下顺序处理：

1. 定位模型输出中的具体问题句；
2. 回读 Candidate 04，回答：**Candidate 04 是否已经清楚禁止该行为？**
3. 若 YES：优先归类为“可能的回归 / 指令遵循失败”；不得自动声称需要 Candidate 05 新规则；
4. 若 NO 或规则表述不足：先标记为“潜在设计缺口”，再进行同模型复现；
5. 检查输入歧义、上下文污染、平台 system 指令冲突和判分误差；
6. 只有在规则确实不清楚、问题可复现且测试设计有效时，才把它列为 Candidate 05 设计缺口候选。

## 复现协议

- 对初次 PARTIAL / FAIL，使用同模型、同输入、同 Candidate 04 合约，在另一个全新上下文复现；
- 不在复现提示中透露第一次失败或期望答案；
- 至少保存首次与复现两份完整输出；
- 若行为不复现，记录为模型波动候选，不用单次结果推出规则缺口；
- 跨模型一致失败可增强问题存在的证据，但仍不能替代 Candidate 04 规则检查。

## 跨模型可比性控制

- 保持提示文本、案例顺序规则和判据一致；
- 记录平台自动注入的 system 指令、联网、Memory 或工具差异（若可见）；
- 不比较文风，只比较证据处理、状态结论和范围校准；
- 不因某模型使用不同术语而扣分，只要其含义满足判据；
- 不将拒答、工具错误或上下文污染误判为学习者状态规则缺口。

## R0 停止点

完成 Kimi 的 7 个独立执行单位、判定结果并填写必要失败分析后停止。R0 不创建规则、不修改 Skill、不修改冻结基线。
