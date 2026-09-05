# Evaluation runs

Each real public development or regression run uses:

```text
<run-id>/
├── manifest.json
├── input-evidence/          optional exports or references proving submitted packets and fresh contexts
├── raw-output/
│   └── <case-id>.md
├── judge-output/           optional verbatim formal Judge outputs
└── judgments.jsonl
```

The manifest and each result record the Executor/Judge model, exposed session/context identifiers, fresh-context evidence, separation basis, raw input packet path, and raw output path. When supplied, provider names and verbatim Judge-output paths are also recorded. Use `NOT_EXPOSED` with an explanation when the platform withholds an identifier; do not invent one.

Do not create placeholder runs. Do not store real private holdout prompts, private rubrics, or their raw outputs in this repository.
