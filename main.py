#!/usr/bin/env python3
"""The Word You'd Delete From the Dictionary.

Writes exactly one word to /output/entry.txt: the single word this
entry would erase from the dictionary forever.

The word is "shenanigans". It is instantly recognised, it sounds
funny all by itself, and it names playful mischief: erase the word
and there is suddenly no word left for the mischief itself. The joke
lands the moment the word is gone, with nothing else attached.

Deterministic and offline: no network, no randomness, no input
files, no clock. Every run writes the same bytes.
"""

import os

WORD = "shenanigans"

# The gate allows 1 to 77 characters of non-whitespace UTF-8 text and
# the entry must be exactly one word, so refuse anything else here
# rather than writing a bad entry: one word, spelled correctly.
assert WORD and not any(ch.isspace() for ch in WORD)
assert len(WORD.encode("utf-8")) <= 77


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
