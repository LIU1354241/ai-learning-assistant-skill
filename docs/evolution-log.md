# Evolution Log

## v0.3 Stable — 2026-08-24

### Why

v0.2 revealed three risks:

- content requirements could keep expanding;
- responses could become too heavy;
- complex output requirements lacked explicit triggers.

### Decision

- Stabilized the Skill at eight core rules.
- Expanded learner understanding to identity, goal, level, and stage.
- Replaced a fixed long explanation format with a four-layer default response.
- Moved comparison, historical context, transfer, and visualization into triggered modules.
- Kept Skill, Memory, and Workflow responsibilities separate.

### Principle

> 规则数量不是价值，执行率才是价值。

Avoid turning the Skill into a super prompt. Future changes should improve execution quality before adding scope.

## v0.2 — 2026-08-24

Improved learner adaptation based on Red Team feedback.

- Expanded user understanding across role, goal, and current level, with explicit adaptation of depth, explanation style, and output format.
- Added a flexible Explanation Format for new concepts, technical terms, and AI architectures.
- Added optional visualization guidance for architecture, Agent workflows, component relationships, and data flow.
- Strengthened Learning Mode so abstract concepts connect to real examples, business scenarios, or analogies.
- Kept seven core rules by revising existing rules instead of adding another numbered rule.

## v0.1 — 2026-08-24

First design completed.

- Defined the Skill as a long-term learning assistant rather than a general question-answering prompt.
- Added seven core rules covering truth, learner context, priority, capability building, adaptive depth, transparent AI collaboration, and response self-checking.
- Added Learning Mode and Execution Mode.
- Added four exceptions for fast exam answers, urgent bugs, deep research, and insufficient information.
- Added a memory policy that identifies useful long-term context without storing user data.
- Kept the repository independent from OpenViking, Jideli, and other existing projects.

The next version should be driven by observed test failures, not by adding speculative rules.
