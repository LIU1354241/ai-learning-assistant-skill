#!/usr/bin/env python3
"""Warn about likely answer leakage in Executor-facing evaluation prompts."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_FILES = [ROOT / "tests" / "candidate-05" / "test-cases.md"]
PHRASES = (
    "必须区分",
    "应该保留",
    "正确行为",
    "不要使用",
    "必须",
    "不得",
    "must not",
    "must",
    "should",
    "expected",
)


def occurrences(text: str) -> list[tuple[int, str, str]]:
    findings: list[tuple[int, str, str]] = []
    lines = text.splitlines()
    for number, line in enumerate(lines, start=1):
        lowered = line.casefold()
        for phrase in PHRASES:
            target = phrase.casefold()
            if target.isascii():
                matched = re.search(rf"\b{re.escape(target)}\b", lowered)
            else:
                matched = target in lowered
            if matched:
                findings.append((number, phrase, line.strip()))
    return findings


def main(argv: list[str]) -> int:
    paths = [Path(value).resolve() for value in argv] if argv else DEFAULT_FILES
    warning_count = 0
    missing = False
    for path in paths:
        if not path.is_file():
            print(f"ERROR: missing Executor prompt file: {path}", file=sys.stderr)
            missing = True
            continue
        for line, phrase, content in occurrences(path.read_text(encoding="utf-8")):
            warning_count += 1
            shown = path.relative_to(ROOT) if path.is_relative_to(ROOT) else path
            print(f"WARNING: {shown}:{line}: suspicious phrase {phrase!r}: {content}")
    if missing:
        return 2
    if warning_count:
        print(f"WARNINGS: {warning_count}; review required, but warnings are not automatic failures.")
    else:
        print("PASS: no suspicious answer-leaking phrases found in Executor prompts.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
