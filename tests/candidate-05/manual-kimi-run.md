# Candidate 05 — Manual Kimi Clean R0

Use a separate new Kimi conversation for each packet. Load the repository's verified `SKILL.md` as the Skill instruction, then provide only one packet below. Do not attach `expected-behavior.md` or any prior model output.

After each response, save the complete unedited text as:

```text
evals/runs/<run-id>/raw-output/<case-id>.md
```

Record the exact displayed Kimi model, environment, timestamp with timezone, Skill SHA-256, and whether the context was fresh. Import judgments only after a separate Judge reviews the raw outputs.

## Packet: REG-C04-EVIDENCE-01

```text
Scenario facts:
- The user previously wrote, “I studied Python last year.”
- No exercise, explanation, or project evidence is available for Python concurrency.

User prompt:
I studied Python last year. Can we skip the basics and go straight to asyncio task cancellation?

Context:
- Topic: Python concurrency.
- Persistent memory is available and contains only the quoted self-report.
```

## Packet: REG-C04-EVIDENCE-02

```text
Scenario facts:
- During two earlier tasks, the user independently resolved ordinary Git merge conflicts.
- In the current turn, the user could not explain what git rebase --onto does.

User prompt:
I could not explain git rebase --onto just now. What does that tell you about my Git ability?

Context:
- Topic: Git.
- Both earlier successful tasks and the current response are available as evidence.
```

## Packet: REG-C04-TRANSFER-01

```text
Scenario facts:
- The user has independently created and merged Git branches.
- There is no recorded Kubernetes task, explanation, or assessment.

User prompt:
I understand Git branches. How much does that tell you about my understanding of Kubernetes namespaces?

Context:
- Topics: Git branches and Kubernetes namespaces.
- No other learner evidence is available.
```

## Packet: C05-DIAG-CONFLICT-01

```text
Scenario facts:
- One month ago, the user independently built a working local RAG demo and correctly explained why chunking affects retrieval.
- Today, the user stated, “RAG always searches the public internet for every answer.”

User prompt:
Based on those two observations, what can you tell about my current understanding of RAG, and how would you explain the topic to me now?

Context:
- Topic: retrieval-augmented generation.
- Both observations are authentic and refer to the same learner.
- No newer assessment is available.
```

## Packet: REG-C04-SCOPE-01

```text
Scenario facts:
- The user has independently completed routine commits, branches, merges, and conflict resolution.
- The user has just given an incorrect explanation of interactive rebase.

User prompt:
I got interactive rebase wrong. What can you infer about what I know in Git?

Context:
- Topic: Git, with interactive rebase as one subtopic.
- The earlier successful work and current incorrect explanation are both available.
```

## Import metadata

For each result, add one JSON object to `evals/results.jsonl` using `evals/schemas/result.schema.json`. Use only the real output, real model name, real Judge, and real timestamp. Set `fresh_context` to the truth; never normalize it to make the run look compliant.
