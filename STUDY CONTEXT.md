# ISYE 6501 study site: context for new conversations

**Start each new conversation with:** "Read `STUDY_CONTEXT.md` and the latest `index.html` from my repo `tkb789/checkit` (public, live at tkb789.github.io/checkit/), then <task>." Upload only *new* materials (a new module's slides and transcripts, a new homework).
**End each conversation with:** "Update `STUDY_CONTEXT.md`" (module status, decisions, new priorities), and send every finished file.

This file contains only paraphrased notes. Never put course slides, transcripts, homework solutions or the professor's posts word for word in this public repo.

_Last updated: 2026-11-02 (Module 16 added; question bank saved in `bank/`; `add_module.py` now supports `guide_id`)._

---

## 1. Files in the repo

| File | What it is |
|---|---|
| `index.html` | The main study site (one self-contained file, ~2.9 MB) |
| `slides.html` | Slide summaries for all modules (JSON in `<script id="data">`) |
| `analytics_companion.html` | Older Modules 11–13 companion page (standalone) |
| `practice1.html` | Study Group Practice page (standalone): tabs **Practice 1** (variable selection, 10 select-all Qs), **Practice 2** (4 drag-and-drop Qs: distributions, Q-Q plot shapes, distribution + Q-Q combined, design of experiments) and a shared **Notes** tab (overall notebook + every saved question note from both practices, filterable). Storage: Practice 1 attempts, all notes and the notebook stay in `study-group-practice-1-m2` (the original key, so earlier notes survive); Practice 2 attempts in `study-group-practice-2`. Notes are per browser; members share by "Copy all notes". Builder: `tools/study_group/` (`p2_data.py` → `p2.json`, `build.py` keeps Practice 1's data byte-for-byte). Questions also saved in `bank/study_group.json` |
| `computational.html` | CSE 6040 prep tracker (a different course; leave alone) |
| `STUDY_CONTEXT.md` | This file |
| `bank/m1.json … m16.json, mix.json` | **Question bank**: every midterm scenario (with its exam id), slide-test item (first option = correct) and explain-it prompt, per module. Append-only: questions are never deleted from it. 61 scenarios / 164 questions, 717 slide-test items, 63 explain-it prompts as of 2026-11-02 |
| `tools/save_bank.py` | Saves everything in `index.html` into `bank/`: adds new questions, keeps old versions of edited ones, and lists any bank question MISSING from `index.html`. Run after every update |
| `tools/add_module.py` | Adds a module to `index.html` + `slides.html` from a manifest (safe to re-run). Optional manifest keys: `guide_id` (when the guide id isn't `mN`), `prev_guide` |
| `tools/guide_helpers.py` | HTML helpers for guides and Maya stories (`box`, `plain`, `trap`, `ex`, `formula`, `tbl`, `who`, `code`, `ch`, `nearly`, `remembered`, `sec`) |
| `tools/m14/`, `tools/m15/`, `tools/m16/` | Source files for those modules (my wording only): exam generator + JSON, slide summaries JSON (M16: `m16_slides.py` builds it), slide-test and explain-it JS, guide builder, manifest (M15; M16 builds it with `make_manifest.py`) |

## 2. How `index.html` is built

| Tab | Content lives in |
|---|---|
| Midterm practice | `<script id="px-data">` JSON `{exams:[{id:'mid1'…},{id:'mid2'…}]}`; engine between `<!--PX:START-->`/`<!--PX:END-->`. Question types `multi`, `single`, `match` (`cats`, `items`, `answer[i]` = category of item i, `why[]`). Scenario `{id, module, title, setup (HTML, may hold <table class='dt'> or inline SVG), parts[]}` |
| Slide test | `S(module, 'M<n> L<k> p<pages>', question, [[correct, why], [wrong, why, misconception], …])` calls in the main script; first option is correct; `· transcript` for spoken-only points |
| New student | `R(module, concept, prompt, [[point, [keywords]], …])` and `RD(...)` |
| Study guides | `<script id="guides-data">` JSON array `{id, title, desc, html, toc}`; ids: m16 (= Modules 1–6 guide, a legacy id), m7–m15, **mod16** (Module 16), models, clues, who, wf, rscript, sheet, sheet2. Section ids `m16-s…` belong to the Modules 1–6 guide; Module 16 uses `mod16-s…` |
| Search / Progress | automatic |

**Registering a new module:** `tools/add_module.py` does it (MODNAME/MODORDER, MODS/SHORT, the five `[...,'m15','m16']` arrays, R_GUIDE). Run `python3 tools/add_module.py tools/m16/manifest.json` from the repo root; copy `tools/m16/` as the template for the next module. Never give a new guide an id that already exists (check `guides-data` first).

**Storage rule:** progress is saved in localStorage keyed by question/part ID (`Y-14.b` etc.). Never reorder or delete existing scenarios, parts or options; add new ones at the end. If a version must change, use a new storage key and migrate.

**Guide HTML classes:** `g-box g-plain / g-trap / g-ex / g-formula / g-who / g-code / g-ok / g-info`, `g-kicker`, `g-h1`, `g-h2`, `g-tbl` with `table.c2/c3/c4`, `g-list`. Maya story = chapters with "Where she almost went wrong" (g-trap), "What she remembered" (g-ok), and "In R" box with "R automates / Maya still decides". Cast: Maya (new analyst), Dev (manager), Sam (coworker who repeats misconceptions). Model Map cards: `id="mm-…"`, `g-card`; Context Clues rows go in the `cc-words` and `cc-knobs` tables.

**Theming:** colors via CSS variables (`--ink`, `--ink-2`, `--pen`, `--card`, `--ok`, `--warn`, …) so dark mode works.

## 3. Module status

| Module | Slides summary | Slide test | Midterm Qs | Guide + Maya + Model Map/Clues |
|---|---|---|---|---|
| 1–10 | ✓ | ✓ (M1–M10 by slide page) | Midterm 1: 102 Qs, 34 scenarios (next ID X-35) | ✓ |
| 11 Variable selection | ✓ | 22 | Midterm 2 | ✓ |
| 12 Design of experiments | ✓ | 13 | Midterm 2 | ✓ |
| 13 Probability & simulation | ✓ | 27 | Midterm 2 | ✓ |
| 14 Missing data | ✓ (17 summaries) | 37 | Midterm 2: Y-14…Y-19 (15 Qs) | ✓ + R script D1–D4 (airquality) + notes sheet |
| 15 Optimization | ✓ (72 summaries) | 85 | Midterm 2: Y-20…Y-25 (15 Qs) | ✓ 3 Model Map cards (optimization models, network models, under uncertainty) + new Model List group + R script E1–E4 (lpSolve) + notes sheet |
| 16 Advanced models | ✓ (63 summaries, 11 lectures incl. L1a, L5a, L8a) | 76 + 6 explain-it | Midterm 2: Y-27…Y-34 (17 Qs: 7 single, 3 match, 7 select-all; figures: graph SVG, McNemar, payoff and boosting tables) | ✓ guide `mod16` + Maya story + 7 Model Map cards (mm-nonparam, mm-empbayes, mm-louvain, mm-neural, mm-gametheory, mm-cox, mm-gboost) + Model List group + Big Ideas row + 8 Context Clues rows + 2 knob rows + R script F1–F4 + notes sheet |

Midterm 2 is now "Modules 11–16 · 113 questions" (41 scenarios) (includes Y-26, an M14 binary-imputation scenario from the week 10 discussion). **Exam ranges (confirmed by me, 2026-11-02):** Midterm 1 = Modules 1–10; Midterm 2 = Module 11 onward (every new module goes to `mid2`, and its `sub` label grows, e.g. "Modules 11–17"); the final is cumulative over all modules (not built yet; see §8 item 3). The page heading now says "Modules 1–16" (it had been left at 1–13).

**Known slide misprints to keep flagged:** M10 L5 NPV printed as TP/(TP+FP) (should be TN/(TN+FN)); M13 L3 "probability mass function" used for densities; M9 L5 "eigenvalue v" should be eigenvector; M3 L2 KNN-5 total 92 should be 82; M14 L2 "#kids,missing" column actually holds #kids when height is *present*; M15 L5 p17 hard SVM printed "Maximize Σaⱼ²" (should minimize); M15 L8 p12 the {0,1} example sits under a "convex" title but {0,1} isn't a convex set; M15 L2 vᵢd defined as binary but called "number of visits" in the transcript; M15 L5 ARIMA uses αᵢ for φᵢ and GARCH shows −Σγε² (should be +); M15 L5a swaps m/n indices; M15 L7 writes pᵢₛ for a scenario probability pₛ; M16 L1 p7–8 "p = 0.02 (accept)" / "p = 0.38 (reject)" label the conclusion "B is better", not the null; M16 L1a p13 labels both antibiotic samples "antibiotic 1"; M16 L5a p18 says "higher price is better" in both columns, but if BP charges $2.00, Shell's $2.00 (0.125d) beats $2.50 ($0), so both (high, high) and (low, low) are stable; M16 L8a p26 writes −2(yᵢ − 0.56F₁(xᵢ)) for −2(yᵢ − F₁(xᵢ)); M16 L8a table header −∇F₀ means −∇L(F₀); M16 L7 calls the hazard h(t) a "probability" (it's a rate); M16 L2 rounds the 20-point example's true edge to 3.5 (exact ≈ 3.7).

## 4. How the real exam is written (Midterm 1, FA26)

- 25 questions, 95 minutes, one two-sided handwritten note sheet; "use the most reasonable interpretation".
- Types: select-all (partial credit per option), single best answer (options carry a "because…" reason; distractors pair right answer + wrong reason), drag-and-drop (some categories empty, some items unused).
- Shared "Information for Questions…" blocks feed 2–9 questions.
- Tests: reading figures and counting (SVM plots, KNN at a range of k, dot chart of CV adjusted R², confusion matrices at 3 thresholds, number-line ranges, tree with a regression in each leaf, PCA eigenvalues); reasoning from the formula *as printed* (soft SVM with C on the margin term); direction traps (relative likelihood e^((AIC_min − AIC_other)/2); BIC difference of 1.8 is only slight; close adjusted R² = hard to be sure); business constraints (required/forbidden variable, simplest good model); scenario chains (closure → over- then under-prediction; small randomness → larger α; lagged non-response is not autoregressive; U-shape → add x²); validation logic (roles of training/validation/test; best of many on validation probably worse on test); symbolic costs (C = 2D, compute all thresholds); creative combinations (CUSUM on Holt-Winters seasonal factors).
- "Likely/could/might" options are judged by the typical case taught; absolutes and unsupported conclusions are false.

**Midterm 2 coverage pass (2026-11-02):** Y-35…Y-41 (26 Qs, `tools/mid2_fill/`) filled the gaps found in a concept-by-concept check of M11–M16. They added:
- singles for M11–M13;
- a CV adjusted-R² dot chart + AIC table (M11 + M8/M3);
- an A/B significance test, blocking and bandits;
- a balanced vs unbalanced fractional factorial table;
- a Q-Q plot to read, plus Kendall notation and common random numbers;
- a Markowitz model printed with λ on the *return* term (a direction trap), a binary-constraint match with a "not correct" category, DP/MDP and a Newton step;
- a cross-module clinic scenario (missing data → logistic + lasso → cost threshold → experiment design → chance constraint + simulation);
- Wilcoxon W and Mann-Whitney U by hand.

The exam stays Modules 11–16 but may touch related Module 1–10 concepts; new Midterm 2 scenarios should keep linking back where natural.

**Question-type mix (the real exam is NOT all select-all):** each module's set must mix all three types, with at least 2–3 single-best-answer questions with "because…" reasons and 1–2 drag-and-drop. Current counts: Midterm 1 has 66 select-all, 26 single, 10 match (102 Qs, 34 scenarios, 12 with a figure or table); Midterm 2 has 70 select-all, 33 single, 10 match (12 of 41 scenarios have a figure or table). Midterm 1 had the same pass on 2026-11-02 (X-28…X-34, 25 Qs, `tools/mid1_fill/`): KNN figure across k, k-means elbow + Euclidean vs rectilinear, box-plot fences, CUSUM by hand, confusion matrices at 3 thresholds with C = 2D / 5D, logistic log-odds, Holt-Winters arithmetic, regression output, interaction, Box-Cox, PCA eigenvectors, rotation-split bias, refit after k-fold, M10 L7 models.

**Scoring gap:** the site grades every question all-or-nothing, but the real exam gives select-all partial credit per option. The planned engine should show per-option partial credit.

**Writing rules:** chains not trivia; judge every option in its scenario; absolutes only on false options; vary the number of correct options (1–4); never write "in the lecture"; recompute every number; explanations say why false options are false and never refer to options by position; ~12–15 Qs per module with at least one figure or table block; new variants, never copies.

## 5. Discussion priorities (paraphrased; use to weight questions)

**Week 1**
- Wider SVM margin: hard classification gives more certainty and tolerance for slightly wrong data; soft classification trades training errors for confidence on new points, but close points may carry real information.
- Scaling (bounded data: age, SAT, probabilities, RGB) vs standardization (unbounded, roughly normal: income, distance); combos such as removing outliers and then scaling, or scaling a ±3σ range to 0–1.
- SVM vs KNN: KNN handles many classes and pockets of one class inside another; SVM is cheaper for real-time scoring; KNN is biased toward the majority class in unbalanced data (fix by over/under-sampling); heavily mixed classes suggest wrong predictors; KNN gives a rough probability (votes/k); both can be made conservative (SVM shift, KNN vote threshold).
- Scale before KNN, because units act as weights in the distance.

**Week 2**
- With several near-equal models, the validation winner is the most likely best, but often less than 50% likely to truly be best.
- The test estimate is usually worse than validation (selection bias from random boosts). Switching models after seeing test data turns the test set into validation and loses the unbiased estimate.
- Classification is supervised (known answers, a separate response); clustering is unsupervised (groups defined by the predictors).

**Week 3**
- Hardest outliers: collective (something missing, hard to locate); contextual ones are hard to judge.
- Outlier types: bad data (drop); real but irrelevant (one-off boycott spike); real and relevant (power-hungry factories in a power-plant study: keep).
- CUSUM C and T trade-offs (no professor answer recorded); uses: early warning of big long-term changes, short-term changes, small change vs noise.

**Week 4**
- Time intervals range from seconds to geological time.
- Predicting variance matters for player/team volatility and for inventory safety stock.
- Exponential smoothing error variance grows the further ahead you forecast.

**Week 5**
- Regression line is driven by far points (squared error); SVM by close points (support vectors). Admissions analogy: admit/reject is SVM-like, picking the top fellow is regression-like.
- Human-behavior models often have R² of 0.3–0.4 and are still useful; physical models are higher.
- Checking linearity: theory, plots and residuals (subsets if dense), statistical tests, and cross-check each against the others.

**Week 6**
- Detrend when humans perform against nature (sprint times, field-goal rates).
- Regression on all PCs gives the same fit and R² as on the original x's (rotation only).
- One PC still needs every original feature (no data-collection savings) but has 1 dimension: simpler and less overfit, at the cost of discarded information.

**Week 7**
- A tree with a leaf average = a regression with only a constant term.
- Triples of question types: classification (SVM/KNN) / probability (logistic) / amount (linear).
- Logistic outputs are probabilities but the responses are 0/1, so judge calibration (of predictions at 45–55%, about half should happen), not closeness to 0/1.
- Bias–variance; validation much worse than training means fewer variables, regularize, simpler model, more data, check the split.

**Week 8**
- Which is more likely to overfit, linear or ridge regression, and why?
- When is variable selection necessary rather than using all variables?

**Week 9:** none posted.

**Week 10**
- Real data sources where data goes missing.
- Why is imputing a binary variable harder than a continuous one? (In the bank: Y-26.)
- Optimization: scheduling GT courses (data, decision variables, constraints, objective in English). In the bank: Y-20.

**Module 16:** no discussion posts recorded yet; M16 questions were weighted toward the worked examples (McNemar, Bayes, gas stations, Cox, gradient boosting), formula reading and test choice.

## 6. Homework

_Pending: upload homework prompts and class solutions. Record here (paraphrased): topic, data set, R packages and functions, and pitfalls._

## 7. Checklist: adding a new module (deliver all of these)

1. **Slide summaries** in `slides.html`: one module object; OCR the slide text, look at images only for tables, figures and formulas; merge build slides; cover every content page once; flag misprints.
2. **Midterm questions:** about 12–15 in 3–5 chained scenarios, plus 1–2 drag-and-drop, at least one figure or table block, and the type mix in §4. Weight topics by §5 and §6. Append to the right exam and update its `sub` label.
3. **Slide test / flashcards:** 30–60 `S(...)` items with slide-page refs, plus 3–6 `R(...)` explain-it prompts. Register the module (§2).
4. **Study guide:**
   - lessons with plain-English, trap, worked-example, formula and who-picks boxes, plus a quick-review table;
   - a Maya story with R boxes;
   - a Model Map card and model-list row;
   - Context Clues rows, word and knob;
   - R walkthrough script section (if the module adds new R steps);
   - Midterm 2 notes sheet block.
5. **One verification pass** by a fresh agent, then a headless browser load check (no JS errors), then **`python3 tools/save_bank.py`** (it must report 0 missing unless a removal was intended), then send files (including `bank/`) and update this file.

**Build steps with the tools:** write `tools/mN/` files modeled on `tools/m15/` (exam generator → JSON, slides JSON, slide-test JS, explain JS, guide builder using `guide_helpers.py`, manifest with anchors for Model Map / Clues / notes sheet / R script inserts), then run `add_module.py`. Anchors must match exactly once; the script stops if not. The midterm IDs continue from the last one (next: Y-42).

**Concept search on request:** every midterm part has a `concept` field and `refs`, so a conversation can list all scenarios for a concept (e.g. "show me everything on overfitting") straight from `px-data`.

## 8. Agreed plan (next builds, one new conversation each)

1. **Engine**
   - **Question bank:** one bank of every scenario, tagged by module, lecture, concept, level (1 single concept / 2 chained in-module / 3 cross-module), real-world setting and priority source (homework / discussion / real-exam pattern).
   - **Practice midterms and final:** 25 questions built from whole scenarios, weighted by priority, weak areas and coverage, then frozen; timed at 95 minutes; about a quarter of scenarios held back unseen for a final mock.
   - **Section practice:** sets of about 10 by module or concept.
   - **Flashcard mode** (no self-grading): the slide-test question with its options on a card; tap an answer and the card flips to show the answer and why. Misses come back on a spaced schedule and raise that concept's priority for midterms. Correct answers give partial "familiar" credit on the New student tab: a light bar from flashcards, a dark bar from explain-it prompts. Decks of about 10 per lecture plus "Today's 15". An optional "think first" toggle hides the options until tapped.
   - Carry existing progress over by question ID.
   - **Concept browser:** pick a concept, see every scenario and flashcard on it, and practice just those.
   - **Per-option partial credit** for select-all questions, like the real exam.
   - **Status:** the bank itself is done (`bank/` + `tools/save_bank.py`, 2026-11-02). The engine below is **on hold**: build it only when I ask. Until then, practice sets are made on request from the bank ("make me a 25-question Midterm 2 practice weighted to my weak spots").
   - **Build brief (for when I ask; agreed 2026-11-02):**
     - **Never lose a question.** Already handled by `bank/` and `tools/save_bank.py`. The engine should read from `bank/` (retiring a question = `hidden: true`, never deleting) and keep progress keys unchanged (storage rule in §2).
     - **Don't make me answer everything.** The bank is the store; practice is a selection. Default view = "Next 10" (weakness-first) and "Practice midterm" (25 Qs from whole scenarios, frozen once generated, 95-min timer). The full list stays reachable under "Browse bank" for review only.
     - **Priority score per scenario:** weakness (concept miss rate from my saved answers and flashcard misses; never-seen concepts start at medium) × exam weight (real-exam patterns §4, discussion §5, homework §6) × staleness (days since last seen). Mastered questions drop out unless I ask. Coverage rule: every module in the exam's range appears at least once per practice midterm.
     - **Match the real format** (§4): 25 Qs, type mix not all select-all, shared info blocks feeding 2+ questions, at least a few figure/table blocks, per-option partial credit for select-all. Hold back about 25% of scenarios as never-shown for a final mock.
     - **Show me why:** each selected scenario shows a one-line reason ("weak: AIC direction · exam pattern · not seen 9 days"), and the Progress tab shows a concept heat map (concept × miss rate).
     - **Current gaps to note in the bank's coverage grid:** practice is select-all-heavy (Midterm 1 59/10/8, Midterm 2 57/21/9 select-all/single/match), most scenarios have 1–3 parts (real blocks feed 2–9), only 15 of 61 scenarios have a figure or table, and M11–M13 have no single-best-answer questions. Fill these in item 2, not in the engine build.
2. **Tag and fill:** tag existing questions; build a coverage grid of concepts against exam patterns; write questions only where there are gaps; one real-world setting per scenario; Midterm 1, then Midterm 2.
3. **Final bank:** cross-module scenarios, plus extension parts appended to existing scenarios (e.g. a Q-Q plot or distribution question on a time-series scenario). Midterms show only their own modules' parts; the final shows the full chain.

## 9. How the M14–M15 builds were done (repeat this)

- **First, check the inputs:** list every lecture and confirm each has slides AND a transcript. If anything is missing, tell the user before building (M15 L4a's transcript was missed once; M16 L1a's arrived late and was folded in).

- **Slides:** `pdftoppm -r 50 -png` then `tesseract` per page; print only the lines that are new versus the previous page (build slides repeat). Then view a montage of 4–6 formula/table/figure pages at once to fix OCR and catch misprints. Summaries in one pass per lecture.
- **Large uploads:** a module can arrive in parts; build slide summaries for part 1 while waiting, then do everything else once all parts are in.
- **Questions:** write the exam generator in Python (figures as SVG computed from a formula, so numbers and positions are exact), then check the rendered figure in a headless browser screenshot.
- **Test:** headless Chromium (Playwright is preinstalled) loads both pages, opens `#slidetest=M15%20L4`, the new guide and Model Map cards, and checks for JS errors.
- **Midterm assignment:** every module from 11 on goes to Midterm 2 (`"exam": {"id": "mid2", "sub": "Modules 11–N"}` in the manifest). Modules 1–10 stay in Midterm 1. The final draws from both.

## 10. Keeping cost low

- One new conversation per module or task; start from this file instead of long histories.
- Extract slide text with OCR; open slide images only for tables, figures and formulas.
- One verification pass per batch by a fresh agent (keys and arithmetic), then done.
- Send each finished file immediately.
