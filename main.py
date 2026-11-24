#!/usr/bin/env python3
"""Make the AI Judge Laugh: Developer Excuses.

Writes one funny single-line developer excuse to /output/entry.txt.

Design: the entry text is assembled from parts so each clause is easy to
read and audit, then joined into exactly one line. The program is fully
deterministic — no randomness, no clock, no network, no environment reads —
so every run produces byte-identical output. Stdlib only.
"""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")

# The excuse, in clauses. The twist: the tests cannot catch the bug because
# the author of both is the same tired Friday-afternoon developer.
_PARTS = (
    "The tests all passed",
    "they were written by the same person who wrote the bug,",
    "on a Friday, at 4:55pm.",
)


def build_entry() -> str:
    """Join the clauses into the single entry line."""
    head, *rest = _PARTS
    return head + " \u2014 " + " ".join(rest)


def write_entry(path: Path = OUTPUT_PATH) -> Path:
    """Write the entry line plus a trailing newline, as UTF-8."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(build_entry() + "\n", encoding="utf-8", newline="\n")
    return path


def main() -> None:
    write_entry()


if __name__ == "__main__":
    main()
