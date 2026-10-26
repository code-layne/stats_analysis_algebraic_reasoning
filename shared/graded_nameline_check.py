#!/usr/bin/env python3
"""Fail when a document that loads grading carries a name line.

Graded pages are scanned and sent to an outside API, so they carry the
student's tracking id in the strip and nothing else. Her name goes only on
math-shared's cover sheet. A name line on a graded page invites her to write
her name on a page that leaves the school, so this check fails the build on:

  - a live \\namedateperiod or \\namepartnerperiod, and
  - a hand-written Name:, Date: or Period: field (e.g. "Name: \\blank{4cm}").

Comments are skipped. A document "loads grading" when its preamble has
\\usepackage{grading} (or \\RequirePackage, with or without options).

Usage:
    python3 shared/graded_nameline_check.py unit02/tests/actual_test/main.tex ...
    python3 shared/graded_nameline_check.py --project .     # every main.tex
Files that do not load grading are ignored, so a component and its key can be
passed without checking which of them is graded. Exit status 1 on any hit.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

LOADS_GRADING = re.compile(r"\\(?:usepackage|RequirePackage)\s*(?:\[[^\]]*\])?\s*\{[^}]*\bgrading\b[^}]*\}")
NAME_MACRO = re.compile(r"\\name(?:dateperiod|partnerperiod)\b")
NAME_FIELD = re.compile(r"\b(?:Name|Date|Period)\s*:")


def strip_comments(text: str) -> list[str]:
    """Each line with its % comment removed (an escaped \\% is kept)."""
    return [re.sub(r"(?<!\\)%.*$", "", line) for line in text.splitlines()]


def check(tex: Path) -> list[str]:
    lines = strip_comments(tex.read_text(encoding="utf-8", errors="ignore"))
    if not any(LOADS_GRADING.search(line) for line in lines):
        return []
    hits = []
    for n, line in enumerate(lines, 1):
        for m in NAME_MACRO.finditer(line):
            hits.append(f"{tex}:{n}: {m.group(0)} in a document that loads grading")
        for m in NAME_FIELD.finditer(line):
            hits.append(f"{tex}:{n}: '{m.group(0)}' field in a document that loads grading")
    return hits


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("files", nargs="*", type=Path)
    ap.add_argument("--project", type=Path, help="check every main.tex under this directory")
    args = ap.parse_args()
    files = list(args.files)
    if args.project:
        files += sorted(p for p in args.project.rglob("main.tex")
                        if "math-shared" not in p.parts and "target" not in p.parts)
    hits = [h for f in files if f.exists() for h in check(f)]
    for h in hits:
        print(f"!  {h} — graded pages carry no name line; the name goes on the cover sheet",
              file=sys.stderr)
    return 1 if hits else 0


if __name__ == "__main__":
    sys.exit(main())
