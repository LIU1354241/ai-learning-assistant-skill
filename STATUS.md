# AI Learning Assistant — Current Status

Baseline: Candidate 04

Baseline status: FROZEN

Role: CURRENT_BASELINE

Freeze commit: `164c4d9`

Baseline SHA-256: `c41bd7d50fdbecf4fc9b16aabd613f16f0fdc8bf5a01c7d3f32e2b4aeaac37fa`

Canonical Skill: `SKILL.md`

Frozen source: `SKILL-v0.6-candidate-04-failure-aware-degradation.md`

Current diagnostic: Candidate 05 — Learner Evidence Conflict

Candidate 05 status: DIAGNOSTIC

Candidate 05 role: CURRENT_DIAGNOSTIC

Candidate 05 is not:

- accepted;
- validated;
- baseline behavior.

Evaluation status: three independent Executor environments are recorded. Codex Work and Anthropic Claude Haiku 4.5 through Duck.ai each recorded 5/5 `PASS`; external Kimi recorded 3 `PASS` and 2 `PARTIAL / MODEL_COMPLIANCE`. Exact Kimi model/version and session identifiers were not exposed; the Claude and Kimi runs used OpenAI / GPT-5.6 Sol Judges in fresh conversations, with unavailable context identifiers recorded as `NOT_EXPOSED`.

Claude Clean R1 evidence import: `COMPLETE`. Import commit `32256080a2d304db79876eb7d3999debc85bb467` was merged through PR #2, `Record Claude Candidate 05 Clean R1 evidence`, into `main` at `ef9255696fe09947b40197ce1eda0cf9b585769e`.

Final fresh-Agent AgentOS smoke: `PASS` against `chore/ai-learning-agentos-readiness` at `4a52a333a83ed8ba41195c82eabc2e40b27db797`, with the target working tree reported clean. The complete raw input and first complete raw output are preserved under `audit/agentos-smoke/agentos-handoff-final-20260905-4a52a33/`.

Hosted CI: `PASS / Success` for final `main` commit `ef9255696fe09947b40197ce1eda0cf9b585769e`, as independently observed by the owner. No run ID, URL, timestamp, job ID, or environment metadata was supplied.

AgentOS readiness: `READY`. Unresolved release blockers: `0`.

Next action: Candidate 05 remains open as `CURRENT_DIAGNOSTIC`; no behavioral Candidate proposal is justified. Await a separately authorized diagnostic or policy decision.

Provenance status: the original untracked Candidate 05 R0 files from the Windows working tree have been recovered and imported byte-for-byte under `tests/candidate-05/history/windows-main-164c4d9-untracked/`. They remain `INVALID_TEST / PROMPT_LEAKAGE`; the active diagnostic input is the separate Clean R0.

Candidate 05 remains `DIAGNOSTIC`: the valid external Kimi partial results remain classified as `MODEL_COMPLIANCE`, not a rule gap, and are not erased by the Claude 5/5 `PASS` run. No Candidate 05 rule file exists. Candidate 04 behavior remains frozen.
