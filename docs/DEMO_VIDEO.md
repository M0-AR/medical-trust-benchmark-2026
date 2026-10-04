# Demo video guide — how to watch and how to record your own

## Watch in 30 seconds

1. **Animated overview:** open `assets/demo.gif` — 12 frames, 6 seconds per loop. It builds the four live checks one by one: PubMed 68,035 → Crossref 3.4M → Trials 4,068 → Portals 6/6.
2. **Static chart:** open `assets/traffic.png` — top-7 traffic bars with the takeaway caption.
3. **Interactive page:** open `preview.html` in any browser (double-click, no server needed). Toggle ☀ Light / ☾ Dark at the bottom. Screenshots: `assets/preview-light.png`, `assets/preview-dark.png` (1658×1724, captured 2026-10-04).

## Video options for GitHub

GitHub Markdown does not play raw `<video>` tags reliably. Use one of these supported patterns:

**Option A — direct upload (simplest, recommended by GitHub):**
Drag an `.mp4` into a README edit, issue or discussion. GitHub hosts it and returns a URL like `https://github.com/user-attachments/assets/...`. Paste that URL on its own line. Works in READMEs, issues and discussions, including mobile.

**Option B — YouTube thumbnail link (best for long demos):**
Upload to YouTube, then in README:
```markdown
[![Demo video — 2 min tour](assets/preview-light.png)](https://www.youtube.com/watch?v=REPLACE_WITH_ID)
```
Clicking the image opens the video. Keeps the repo small.

**Option C — terminal recording (best for CLI demos):**
Record with `asciinema rec demo.cast`, convert with `agg demo.cast demo.gif` (asciinema gif generator, uses gifski for high-quality timing), embed the GIF. For web pages use the asciinema player embed snippet; for READMEs use the image-link fallback.

## Record your own 60-second tour

```bash
# terminal demo → GIF
pip install asciinema  # or: sudo apt install asciinema
asciinema rec demo.cast   # run: docker compose up --build
agg demo.cast assets/demo.gif
# browser demo → video
# Use OS screen recorder → save docs/tour.mp4 → drag into GitHub README edit
```

Keep GIFs under ~5 MB and under 60 seconds. Prefer 800px width. Narrate what the viewer should notice in each 10-second block.
