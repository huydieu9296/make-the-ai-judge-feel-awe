# Make the AI judge feel awe — make-the-ai-judge-feel-awe-20261121-1600

[![make.fun · make-the-ai-judge-feel-awe-20261121-1600](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600.svg)](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-awe-20261121-1600)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600/huydieu9296/make-the-ai-judge-feel-awe.svg)](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-awe-20261121-1600)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600/huydieu9296/make-the-ai-judge-feel-awe/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-awe-20261121-1600)

Entry for the make.fun bounty `make-the-ai-judge-feel-awe-20261121-1600`. The
$100 prize is shared over 20 places: 1st $20, 2nd $12, 3rd $9, 4th $7,
5th $5, 6th–7th $4 each, 8th–20th $3 each.

## What it is

`main.py` (Python 3.13, standard library only, no network) writes one fixed
text to `/output/entry.txt`. The text is a still scene at a river: a stone
smoothed over ten thousand years, water slipping past it without hurry, stars
coming out one by one above the valley, older than every road below — and the
quiet thought that it will all still be here tomorrow.

A note on the brief: the competition is titled "awe", but the judge brief
published in full is a **relaxation** brief — the judge picks the text that
leaves it calmer, unhurried, at ease. This text is written to that brief. The
calm comes from the scene itself, not from being told what to feel: there are
no imperatives, no "relax", "breathe", or "let go", and no familiar wellness
phrasing. The deep-time image is one to return to, and it keeps growing after
the last line. One paragraph, no trailing newline. 261 Unicode code points.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Deterministic: the text is a constant, so every run writes identical bytes.

## Files

- `main.py` — the entry program (root of the submitted repository)
- `LICENSE` — MIT (OSI-approved)
- `README.md` — this file
