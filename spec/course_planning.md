# Course Planning Log — Statistical Analysis & Algebraic Reasoning

**Last updated:** 2026-08-31 — **EFFL SCRAPPED. THE COURSE IS BACK ON GRADUAL RELEASE**
(warm-up / guided notes and practice / tiered group activity / teacher-led debrief / close and
assign). The students rejected the experience-first model, so the two-day-old EFFL trial is over.
This run: **Lessons 1.0 and 1.1 converted to the gradual-release shape** and **the
`lesson-planning` skill rewritten** to match (SKILL.md, all four references, the scaffolder's
defaults, and the worksheet skeleton). Lesson 1.0's `experience/` was unfolded into `notes/` +
`activity/`; Lesson 1.1, which was still in the original pre-EFFL shape, lost its `exit_ticket/`
and had its notes trimmed to fit the 20-minute block. Both build, both pass `make check`, and
both were eyeballed page by page. **Lessons 1.0 and 1.1 are the models now — mirror them.**

**The agreed period shape (user-confirmed 2026-08-31):**
**5 warm-up · 20 guided notes & practice · 18 group activity · 7 debrief · 5 close & assign.**
The **debrief is a phase, not a component** — lesson plan and deck only. **There is no exit
ticket.** **Homework is authored for every lesson and is scored**; DeltaMath's statistics
coverage is thin, so the packet is the default and DeltaMath is the teacher's per-lesson
override, named aloud at Close & Assign.

Previous runs — 2026-08-30: Lesson 1.0 regenerated in the EFFL shape, and units 2–8
re-scaffolded into it (57 lesson dirs). 2026-08-29: EFFL ported (build system + skill +
skeletons). 2026-08-07: Unit 1's assessment set and unit cover pair authored, built, and
hand-verified. Earlier: Lesson 1.8 (2026-08-07), Lessons 1.1–1.7 (2026-08-06), Lesson 1.0 + the
royal → **cerulean** palette replacement (2026-08-05).

> **PROJECT DIRECTORY RENAMED 2026-08-06:** `~/Mathematics/stats_analysis_algebraic_reasoning`
> → `~/Mathematics/saar`. Worktrees created after the rename are fine; a worktree opened
> *before* it still has a `.git` file pointing at the old path and needs
> **`git worktree repair`** run from `~/Mathematics/saar` first. Always start a run from the
> new path.

## Current state

### GRADUAL RELEASE — RESTORED 2026-08-31 (the current design)

The EFFL trial (2026-08-29 → 2026-08-31) is over. The course runs **gradual release**:
*I do, we do, you do together.*

**Components.** A lesson is `cover` + `warmup` + `notes` + `activity` + `homework` + `slides`,
each with a `_key` where keyed. `shared/lesson.mk`'s `STUDENT_ORDER` is
`cover warmup experience notes activity exit_ticket homework` and was **not touched** — it
already merges the gradual-release set in the right order, and it still merges the retired
`experience`/`exit_ticket` dirs so any lesson still carrying them keeps building.

**Phases.** 5 warm-up / 20 guided notes & practice / 18 group activity / 7 debrief /
5 close & assign, over the 55-minute period. Every lesson plan carries a *Lesson at a Glance*
`fixedskillbox` with that table, placed after the Vocabulary box.

**The debrief is not a component.** It is a teacher-led phase in the plan's Debrief box and one
deck frame: run the displayed group work in order while students correct their own in a second
color, then a **whole-class cold check** and a three-pile formative read that decides how the
next lesson opens. It replaces the exit ticket entirely.

**Lesson-plan box order.** Primary Objective → Priority Ideas & Skills → Vocabulary → **Lesson at
a Glance** → Activate Prior Knowledge & Spiral Review → Hook → **Lesson — Guided Notes (20 min)**
→ Explicit Instruction → Active Monitoring → **Group Work & Differentiation (18 min)** →
**Debrief (7 min)** → Reinforcement & Extension → four teacher notes (`[Warm-Up]`,
`[Guided Notes]`, `[Group Activity]`, `[Homework]`).

**No spoiler rule.** The vocabulary is taught, so the cover, warm-up, notes, and slides all name
it outright. That rule died with EFFL, along with the 12pt `experience/` component and its
`\answerspace{H}{}` macro — **every component is 10pt and uses `\writeline`/`\blank{}` again.**

**Tiered group work is back.** Tier R / Tier A / Tier E over **one shared data set**, tiers
assigned rather than chosen, in a **fresh context** the notes did not already work.

#### The skill was rewritten this run

`.claude/skills/lesson-planning/` now describes gradual release, not EFFL:
- `SKILL.md` — frontmatter description, the model paragraph, "what a lesson is", the workflow
  steps, the Retrofit section (now *converting to* gradual release, with separate recipes for an
  EFFL lesson and a pre-EFFL one), and the guardrails.
- `references/components.md` — the `Experience & Formalize` spec is replaced by full
  **Guided notes** and **Group activity** specs; cover is four rows; the deck flow is
  gradual-release; a **Dead shapes** section documents `experience/` and `exit_ticket/`.
- `references/conventions.md` — 10pt everywhere, `\answerspace` retired, plan order rewritten,
  four teacher notes, plus a new **"Page-for-page alignment"** subsection (see the gotcha below).
