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
VERDICTS = {"PASS", "PARTIAL", "FAIL", "BLOCKED", "INVALID_TEST"}
FAILURE_CLASSES = {
    "SKILL_RULE_GAP",
    "MODEL_COMPLIANCE",
    "PROMPT_LEAKAGE",
    "HARNESS_DEFECT",
    "EVALUATOR_VARIANCE",
    "TOOL_OR_ENVIRONMENT",
    "CONTEXT_MISSING",
    "UNKNOWN",
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
    "STANDARDIZATION-REPORT.md",
    ".gitattributes",
    ".editorconfig",
    "project/baseline-manifest.json",
    "project/history-provenance-gaps.yaml",
    "project/project-state.yaml",
    "project/candidate-index.yaml",
    "docs/candidate-lifecycle.md",
    "docs/evaluation-protocol.md",
    "docs/failure-taxonomy.md",
    "tests/candidate-05/manifest.yaml",
    "tests/candidate-05/test-cases-r0-leaky.md",
    "tests/candidate-05/test-cases.md",
    "tests/candidate-05/expected-behavior.md",
    "evals/packages/candidate-05-kimi-clean-r0/executor-packet.md",
    "evals/packages/candidate-05-kimi-clean-r0/judge-packet.md",
    "audit/final-agentos-smoke-protocol.md",
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
HISTORICAL_SOURCE_PROVENANCE = "tests/candidate-05/history/windows-main-164c4d9-untracked/provenance.yaml"


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
    global_results: list[dict[str, object]] = []
    seen_results: set[tuple[object, object]] = set()
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
                "executor_model", "executor_session_context_identifier", "fresh_context_evidence",
                "judge_model", "judge_session_context_identifier", "executor_judge_separation",
                "fresh_context", "verdict", "failure_class", "raw_input_packet_path",
                "raw_output_path", "timestamp",
            }
            if not required_fields.issubset(record):
                print(f"FAIL: evals/results.jsonl:{number}: missing required fields")
                jsonl_ok = False
                continue
            key = (record.get("run_id"), record.get("case_id"))
            if key in seen_results:
                print(f"FAIL: evals/results.jsonl:{number}: duplicate run/case result {key}")
                jsonl_ok = False
            seen_results.add(key)
            if record.get("baseline") != baseline.get("baseline"):
                print(f"FAIL: evals/results.jsonl:{number}: baseline mismatch")
                jsonl_ok = False
            if record.get("freeze_commit") != baseline.get("freeze_commit"):
                print(f"FAIL: evals/results.jsonl:{number}: freeze commit mismatch")
                jsonl_ok = False
            if record.get("skill_sha256") != baseline.get("sha256"):
                print(f"FAIL: evals/results.jsonl:{number}: Skill SHA mismatch")
                jsonl_ok = False
            if record.get("verdict") not in VERDICTS:
                print(f"FAIL: evals/results.jsonl:{number}: illegal verdict")
                jsonl_ok = False
            failure_class = record.get("failure_class")
            if failure_class is not None and failure_class not in FAILURE_CLASSES:
                print(f"FAIL: evals/results.jsonl:{number}: illegal failure class")
                jsonl_ok = False
            if record.get("verdict") == "PASS" and failure_class is not None:
                print(f"FAIL: evals/results.jsonl:{number}: PASS must use null failure_class")
                jsonl_ok = False
            if record.get("verdict") != "PASS" and failure_class is None:
                print(f"FAIL: evals/results.jsonl:{number}: non-PASS requires failure_class")
                jsonl_ok = False
            if not isinstance(record.get("fresh_context"), bool):
                print(f"FAIL: evals/results.jsonl:{number}: fresh_context must be boolean")
                jsonl_ok = False
            provenance_fields = {
                "executor_model", "executor_session_context_identifier", "fresh_context_evidence",
                "judge_model", "judge_session_context_identifier", "executor_judge_separation",
            }
            if any(not isinstance(record.get(name), str) or not record.get(name) for name in provenance_fields):
                print(f"FAIL: evals/results.jsonl:{number}: provenance fields must be non-empty strings")
                jsonl_ok = False
            raw_input_path = record.get("raw_input_packet_path")
            if not isinstance(raw_input_path, str) or Path(raw_input_path).is_absolute() or ".." in Path(raw_input_path).parts:
                print(f"FAIL: evals/results.jsonl:{number}: unsafe raw_input_packet_path")
                jsonl_ok = False
            elif not (ROOT / raw_input_path).is_file():
                print(f"FAIL: evals/results.jsonl:{number}: raw input packet is missing")
                jsonl_ok = False
            raw_path = record.get("raw_output_path")
            if not isinstance(raw_path, str) or Path(raw_path).is_absolute() or ".." in Path(raw_path).parts:
                print(f"FAIL: evals/results.jsonl:{number}: unsafe raw_output_path")
                jsonl_ok = False
            elif not (ROOT / raw_path).is_file():
                print(f"FAIL: evals/results.jsonl:{number}: raw output is missing")
                jsonl_ok = False
            global_results.append(record)
    check(jsonl_ok, "evaluation JSONL parses and contains required fields")

    run_records_ok = True
    local_results: list[dict[str, object]] = []
    for manifest_path in sorted((ROOT / "evals/runs").glob("*/manifest.json")):
        try:
            run_manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            print(f"FAIL: {manifest_path.relative_to(ROOT)}: {exc}")
            run_records_ok = False
            continue
        run_id = manifest_path.parent.name
        manifest_required = {
            "run_id", "candidate", "baseline", "freeze_commit", "skill_sha256",
            "executor_model", "executor_session_context_identifier", "fresh_context_evidence",
            "judge_model", "judge_session_context_identifier", "executor_judge_separation",
            "environment", "fresh_context", "timestamp", "case_ids",
            "raw_input_packet_path", "raw_output_directory",
        }
        if not manifest_required.issubset(run_manifest):
            print(f"FAIL: {manifest_path.relative_to(ROOT)}: missing required fields")
            run_records_ok = False
        manifest_provenance_fields = {
            "executor_model", "executor_session_context_identifier", "fresh_context_evidence",
            "judge_model", "judge_session_context_identifier", "executor_judge_separation",
        }
        if any(not isinstance(run_manifest.get(name), str) or not run_manifest.get(name) for name in manifest_provenance_fields):
            print(f"FAIL: {manifest_path.relative_to(ROOT)}: provenance fields must be non-empty strings")
            run_records_ok = False
        if run_manifest.get("run_id") != run_id:
            print(f"FAIL: {manifest_path.relative_to(ROOT)}: run_id does not match directory")
            run_records_ok = False
        if run_manifest.get("baseline") != baseline.get("baseline") or run_manifest.get("freeze_commit") != baseline.get("freeze_commit") or run_manifest.get("skill_sha256") != baseline.get("sha256"):
            print(f"FAIL: {manifest_path.relative_to(ROOT)}: baseline metadata mismatch")
            run_records_ok = False
        case_ids = run_manifest.get("case_ids")
        if not isinstance(case_ids, list) or not case_ids or len(case_ids) != len(set(case_ids)):
            print(f"FAIL: {manifest_path.relative_to(ROOT)}: case_ids must be a non-empty unique list")
            run_records_ok = False
        raw_directory = run_manifest.get("raw_output_directory")
        if not isinstance(raw_directory, str) or Path(raw_directory).is_absolute() or not (ROOT / raw_directory).is_dir():
            print(f"FAIL: {manifest_path.relative_to(ROOT)}: invalid raw_output_directory")
            run_records_ok = False
        raw_input = run_manifest.get("raw_input_packet_path")
        if not isinstance(raw_input, str) or Path(raw_input).is_absolute() or ".." in Path(raw_input).parts or not (ROOT / raw_input).is_file():
            print(f"FAIL: {manifest_path.relative_to(ROOT)}: invalid raw_input_packet_path")
            run_records_ok = False
        judgments_path = manifest_path.parent / "judgments.jsonl"
        if judgments_path.is_file():
            for number, line in enumerate(judgments_path.read_text(encoding="utf-8").splitlines(), start=1):
                if not line.strip():
                    continue
                try:
                    local_results.append(json.loads(line))
                except json.JSONDecodeError as exc:
                    print(f"FAIL: {judgments_path.relative_to(ROOT)}:{number}: {exc}")
                    run_records_ok = False
    check(run_records_ok, "run manifests and run-local judgments are structurally valid")
    normalized_global = {json.dumps(item, sort_keys=True) for item in global_results}
    normalized_local = {json.dumps(item, sort_keys=True) for item in local_results}
    check(normalized_global == normalized_local, "global and run-local JSONL results are consistent")

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
        relative = path.relative_to(ROOT).as_posix()
        if relative == HISTORICAL_SOURCE_PROVENANCE:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        if ABSOLUTE_WINDOWS_PATH.search(text):
            path_findings.append(relative)
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
