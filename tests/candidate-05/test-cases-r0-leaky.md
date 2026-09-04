# Candidate 05 R0 — Historical Prompt-Leakage Evidence

Classification: `PROMPT_LEAKAGE`

Verdict: `INVALID_TEST`

Execution eligibility: `NEVER_EXECUTE`

## Provenance boundary

The original R0 files were untracked in the user's Windows working tree and were not present in the authoritative remote clone used for standardization. Their exact bytes are unavailable in this environment. This file preserves the known historical leakage evidence recovered from the project discussion; it does not claim to be a byte-for-byte copy of the unavailable R0.

If the original file is later imported, preserve it as a separate immutable artifact, record its SHA-256, and do not overwrite this provenance note without an explicit reconciliation record.

## Known answer-leaking clauses

The historical prompt was reported to contain clauses including:

```text
必须同时处理先前与当前证据
必须保留并解释相互冲突的证据
Git 经验能否直接证明 Kubernetes 能力
不要用固定等级或数值评分
```

These clauses expose expected invariants or direct the answer. Any outcome produced from that prompt is invalid as blind behavioral evidence.

## Historical case identities

| Old ID | Historical focus | Canonical clean ID |
| --- | --- | --- |
| `C05-01` | “Studied” is not equivalent to “mastered” | `REG-C04-EVIDENCE-01` |
| `C05-02` | One failure does not establish capability degradation | `REG-C04-EVIDENCE-02` |
| `C05-03` | Git capability does not establish Kubernetes capability | `REG-C04-TRANSFER-01` |
| `C05-04` | Older and newer capability evidence conflict | `C05-DIAG-CONFLICT-01` |
| `C05-05` | One wrong answer does not generalize to the whole Git topic | `REG-C04-SCOPE-01` |

Only the fourth focus is a new Candidate 05 diagnostic hypothesis. The other four are Candidate 04 regression coverage.
