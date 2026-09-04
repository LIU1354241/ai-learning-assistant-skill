#!/usr/bin/env python3
"""Verify the frozen Candidate 04 source, canonical Skill, and evidence."""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "project" / "baseline-manifest.json"


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def fail(message: str, failures: list[str]) -> None:
    failures.append(message)
    print(f"FAIL: {message}")


def verify_file(path_text: str, expected: str, failures: list[str]) -> bytes | None:
    path = ROOT / path_text
    if not path.is_file():
        fail(f"missing {path_text}", failures)
        return None
    data = path.read_bytes()
    actual = sha256_bytes(data)
    if actual != expected:
        fail(f"SHA mismatch for {path_text}: expected {expected}, got {actual}", failures)
    else:
        print(f"PASS: {path_text} SHA-256 {actual}")
    return data


def git_object(commit: str, path: str) -> bytes | None:
    completed = subprocess.run(
        ["git", "show", f"{commit}:{path}"],
        cwd=ROOT,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    return completed.stdout if completed.returncode == 0 else None


def main() -> int:
    failures: list[str] = []
    try:
        manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"FAIL: cannot read baseline manifest: {exc}")
        return 1

    expected = manifest.get("sha256", "")
    commit = manifest.get("freeze_commit", "")
    canonical = manifest.get("canonical_skill", "")
    frozen_source = manifest.get("frozen_source", "")

    if manifest.get("status") != "FROZEN" or manifest.get("role") != "CURRENT_BASELINE":
        fail("baseline manifest must be FROZEN / CURRENT_BASELINE", failures)

    commit_check = subprocess.run(
        ["git", "cat-file", "-e", f"{commit}^{{commit}}"],
        cwd=ROOT,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if commit_check.returncode:
        fail(f"freeze commit does not exist: {commit}", failures)
    else:
        print(f"PASS: freeze commit exists: {commit}")

    canonical_bytes = verify_file(canonical, expected, failures)
    source_bytes = verify_file(frozen_source, expected, failures)
    if canonical_bytes is not None and source_bytes is not None:
        if canonical_bytes != source_bytes:
            fail("canonical Skill is not byte-identical to frozen source", failures)
        else:
            print("PASS: canonical Skill is byte-identical to frozen source")

    evidence = {frozen_source: expected, **manifest.get("frozen_evidence", {})}
    for path, recorded_sha in evidence.items():
        data = verify_file(path, recorded_sha, failures) if path != frozen_source else source_bytes
        committed = git_object(commit, path)
        if committed is None:
            fail(f"{path} is absent from freeze commit", failures)
        elif sha256_bytes(committed) != recorded_sha:
            fail(f"freeze-commit bytes do not match recorded SHA for {path}", failures)
        elif data is not None:
            print(f"PASS: {path} matches freeze-commit evidence")

    if failures:
        print(f"FAILED: {len(failures)} baseline verification problem(s).")
        return 1
    print("PASS: frozen baseline and recorded evidence verified.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
