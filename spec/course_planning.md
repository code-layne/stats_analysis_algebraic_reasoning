# Course Planning Log — Statistical Analysis & Algebraic Reasoning

**Last updated:** 2026-08-06 — **Lesson 1.5 authored, built, and gated** (all components +
keys + slides). Earlier the same day: Lessons 1.1, 1.2, 1.3, and 1.4. Previous run
(2026-08-05): Lesson 1.0 authored and the course palette replaced royal blue → **cerulean**
across the whole tree.

> **PROJECT DIRECTORY RENAMED 2026-08-06:** `~/Mathematics/stats_analysis_algebraic_reasoning`
> → `~/Mathematics/saar`. Worktrees created after the rename are fine; a worktree opened
> *before* it still has a `.git` file pointing at the old path and needs
> **`git worktree repair`** run from `~/Mathematics/saar` first. Always start a run from the
> new path.

## Current state

### Palette — CHANGED 2026-08-05 (user decision)

The scaffold had copied Algebra/Trig/Data Analysis's royal blue (`#1D3F94`) **verbatim**, so the
two courses were visually identical. The dominant color is now **cerulean `#0B6FA4`** — the third
blue across the stats-family courses, separated by *hue* so it survives a photocopy:

| Course | Dominant | Hex |
|---|---|---|
| AP Statistics | navy | `#1F3A5F` |
| Algebra, Trig & Data Analysis | royal | `#1D3F94` |
| **Statistical Analysis & Algebraic Reasoning** | **cerulean** | **`#0B6FA4`** |
| Algebra 2 | forest | `#1E5631` |
| Precalculus | plum | `#4B2A6C` |
| Linear Algebra | burgundy | `#6B2137` |

- Names renamed tree-wide (895 files): `royal`→`cerulean`, `royallight`→`ceruleanlight`,
  `mist`→`frost`, `mistmid`→`frostmid`, `bluebox`→`frostbox`, `\royalheader`→`\ceruleanheader`.
- **No deprecated aliases** — the old names are undefined, so a stale reference fails loudly.
- Unchanged: gold accent, green vocab, red, plum `practicebox` (deliberately not blue),
  `graybg` teachernote, `keyred`.
- Beamer override: brighter cerulean `#1785BF` for dark slides.
- Contrast checked: white on cerulean **5.49:1** (WCAG AA, normal text).
- `.claude/skills/lesson-planning/` docs (SKILL.md, conventions.md, components.md) and
  `new_lesson.py` were all updated to match — new scaffolds emit cerulean.

*(An earlier pass in this session briefly ported Linear Algebra's burgundy palette before the
user redirected to a third blue. No burgundy remains in the tree.)*

### Lessons

- `spec/statistical_analysis_algebraic_reasoning.md` is the **confirmed** course map: 8 units,
  58 content lessons + one Lesson 0 per unit (66 lesson dirs), semester split after Unit 4.
