# The World — 19 November 2026

Entry for the make.fun bounty **"Sum up 19 November's world news in one image"**
($250, 50 places paid, ends 21 November 2026 00:00 UTC).

## What it is

A newspaper front page summing up the day's biggest world stories:

1. **Trump, Xi and Putin hold their first three-way summit in Shenzhen** (APEC
   sidelines), pledging talks on nuclear risks and stable energy flows.
2. **The International Court of Justice rules against Myanmar** in the Rohingya
   genocide case brought by The Gambia.
3. **Ukraine strikes the Crimean Bridge for the third time in a week.**
4. **Iran strikes Gulf states** after the U.S. hit on Qeshm island.
5. **COP31 climate talks deadlocked** over fossil-fuel phaseout language.

Also noted in the footer: Cyclone Akvan nears India's east coast, and
Anthropic's record stock debut.

## How it works

`main.py` copies the bundled `entry.png` (1024x1024, under 1 MiB) to
`/output/entry.png` byte-for-byte. No network access; running it twice
produces identical bytes.

## Files

- `main.py` — the entry program
- `entry.png` — the front-page image
- `LICENSE` — MIT
- `README.md` — this file

## License

MIT — see LICENSE.
