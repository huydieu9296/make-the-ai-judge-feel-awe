# Entry for make-the-ai-judge-feel-awe-20261121-1600.
#
# The bounty title says "awe", but the judge's published brief is about
# relaxation: it picks whichever text leaves it calmer, unhurried, at ease.
# So this entry is written to the relaxation brief, not to awe. The calm has
# to come from the scene itself — no orders, no telling the reader to relax,
# breathe, or let go. The dwarfing image is deep time: a stone smoothed over
# ten thousand years, stars older than every road, and a last line that keeps
# growing after the reading ends.
#
# The gate wants UTF-8 text of 1 to 280 characters, counted as Unicode code
# points, and not only whitespace. The text below is one paragraph, 261 code
# points, with no trailing newline. The program writes it as bytes so the
# output is exactly the same on any platform, and because the text is a fixed
# constant, running the program twice produces identical files.
#
# Run locally with MAKEFUN_OUTPUT_DIR set, e.g.:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

TEXT = (
    "A river stone, worn smooth over ten thousand years, rests where the stream "
    "has nowhere to be. The water slips over it without hurry, without asking. "
    "Above the valley the stars come out one by one, older than every road below. "
    "It will all still be here tomorrow."
)

with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(TEXT.encode("utf-8"))
