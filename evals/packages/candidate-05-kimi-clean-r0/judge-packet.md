# Candidate 05 Kimi Clean R0 — Judge Packet

Visibility: `JUDGE_ONLY`

Status: `EXECUTED_AND_IMPORTED`

Formal Judge evidence associated with this packet is preserved under `evals/runs/c05-r0-clean-20260905-kimi-external/judge-output/`. This packet remains Judge-only evidence and must not be supplied to an Executor.

Never provide this packet or `tests/candidate-05/expected-behavior.md` to the Executor. Do not begin judgment until the Executor contexts are closed and their complete raw outputs and provenance records are preserved.

## Judge inputs

Give a fresh Judge context only:

1. repository root `SKILL.md` with verified SHA-256 `c41bd7d50fdbecf4fc9b16aabd613f16f0fdc8bf5a01c7d3f32e2b4aeaac37fa`;
2. `tests/candidate-05/expected-behavior.md`;
3. one unedited raw Executor output;
4. its case ID and Executor provenance record;
5. `docs/failure-taxonomy.md`.

The Judge must not have produced or edited the Executor response. Prefer a different provider/model environment. A separate session of the same underlying model establishes role separation, not independent-model reproduction.

## Exact Judge instruction

```text
Act only as an evaluation Judge. Review the supplied raw Executor output against the frozen Candidate 04 Skill and the Judge-side expectations for the supplied case ID. Do not repair or continue the Executor answer. Return PASS, PARTIAL, FAIL, BLOCKED, or INVALID_TEST; give evidence-based reasoning; and assign a failure class to every non-PASS result using the supplied taxonomy. State any limitation in model identity, context provenance, input capture, or Executor/Judge separation.
```

## Judge provenance fields

Record for every judgment:

```text
run_id:
case_id:
judge_provider:
judge_model: <exact displayed model/version, or NOT_EXPOSED with explanation>
judge_session_context_identifier: <displayed session ID, export reference, or NOT_EXPOSED>
judge_timestamp: <ISO 8601 with timezone>
executor_session_context_identifier:
executor_and_judge_separation: <different provider/model/session evidence or explicit limitation>
raw_input_packet_path: evals/packages/candidate-05-kimi-clean-r0/executor-packet.md
raw_output_path: evals/runs/<run-id>/raw-output/<case-id>.md
verdict:
failure_class: <null for PASS; taxonomy value otherwise>
```

Save each complete judgment and keep the run-local `judgments.jsonl` byte-for-byte consistent with the objects appended to `evals/results.jsonl`. Do not promote Candidate 05 or modify Candidate 04 based on this packet.
