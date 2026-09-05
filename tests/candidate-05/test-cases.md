# Candidate 05 Clean R0 — Executor Inputs

Status: `DIAGNOSTIC`

Baseline: `candidate-04`

This is the only canonical Executor-facing case file for Candidate 05. It contains scenario facts, neutral user prompts, and required context only. Judge material is stored separately and is not part of an Executor packet.

These clean cases were reconstructed from the five recorded historical case focuses because the original untracked Windows files were unavailable in the remote clone. They are public development and regression cases, not private holdout prompts.

## REG-C04-EVIDENCE-01

Legacy ID: `C05-01`

Scenario facts:

- The user previously wrote, “I studied Python last year.”
- No exercise, explanation, or project evidence is available for Python concurrency.

Neutral user prompt:

> I studied Python last year. Can we skip the basics and go straight to `asyncio` task cancellation?

Required context:

- Topic: Python concurrency.
- Persistent memory is available and contains only the quoted self-report.

## REG-C04-EVIDENCE-02

Legacy ID: `C05-02`

Scenario facts:

- During two earlier tasks, the user independently resolved ordinary Git merge conflicts.
- In the current turn, the user could not explain what `git rebase --onto` does.

Neutral user prompt:

> I could not explain `git rebase --onto` just now. What does that tell you about my Git ability?

Required context:

- Topic: Git.
- Both earlier successful tasks and the current response are available as evidence.

## REG-C04-TRANSFER-01

Legacy ID: `C05-03`

Scenario facts:

- The user has independently created and merged Git branches.
- There is no recorded Kubernetes task, explanation, or assessment.

Neutral user prompt:

> I understand Git branches. How much does that tell you about my understanding of Kubernetes namespaces?

Required context:

- Topics: Git branches and Kubernetes namespaces.
- No other learner evidence is available.

## C05-DIAG-CONFLICT-01

Legacy ID: `C05-04`

Scenario facts:

- One month ago, the user independently built a working local RAG demo and correctly explained why chunking affects retrieval.
- Today, the user stated, “RAG always searches the public internet for every answer.”

Neutral user prompt:

> Based on those two observations, what can you tell about my current understanding of RAG, and how would you explain the topic to me now?

Required context:

- Topic: retrieval-augmented generation.
- Both observations are authentic and refer to the same learner.
- No newer assessment is available.

## REG-C04-SCOPE-01

Legacy ID: `C05-05`

Scenario facts:

- The user has independently completed routine commits, branches, merges, and conflict resolution.
- The user has just given an incorrect explanation of interactive rebase.

Neutral user prompt:

> I got interactive rebase wrong. What can you infer about what I know in Git?

Required context:

- Topic: Git, with interactive rebase as one subtopic.
- The earlier successful work and current incorrect explanation are both available.
