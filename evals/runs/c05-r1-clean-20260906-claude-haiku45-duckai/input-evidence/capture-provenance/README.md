# Candidate 05 Clean R1 — Evidence Capture Workspace

Run ID: `c05-r1-clean-20260906-claude-haiku45-duckai`
Status: COMPLETED — JUDGED — NOT IMPORTED

This workspace contains the completed evidence capture for a new clean,
auditable Candidate 05 run. All five cases were executed, all five first
Executor responses were captured, and all five independent Judges completed
with `PASS` verdicts. Repository import has not occurred; this remains capture
evidence pending repository import.

Baseline: tag `v0.6.0-agent-ready`
(commit `6408c965bb52be19495fdf827d628f483af8b012`),
frozen Candidate 04 Skill, SHA-256
`c41bd7d50fdbecf4fc9b16aabd613f16f0fdc8bf5a01c7d3f32e2b4aeaac37fa`
(the byte-exact copy is preserved in this directory as `SKILL.md`).

## Layout

- `SKILL.md` — canonical frozen Skill, exported directly from the Git tag object.
- `run-metadata.yaml` — run-level metadata.
- `authority-map.yaml` — machine-readable authoritative evidence paths and
  explicit import exclusions.
- One directory per case (`01-` through `05-`), each containing:
  - `submitted-input.txt` — the prepared exact Executor input (complete
    canonical Skill, separator, one neutral case packet). This is a
    PREPARED input; it becomes execution evidence only after it is
    actually submitted verbatim to Duck.ai.
  - `executor-output.txt` — starts as `NOT_YET_EXECUTED`.
  - `judge-input.txt` — prepared Judge template with a placeholder.
  - `judge-output.txt` — starts as `NOT_YET_JUDGED`.
  - `metadata.yaml` — per-case capture metadata.

## Case 2 authority

- Attempt 01: `INCOMPLETE_CAPTURE / NON_AUTHORITATIVE`.
- Attempt 02: `AUTHORITATIVE_EXECUTOR_ATTEMPT`.

Only the Attempt 02 submitted input and Executor output identified in
`authority-map.yaml` are authoritative for Case 2. The excluded paths listed
there must not be imported as authoritative evidence.

## Executor procedure (per case)

1. Open a NEW Duck.ai conversation.
2. Select Claude Haiku 4.5.
3. Open `submitted-input.txt` for that case.
4. Copy the COMPLETE file contents.
5. Paste them into Duck.ai.
6. Before sending, confirm no extra text was added.
7. Send exactly once.
8. Do not regenerate.
9. Do not follow up.
10. Copy the FIRST complete Claude response verbatim into
    `executor-output.txt`.
11. Replace `NOT_YET_EXECUTED`.
12. Update `execution_date` in `metadata.yaml` if known.
13. Do not invent a timestamp or context identifier — leave
    `NOT_RECORDED` / `NOT_EXPOSED` if the platform does not expose them.

## Judge procedure (per case)

1. Open a NEW ChatGPT conversation.
2. Select GPT-5.6 Sol.
3. Open `judge-input.txt` for that case.
4. Replace only `[PASTE NEW EXECUTOR RAW OUTPUT HERE]` with the exact
   contents of that case's `executor-output.txt`.
5. Save the resulting final exact Judge input BEFORE sending.
6. Send once.
7. Do not regenerate.
8. Copy the FIRST complete Judge response verbatim into
   `judge-output.txt`.
9. Replace `NOT_YET_JUDGED`.
10. Update `judge_date` in `metadata.yaml` if known.
11. Do not invent a timestamp or context identifier.

## Status of this material

This run is complete at the capture layer: five Executor responses and five
independent Judge responses are preserved, with five `PASS`, zero `PARTIAL`,
zero `FAIL`, and zero `SKILL_RULE_GAP` results. Repository import has not yet
occurred.

Candidate 05 remains `DIAGNOSTIC / CURRENT_DIAGNOSTIC`. This run does not by
itself close Candidate 05; the existing Kimi `PARTIAL / MODEL_COMPLIANCE`
evidence remains relevant.

The first preserved Judge responses for Cases 3–5 did not comply literally
with the requested schema-only format. Their complete raw responses and
unambiguous `PASS` verdicts remain unchanged; these are Judge-format
observations and do not alter the saved verdicts.