- **Lesson 1.0 — "Unit Launch: Study Design" — is COMPLETE.** All components authored, built,
  and passing the gate. It is the **model lesson**; mirror its structure and voice.
  - Standards: **PS.DC.1a–c; AFDA.DA.2a** (previews PS.DC.1d–e, PS.DC.2, PS.DC.3).
  - Scope: data-in-context (who/what/units), individuals vs. variables, **categorical vs.
    quantitative**, the numbers-that-are-really-labels trap (grade level, jersey #, ZIP),
    statistical questions, and a preview of the 4-stage data cycle. The cycle is *previewed*
    only — Lesson 1.1 teaches it formally.
  - Contexts: Riverbend HS Student Life Survey (notes), Riverbend Athletics (activity),
    Northgate Recreation Center (homework). All arithmetic verified in Python.
  - Page counts: warmup 1/1, notes 4/4, activity 2/2, exit ticket 1/1, homework 2/2;
    plan 5pp, slides 9 frames.
  - `make -C unit01/lesson00 all` exits 0; `make -C unit01/lesson00 check` **passes**.
- **Lesson 1.1 — "The Statistical Cycle and Types of Data" — is COMPLETE.** All components
  authored, built, and passing the gate.
  - Standards: **PS.DC.1a–c; AFDA.DA.2a** (previews PS.DC.1d–e in the 1.2 hand-off).
  - Scope: the four stages named formally and what each *hands to the next*; the three tests
    for a question (answers vary / group named / measurement named) and repairing one that
    fails; **the question decides the data type** (the lesson's pivot — 1.0 classified
    variables in a finished table, 1.1 decides the type before any data exist); frequency
    tables and relative frequency; conclusion in context; diagnosing which stage a flawed
    study broke at.
  - Contexts: Riverbend Student Council bike-rack survey (notes; 60 students — bus 27, car 15,
    walk 12, bike 6, scaled to 900), Riverbend breakfast cart (activity; 40 students), Lakeside
    Farmers Market (homework; 50 shoppers, 800 Saturday total). All arithmetic verified in
    Python.
  - Page counts: warmup 1/1, notes 4/4, activity 2/2, exit ticket 1/1, homework 2/2;
    plan 5pp, slides 9 frames. `make -C unit01/lesson01 all` and `check` both exit 0.
- **Lesson 1.2 — "Populations, Samples, Parameters, and Statistics" — is COMPLETE.** All
  components authored, built, and passing the gate.
  - Standards: **PS.DC.1d, PS.DC.1e** (PS.DC.1b carried forward in the conclusion items).
  - Scope: population vs. sample vs. sample size; census; parameter vs. statistic (decided by
    *who the number describes*, never by what it looks like — the trap row is a percent drawn
    from district records for a whole population); the five constraints (**time, cost, access,
    destruction, change**) that make a census impractical; **sampling variability** — three
    honest samples, three statistics, one parameter, nobody wrong; and what a sample does and
    does not license a report to claim.
  - Notation (μ, x̄, p, p̂) appears **once**, pre-filled, as exposure only in notes §2 — not
    assessed anywhere in the lesson. Flagged as such in the Guided Notes teacher note.
  - Contexts: Lakeside Farmers Market carried over from 1.1's homework (notes; 800 Saturday
    shoppers, 50 asked, 26 drove → 52%, scaled to 416; Ana/Ben/Cleo 26/24/29 of 50 → 52/48/58%),
    Millbrook Public Library (activity; 1,200 card holders, 60 asked → 21/18/15/6 = 35/30/25/10%,
    second sample 27/60 = 45%, mean 30/6 = 5 items), Westfield High School (exit ticket; 800
    students, 40 asked, 26 = 65%), Harbor Point Community Pool (homework; 1,500 members, 75
    asked → 27/21/18/9 = 36/28/24/12%, 0.36×1500 = 540, mean 80/8 = 10 visits, second sample
    30/75 = 40%). All arithmetic verified in Python before authoring.
  - Page counts: warmup 1/1, notes 4/4, activity 2/2, exit ticket 1/1, homework 2/2;
    plan 5pp, slides 9 frames. `make -C unit01/lesson02 all` and `check` both exit 0.
