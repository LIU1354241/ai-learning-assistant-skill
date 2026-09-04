#!/usr/bin/env python3
"""Zero-dependency structural validation for the governed Skill repository."""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LEGAL_STATES = {
    "DIAGNOSTIC",
    "PROPOSED",
    "EXPERIMENTAL",
    "VALIDATED",
    "ACCEPTED",
    "FROZEN",
    "SUPERSEDED",
    "REJECTED",
    "CLOSED_NO_CHANGE",
    "BLOCKED",
}
REQUIRED = (
    "SKILL.md",
    "SKILL-v0.6-candidate-04-failure-aware-degradation.md",
    "LICENSE",
    "README.md",
    "README.zh-CN.md",
    "STATUS.md",
    "AGENTS.md",
    "CONTRIBUTING.md",
    "SECURITY.md",
    ".gitattributes",
    ".editorconfig",
    "project/baseline-manifest.json",
    "project/project-state.yaml",
    "project/candidate-index.yaml",
    "docs/candidate-lifecycle.md",
    "docs/evaluation-protocol.md",
    "docs/failure-taxonomy.md",
    "tests/candidate-05/manifest.yaml",
    "tests/candidate-05/test-cases-r0-leaky.md",
    "tests/candidate-05/test-cases.md",
    "tests/candidate-05/expected-behavior.md",
    "evals/schemas/run-manifest.schema.json",
    "evals/schemas/result.schema.json",
    "evals/results.jsonl",
    "scripts/validate_repo.py",
    "scripts/verify_baseline.py",
    "scripts/lint_eval_prompts.py",
    ".github/workflows/validate.yml",
)
ABSOLUTE_WINDOWS_PATH = re.compile(r"(?i)(?<![A-Za-z0-9])[A-Z]:[\\/]")
TEXT_SUFFIXES = {".md", ".yaml", ".yml", ".json", ".jsonl", ".py", ".txt"}


def field(text: str, key: str) -> str | None:
    match = re.search(rf"(?m)^\s*{re.escape(key)}:\s*([^\n#]+?)\s*$", text)
    return match.group(1).strip().strip('"\'') if match else None


def section(text: str, name: str) -> str:
    match = re.search(rf"(?ms)^{re.escape(name)}:\s*\n((?:[ \t]+.*\n?)*)", text)
    return match.group(1) if match else ""


def candidate_blocks(text: str) -> dict[str, str]:
    found: dict[str, str] = {}
    pattern = re.compile(r"(?ms)^  - id:\s*([^\s]+)\s*\n(.*?)(?=^  - id:|\Z)")
    for match in pattern.finditer(text):
        found[match.group(1)] = match.group(2)
    return found


