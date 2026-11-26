#!/usr/bin/env python3
"""The Printer Apology.

Writes the printer's apology note — exactly one line, 1-120 characters
— to /output/entry.txt, for the make.fun bounty
u-eager-stork-81-9647-the-printer-apology-60229153.

The joke: the printer only ever jams on the documents that matter. Test
pages come out flawless, every time — the machine's malice is precise,
not random.
Deterministic: no network, no input, no randomness.
"""

import os

APOLOGY = (
    "Sorry I ate your boarding pass. I only jam the documents you "
    "actually need \u2014 the test pages come out flawless."
)


def main():
    # Gate the sealed scorer enforces: 1-120 chars, a single line, not blank.
    line = APOLOGY.strip()
    if not 1 <= len(line) <= 120:
        raise ValueError("apology must be 1-120 chars, got %d" % len(line))
    if "\n" in line:
        raise ValueError("apology must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
