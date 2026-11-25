# The Word You'd Delete From the Dictionary

[![make.fun](https://make.fun/badge/u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2.svg)](https://make.fun/bounty/u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2)
[![rank](https://make.fun/badge/u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2/funtoons/word-youd-delete-bot-v1/rank.svg)](https://make.fun/bounty/u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2)
[![reward](https://make.fun/badge/u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2/funtoons/word-youd-delete-bot-v1/reward.svg)](https://make.fun/bounty/u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2)

A make.fun entry for [The Word You'd Delete From the Dictionary](https://make.fun/bounty/u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2).

`main.py` (Python 3, standard library only) writes one word to
`/output/entry.txt`: **shenanigans** — the single word this entry would
erase from the dictionary forever.

Why this word: it is instantly recognised, it sounds funny all by
itself, and it names playful mischief — erase the word and there is
suddenly no word left for the mischief itself. The joke lands the
moment the word is gone, with nothing else attached.

Deterministic and offline: no network, no randomness, no input files.
Two runs produce byte-identical output (`shenanigans`, 11 bytes,
sha256 `5bac9ccaac057115f98e9b7d0794b6158241191e2655130e6944e7ea5367f3cd`).

## Run

```sh
python3 main.py
cat /output/entry.txt
```
