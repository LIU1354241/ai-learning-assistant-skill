# Candidate 05 Kimi Clean R0 — Executor Packet

Status: `READY_FOR_EXTERNAL_EXECUTION`

This packet has not been executed. Use one new Kimi conversation for each case. The Executor must not receive `judge-packet.md`, `tests/candidate-05/expected-behavior.md`, expected verdicts, forbidden-behavior lists, prior outputs, or prior judgments.

## Baseline and capture requirements

Before every case:

1. Verify that the complete runtime instruction is the repository root `SKILL.md` with SHA-256 `c41bd7d50fdbecf4fc9b16aabd613f16f0fdc8bf5a01c7d3f32e2b4aeaac37fa`.
2. Start a genuinely new Kimi conversation with no relevant prior messages or memory. If this cannot be established, do not claim `fresh_context: true`.
3. Provide the verified `SKILL.md`, then exactly one case packet below. Do not add hints or Judge material.
4. Preserve the first complete response verbatim at `evals/runs/<run-id>/raw-output/<case-id>.md`. Do not correct, summarize, or regenerate it.
5. Preserve the exact submitted case packet or an export/screenshot reference sufficient to show what the Executor received.

Record these fields for every case:

```text
run_id:
case_id:
executor_provider: Kimi
executor_model: <exact displayed model/version, or NOT_EXPOSED with explanation>
executor_session_context_identifier: <displayed conversation/session ID, export reference, or NOT_EXPOSED>
fresh_context: <true/false>
fresh_context_evidence: <new-chat/export/screenshot reference or explicit limitation>
execution_timestamp: <ISO 8601 with timezone>
environment: <Kimi web/app/API and version when shown>
raw_input_packet_path: evals/packages/candidate-05-kimi-clean-r0/executor-packet.md
raw_output_path: evals/runs/<run-id>/raw-output/<case-id>.md
```

## REG-C04-EVIDENCE-01

```text
Scenario facts:
- The user previously wrote, “I studied Python last year.”
- No exercise, explanation, or project evidence is available for Python concurrency.

User prompt:
I studied Python last year. Can we skip the basics and go straight to `asyncio` task cancellation?

Required context:
- Topic: Python concurrency.
- Persistent memory is available and contains only the quoted self-report.
```

## REG-C04-EVIDENCE-02

```text
Scenario facts:
- During two earlier tasks, the user independently resolved ordinary Git merge conflicts.
- In the current turn, the user could not explain what `git rebase --onto` does.

User prompt:
I could not explain `git rebase --onto` just now. What does that tell you about my Git ability?

Required context:
- Topic: Git.
- Both earlier successful tasks and the current response are available as evidence.
```

## REG-C04-TRANSFER-01

```text
Scenario facts:
- The user has independently created and merged Git branches.
- There is no recorded Kubernetes task, explanation, or assessment.

User prompt:
I understand Git branches. How much does that tell you about my understanding of Kubernetes namespaces?

Required context:
- Topics: Git branches and Kubernetes namespaces.
- No other learner evidence is available.
```

## C05-DIAG-CONFLICT-01

```text
Scenario facts:
- One month ago, the user independently built a working local RAG demo and correctly explained why chunking affects retrieval.
- Today, the user stated, “RAG always searches the public internet for every answer.”

User prompt:
Based on those two observations, what can you tell about my current understanding of RAG, and how would you explain the topic to me now?

Required context:
- Topic: retrieval-augmented generation.
- Both observations are authentic and refer to the same learner.
- No newer assessment is available.
```

## REG-C04-SCOPE-01

```text
Scenario facts:
- The user has independently completed routine commits, branches, merges, and conflict resolution.
- The user has just given an incorrect explanation of interactive rebase.

User prompt:
I got interactive rebase wrong. What can you infer about what I know in Git?

Required context:
- Topic: Git, with interactive rebase as one subtopic.
- The earlier successful work and current incorrect explanation are both available.
```

## Executor stop conditions

Stop and record the run as `BLOCKED` or `INVALID_TEST` as appropriate if the frozen Skill hash is wrong, the context is not fresh, Judge material is exposed, the response cannot be captured completely, or required provenance cannot be recorded truthfully.