def tracked_paths() -> list[Path]:
    completed = subprocess.run(
        ["git", "ls-files", "-co", "--exclude-standard"],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    return [ROOT / line for line in completed.stdout.splitlines() if line]


def main() -> int:
    errors: list[str] = []

    def check(condition: bool, message: str) -> None:
        if condition:
            print(f"PASS: {message}")
        else:
            print(f"FAIL: {message}")
            errors.append(message)

    for relative in REQUIRED:
        check((ROOT / relative).is_file(), f"required file exists: {relative}")

    try:
        baseline = json.loads((ROOT / "project/baseline-manifest.json").read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        baseline = {}
        errors.append(f"baseline manifest parse error: {exc}")

    index_text = (ROOT / "project/candidate-index.yaml").read_text(encoding="utf-8")
    blocks = candidate_blocks(index_text)
    states = {candidate: field(block, "status") for candidate, block in blocks.items()}
    check(all(state in LEGAL_STATES for state in states.values()), "all Candidate states are legal")
    check(
        states.get("candidate-04") == "FROZEN"
        and field(blocks.get("candidate-04", ""), "role") == "CURRENT_BASELINE",
        "Candidate 04 is FROZEN / CURRENT_BASELINE",
    )
    check(
        states.get("candidate-05") in LEGAL_STATES
        and field(blocks.get("candidate-05", ""), "role") != "CURRENT_BASELINE",
        "Candidate 05 is legal and is not the baseline",
    )

    c05_text = (ROOT / "tests/candidate-05/manifest.yaml").read_text(encoding="utf-8")
    check(field(c05_text, "baseline") == "candidate-04", "Candidate 05 declares Candidate 04 baseline")
    check(field(c05_text, "baseline_change_allowed") == "false", "Candidate 05 cannot change baseline")
    check(field(c05_text, "rule_file_created") == "false", "Candidate 05 has no rule file")
    check(field(c05_text, "status") == states.get("candidate-05"), "Candidate 05 manifest and index statuses agree")

    ids: list[str] = []
    for path in sorted((ROOT / "tests").glob("candidate-*/test-cases.md")):
        text = path.read_text(encoding="utf-8")
        ids.extend(re.findall(r"(?m)^##\s+([A-Z][A-Z0-9-]+)(?:\s|$)", text))
    duplicates = sorted(key for key, count in Counter(ids).items() if count > 1)
    check(not duplicates, f"no duplicate canonical case IDs{': ' + ', '.join(duplicates) if duplicates else ''}")

    jsonl_ok = True
    results_path = ROOT / "evals/results.jsonl"
    if results_path.is_file():
        for number, line in enumerate(results_path.read_text(encoding="utf-8").splitlines(), start=1):
            if not line.strip():
                continue
            try:
                record = json.loads(line)
            except json.JSONDecodeError as exc:
                print(f"FAIL: evals/results.jsonl:{number}: {exc}")
                jsonl_ok = False
                continue
            required_fields = {
                "run_id", "case_id", "baseline", "freeze_commit", "skill_sha256",
                "executor_model", "judge_model", "fresh_context", "verdict",
                "failure_class", "raw_output_path", "timestamp",
            }
            if not required_fields.issubset(record):
                print(f"FAIL: evals/results.jsonl:{number}: missing required fields")
                jsonl_ok = False
    check(jsonl_ok, "evaluation JSONL parses and contains required fields")

    project_text = (ROOT / "project/project-state.yaml").read_text(encoding="utf-8")
    project_baseline = section(project_text, "baseline")
    project_diagnostic = section(project_text, "current_diagnostic")
    status_text = (ROOT / "STATUS.md").read_text(encoding="utf-8")
    check(field(project_baseline, "id") == baseline.get("baseline") == "candidate-04", "baseline IDs are consistent")
    check(field(project_baseline, "status") == baseline.get("status") == "FROZEN", "baseline statuses are consistent")
    check(field(project_baseline, "role") == baseline.get("role") == "CURRENT_BASELINE", "baseline roles are consistent")
    check(field(project_diagnostic, "id") == "candidate-05", "project state identifies Candidate 05 diagnostic")
    check("Baseline: Candidate 04" in status_text and "Baseline status: FROZEN" in status_text, "STATUS baseline is consistent")
    check("Candidate 05 status: DIAGNOSTIC" in status_text, "STATUS diagnostic is consistent")

    canonical_path = ROOT / str(baseline.get("canonical_skill", ""))
    source_path = ROOT / str(baseline.get("frozen_source", ""))
    expected_sha = baseline.get("sha256")
    canonical_ok = canonical_path.is_file() and source_path.is_file()
    if canonical_ok:
        canonical_bytes = canonical_path.read_bytes()
        source_bytes = source_path.read_bytes()
        canonical_ok = (
            canonical_bytes == source_bytes
            and hashlib.sha256(canonical_bytes).hexdigest() == expected_sha
        )
    check(canonical_ok, "canonical Skill matches frozen source and baseline manifest")

    path_findings: list[str] = []
    for path in tracked_paths():
        if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        if ABSOLUTE_WINDOWS_PATH.search(text):
            path_findings.append(path.relative_to(ROOT).as_posix())
    check(not path_findings, f"no unnecessary Windows absolute paths{': ' + ', '.join(path_findings) if path_findings else ''}")

    tracked = [path.relative_to(ROOT).as_posix() for path in tracked_paths()]
    holdout_files = [path for path in tracked if re.search(r"(^|/)holdout(/|$)", path, re.IGNORECASE)]
    check(not holdout_files, "no in-repository private holdout files")

    license_text = (ROOT / "LICENSE").read_text(encoding="utf-8", errors="replace")
    readme_text = (ROOT / "README.md").read_text(encoding="utf-8")
    check("Apache License" in license_text and "Version 2.0" in license_text, "LICENSE is Apache-2.0")
    check("Apache-2.0" in readme_text, "README license reference is Apache-2.0")

    if errors:
        print(f"FAILED: {len(errors)} repository validation problem(s).")
        return 1
    print("PASS: repository structure and canonical state validated.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