- **Lesson 1.3 — "Choosing a Sample: Four Sampling Techniques" — is COMPLETE.** All components
  authored, built, and passing the gate.
  - Standards: **PS.DC.2a, PS.DC.2b; AFDA.DA.2b**.
  - Scope: the **sampling frame**, and the one line that separates a **probability sample**
    (chance chooses) from a **convenience sample** (the researcher / the schedule chooses);
    then the four techniques with an executable procedure each — SRS off a random digit strip
    (skip out-of-range, skip repeats), **stratified** allocation proportional to strata size,
    **systematic** interval $k = N \div n$ from a random start, and **cluster** (a few whole
    groups, everyone in them). The lesson's pivot is **stratified vs. cluster**, taught as
    *some from every group vs. everyone from a few groups*, with a fill-in contrast table.
    Closes on PS.DC.2b: choosing a technique from **what the context allows** (what list
    exists; which subgroups differ) and justifying it. Bias is named only as a hand-off.
  - Contexts: Riverbend HS carried from 1.1/1.2 (notes; 900 students → 60; strata 270/240/210/180
    → 18/16/14/12 at 1/15; systematic $k=15$ from start 7 → 22, 37, 52; 36 homerooms × 25,
    3 drawn → 75), Cedar Ridge Apartments (activity; 600 households in 30 buildings × 20,
    unit-type strata 120/280/200 → 12/28/20 at 1/10, $k=10$ from start 4; buildings 1–6 studio,
    7–20 one-bed, 21–30 two-bed, so a building is a **stratum wearing a cluster's clothes** —
    Tier E), Bayside Middle School (exit ticket; 750 → 30, $k=25$ from start 6 → 31, 56),
    Harbor Point Community Pool (homework; **1.2's flawed Tuesday-evening study, replanned** —
    1,500 members → 100, generator returns 0412/1587/0973/0412/0288 → members 412, 973, 288;
    strata 600/525/375 → 40/35/25 at 1/15; $k=15$ from start 9; 4 of 25 swim sessions × 25 ≈ 100).
    All arithmetic verified in Python before authoring.
  - Page counts: warmup 1/1, notes 4/4, activity 2/2, exit ticket 1/1, homework 2/2;
    plan 5pp, slides 9 frames. `make -C unit01/lesson03 all` and `check` both exit 0; PDFs
    eyeballed for stranded boxes (none — the homework's Practice box splits 4 items / 4 items).
- **Lesson 1.4 — "Bias in Samples and Surveys" — is COMPLETE.** All components authored,
  built, and passing the gate.
  - Standards: **PS.DC.2c; AFDA.DA.2e, 2f, 2g**.
  - Scope: **bias is a direction, not bad luck** — the lesson's pivot, taught by contrasting
    1.2's honest samples (which scatter *around* the parameter) with a biased procedure that
    misses the same way every time. Then **sampling bias** split into **undercoverage** (off
    the frame) and **nonresponse** (chosen but silent), with the test question *could that
    person have been chosen?* separating them; the standard's line that **a large sample size
    does not make up for bias**, carried by arithmetic rather than assertion; the seven named
    **response biases** (demand, social desirability, dissent, acquiescence, extreme responses,
    neutral responding, question order) as a pre-filled reference table plus four diagnostic
    rows; and closing on **AFDA.DA.2g** — four ways to reduce bias, each attached to the bias
    it removes. Students are asked for the **direction** of the error throughout, not just the
    label.
  - Contexts: Harbor Point Community Pool carried from 1.2/1.3 (warm-up + notes; census truth
    $300/1500 = 20\%$, Tuesday-evening sample $27/75 = 36\%$ scaled to $0.36 \times 1500 = 540$,
    off by $240$ members; the ten-week repeat $270/750 = 36\%$ — same answer, same $16$-point
    error; three honest samples 19/22/19 average exactly $20\%$ against three Tuesday samples
    35/36/37 averaging $36\%$; question-order pair $62\%$ vs. $41\%$, a $21$-point gap), Cedar
    Ridge Apartments carried from 1.3 (activity; $600$ households mailed, $150$ return =
    $25\%$, $96/150 = 64\%$ scaled to $384$, census truth $240/600 = 40\%$ → $24$ points and
    $144$ households too many; the double-size re-run $192/300 = 64\%$ is the "size doesn't
    fix it" payoff), Bayside Middle School carried from 1.3 (exit ticket; $24/30 = 80\%$, then
    $48/60 = 80\%$), Millbrook Public Library carried from 1.2 (homework; front-desk pile
    $72/90 = 80\%$ → $960$ of $1{,}200$, against a proper phone sample $54/120 = 45\%$ → $540$,
    a gap of $35$ points and $420$ card holders; order effect $68\%$ vs. $47\%$; a $78/120 =
    65\%$ response rate as the closing transfer item). All arithmetic verified in Python
    before authoring.
  - Page counts: warmup 1/1, notes 4/4, activity 2/2, exit ticket 1/1, homework 2/2;
    plan 6pp, slides 9 frames. `make -C unit01/lesson04 all` and `check` both exit 0; PDFs
    eyeballed for stranded boxes (see the Tier E note under "Gotchas").
- **Lesson 1.5 — "Observational Studies" — is COMPLETE.** All components authored, built,
  and passing the gate.
  - Standards: **PS.DC.2d** (PS.DC.1a–b carried forward in the cycle and conclusion items).
  - Scope: the one-word definition — you measure or survey **without assigning**, so the
    groups formed themselves (and a **survey is one type of observational study**, which
    makes every Unit 1 study so far one); **using the statistical cycle to plan and conduct**
    the study, which is what PS.DC.2d actually asks and is the section not to skip; comparing
    two already-existing groups with two different denominators; **explanatory vs. response**
    variable; and the lesson's pivot — **association is not causation**, taught as *three live
    stories for one table*: the claim, the same arrow **backwards**, and a **lurking
    variable** outside the study moving both. Closes on which statements the study licenses,
    a banned-verb list (*causes, makes, raises, improves*), and the fact that a prediction
    about switching groups is a causal claim in disguise. Experiments are named only as the
    1.6 hand-off.
  - **Deliberate placement after 1.4:** every scenario in 1.5 is drawn at random with a 100%
    response rate, so bias is off the table and what remains is visible. The homework's
    closing item is exactly this — *no bias at all, and still no causation*.
  - Contexts: Harbor Point Community Pool carried from 1.2/1.3/1.4 (warm-up + notes; SRS of
    $200$ from $1{,}500$, $80$ morning / $120$ evening, sleep $7+$ hrs $56/80 = 70\%$ against
    $54/120 = 45\%$, a $25$-point gap; pooled $110/200 = 55\%$ scaled to $825$; the lurking
    variable is retirement, $60/80 = 75\%$ against $18/120 = 15\%$), Riverbend HS carried from
    1.0–1.3 (activity; $900$ students, sample of $150$, Study Center users $39/60 = 65\%$
    against non-users $72/90 = 80\%$ — the association runs **backwards**, and Tier E proves
    it with the previous quarter's records, $45/60 = 75\%$ had already failed a class against
    $9/90 = 10\%$; pooled $111/150 = 74\%$ scaled to $666$), Bayside Middle School carried
    from 1.3/1.4 (exit ticket; band $90/150 = 60\%$ against $240/600 = 40\%$, a $20$-point
    gap), Millbrook Public Library carried from 1.2/1.4 (homework; $1{,}200$ card holders,
    unbiased phone sample of $240$, Summer Reading Program $72/90 = 80\%$ against $48/150 =
    32\%$, a $48$-point gap; pooled $120/240 = 50\%$ scaled to $600$; previous-summer records
    $63/90 = 70\%$ against $30/150 = 20\%$). All arithmetic verified in Python before
    authoring.
  - Page counts: warmup 1/1, notes 4/4, activity 2/2, exit ticket 1/1, homework 2/2;
    plan 6pp, slides 9 frames. `make -C unit01/lesson05 all` and `check` both exit 0; every
    page of both packets was rendered and eyeballed (see "Gotchas" for the two boxguard
    repairs that took).
- **All other 60 lesson dirs are unmodified skeletons** (now cerulean). Unit tests/test keys
  are skeletons too.
- Per-unit progress: **U1: 6 of 9 authored (lesson00, lesson01, lesson02, lesson03,
  lesson04, lesson05)**; U2–U8 scaffolded, 0 authored.
- Key design decisions (user-confirmed 2026-08-05): AFDA.AF.3 excluded; no trig; polynomial/log
  from A2.F.1/A2.F.2; counting = two lessons (3.7, 3.8); projects close U1, U5, U6, U7 + U8
  capstone; every unit gets a `lesson00/` launch outside the 8-content-lesson cap.

## Next steps

1. **Commit Lesson 1.5** on `claude/lesson-1-5-generation-ffc6b9` and open its PR. The lesson is
   authored, built, and gated but **not yet committed** — the run stopped short of committing
   because commits/pushes are only made on request.
2. **Author Unit 1 Lesson 1.6** — "Principles of experimental design" (PS.DC.3a–b;
   AFDA.DA.2c). Lesson 1.5's homework remindbox sets it up and already names all four
   principles, so do not re-introduce them from scratch: an observational study cannot reach
   causation because the groups build themselves, so build them instead. Scope from PS.DC.3a:
   treatment/control groups, blinding and the placebo effect, experimental units/subjects,
   and blocking / matched pairs / completely randomized designs; then PS.DC.3b's four
   principles — **comparison, randomization, replication, control** — evaluated in context.
   Can assume all of 1.0–1.5's vocabulary, and specifically 1.5's association/causation,
   lurking variable, and explanatory/response pair. The activity's Tier E item 3(b) already
   floated a randomized design for the Riverbend Study Center *and* the ethical objection
   (you must deny half the students help) — that is the natural opening context. Live
   contexts for reuse: Harbor Point pool, Riverbend HS Study Center, Millbrook Library
   Summer Reading Program, Cedar Ridge Apartments, Bayside Middle School.
3. Then finish Unit 1 (1.7–1.8), building + `make check` per lesson.
4. Author the Unit 1 practice/actual tests once its lessons exist, plus `unit01/unit_cover/` and
   `unit_cover_key/` (the test rationale/scoring page).
5. The lesson-1.0 + palette work merged to `main` as PR #3; Lesson 1.1 as PR #4; Lesson 1.2 as
   PR #5; Lesson 1.3 as PR #6; Lesson 1.4 as PR #7.

## Gotchas found this session

- **`sed -i '' -e 's/\bfoo\b/'` silently does nothing on macOS** — BSD sed has no `\b`. Use
  `perl -pi -e` for any word-boundary rename.
- `\ansline` answers longer than ~90 characters wrap and break blank/key page parity. Keep them
  to one line, or reserve a second `\writeline` in the blank.
- `\boxguard` defaults to 16 baselines, which over-refuses for a short box. Size it to the box:
  `\boxguard[12]` for a ~10-line box like `hookbox`.
- **`\writeline` does not break the line** (it is `\hrulefill` + spacing), so two in a row render
  as *one* writing line while the matching pair of `\ansline`s in the key prints two. Page parity
  still passes, but the student is short a line. Use `\writelines{2}` wherever the key answer
  needs two lines. (Lesson 1.0 has the older two-`\writeline` pattern in a few places; harmless,
  worth converting whenever 1.0 is next revised.)
- A ~6.0pt overfull `\hbox` appears once in every component log — it is the `\pageheader` banner
  (10.8pt on the cover), same as the model lesson. Not a defect.
- **A key can fail page parity by being too SHORT, not just too long** (1.2's notes: blank 4,
  key 3). The cause is `\termblanklong`, which reserves a fixed term line + two write lines in
  the blank while the matching `\vocabans` collapses to however long the definition is. Two
  fixes, in this order: (1) write the key's definitions out fully so each wraps to ~3 lines —
  a real improvement, not padding; (2) if that is not enough, find the box where the two
  documents first diverge and raise `\boxguard[n]` on it **in both files** so the box starts on
  the same page in each. For 1.2, `\boxguard[30]` on notes §1 realigned everything downstream
  and closed a whole page of drift.
- **A `work` block reads as a labeled gap, so give it a lead-in question.** Lesson 1.3 uses the
  pattern "Show the work for the \textbf{10th grade} row:" / "About how many members does that
  reach?" immediately before every `work` block. Without the lead-in the blank looks like an
  authoring mistake rather than a place to write.
- **Lesson 1.3 built clean on the first compile** — the only log noise was the known ~6.0pt
  `\pageheader` overfull `\hbox` in every component and the 10.8pt one on the cover. Neither is
  a defect. Guards used: `\boxguard[30]` on the notes' §1, §3, and §5 and on activity Tier R,
  `\boxguard[26]` on notes §4, `\boxguard[24]` on the homework scenario box, `\boxguard[12]` on
  the `hookbox`, bare `\boxguard` elsewhere — mirrored byte-for-byte into every `_key`.
- **`make check` cannot see the one failure mode that actually shipped in 1.4.** The gate passed
  on the first build with the activity at 3/3 pages — perfect parity — while Tier E was split
  across the break with *only its final table* on page 3, a ~1.5in stub under two-thirds of a
  blank page. Page parity and the stub are independent failures; the gate proves the first and
  says nothing about the second. **Render the packet and look at every page**, not just the
  page counts.
- **A wide fill-in table is the most expensive block you can put at the end of a tier**, and it
  is usually convertible. Lesson 1.4's Tier E closed on a 3-row × 3-column removes/costs table
  (~1.75in tall) that would not fit; rewriting it as three `(a)/(b)/(c)` lines each with one
  `\writeline` kept all three options, saved ~0.75in, and pulled the activity from 3 pages to 2.
  Prefer this to `\boxguard`-ing a tail block onto its own page, which buys a stub-free layout
  at the cost of two two-thirds-empty pages. Shave the cheap things first (inter-box `\vspace`,
  `arraystretch`, box padding, `itemsep`) — on 1.4 those together were worth only ~0.2in and did
  not close the gap on their own.
- **A key's table cells are usually taller than the blank's.** A `\blank{3.9cm}` cell is always
  one line; the `\ans{}` that replaces it often wraps to two or three. That asymmetry is
  already absorbed once the pair builds at equal page counts, so **re-measure both files after
  any table edit** rather than assuming a change that shortens the blank shortens the key.
- **The gate passed on 1.5's first build and the activity still had a stub** — the same
  failure 1.4 shipped, in the same component. Activity was 2/2 pages, parity perfect, while
  Tier A broke leaving only its closing rule and one write-line (~0.4in) at the top of page 2.
  The repair was ~35pt of *mirrored* shaving, not a guard: `itemsep` 4pt→2pt on Tier R and
  5pt→3pt on Tier A, box padding 1.5mm→1mm and 2mm→1.5mm, the three inter-box `\vspace`s
  0.06in→0.03in, and Tier R item 1's two blank-lines merged into one four-field line. Tier E's
  existing `\boxguard` is what made the shaving safe — over-shaving could only have pulled
  Tier E up, and the guard refuses that. **Shave the page above a stub before guarding the box
  below it.**
- **`\tcbbreak` is the right tool when a prompt gets separated from its table.** 1.5's
  homework broke inside the `notesbox` with item 6's question at the foot of page 1 and its
  four-row table at the head of page 2 — not a stub (both sides were full), just bad reading.
  `\boxguard` cannot fix it (inert inside a breakable tcolorbox); one `\tcbbreak` before the
  `\item`, mirrored byte-for-byte into the key, moved item 6 whole to page 2 with no page-count
  change. The blank and key had chosen the *same* break point, which is what made an
  unconditional break safe — check that first.
- **The lesson plan gets stubs too, and nothing checks it.** 1.5's plan left a 7-line tail of
  the Homework `teachernote` alone on page 6. `\boxguard[26]` before that one note moved the
  whole note down and kept the plan at 6 pages. Do not guard *every* teacher note — they total
  ~95 lines and guarding them all costs a seventh page; guard only the one that strands.
- **A wide beamer table overflows silently at 16pt.** 1.5's cycle-table slide reported one
  `Overfull \hbox (16.19pt)` logged at the *frame's* closing line, not the table's, so the line
  number points nowhere useful. The offending row was ~77 characters at `\small`; ~70 fits.
  Trim the longest row and the label ("Analyze \& communicate" → "Analyze \& report") rather
  than shrinking the font.
- **Do not trust a cached absolute path across a run.** The project directory was renamed
  mid-session and eight `Write` calls silently recreated the old path as an empty shell instead
  of failing. Nothing was lost, but the files had to be relocated by hand. If a `make` target
  that worked earlier suddenly reports "No rule to make target," check `ls` on the project root
  before assuming the Makefile is at fault.
