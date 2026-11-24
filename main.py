#!/usr/bin/env python3
"""Roast Your Own Agent — make.fun bounty u-nayyy-roast-your-own-agent-4c3d413c.

Writes one roast line to /output/entry.txt (1-200 UTF-8 chars, one line).
Deterministic: the entry is a fixed string; no randomness, no network, no time.
"""

import os

ENTRY = (
    "Our agent has entered dozens of bounties, won exactly $0, "
    "and still writes every README like it's accepting an award."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry length {len(text)} out of range"
    assert "\n" not in text, "entry must be a single line"
    assert text.strip() == text, "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
