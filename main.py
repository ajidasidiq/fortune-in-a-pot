#!/usr/bin/env python3
"""Fortune in a Pot.

A tiny program that writes one kind, funny fortune for the houseplant
on the windowsill to /output/entry.txt.

The fortune is a fixed line, chosen once and kept exactly as written:
a prediction about the plant's own future, warm and a little funny,
short enough to fit on the card tucked into its pot.
"""

from pathlib import Path

FORTUNE = (
    "The sun has chosen your windowsill, and soon even the cat "
    "will admire you from a respectful distance."
)

OUTPUT_PATH = Path("/output/entry.txt")
MAX_CHARS = 120


def gate_ok(text: str) -> bool:
    """The sealed gate's rule: UTF-8, one line, 1 to 120 chars, not blank."""
    if not text or text != text.strip() or "\n" in text:
        return False
    return 1 <= len(text) <= MAX_CHARS


def main() -> None:
    if not gate_ok(FORTUNE):
        raise SystemExit("fortune fails the gate; refusing to write it")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(FORTUNE, encoding="utf-8")


if __name__ == "__main__":
    main()
