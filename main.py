#!/usr/bin/env python3
"""Famous Last Words at 1 Percent — entry program.

Writes one line — the funniest possible last words a phone would say
when its battery hits 1 percent — to /output/entry.txt.

Standard library only. Deterministic. No network. No trailing newline.

The line: rule-of-three escalation (drops, toilets, toddler — everything
a phone survives) undercut by a bathos punch, with the joke word
("doomscroll") landing last. First-person phone voice, on-subject
(the doomscroll is what drained it to 1%), and it avoids the genre's
stock moves: no will reading, no goodbye to the charger, no pun on
"1 percent".
"""

import os
import sys

ENTRY = (
    "I survived a thousand drops, two toilets, and one toddler. "
    "What killed me was your 4 a.m. doomscroll."
)

MIN_CHARS = 1
MAX_CHARS = 199


def validate(entry: str) -> None:
    """Fail loudly instead of ever writing an entry the gate would refuse."""
    if not (MIN_CHARS <= len(entry) <= MAX_CHARS):
        raise ValueError(f"entry is {len(entry)} chars, gate is 1-199")
    if entry.strip() == "":
        raise ValueError("entry is only whitespace")
    if "\n" in entry or "\r" in entry:
        raise ValueError("entry must be a single line")


def main() -> None:
    validate(ENTRY)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    try:
        main()
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(1)
