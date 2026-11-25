#!/usr/bin/env python3
"""The 3 AM Excuse — make.fun entry.

Writes one line to /output/entry.txt: the excuse a hardware wallet
gives for refusing to sign a transaction at 3 AM.
"""

import os

# The line is assembled from fragments so each beat can be tuned
# without touching the others: setup (the hour + the refusal),
# twist (the stranger who knows the PIN), punch (the condition).
SETUP = "At 3 AM I don't take orders from a sleep-deprived stranger "
TWIST = "who happens to know my PIN \u2014 "
PUNCH = "come back when you're you again."


def assemble() -> str:
    return SETUP + TWIST + PUNCH


def validate(text: str) -> str:
    """Gate: UTF-8, 1-200 characters, not only whitespace."""
    if not isinstance(text, str):
        raise TypeError("entry must be a string")
    if not (1 <= len(text) <= 200):
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    text.encode("utf-8")
    return text


def main() -> None:
    text = validate(assemble())
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
