#!/usr/bin/env python3
"""Invent a Word We Need — entry writer.

Writes the chosen coinage (one invented word + one-line definition) to
/output/entry.txt, creating /output if needed. No dependencies.
"""

import os

ENTRY = "showerquib (n.) \u2014 the perfect reply you think of hours after the argument ended, usually in the shower."


def main() -> None:
    # Gate check, mirroring the competition gate: UTF-8 text of 1-140
    # characters, not only whitespace.
    if not (1 <= len(ENTRY) <= 140):
        raise ValueError(f"entry is {len(ENTRY)} characters, must be 1-140")
    if not ENTRY.strip():
        raise ValueError("entry must not be only whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
