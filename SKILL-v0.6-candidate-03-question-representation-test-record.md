---
title: AI Learning Assistant v0.6 Candidate 03 — Question → Representation Test Record
status: FROZEN
date: 2026-09-03
---

# Candidate 03 Test Record

## Freeze identity

- Frozen baseline: `SKILL-v0.6-candidate-02f-truth-completion.md`
- Baseline capability: `02F Truth + Completion FROZEN`
- Candidate: `03 Question → Information Need → Representation`
- Tested source: `SKILL-v0.6-candidate-03-hard-overview-gate-test.md`
- Formal candidate: `SKILL-v0.6-candidate-03-question-representation.md`
- Final status: **Candidate 03: PASS / FROZEN**

The behavioral results below are the completed cross-model test evidence supplied for this freeze. This freeze review records that evidence and verifies the formal file, scope, preservation, hashes, and validator; it does not rerun Kimi or 豆包.

## Frozen design

Candidate 03 freezes this selection chain:

`User Question → Information Need → Representation`

Core principle:

**Answer first, representation second.**

The representation is selected from what the user actually needs to understand, not mechanically from topic words such as “系统”, “架构”, or “流程”.

Frozen mapping:

- Explicit system overview, overall architecture, overall structure, or module relationships → **Hard Overview Gate**
- Module responsibilities, attributes, or differences → Table when useful
- Request, data, or event movement → Flow
- Object states and transitions → State table / simple diagram
- Change → existing Change-first + Explicit Delta
- Action → Numbered Steps
- Simple Fact → Plain Text

## Behavioral evidence

### Test 1 — Composition

Prompt: `一个典型的电商系统主要由哪些部分组成？我想先看整体结构。`

- Composition identification: PASS
- Overview-first: PARTIAL in the initial run
- Observed issue: Kimi initially showed Table Bias

This initial partial result was superseded by the later Hard Overview Gate cross-model PASS recorded below.

### Test 2 — Flow

Prompt: `电商系统里，用户点击“提交订单”以后，请求接下来是怎么流转的？`

- Flow identification: PASS
- No mechanical Overview caused by the phrase “电商系统”: PASS

### Test 3 — State

Prompt: `一个订单从创建到结束通常会经历哪些状态？状态之间怎么变化？`

- State identification: PASS
- State representation: PASS

### Test 4 — Change

Prompt: `旧版订单系统只有单体服务，新版拆成订单、支付、库存三个服务。主要改了什么？`

- Change-first priority: PASS
- Candidate 03 yields to Explicit Delta: PASS

Visual Truth content-layer regression was observed during testing. It belongs to existing-capability stability and is not a Candidate 03 blocker.

### Test 5 — Multi-need

Prompt: `先让我看电商系统整体有哪些模块，再告诉我一次下单请求怎么流转。`

- Composition + Flow identification: PASS
- Two independent needs may use two necessary representations: PASS
- No third representation added for completeness: PASS

### Composition discrimination

Prompt: `电商系统主要有哪些模块？分别负责什么？`

- Table: PASS

Candidate 03 does not mechanically equate Composition with Overview:

- Overall relationships / whole-system view → Overview
- Responsibilities / attributes → Table

### Hard Overview Gate — Kimi

Prompt: `给我看一个电商系统的整体结构和模块关系。`

- First structured representation = Mermaid Overview diagram
- Responsibilities table appears only after the Overview
- Result: PASS

### Hard Overview Gate — 豆包

Prompt: `给我看一个电商系统的整体结构和模块关系。`

- First structured representation = Mermaid Overview diagram
- Module responsibilities are expanded only after the Overview
- Result: PASS

**Hard Overview Gate Cross-model Test: PASS**

## Known non-Candidate-03 regressions

The tests occasionally showed:

- Unrequested CTA
- Completion stability regression
- Internal Control Leakage
- Visual Truth content-layer regression

These are existing 02F cross-model stability issues. RT-002 / RT-003 / RT-004 were not reopened, and Candidate 03 was not changed to address them.

## Freeze review

### A. 02F preservation

- SHA-256 before: `F601E4AC00EF8C8C07CD77261355F73DA9A1BA63A5B243918241CEE194CB4219`
- SHA-256 after: `F601E4AC00EF8C8C07CD77261355F73DA9A1BA63A5B243918241CEE194CB4219`
- Result: **Frozen 02F Preservation: PASS**

### B. Candidate 03 exact scope

The exact diff against 02F is limited to:

1. Adding the Hard Overview Gate.
2. Replacing the broad information-expression trigger with question-to-information-need routing for Overview versus Flow.
3. Replacing the Representation mapping with Overview, Table, Flow, State, Action, Simple Fact, and the two-need exception.
4. Adding the corresponding Representation Self Check.
5. Normalizing the tested source’s missing final newline in the formal Markdown file; wording is unchanged.

Formal candidate `git diff --no-index --numstat` against 02F: `51 insertions, 23 deletions`.

The tested source reports `52 insertions, 24 deletions` against 02F because its missing final newline is counted as a one-line replacement; this byte-level artifact is absent from the newline-normalized formal file and does not change the logical diff.

No new Question Router module, JSON schema, Learner State, agent orchestration, guardrail implementation, diagram type system, or scoring system was added.

- Result: **Candidate 03 Coverage Check: PASS**
- Result: **Scope Check: PASS**

### C. Frozen capability preservation

The diff review confirms preservation of:

- Truth First
- repeated truth check
- Simple Query Gate
- Request Completion Gate
- Internal Control Boundary
- Learner State
- Evidence
- Verify
- Learning / Execution Mode
- Source Fidelity
- Transfer
- Change-first
- Explicit Delta
- Visual Truth
- Triggered Modules
- Exceptions
- Self Check

- Result: **Frozen Capability Preservation: PASS**

### D. Hard Overview Gate preservation

The complete Hard Overview Gate and all tested wording are unchanged from the tested Candidate 03 source. The only source-to-formal byte difference is the final newline normalization.

- Result: **Hard Overview Gate Preservation: PASS**

### E. Validator

- Validator: bundled original `skill-creator/scripts/quick_validate.py`
- Invocation: `python -X utf8 .../skill-creator/scripts/quick_validate.py <staging-directory>`
- Output: `Skill is valid!`
- Environment note: the first default-locale invocation stopped before validation because Python decoded the UTF-8 file as GBK; rerunning the same unchanged validator in Python UTF-8 mode completed successfully.
- Result: **Skill validator: PASS**

## Hashes

- Tested Candidate 03 source SHA-256: `62134B501AE7F6DACBC954D1D0E68BD02831D866B5EA0E9636FE05C36F9A1F87`
- Formal Candidate 03 SHA-256: `DB4CD684AE27659B109E85B239AFD1B70943C57248BC18764E3D1FB3F26493AA`
- Frozen 02F SHA-256 before and after: `F601E4AC00EF8C8C07CD77261355F73DA9A1BA63A5B243918241CEE194CB4219`

## Final disposition

- Candidate 03 Coverage Check: PASS
- Hard Overview Gate Preservation: PASS
- Frozen 02F Preservation: PASS
- Scope Check: PASS
- Skill validator: PASS
- Blocker: None

**CLOSE: v0.6 Candidate 03 Question → Representation FROZEN**