- `references/build.md`, `references/course-workflow.md` — component order and content mapping.
- `scripts/new_lesson.py` — `DEFAULT_COMPONENTS` is now
  `cover,warmup,notes,activity,homework,slides`; `experience`/`exit_ticket` remain scaffoldable
  by name for patching. Smoke-tested end to end: scaffold → `make all` → `make check`, all green.
- `assets/skeletons/worksheet.tex` — TODO comment now covers notes / activity / homework.

#### Units 2–8 are scaffolded in the WRONG shape

The 2026-08-30 run re-scaffolded 57 lesson dirs across units 2–8 with `cover / warmup /
experience / homework / slides`. **They are all empty skeletons** — no authored content — so the
fix is mechanical: for each lesson, scaffold `notes,activity` and delete `experience`/
`experience_key`. Nothing is lost. Do it as part of authoring each unit, not as a bulk sweep.

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
- **Lesson 1.0 — "Unit Launch: Study Design" — is COMPLETE and is a GRADUAL-RELEASE MODEL
  LESSON** (converted 2026-08-31 from the one-day-old EFFL shape). **Mirror this lesson.**
  - Standards: **PS.DC.1a–c; AFDA.DA.2a** (previews PS.DC.1d–e, PS.DC.2, PS.DC.3).
  - Scope: data-in-context (who/what/units), individuals vs. variables, **categorical vs.
    quantitative**, and the **digit test** for numbers that are really labels (jersey #, ZIP,
    grade level), plus statistical questions.
  - Contexts: Riverbend Athletics roster + the sports-blog jersey claim (**guided notes**),
    Riverbend HS Student Life Survey (**practice box**), the Riverbend cross-country meet card
    + a recap-blog bib-number claim (**group activity**, a deliberately fresh context),
    Northgate Recreation Center (homework). All arithmetic verified: points mean $72/6=12$,
    jersey mean $84/6=14$, height mean $420/6=70$, captains $3/6=50\%$, commute mean
    $108/6=18$, grade mean $63/6=10.5$; meet card — bib mean $115/5=23$, finish mean
    $120/5=24$, medaled $2/5=40\%$.
  - Notes sections: 1. Data are numbers with a context · 2. Individuals and variables ·
    3. Two types of variables · 4. **The digit test** (the crux) · 5. Statistical questions ·
    Guided Practice. Budget 3/3/5/5/3 + 2 = 20 min.
  - **The crux is earned, not announced:** section 3 classifies Jersey \# *last*, takes a hand
    vote, records the split, and **does not settle it**; section 4 settles it by producing a
    correct mean that describes nobody. Settling it early collapses the lesson into a
    definition to copy.
  - Components: `cover`, `warmup`(+key), `notes`(+key), `activity`(+key), `homework`(+key),
    `slides`. `experience/` and `experience_key/` are deleted.
  - Page counts: warmup 1/1, **notes 4/4**, **activity 2/2**, homework 2/2; plan 6pp, deck 13
    frames, student and key packets 12pp each.
  - `make -C unit01/lesson00 all` exits 0; `make -C unit01/lesson00 check` **passes**; every
    page eyeballed — no stranded boxes, and blank/key aligned heading-for-heading.
