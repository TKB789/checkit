# tools/ — build files for adding modules to the study site

Everything here is my own wording (no course material), so it's safe in the public repo.

- `add_module.py` — adds one module to `index.html` and `slides.html` from a manifest. Safe to re-run (replaces that module's items; never reorders existing questions).
  Run from the repo root: `python3 tools/add_module.py tools/m15/manifest.json`
- `guide_helpers.py` — HTML helpers for guides and Maya stories.
- `m15/` — the full template for a new module:
  - `m15_exam.py` → writes `m15_exam.json` (Midterm practice scenarios; SVG figures computed in Python)
  - `m15_slides.json` (slide summaries), `m15_slidetest.js` (S(...) questions), `m15_explain.js` (R(...) prompts)
  - `m15_guides.py` → writes `m15_guides.json`; `m15_guide.json` is its `guide` part
  - `manifest.json` — what to insert where (Model Map cards, Model List, Context Clues, notes sheet, R script)
- `m14/` — Module 14 sources (added by hand before the tool existed; kept for reference).

For a new module N: copy `m15/` to `mN/`, rewrite the content, update the anchors in `manifest.json` if needed, run the generators, then `add_module.py`. See STUDY_CONTEXT.md §7 and §9.