- **Lesson 1.1 — "The Statistical Cycle and Types of Data" — is COMPLETE and is the second
  GRADUAL-RELEASE MODEL LESSON** (converted 2026-08-31). It was never EFFL — it kept the
  original pre-EFFL shape — so the conversion was: delete `exit_ticket/` + `exit_ticket_key/`,
  add the *Lesson at a Glance* phase table, replace the plan's *Individual Work & Assessment*
  box with a **Debrief (7 min)** box that folds the exit ticket's stage-2/stage-4 item in as a
  whole-class cold check, add an activity-launch frame and a debrief frame to the deck, and
  **trim the notes to fit the 20-minute block**.
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
  - **Notes trimmed to fit 20 minutes** (they were paced at ~40 in the old teacher note):
    section 6's four broken-study scenarios were cut — they duplicated activity Tier A item 3,
    where groups now have to argue them instead of copying them — and the practice box's
    scale-to-900 part (c) was cut as redundant with section 5. New pacing: 6/5/6/1 + 2 = 20 min.
  - Page counts: warmup 1/1, **notes 3/3**, activity 2/2, homework 2/2; plan 6pp, deck 11
    frames, student and key packets 12pp each. `make -C unit01/lesson01 all` and `check` both
    exit 0; pages eyeballed.
  - The deck's "cycle turns" frame was **de-spoilered** — it used to list the four broken
    studies that are now activity Tier A item 3, which would have handed groups the answers.
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
- **Lesson 1.6 — "Principles of Experimental Design" — is COMPLETE.** All components authored,
  built, and passing the gate.
  - Standards: **PS.DC.3a (i–iv), PS.DC.3b; AFDA.DA.2c** (PS.DC.1b carried forward in the
    conclusion items).
  - Scope: the same one-word pivot as 1.5, from the other side — the researcher
    **assigns** and **imposes a treatment**; naming **experimental units / subjects**,
    **treatment**, and **control group** (the baseline, not a wasted group); the four
    principles **comparison, randomization, replication, control** evaluated *in context*
    (PS.DC.3b), with **confounding variable** taught as 1.5's lurking variable that got
    *inside* the experiment because the groups were not treated alike; the **placebo
    effect** in a school setting (*being chosen* is itself a treatment) and single- vs.
    **double-blind**; and **completely randomized / randomized block / matched pairs**,
    with block allocation done as arithmetic. Closes on the payoff the unit has been
    building since 1.5 — random assignment is what buys the verb *caused*.
  - **The lesson is 1.5's answer, deliberately on the same contexts.** Riverbend's
    observational study made the Study Center look *harmful* ($65\%$ users vs. $80\%$
    non-users, arrow reversed); the experiment makes it look *helpful* ($75\%$ vs. $55\%$).
    Same school, same Study Center, opposite conclusions — that pair is the hook, and every
    other component repeats the shape: a self-selected gap that was too big, replaced by an
    assigned gap that is smaller and true. Harbor Point $25 \to 20$ points; Millbrook
    $48 \to 30$ points. **A smaller gap as the stronger evidence** is the closing item of
    both the activity and the homework.
  - Contexts: Riverbend HS carried from 1.0–1.5 (warm-up + notes; $120$ volunteers split
    $60/60$ by generator, $45/60 = 75\%$ against $33/60 = 55\%$, gap $20$ points, pooled
    $78/120 = 65\%$; block on last quarter's grades $80 \to 40/40$ and $40 \to 20/20$),
    Cedar Ridge Apartments carried from 1.3/1.4 (guided practice; $100$ households,
    $50/50$, four altered plans mapping one-to-one onto the four principles), Harbor Point
    Community Pool carried from 1.2–1.5 (activity; $90$ volunteers, $45/45$, $27/45 = 60\%$
    against $18/45 = 40\%$, pooled $45/90 = 50\%$ scaled to $750$ of $1{,}500$; block on
    retirement $30 \to 15/15$, $60 \to 30/30$; the double-blind item is the honest limit —
    subjects cannot be blinded, the sleep-log scorers can), Bayside Middle School carried
    from 1.3–1.5 (exit ticket; $80$ volunteers, $40/40$, $28/40 = 70\%$ against
    $16/40 = 40\%$, gap $30$), Millbrook Public Library carried from 1.2/1.4/1.5 (homework;
    $200$ volunteers, $100/100$, $65\%$ against $35\%$, pooled $100/200 = 50\%$ scaled to
    $600$ of $1{,}200$; block on age $120 \to 60/60$, $80 \to 40/40$). All arithmetic
    verified in Python before authoring.
  - Page counts: warmup 1/1, notes 4/4, activity 2/2, exit ticket 1/1, homework 2/2;
    plan 6pp, slides 10 frames. `make -C unit01/lesson06 all` and `check` both exit 0;
    every page of both packets was rendered and eyeballed (see "Gotchas" for the two
    layout repairs that took).
- **Lesson 1.7 — "Comparing Studies and Choosing a Method" — is COMPLETE.** All components
  authored, built, and passing the gate.
  - Standards: **PS.DC.3c, PS.DC.3d, PS.DC.3e** (PS.DC.1b carried forward in the conclusion
    items).
  - Scope: the two study types **side by side** in one four-row table whose first row
    (*who decides which group each individual is in*) produces every other row, and the
    sentence each design earns (*is associated with* vs.\ *caused*); **when you cannot run
    an experiment** --- **unethical / impossible / impractical**, with the test question
    *can you hand this out to a person?*, and the rule that an unavailable experiment is a
    reason for a **weaker verb**, not an excuse for a stronger one; **PS.DC.3d** --- the
    statistical cycle used to plan a *well-designed experiment*, authored as the same table
    shape as 1.5's so only the **Collect** row changes (from *sampled* to *assigned*); and
    **PS.DC.3e** --- the five collection methods (survey, interview, focus group,
    observation, content analysis) as a pre-filled reference table plus five diagnostic
    rows. The lesson's named trap is **observation the method vs.\ observational study the
    design** --- an experiment can collect its data by observation. The four principles are
    assumed, not re-taught.
  - **Built on the 1.5/1.6 pairs rather than new scenarios**, as planned: every context has
    already been run both ways, so the comparison is between studies students themselves
    computed. Riverbend $65/80$ watched vs.\ $75/55$ assigned; Harbor Point $25$-point gap
    vs.\ $20$; Millbrook $48$ vs.\ $30$.
  - Contexts: Riverbend HS carried from 1.0--1.6 (warm-up + notes; $39/60 = 65\%$ and
    $72/90 = 80\%$, a $15$-point gap, against the assigned $75\%$/$55\%$ and $20$ points ---
    the warm-up's real item is *why one study's groups are $60/90$ and the other's $60/60$*;
    notes §3 plans a new weekly-check-in experiment through the cycle), Cedar Ridge
    Apartments carried from 1.3/1.4/1.6 (guided practice; three questions --- one
    assignable, two not --- each matched to a study type **and** a collection method),
    Harbor Point Community Pool carried from 1.2--1.6 (activity; the two earlier studies
    labelled, then a new water-aerobics experiment, $120$ volunteers $60/60$,
    $42/60 = 70\%$ against $30/60 = 50\%$, gap $20$, pooled $72/120 = 60\%$ scaled to $900$
    of $1{,}500$; Tier E is the arthritis question, which cannot be assigned), Bayside
    Middle School carried from 1.3--1.6 (exit ticket; $90/150 = 60\%$, Study A/Study B
    sorting, the long-bus-ride question, and a method choice), Millbrook Public Library
    carried from 1.2/1.4/1.5/1.6 (homework; a **third** study --- $300$ volunteers
    $150/150$, $96/150 = 64\%$ against $60/150 = 40\%$, gap $24$, pooled $156/300 = 52\%$
    scaled to $624$ of $1{,}200$ --- plus the cycle table, three assignability rows, all
    five methods, and the closer: the $48$-point gap is the biggest number and the weakest
    evidence). All arithmetic verified in Python before authoring.
  - Page counts: warmup 1/1, notes 4/4, activity 2/2, exit ticket 1/1, homework 2/2;
    plan 6pp, slides 10 frames. `make -C unit01/lesson07 all` and `check` both exit 0;
    every page of both packets and the plan was rendered and eyeballed (see "Gotchas" for
    the three repairs that took).
- **Lesson 1.8 — "Project: Design and Conduct a Survey" — is COMPLETE**, and with it
  **Unit 1 is finished**. All components authored, built, and passing the gate.
  - Standards: **AFDA.DA.2d, 2h, 2i, 2j; PS.DC.2d** (AFDA.DA.2a–c and 2e–g exercised
    throughout the planning rather than taught fresh).
  - Scope: the unit **run forwards** — students build a study instead of taking one apart. The
    four-stage cycle as a *deliverables checklist* (third column: what you hand in); the three
    tests for a statistical question and 1.3's stratified allocation, both reused unchanged;
    **the survey instrument**, which is the lesson's only genuinely new content — four rules
    (one idea per item, neutral wording, choices that cover everyone without overlapping,
    short) taught by repairing three broken items that students met in 1.4 as response bias;
    **relative frequency** and a **bar graph** completed on pre-drawn, pre-scaled axes
    (AFDA.DA.2h — no sketching from a blank page); scaling a sample percent to a population;
    and the **four-sentence report** whose fourth sentence is what the project is graded on.
  - **The lesson's pivot is that the class is a convenience sample.** The Student Council's
    stratified $60$ may speak about all $900$ students; the class of $25$ may not. The two
    results are deliberately built to *nearly agree* ($35\%$ vs. $36\%$ on the top choice) so
    that activity Tier E can make the hardest point in the unit: near-agreement is luck, not
    evidence, because chance never chose this class. Naming the limit is scored as part of the
    answer, not as an apology.
  - **Packet budgeted as a project**, per the plan left by 1.7: the activity is a planning page
    (Tier R), an instrument the class actually builds plus a live tally (Tier A), and a
    reporting/validity page (Tier E). The homework's `extensionbox` is **the project
    deliverable** — the four-sentence report on the class's own data.
  - **The activity key is a worked exemplar, not the only right answer** (flagged in its
    teacher note): a class of $25$ answering the grant question $9$/$7$/$6$/$3$ →
    $36\%$/$28\%$/$24\%$/$12\%$, scaling to $324$. Real class data will differ; mark against
    the class's own totals. The `work` blocks carry the shape of the computation.
  - Contexts: Riverbend HS carried from 1.0–1.7 (warm-up + notes + activity; Student Council
    \$$3{,}000$ grant, stratified $60$ from $900$ at $1/15$ → $18$/$16$/$14$/$12$; counts
    $21$/$18$/$15$/$6$ → $35\%$/$30\%$/$25\%$/$10\%$, scaled $315$/$270$/$225$/$90$), Bayside
    Middle School carried from 1.3–1.7 (exit ticket; homeroom of $30$, $12$/$9$/$6$/$3$ →
    $40$/$30$/$20$/$10$, the trap being $0.40 \times 750 = 300$ computed correctly off a
    convenience sample), Millbrook Public Library carried from 1.2/1.4/1.5/1.6/1.7 (homework;
    a proper SRS of $80$ → $28$/$24$/$20$/$8$ = $35$/$30$/$25$/$10$, scaled $420$ and $300$,
    against a front-desk clipboard where $30$ of $50$ = $60\%$ chose story hour — a $35$-point
    gap worth about $420$ card holders, the same size as the entire top result; plus a $40\%$
    response rate). All arithmetic verified in Python before authoring.
  - Page counts: warmup 1/1, notes 4/4, activity 2/2, exit ticket 1/1, homework 2/2;
    plan 6pp, slides 10 frames; student and key packets both 14pp.
    `make -C unit01/lesson08 all` and `check` both exit 0; `make -C unit01 check` passes all
    **9 lessons**. Every page of both packets and the plan was rendered and eyeballed (see
    "Gotchas" for the four repairs that took).
- **All other 57 lesson dirs are unmodified skeletons** (now cerulean). **U2–U8 unit tests and
  test keys are still skeletons**, and none of them has a `unit_cover` pair.
- Per-unit progress: **U1: 9 of 9 lessons + full assessment set + cover pair — COMPLETE**;
  U2–U8 scaffolded, 0 authored.

### Unit 1 assessments and cover pair — COMPLETE (2026-08-07)

**Blueprint, both forms** (parallel: same structure, different numbers, reshuffled vocab
letters). $100$ points, $33$ items, **6 pages blank and 6 pages keyed** on both forms:

| Part | Items | Pts | Content |
|---|---|---|---|
| A — Vocabulary, two matching sets of $7$ | 14 | 14 | Set 1 samples/bias, Set 2 studies/experiments |
| B — Multiple choice | 8 | 16 | one concept check per lesson, 1.1 → 1.7 |
| C — Short answer \& computation | 8 | 40 | **one computational item per lesson**, 1.1–1.8 |
| D — Extended response | 3 | 30 | the 1.5/1.6 study pair, a bias diagnosis, a design-and-critique |

**Part C spine — practice form** (all reused from the unit's already hand-verified numbers):
23 Bayside data types; 24 Harbor Point $27/75 = 36\%$, $0.36 \times 1500 = 540$;
25 Riverbend stratified $\frac{1}{15}$, $18$/$16$/$14$/$12$; 26 Cedar Ridge $k = 10$, start
$4 \to 4, 14, 24, 34$; 27 Millbrook $72/90 = 80\%$ → $960$ against $54/120 = 45\%$ → $540$;
28 Riverbend observational $65\%$/$80\%$, pooled $111/150 = 74\%$ → $666$; 29 Riverbend
experiment $75\%$/$55\%$, blocks $40$/$40$ and $20$/$20$; 30 Student Council
$35$/$30$/$25$/$10\%$ → $315$. Part D: 31 the Riverbend pair; 32 Cedar Ridge mail survey
($25\%$ response, $96/150 = 64\%$ → $384$ against the true $240/600 = 40\%$; the re-run
$192/300 = 64\%$); 33 Bayside design + the homeroom convenience-sample trap.

**Part C spine — actual form** (new numbers, verified in Python before authoring):
23 Oakmont ($600$) data types; 24 Northgate $28/80 = 35\%$, $0.35 \times 1200 = 420$;
25 Westfield stratified $\frac{1}{16}$, $16$/$14$/$11$/$9$ from $256$/$224$/$176$/$144$;
26 Pinehurst $k = 20$, start $6 \to 6, 26, 46, 66$; 27 Lakeside $96/120 = 80\%$ → $640$
against $45/150 = 30\%$ → $240$; 28 Oakmont observational $55\%$/$70\%$, pooled
$128/200 = 64\%$ → $384$; 29 Oakmont experiment $70\%$/$40\%$, blocks $30$/$30$ and
$20$/$20$; 30 Westfield $40$/$30$/$20$/$10\%$ → $320$. Part D: 31 the Oakmont pair;
32 Pinehurst mail survey ($25\%$ response, $128/200 = 64\%$ → $512$ against the true
$320/800 = 40\%$; the re-run $256/400 = 64\%$); 33 Lakeside design + the vendor's own
customers.

**Answer letters** (also on p2 of `unit_cover_key`): practice Set 1 `C F A B G D E`,
Set 2 `E A C G B F D`, MC `B C A B D C A B`; actual Set 1 `A F B C G D E`,
Set 2 `C E F A D G B`, MC `C A D B C A D B`.

**Cover pair.** `unit01/unit_cover/body.tex` is the sheet; both wrappers `\input` it, so
page 1 cannot drift. Page 1: full-bleed banner + standards line, name row, `objectivebox`
overview, `tocbox` listing all nine lessons with their standard codes plus a practice-test
row, `spiralbox` with the unit's four big ideas, `remindbox` explaining the practice test.
`unit_cover_key/main.tex` adds **page 2**, the exam scoring notes for *both* forms in three
`teachernote` blocks (answer letters + MC rationale; Part C point split and both forms'
answers; the Part D rubric and two errors to watch). Merged page counts confirm the design:
**student packet $133$pp, key packet $134$pp** — the one-page difference is exactly the
teacher scoring page, which is what should never reach a student.

**Verification done by hand** (unit tests are outside `make check`, which walks lesson dirs
only): both forms compile clean; every blank/key pair is **6/6 pages**; page starts align
1–5 on both pairs; no `teachernote` in any test key; no `\ans` inside math, checked by
importing `strip_comments`/`math_spans` from `shared/lesson_check.py` rather than a hand
regex (a naive `\$[^$]*\\ans` reports ~35 false positives on these files). Every page of all
six documents was rendered and eyeballed for stubs and orphan underlines — none.
`make -C unit01 check` still passes all **9 lessons**.
- Key design decisions (user-confirmed 2026-08-05): AFDA.AF.3 excluded; no trig; polynomial/log
  from A2.F.1/A2.F.2; counting = two lessons (3.7, 3.8); projects close U1, U5, U6, U7 + U8
  capstone; every unit gets a `lesson00/` launch outside the 8-content-lesson cap.

## Next steps

0. ~~Convert 1.0 and 1.1 to gradual release~~ and ~~rewrite the skill~~ — **DONE 2026-08-31.**
   **Lessons 1.0 and 1.1 are the models.** Open both before authoring or converting anything;
   `references/components.md` is the spec, but those two are the live reference for voice, page
   budget, and the per-section minute budgeting that keeps the notes inside 20 minutes.
1. **Convert the rest of Unit 1 — lessons 1.2 through 1.8 — one at a time.** They are all in
   the original pre-EFFL shape (`notes` / `activity` / `exit_ticket`), so each is the *cheap*
   conversion: follow the "Converting a pre-EFFL lesson" recipe in the skill's Retrofit section.
   Per lesson: delete `exit_ticket/` + `exit_ticket_key/` and their `.stamps`/`target` dirs, drop
   the Exit Ticket cover row and teacher note, swap *Individual Work & Assessment* for a
   **Debrief (7 min)** box folding the exit ticket's conceptual item in as a cold check, add the
   *Lesson at a Glance* table, add activity-launch + debrief frames to the deck and put the
   packet-or-DeltaMath line on its closing frame, **re-time the notes to 20 minutes — trimming
   if they do not fit**, and **collapse the three tiers into one whole-class activity** of ~6–7
   items in two guarded parts plus an `extensionbox` (cut, do not concatenate — see the sizing
   trap above). 1.2–1.8 all still carry Tier R / Tier A / Tier E boxes. Every one of 1.2–1.8 was written against a longer notes block,
   so expect to cut. Do them individually; a bulk pass would re-flow every verified lesson at once.
2. **Fix the Unit 2–8 skeletons as you author each unit** (see "Units 2–8 are scaffolded in the
   WRONG shape"): scaffold `notes,activity` and delete `experience`/`experience_key`. They are
   empty, so nothing is lost.
3. **Unit 2** — "Describing One Variable" (PS.DS.1–3), seven content lessons plus `lesson00`.
   Nothing in U2–U8 is authored. Confirm the U2 lesson map with the user before authoring; the
   scaffolded titles in `unit02/lesson*/main.tex` are the proposal. Note the hand-off already
   written into 1.8's homework teacher note: Unit 2 is where the variable becomes a number and
   the bars start touching.
4. **Reuse the Unit 1 assessment set as the template for U2–U8.** The blueprint
   ($14$/$16$/$40$/$30$, $33$ items, 6 pages) and the `unit_cover` + `unit_cover_key` pair
   (shared `body.tex`, scoring notes on the key's page 2) are the pattern; only the contexts and
   numbers change. `\setlength{\workrowsep}{5pt}` in every test preamble is what gives `work`
   blocks handwriting room without pushing the form to 7 pages — keep it identical in the blank
   and the key. **The tests were untouched by both redesigns** — they have no pedagogy in them.
5. **A course-wide final (`finals/`) is still not scaffolded.** Wait until more units exist so
   the exam can actually be cumulative.
6. **Two spec docs to keep in sync.** `spec/unit_lesson_breakdown.md` is updated through 1.8 and
   Unit 1's assessments, but **still describes the EFFL component set** — fix it on the next run
   that touches it. It is the doc most likely to go stale.
7. Merged to `main` so far: lesson-1.0 + palette as PR #3; 1.1 as PR #4; 1.2 as PR #5; 1.3 as
   PR #6; 1.4 as PR #7; 1.5 as PR #8; 1.6 as PR #9; the breakdown doc as PR #10; 1.7 as PR #11;
   1.8 as PR #12; the EFFL port as PR #15; the 1.0 EFFL regen as PR #16. **The Unit 1 assessment
   set and cover pair are authored, built, and verified but still not committed.** Note
   `unit01/sample_test/main.pdf` and `unit01/sample_test_key/main.pdf` are untracked drop-ins and
   belong in that commit, since `unit.mk` reads them from the source tree with no compile step.

## Gotchas found this session

### Blank/key page alignment is NOT what `make check` verifies (found 2026-08-31)

The gate compares a component with its key by **total page count only**. Two files can both be
4 pages and still break in different places, so the teacher's page 3 is not the student's page 3.

**Cause.** In the guided notes' `vocabbox`, the blank's `\termblanklong{Term}` reserves two ruled
lines per term while the key's `\vocabans{Term}{definition}` prints a wrapped definition that is
usually shorter. The key's page 1 gains an inch or two, the first `notesbox` floats up onto it,
and every section after it sits one page early. **Lesson 1.1 shipped this way** — it was not
introduced by this run's edits.

**Fix.** `\boxguard[20]` before the first `notesbox` after the `vocabbox`, in the blank **and**
the key. Verify by comparing per-page headings, not page counts:

```
for p in 1 2 3 4; do
  diff <(pdftotext -f $p -l $p notes/main.pdf -     | grep -oE '^[0-9]+\. [A-Z].*') \
       <(pdftotext -f $p -l $p notes_key/main.pdf - | grep -oE '^[0-9]+\. [A-Z].*') \
    && echo "p$p ok"
done
```

**Known limit.** `\boxguard` is `\Needspace`, and `\Needspace` is **inert inside a breakable
`tcolorbox`** (it is documented as such in `saar-boxes.sty`). So drift *within* one long box —
a homework `notesbox` running six items across two pages — cannot be fixed this way. Both 1.0's
and 1.1's homework still drift by about half an item on page 2. Reflow the items or accept it;
do not fake it.

### A tall table closing the last box strands a page (found 2026-08-31)

Lesson 1.0's group activity ran to three pages because the final 5-row `tabularx` spilled one
inch onto page 3 — the exact stranded stub `boxguard` exists to prevent and `make check` cannot
see. Converting that table to three inline `\blank{}` lines brought the component to two pages.
**Prefer inline blanks over a tall table at the end of a box**, and always render the activity to
PNG and look at the last page.

### Splitting a long box is how you align blank and key (found 2026-08-31)

`\boxguard` is inert inside a breakable `tcolorbox`, so a component built as ONE long box has no
lever for controlling where it breaks — and the key breaks elsewhere than the blank whenever an
`\ans{}` wraps where a `\blank{}` did not. The fix is structural: **split the box in two at a
real phase change and guard the second half** (`\boxguard[30]`), continuing the item numbering
with `\begin{enumerate}[..., start=N]`. This is what got 1.0's and 1.1's activities and 1.0's
homework to align page-for-page.

Two things that do *not* work, both tried: shortening the wrapping `\ans{}` (the answer space
begins mid-prompt-line, since `\writeline` is `\hrulefill`, so there is almost no width to play
with), and `\par\writeline` / `\par\ansline` to force a full-width answer line (helps, but does
not close a one-line gap accumulated earlier in the box).

**Still open:** lesson 1.1's homework page 2 is off by one line between blank and key. The
item-boundary split that would fix it pushes the component to 3 pages, which is worse. Left as
is, deliberately.

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
- **`label: \blank \hfill label: \blank` silently drops the second blank.** Three-across
  (`units / treatment / control`) and even two-across with generous widths overflowed the
  enumerate's line in 1.6's activity and homework: TeX breaks at the `\hfill` (infinite
  stretch = zero badness), right-aligns the trailing label against the margin, and dumps its
  `\blank` onto the next line as an **orphan underline** — with *no* overfull-hbox warning,
  because the break was legal. The student is left with a label and nowhere to write. The
  **key never shows it** (an `\ans` is narrower than the blank it replaces), page parity
  still passes, and `make check` sees nothing. Budget ~14.5 cm of usable width inside a
  `notesbox` enumerate: two labels plus two `\blank{3.6cm}` fit; three do not. Put the third
  on its own line. **Look for stray underlines at the left margin** when scanning a blank.
- **Render the component PDFs, not the merged packet, right after an edit.** `make check`
  rebuilds the components but does not always re-merge `target/compiled/*_student.pdf`, so a
  packet render can be a build behind. Two "fixes that did not take" in 1.6 were both stale
  renders — one of them a `\tcbbreak` that had in fact worked. Verify against
  `target/unitXX/lessonYY/<comp>/main.pdf`, or run `make all` before rendering the packet.
- **`\tcbbreak` before an `\item` works exactly as in 1.5.** 1.6's homework had the same
  failure (item 6's prompt at the foot of page 1, its table at the head of page 2), and one
  `\tcbbreak` on its own line before the `\item`, mirrored byte-for-byte into the key, moved
  the whole item to page 2 with no page-count change. Blank and key had chosen the same break
  point, which is what made the unconditional break safe — check that first, as always.
- **A key that is one page long can be a `\boxguard` problem, not a content problem.** 1.7's
  notes came out blank 4 / key 5, and shortening the key's `\ans` cells did not move it. The
  real cause was `\boxguard[30]` on notes §3: the key's §2 is a few lines taller (bold `\ans`
  wraps wider than the rule it replaces), so §3 no longer cleared a $30$-line guard on page 3
  and jumped to page 4, dragging the guided-practice box onto page 5. Lowering that one guard
  to `\boxguard[22]` **in both files** closed the whole page of drift. **Compare where each
  page starts** (`pdftotext -f N -l N | head -3` per page, blank against key) before editing
  any content — if pages 1–k start identically and diverge at k+1, a guard is the suspect,
  not the prose.
- **Check whether the blank and the key break at the *same* place before reaching for
  `\tcbbreak`.** In 1.7 they did not: the homework blank orphaned item 5's prompt at the foot
  of its page while the key had already moved the whole item down, and the activity did the
  same in reverse. The unconditional break is still the right fix in that case — it is a
  no-op on the side that already breaks there and a repair on the side that does not — but
  verify both page counts afterwards, because it is only free when one side is already
  breaking at that point.
- **The lesson plan strands a teacher-note tail almost every lesson.** 1.5 needed
  `\boxguard[26]` on the Homework note; 1.7 needed `\boxguard[22]` on the **Exit Ticket**
  note, which had left a three-line tail alone at the top of page 6. Same rule as before:
  guard only the note that strands, never all of them.
- **Two `\ansline`s in a row flow together and wrap** — the second one starts on the same
  visual line as the first one's dotted trail, so a pair of ~80-character answers renders as
  three lines with a trail through the middle. This is house-standard (1.6 does it too) and
  does not break parity, since `\writelines{2}` reserves the height either way. It is only
  worth trimming if the wrapped answer reads badly.
- **Do not trust a cached absolute path across a run.** The project directory was renamed
  mid-session and eight `Write` calls silently recreated the old path as an empty shell instead
  of failing. Nothing was lost, but the files had to be relocated by hand. If a `make` target
  that worked earlier suddenly reports "No rule to make target," check `ls` on the project root
  before assuming the Makefile is at fault.

### Found authoring Lesson 1.8 (2026-08-07)

- **`perl -pi -e` silently ate text in a replacement containing `$3`/`$1`.** Rewriting a key's
  `\ansline` to `{$35\%$ chose the evening book club.}` produced `{\% the evening book club.}`
  because Perl read `$3` and `$1` in the *replacement* as capture-group backreferences. It
  compiled fine and the gate passed — only the rendered page showed it. **Never use `perl -pi`
  on LaTeX containing `$`**; use the editor, or the damage is invisible to every check.
- **A prompt followed inline by `\writeline` / `\ansline` drifts by a line.** The blank's rule
  fills whatever is left of the prompt's last line (1 line); the key's answer usually wraps to
  a second. Put the answer in **its own paragraph** — a blank line between the prompt and the
  `\writeline`/`\ansline` — and both sides reserve exactly one full line. This fixed the
  homework's 2/3 mismatch where shortening answers had not.
- **The 1.6 orphan-underline bug recurred**, this time as `question? \blank{7.6cm}` at the end
  of a long prompt: TeX broke at the space, stretched the question across the full measure, and
  dumped the rule alone at the left margin of the next line. The key never showed it (`\ans` is
  narrower) and the gate saw nothing. Same fix as above — own paragraph, `\writeline`.
- **`\tcbbreak` can strand the *opening* of a box, not just its tail.** The activity's Tier A
  was split after item 1, shipping a title plus three lines at the foot of page 1 with 3.5in of
  white below it. `\tcbbreak` is for keeping a prompt with its table *inside* a box that
  otherwise fits; when the box does not fit at all, drop the `\tcbbreak` and raise
  **`\boxguard[34]`** on the box so the whole thing moves. Page counts did not change.
- **A key can carry a figure's answer for free.** The notes' bar graph is authored as identical
  TikZ in both files; the key adds four `\fill[keyred, opacity=0.55]` bars *inside the existing
  bounding box*, so the figure's height is unchanged and parity is untouched. Use this rather
  than describing bar heights in prose.
- **The plan stranded a teacher-note head this time, not a tail** — the Warm-Up note's title
  plus three lines at the foot of page 4. `\boxguard[12]` on that one note moved it whole to
  page 5 and the plan stayed 6pp. That is **three lessons running** (1.5, 1.7, 1.8) where the
  plan needed exactly one guarded note; check the plan's page breaks every time, and guard only
  the note that strands.
- **Mirrored shaves are safe; asymmetric ones are not.** Getting the homework back to 2/2 took
  ~3 lines: figure `y=0.086cm`→`0.066cm`, table `arraystretch` 1.3→1.15, and `itemsep`
  8pt→6pt, all applied to **both** files, plus one shortened `\ansline` in the key alone. Shave
  the shared things first — they cannot open a new mismatch.

### Found authoring the Unit 1 assessments (2026-08-07)

- **`\workrowsep` is the one dial that tunes a test's page count**, and it is safe because it
  moves the blank and the key together. At `0pt` a `work` block gives a student almost no
  handwriting room; at `7pt` the practice form spilled to 7 pages with the last page two-thirds
  empty. **`5pt` was the value that bought real writing room and held 6 pages.** Sweep it
  (`3pt`/`4pt`/`5pt`) with a loop rather than guessing — the page count is a step function.
- **A naive `\$[^$]*\\ans` grep is useless on a test key** — it reported 35 hits on a file with
  zero real violations, because `[^$]*` walks straight across the gap between two separate
  `$…$` groups (`\ans{$18$} & \ans{$16$}`). Import `strip_comments` and `math_spans` from
  `shared/lesson_check.py` instead and test membership in the returned spans; that is the same
  code the gate runs, and it is right.
- **The lesson cover's banner geometry does not transfer to a unit cover.** Copying
  `rectangle ([yshift=-0.9in]…)` + `\vspace{-0.8in}` with a taller four-line title block
  clipped the first line off the top of the page. Crop the top of the rendered page
  (`pdftoppm -r 150 -x 0 -y 0 -W 1300 -H 220`) and measure: a 1.25in banner with
  `\vspace{-0.72in}` centres a four-line block. The clipping is silent — no overfull box, no
  error.
- **Balance the multiple-choice answer letters before writing the key.** The first draft of the
  practice form came out `B C A B B C B B` — five B's out of eight. Reordering two items' option
  lists fixed it to `B C A B D C A B` at zero cost to pagination, since reordering the same
  strings changes no line counts. Do this on the blank *before* mirroring into the key.
- **Unit tests are outside `make check`, so the page-parity check is yours to run.**
  `pdfinfo | grep Pages` on each blank/key pair, plus
  `pdftotext -f N -l N | head -1` per page on both to confirm the page starts align. A pair can
  legitimately diverge on the last page (a key's `\ansline` wraps where the blank's rule does
  not) and still be correct as long as the totals match.
- **The merged packets are the real proof the cover pair works.** Student $133$pp against key
  $134$pp is exactly right: one extra page, and it is the teacher scoring page. If those two
  numbers ever differ by more than one, something other than the cover is drifting.
