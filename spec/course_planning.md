# Course Planning Log — Statistical Analysis & Algebraic Reasoning

**Last updated:** 2026-09-14 — **ALL OF UNIT 1 CONVERTED TO THE MAIN IDEAS / NOTES TABLE
SHAPE** (`/lesson-planning regenerate unit 1 with the guided notes redesign`). The 2026-09-12
redesign that commit `bdee5ae` applied to lesson 1.2 is now applied to the other eight lessons:
**1.0, 1.1, 1.3, 1.4, 1.5, 1.6, 1.7 and 1.8**. Each was brought to `cover` + `warmup` + `notes` +
`homework` + `slides`, 12pt student components, one `guidednotes` table of four instruction rows
plus a Guided Practice row, 14–18 numbered problems two across, every display pre-drawn, and a
plan and deck voiced by **row and problem number**. Eight lessons were converted in parallel by
one subagent each; the coordinator verified everything below independently of their reports.

**Unit 1 is now uniform: nine lessons, one shape.** `activity/`, `activity_key/`, `exit_ticket/`
and `exit_ticket_key/` are gone from 1.0, 1.5, 1.6, 1.7 and 1.8 — **no `activity`, `experience`
or `exit_ticket` directory survives anywhere in unit 1.**

**Verified by the coordinator, not taken on report:**

- `make -C unit01/lessonNN all` **and** `check` exit 0 for **all nine** lessons, after
  `rm -rf .stamps/unit01 target/unit01` and a full rebuild.
- **Page-for-page parity holds everywhere**: warm-ups 1/1, homework 2/2, notes 4/4 except **1.7
  and 1.8 at 5/5**; every lesson's student and key packet match (10pp each, 12pp for 1.7/1.8).
- **All 24 keys regenerate byte-identically** from their blanks with `mkkey.py` — proof that
  none was hand-edited and none can have drifted.
- **Zero overfull `\vbox`** anywhere in the unit. The only `\hbox` over 15pt is the cover's
  16.24pt `\namedateperiod` line, **identical in the untouched reference lesson 1.2** — it comes
  from `shared/` and is pre-existing.
- No `\ans{}` inside math and no bare math command inside an `\ans{}` (checked by parser, not
  grep); no `teachernote` in any key; no `\namedateperiod` off a cover; no key loading
  `-boxes`; no three-across `probgrid`; no `\answerspace`, `\extensionbox`, `\termans`,
  `\termblanklong`, DeltaMath, or a foreign palette name anywhere in unit 1.
- Every plan carries *Lesson at a Glance* at **5 / 35 / 10 / 10** and exactly three teacher
  notes in packet order; no retired plan box survives.
- `shared/`, every Makefile, `LESSON_SHAPE.md`, the skeletons, `mkkey.py` and **lesson 1.2**
  were not touched by this run.

**TWO OPEN ITEMS FOR THE USER — both page-budget overruns, neither a defect:**

1. **1.7's notes are 5pp** against the profile's 3–4pp. Closing the ~18cm gap means deleting a
   standards-bearing row — PS.DC.3d's cycle row or half of PS.DC.3e's methods row. The content
   was kept and the overrun flagged.
2. **1.8's notes are 5pp** for a structural reason: it is the project lesson, and its Guided
   Practice row must carry a live instrument card *and* a tally table. 1.8 also runs **26
   `\blank{}`s** against the "handful per lesson" rule — every one is a table cell, the
   instrument the class writes, or the tally, and none is mid-sentence, which is exactly what
   the density rule permits; a project lesson is where students construct rather than classify.

**Either raise the budget for these two, or say which row to cut.** Until then the profile's
3–4pp line and the 5pp reality disagree for 2 of 9 lessons.

**The agreed period shape (user-confirmed 2026-08-31, second revision):**
**5 warm-up · 30 guided notes · 10 independent practice · 7 debrief · 3 close & assign.**

**What changed, and why it matters when authoring:**

- **No group activity, no group work at all.** There is no `activity/` component. The release is
  **individual**.
- **The release runs ONCE per lesson, not per section** (user-confirmed): the 4–6 numbered notes
  sections are the *I do* (teacher models throughout), **one designated "We Do" section** is the
  joint example, and the notes' **closing `practicebox` of 1–3 items** is the *you do*. Do not
  build per-section I-do/we-do/you-do mini-cycles.
- **The We Do runs the same task the practice box releases**, on different data — students hold a
  completed template before they work alone.
- **Independent practice is a phase with a page, not a component.** It is that closing practice
  box, 10 minutes, worked silently and alone. No directory of its own, and **no row of its own on
  the cover** — the cover packet table is now **three rows** (Warm-Up · Guided Notes · Homework).
- **Notes budget is now ≤6pp**, with per-section minutes summing to **30** through the We Do.
- **The debrief survives** as a phase; it now walks the independent practice work instead of
  group work. Still no exit ticket.
- **DESMOS replaces DELTAMATH** as the homework override. Homework is still authored for every
  lesson and still scored; the packet is still the default. The per-lesson question is now
  whether **Desmos** carries an activity adequate to that lesson's skills — its coverage of this
  course's standards is uneven (stronger on function modeling and regression, thinner on
  inference and study design), so it is checked per lesson and never assumed.
- **Three teacher notes**, not four: `[Warm-Up]`, `[Guided Notes]`, `[Homework]`.

**History.** EFFL trial 2026-08-29 → 2026-08-31, scrapped (students rejected it). Gradual release
restored 2026-08-31 with an 18-minute group activity; that activity dropped the same day.
Earlier — 2026-08-30: units 2–8 re-scaffolded into the EFFL shape (57 lesson dirs). 2026-08-07:
Unit 1's assessment set and unit cover pair authored and hand-verified. 2026-08-06: Lessons
1.1–1.7. 2026-08-05: Lesson 1.0 + the royal → **cerulean** palette replacement.

> **PROJECT DIRECTORY RENAMED 2026-08-06:** `~/Mathematics/stats_analysis_algebraic_reasoning`
> → `~/Mathematics/saar`. Worktrees created after the rename are fine; a worktree opened
> *before* it still has a `.git` file pointing at the old path and needs
> **`git worktree repair`** run from `~/Mathematics/saar` first. Always start a run from the
> new path.

## Current state

### THE CURRENT DESIGN — Main Ideas / Notes table (2026-09-12), gradual release (2026-09-06)

*I do → we do → you do*, on the AP Statistics model. **`unit01/lesson02` is the reference
implementation; mirror it.** `LESSON_SHAPE.md` section 1 is the spec.

**Components.** `cover` + `warmup` + `notes` (*Guided Notes & Practice*) + `homework` + `slides`,
each with a `_key` where keyed. `shared/lesson.mk`'s `STUDENT_ORDER` is unchanged and still merges
the retired `activity`/`experience`/`exit_ticket` dirs, so a lesson in another unit that still has
one keeps building — **but no unit-1 lesson has one any more.**

**Phases.** 5 / 35 / 10 / 10. The plan's *Lesson at a Glance* `fixedskillbox` carries that table.

**The notes (2026-09-12 — this replaced the sectioned notes):** `\pageheader` → `vocabbox` of
4–5 fixed-height `\vterm{}` rows (key: `\vtermans{}{}`), filled *as each term is named* →
`hookbox` — the claim, a circle-one vote, two lines of reason, **left unresolved** → **ONE
two-column `guidednotes` table**: four instruction rows then the **Guided Practice row**. Each
row is one idea — a `\mainidea[lead]{Label}` on the left; on the right one or two **complete
printed sentences**, **one large pre-drawn display** read or annotated with `\labelbox`, then
`\notesprompt` and a **two-across `probgrid`** of `\pcell` problems with 1.0–2.6cm of answer
space. Problems run 1..N continuously, **14–18 across the lesson, never three across**. The
**last instruction row carries the crux as problems** and re-takes the hook vote at a named
problem number. **No `objectivebox`, no `notesbox`, no `practicebox`, no `\newpage`.** A
`\blank{}` only where a word or number *is* the answer — a table to fill, a display to name —
and a `\wordbank{}` strip above each such cluster. 3–4pp (see the two 5pp exceptions above).

**The homework is the individual practice**: `remindbox` ("This is your graded homework"),
`scenariobox` (third context), ~6 items in a `notesbox` + `…, continued`, closing `spiralbox`.
Scored 2 per item; started in class in the last ten minutes; due at the start of the first class
after two study halls.

**Plan order:** Primary Objective (+ Standards, Lesson model) → Learning Targets & Key
Understandings → Vocabulary → Lesson at a Glance → Warm-Up (seeds / running it) → Hook →
Guided Notes & Practice (I do | we do, `multicols`) → Debrief, spoken (walk | cold check +
formative read) → Homework → Watch For → Close & Assign → three teacher notes (`[Warm-Up]`,
`[Guided Notes \& Practice]`, `[Homework]`). **Everything is voiced by ROW and PROBLEM NUMBER** —
"row 4, problems 12–15", "the crux is problem 13" — never by section or lettered part.

**Deck (14–16 frames):** title → targets → warm-up → hook (dark, unresolved) → I-do divider
(dark) → 2–3 frames per notes row, each labelled with its row and problem range (the crux frame
`\sectionlabel[redacc]{}`) → Guided Practice (live, un-answered) → debrief + cold check → You do:
start the homework → close (dark).

**Cover packet table is THREE rows** — Warm-Up · Guided Notes & Practice · Homework.

**Student components are 12pt** (cover, warm-up, notes, homework, keys); plan 10pt, deck 11pt.

**Keys are GENERATED, never hand-edited** — `templates/lesson/mkkey.py` plus a JSON spec of
answers in order (`blanks`, `lines`, `vocab`, `cells`, `spaces`, `labels`). Re-run it after every
edit to a blank. Proof the rule is holding: all 24 unit-1 keys regenerate byte-identically.

> The old 55-vs-60 mismatch is **closed** (2026-09-06): the phase table now allocates the whole
> 60-minute period, 5 / 35 / 10 / 10.

### Unit 1 is uniform — all nine lessons in the current shape (2026-09-14)

- **Lesson 1.2 is the reference implementation** (the pilot, 2026-09-06; converted to the table
  2026-09-12 in commit `bdee5ae`). **Mirror it.**
- **Lessons 1.0, 1.1, 1.3, 1.4, 1.5, 1.6, 1.7 and 1.8 are CURRENT** — all converted 2026-09-14.
  1.3 and 1.4 came from the pilot shape (notes, plan and deck only); 1.0 from the
  group-activity shape; 1.1 from the notes-only shape; 1.5–1.8 from the pre-EFFL legacy shape.
- **No `activity/`, `experience/` or `exit_ticket/` directory remains in unit 1.**
- **Units 2–8** (57 lesson dirs) are still empty EFFL skeletons.

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
- **Lesson 1.0 — "Unit Launch: Study Design" — is CURRENT** (regenerated 2026-09-14 in the
  Main Ideas / Notes table shape, from the retired group-activity shape).
  - Components: `cover`, `warmup`(+key), `notes`(+key), `homework`(+key), `slides`.
    `activity/` + `activity_key/` deleted; `experience/` was already gone.
  - Standards: **PS.DC.1a–c; AFDA.DA.2a** (previews PS.DC.1d–e, PS.DC.2, PS.DC.3).
  - Scope: data-in-context (who/what/units), individuals vs. variables, **categorical vs.
    quantitative**, and the **digit test** for numbers that are really labels (jersey #, ZIP,
    grade level), plus statistical questions.
  - **Hook (notes page 1 + dark slide + plan, unresolved):** a sports blog writes *"the
    Riverbend roster's mean jersey number is 14 --- a young, inexperienced team."* The
    arithmetic is correct. Circle yes / no / can't tell; the vote is re-taken at **problem 10**,
    where the digit test settles it.
  - **Notes rows (17 problems):** 1. Data in Context (1--2) · 2. Individual \& Variable (3--4) ·
    3. Two Types (5--9) · 4. **The Digit Test** (10--13, the crux row) · 5. Guided Practice ---
    *Student Life Survey* (14--17). The teacher works problems 1, 3, 6, 11; the class works the
    rest. **The trap is problem 9** (Jersey \#, classified last, voted, left open);
    **the crux is problem 10**; **13 is the counterweight** (Height, $420/6 = 70$ --- a mean that
    does describe somebody); **15 is the crux transferred** (Grade, $63/6 = 10.5$).
  - Where the retired activity went: the cross-country **meet-card bib claim** ($115/5 = 23$) is
    now the debrief's **cold check**; the **Student Life Survey** is the Guided Practice row.
  - Contexts: Riverbend Athletics roster + the sports-blog jersey claim (warm-up + notes),
    Riverbend HS Student Life Survey (Guided Practice), Northgate Recreation Center (homework;
    8 members). All arithmetic re-verified in Python this run: points $72/6=12$, jersey
    $84/6=14$, height $420/6=70$, captains $3/6=50\%$, grades $42/4=10.5$, ZIP mean
    $22{,}115.5$, commute $108/6=18$, GP grade $63/6=10.5$, bibs $115/5=23$; homework ---
    visits $48/8=6$, group class $5/8=62.5\%$, spiral $45/300=15\%$ scaled to $300$, and the
    crux Member ID mean $1{,}124/8=140.5$.
  - Homework: 6 items, 12 points --- 1 individuals \& variables; 2 classify four columns with
    reasons (**the contrast pair**: Member ID vs. Age); 3 mean visits as data; 4 a percent
    ($62.5\%$) and why it is one; 5 the spiral item; 6 **the crux head-on** (the mean Member
    ID). Two pages. Packet night.
  - Page counts (12pt): cover 1, warmup 1/1, **notes 4/4**, homework 2/2; plan 7pp, deck 13
    frames, student and key packets 10pp each. `make -C unit01/lesson00 all` and `check` both
    exit 0; per-page headings compared blank↔key on every component.
  - Keys generated with `templates/lesson/mkkey.py` from
    `templates/lesson/examples/lesson00_{warmup,notes,homework}_key.json`.
  - **Fitting lesson:** the first draft ran **5pp** with four TikZ displays whose labels
    collided. Rescaling all four to the 12.2cm notes column (real column positions; the jersey
    number line staggers the \#21/\#23 labels), trimming the hook lead-in to two lines and the
    Guided Practice intro, and shaving `\pcell` answer heights brought it to 4/4. Eight key
    answers then overflowed their fixed cells and were shortened in the JSON --- **a `\pcell`
    answer longer than its height overflows silently, so render the key and look.**
- **Lesson 1.1 — "The Statistical Cycle and Types of Data" — is CURRENT** (regenerated
  2026-09-14 in the Main Ideas / Notes table shape, from the retired notes-only shape).
  - Components: `cover`, `warmup`(+key), `notes`(+key), `homework`(+key), `slides`. No legacy
    dirs existed to delete. The `practicebox` and the `extensionbox` are gone.
  - Standards: **PS.DC.1a–c; AFDA.DA.2a** (previews PS.DC.1d–e).
  - Scope: the four stages and what each *hands to the next*; the three tests for a statistical
    question and repairing one that fails; **the question decides the data type** (the crux);
    frequency and relative frequency; the conclusion in context; and diagnosing **which stage a
    flawed study broke at**.
  - **Hook (notes page 1 + dark slide + plan, unresolved):** the Student Council's bike-rack
    claim --- 60 asked, 6 said bike, therefore *"10\% bike now, so a lot more would if there
    were racks."* **The arithmetic is right.** Circle yes / no / can't tell; re-voted at
    **problem 14**.
  - **Notes rows (19 problems):** 1. Data Cycle --- four stages in order (1--4) · 2. Three Tests
    --- stage 1 (5--8) · 3. Frequency Table --- stages 2 and 3 (9--11; problem 9 is the fill
    table and carries the lesson's one `\wordbank`) · 4. **The Question Decides** (12--15, the
    crux row) · 5. Guided Practice --- *The Cycle Turns* (16--19). The teacher works 1, 5,
    problem 9's bus row, and 12.
  - **The trap is problem 8** --- a question that already passes all three tests; a student who
    "repairs" it has learned to rewrite rather than to test. **The crux is problem 14** ---
    correct arithmetic ($6/60 = 10\%$, about 90 of 900) behind a claim the data cannot support,
    entered at **stage 1**. **Problem 15 is the counterweight** (the breakfast cart: correct
    $35\%$, but entered at **stage 2**), and **problem 19 is the crux transferred**.
  - Contexts: Riverbend Student Council bike-rack survey (warm-up + notes; 60 students --- bus
    27, car 15, walk 12, bike 6, scaled to 900), **the council's second survey (Guided
    Practice; "would you ride if there were racks?", 80 asked, 24 yes → $30\%$ → about 270 of
    900 --- the cycle visibly turns)**, Lakeside Farmers Market (homework; about 800 Saturday
    shoppers, 50 asked → drove 26, walked 12, biked 7, bus 5). All arithmetic re-verified in
    Python this run.
  - Homework: 6 items, 12 points --- 1 variable, type and reason; 2 the frequency table with
    relative frequencies (spiral to 1.0) in a `work` block; 3 scale to 800 and write the
    conclusion; 4 **the contrast pair** (the same 50 shoppers, two questions, two types, decided
    before collection); 5 four failures, one per stage; 6 **the crux head-on** (right numbers,
    a conclusion that does not follow, entered at stage 1). Two pages. Packet night.
  - Page counts (12pt): cover 1, warmup 1/1, **notes 4/4**, homework 2/2; plan 7pp, deck 15
    frames, student and key packets 10pp each. `make -C unit01/lesson01 all` and `check` both
    exit 0; per-page opening headings compared blank↔key on every component, and every page
    rendered and inspected.
  - Keys generated with `templates/lesson/mkkey.py` from
    `templates/lesson/examples/lesson01_{warmup,notes,homework}_key.json`.
- **Lesson 1.2 — "Populations, Samples, Parameters, and Statistics" — is COMPLETE and is THE
  PILOT (regenerated 2026-09-06 on the AP Statistics 1.4 model minus AP Practice). Mirror it.**
  - Components: `cover`, `warmup`(+key), `notes`(+key), `homework`(+key), `slides`. `activity/`,
    `activity_key/`, `exit_ticket/`, `exit_ticket_key/` deleted (`git rm`).
  - Standards: **PS.DC.1d, PS.DC.1e** (PS.DC.1b carried forward in the conclusion items).
  - Scope: population / sample / sample size / census; **parameter vs. statistic decided by *who
    the number describes*** (second trap, section 1's second half: 61% from district records of
    all 900 students is a parameter); the five constraints (time, cost, access, destruction,
    change); **sampling variability — the target misconception**, section 2's second half: three
    volunteers, three statistics, one parameter, nobody wrong; then the claims table (an estimate
    is not a count; residents were never the population). Notation line (μ, x̄, p, p̂) pre-printed
    once, exposure only.
    - **Hook (notes page 1 + slide + plan, unresolved):** Ana 52%, Ben 48%, Cleo 58% — *who made the
    mistake?* Circle one in the hook box and write why; re-vote in section 2's second half.
  - Contexts: Lakeside Farmers Market (warm-up + notes; 800 shoppers, 50 asked, 26 drove → 52%,
    0.52 × 800 = 416; Ana/Ben/Cleo 26/24/29 of 50 → 52/48/58%), **Riverbend HS job survey
    (Guided Practice; 900 students, 50 asked, 20 → 40%, 0.40 × 900 = 360; a second 50, 23 → 46%)**,
    Harbor Point Community Pool (homework; 1,500 members, 75 asked → 27/21/18/9 = 36/28/24/12%,
    0.36 × 1500 = 540; front-desk records 62% of all 1,500 = the parameter row of the contrast
    pair; second sample 30/75 = 40%). All arithmetic verified in Python before authoring.
  - Homework: 6 items, 12 points — groups; frequency table (spiral to 1.1); scale-up as an
    estimate; label four numbers (rows ii/iv the contrast pair); four constraints; the second
    sample (crux head-on). Two pages max (user decision 2026-09-06); the board's over-claim
    moved to Guided Practice (e). Packet night (Desmos carries only the
    percent arithmetic).
  - Page counts (12pt): warmup 1/1, **notes 4/4** (per-page headings identical), homework 3/3;
    plan 6pp, deck 14 frames, student and key packets 12pp each. `make -C unit01/lesson02 all` and
    `check` both exit 0; every page rendered and eyeballed.
  - Keys generated with `templates/lesson/mkkey.py` from
    `templates/lesson/examples/lesson02_{warmup,notes,homework}_key.json`.
- **Lesson 1.3 — "Choosing a Sample: Four Sampling Techniques" — is CURRENT** (converted
  2026-09-14 to the Main Ideas / Notes table shape; regenerated into the pilot shape
  2026-09-07 before that).
  - Components: `cover`, `warmup`(+key), `notes`(+key), `homework`(+key), `slides`. `activity/`
    and `exit_ticket/` were already gone.
  - Standards: **PS.DC.2a, PS.DC.2b; AFDA.DA.2b** (PS.DC.1d carried forward).
  - Scope: the **sampling frame**; **probability vs. convenience** decided by *who could never
    have been picked* (the teacher's own third period is convenience, however fair it felt);
    **SRS** off the digit strip and the **systematic** shortcut $k = 900 \div 60 = 15$;
    **stratified** allocation 270/240/210/180 at $1/15$ → 18/16/14/12; and **the target
    misconception --- "chance chose, so it is fine"**: a cluster sample works only when each
    cluster is a small mix of the whole. Riverbend's 30 homerooms of 30 are grouped by grade, so
    Maya's random draw of rooms 4 and 7 is $2 \times 30 = 60$ ninth graders and no seniors ---
    nobody counted wrong, and about one draw in four lands both rooms in one grade. Rule: alike
    inside → some from every group (stratified); a mix of the whole → everyone from a few
    (cluster).
  - **Hook (notes page 1 + dark slide + plan, unresolved):** Maya draws 2 of the 30 homerooms
    from a hat and surveys all 30 students in each --- *is that as trustworthy as drawing 60
    names out of the hat?* Circle yes / no / it depends; the homeroom map is withheld until
    **problem 9**, where the vote is re-taken.
  - **Notes rows (14 problems):** 1. **Who Chooses?** --- frame, chance against convenience
    (1--2) · 2. **SRS \& Systematic** (3--4) · 3. **Stratified** (5--6) · 4. **Cluster** (7--10,
    the crux row) · 5. Guided Practice --- **Cedar Ridge** (11--14). The teacher works 1, 3, 5
    and 7.
  - **The trap is problem 2** --- the teacher's own third period: *random* is not *unplanned*.
    **The crux is problem 9** (vote again: chance chose, nobody miscounted, and both rooms are
    ninth grade); **problem 13 is it transferred**, and 14 is choose-and-justify (PS.DC.2b).
  - Contexts: Riverbend HS (warm-up + notes; 900 → 60), **Cedar Ridge Apartments (Guided
    Practice; 600 households in 30 buildings of 20 --- studios 1--6/120, one-bed 7--20/280,
    two-bed 21--30/200 → strata 12/28/20 at $1/10$; the hat draw of buildings 2, 5 and 6 is 60
    studio households)**, Harbor Point Community Pool (homework; 1,500 → 100). Bayside Middle
    School survives only as the debrief's **cold check**. All arithmetic re-verified in Python
    this run, including $\binom{30}{2} = 435$ with 100 same-grade pairs (about 23\%).
  - Homework: unchanged from 2026-09-07 --- 6 items, 12 points, item 5 the contrast pair plus
    the crux head-on, item 6 the choose-and-justify. Two pages. Packet night.
  - Page counts (12pt): cover 1, warmup 1/1, **notes 4/4**, homework 2/2; plan 6pp, deck 14
    frames. `make -C unit01/lesson03 all` and `check` both exit 0; blank↔key parity verified by
    per-page content, not totals (p1 ends at row 1's definition, p2 at row 3's, p3 at problems
    7--8, p4 at problems 13--14 in both files).
  - Keys generated with `templates/lesson/mkkey.py` from
    `templates/lesson/examples/lesson03_{warmup,notes,homework}_key.json`.
  - **Fitting lesson:** the first table draft ran 5pp with **every key answer overflowing its
    `\pcell` box** and TikZ labels colliding in three displays. All display labels were set
    `\tiny` and shortened, the framed row-4 callout replaced with plain emphasis, and rows 1 and
    3 folded from four problems to two each --- the cut items ("a computer picks 60", the hat
    draw) were already duplicated by problems 3 and 7. Result 4/4 with 14 problems.
- **Lesson 1.4 — "Bias in Samples and Surveys" — is CURRENT** (converted 2026-09-14 to the
  Main Ideas / Notes table shape; regenerated into the pilot shape 2026-09-07 before that).
  - Components: `cover`, `warmup`(+key), `notes`(+key), `homework`(+key), `slides`. `activity/`
    and `exit_ticket/` were already gone.
  - Standards: **PS.DC.2c; AFDA.DA.2e, 2f, 2g** (PS.DC.1d–e, PS.DC.2a carried forward).
  - Scope: **bias is a direction, not bad luck** (three honest samples 19/22/19 averaging 20\%
    against three Tuesday samples 35/36/37 averaging 36\% --- *consistent is not correct*);
    **sampling bias** split into **undercoverage** and **nonresponse** with the test *could that
    person have been chosen?*; the seven named **response biases** as a pre-filled reference
    table plus a five-row diagnostic fill table carrying the 62\% / 41\% question-order pair;
    and **the crux --- "the sample was too small"**: ten Tuesdays, $270/750 = 36\%$, the same
    16-point miss. *A larger sample makes an estimate more precise, not more correct; size
    shrinks variability, and nothing about size touches direction.* Closes with each fix
    attached to the bias it removes (AFDA.DA.2g).
  - **Hook (notes page 1 + dark slide + plan, unresolved):** the staff member blames *size* and
    will run the Tuesday survey for ten weeks --- 750 members instead of 75. *Will her new
    number land closer to 20\%?* Circle yes / no / it depends; **settled at problem 13.**
  - **Notes rows (19 problems, 5 blanks, 6 `\labelbox`):** 1. **Bias** --- *a direction, not bad
    luck* (1--4) · 2. **Sampling Bias** --- *who never had a chance* (5--8) · 3. **Response
    Bias** --- *after the right person is chosen* (9--11; problem 9 is the word-bank fill table)
    · 4. **Bigger Is Not Better** --- *ten Tuesdays* (12--15, the crux row) · 5. Guided Practice
    --- **Cedar Ridge** (16--19).
  - **Problem 4 is the small trap** (the tighter Tuesday row --- consistent is not correct);
    **problem 8 is the main trap** (all 1,500 mailed a card, 200 back --- a perfect frame and a
    broken study: nonresponse); **problem 13 is the crux** and re-takes the hook vote; problem
    14 attaches each fix to its bias; problem 15 is the counterweight; **problem 18 is the crux
    transferred** and 19 is the AFDA.DA.2g rewrite.
  - Contexts: Harbor Point Community Pool (warm-up + notes; census $300/1500 = 20\%$, Tuesday
    $27/75 = 36\%$ → 540, off by 240; $270/750 = 36\%$), **Cedar Ridge Apartments (Guided
    Practice; 600 households all mailed, $150/600 = 25\%$ returned, $96/150 = 64\%$ → 384
    against the census $240/600 = 40\%$ --- 24 points and 144 households too high; $192/300 =
    64\%$ again is the crux transferred)**, Millbrook Public Library (homework). Bayside Middle
    School survives only as the debrief's **cold check**.
  - Homework: unchanged from 2026-09-07 --- 6 items, 12 points, item 4 the contrast pair plus
    the crux head-on, item 6 the 65\% response rate and its fix. Two pages. Packet night.
  - Page counts (12pt): cover 1, warmup 1/1, **notes 4/4** (per-page first *and* last lines
    identical blank↔key), homework 2/2; plan 7pp, deck 14 frames. `make -C unit01/lesson04 all`
    and `check` both exit 0.
  - Keys generated with `templates/lesson/mkkey.py`; the notes spec is
    `templates/lesson/examples/lesson04_notes_key.json`.
  - **Fitting lesson:** the first table draft ran 5pp. All 18 `\pcell` heights were resized to
    1.0--1.4cm, four TikZ scales dropped to 0.65--0.70, five sentences shortened and the
    diagnostic table's `\arraystretch` cut to 1.05 --- 4pp without losing a problem. The key's
    first pass overflowed its cells: **a keyred line holds about 28 characters in a half-column
    `\pcell`**, so every answer was re-cut to two lines or fewer.
- **Lesson 1.5 — "Observational Studies" — is CURRENT** (regenerated 2026-09-14 in the
  Main Ideas / Notes table shape, from the pre-EFFL legacy shape).
  - Components: `cover`, `warmup`(+key), `notes`(+key), `homework`(+key), `slides`.
    `activity/`, `activity_key/`, `exit_ticket/`, `exit_ticket_key/` deleted.
  - Standards: **PS.DC.2d** (PS.DC.1a–b carried forward; previews PS.DC.3a–b).
  - Scope: the one-word definition --- you measure or survey **without assigning**, so the
    groups formed themselves (a survey is one type of observational study, which makes every
    Unit 1 study so far one); using the statistical cycle to plan and conduct the study
    (PS.DC.2d); **explanatory vs. response** variable; and the pivot --- **association is not
    causation**, taught as *three live stories for one table*: the claim, the same arrow
    **backwards**, and a **lurking variable** outside the study moving both. Closes on which
    statements the study licenses, the banned verbs (*causes, makes, raises, improves*), and the
    fact that a prediction about switching groups is a causal claim in disguise.
  - **Deliberate placement after 1.4:** every scenario here is drawn at random with a 100\%
    response rate, so bias is off the table and what remains is visible. The homework's closing
    item is exactly that --- *no bias at all, and still no causation*.
  - **Hook (notes page 1 + dark slide + plan, unresolved):** a random sample of 200, every count
    correct --- $70\%$ of morning swimmers get 7+ hours of sleep against $45\%$ of evening
    swimmers --- and the director's flyer: *"Swim in the morning --- sleep better!"* Circle
    **safe / not safe**; re-voted at **problem 13**.
  - **Notes rows (18 problems):** 1. One word: **Assign** (1--4) · 2. The plan, again: **The
    Cycle** (5--8) · 3. Explanatory \& response: **Two Variables** (9--10) · 4. Association is:
    **Not Causation** (11--14, the crux row) · 5. Guided Practice --- **Study Center** (15--18).
    The teacher works 1, 5, 9 and 11.
  - **The trap is problem 3** --- the director *assigns* swim times, the one non-observational
    plan, which students sort by "is it a survey." **The crux is problem 13** (the hook vote
    re-taken: only *morning swimmers report more sleep* is supported); problem 12 is the lurking
    variable (retirement, $60/80 = 75\%$ against $18/120 = 15\%$) and **problem 14 is the
    prediction about switching groups --- a causal claim in disguise**.
  - Contexts: Harbor Point Community Pool (warm-up + notes; SRS of 200 from 1,500, 80 morning /
    120 evening, $56/80 = 70\%$ against $54/120 = 45\%$), **Riverbend Study Center (Guided
    Practice; random 150 records, users $39/60 = 65\%$ against non-users $72/90 = 80\%$ --- the
    association runs backwards; problem 17 is the crux transferred, 18 the arrow backwards with
    $45/60 = 75\%$ against $9/90 = 10\%$ having already failed a class)**, Millbrook Public
    Library (homework; 1,200 card holders, unbiased phone sample of 240). Bayside Middle School
    ($90/150 = 60\%$ against $240/600 = 40\%$, band "raises" math grades) survives only as the
    debrief's **cold check**, folded in from the deleted exit ticket.
  - Homework: 6 items, 12 points --- 1 individuals and variables; 2 the two rates ($72/90 = 80\%$
    against $48/150 = 32\%$, a 48-point gap); 3 pool and scale ($120/240 = 50\%$ → about 600,
    spiral to 1.2); 4 **the contrast pair** (association against "more than doubles"); 5 the
    previous summer ($63/90 = 70\%$ against $30/150 = 20\%$ --- the arrow backwards); 6 **the
    crux head-on** --- no bias at all, and still no causation. Two pages. Packet night.
  - Page counts (12pt): cover 1, warmup 1/1, **notes 4/4**, homework 2/2; plan 7pp, deck 16
    frames. `make -C unit01/lesson05 all` and `check` both exit 0; per-page first lines compared
    blank↔key on every component.
  - Keys generated with `templates/lesson/mkkey.py` from
    `templates/lesson/examples/lesson05_{warmup,notes,homework}_key.json`.
  - **Two documented deviations:** `\termrowheight` is **2.1cm** here, not the usual 2.3cm (the
    file says so in a comment) --- needed so the table's first sub-row starts on page 1 and the
    notes land at four pages; and the lesson carries **18 problems, not 19** (one was cut from
    row 4 for the same reason).
- **Lesson 1.6 — "Principles of Experimental Design" — is CURRENT** (regenerated 2026-09-14 in
  the Main Ideas / Notes table shape, from the pre-EFFL legacy shape).
  - Components: `cover`, `warmup`(+key), `notes`(+key), `homework`(+key), `slides`.
    `activity/`, `activity_key/`, `exit_ticket/`, `exit_ticket_key/` deleted.
  - Standards: **PS.DC.3a (i–iv), PS.DC.3b; AFDA.DA.2c** (PS.DC.1b carried forward).
  - Scope: 1.5's pivot from the other side --- the researcher **assigns** and **imposes a
    treatment**; **experimental units / subjects**, **treatment**, **control group** (the
    baseline, not a wasted group); the four principles **comparison, randomization,
    replication, control** evaluated in context (PS.DC.3b); **confounding variable** taught as
    1.5's lurking variable that got *inside* the experiment; the **placebo effect** in a school
    setting (*being chosen* is itself a treatment) and single- vs. **double-blind**; and
    completely randomized / randomized block / matched pairs, with block allocation done as
    arithmetic. Closes on the payoff --- random assignment is what buys the verb *caused*.
  - **The lesson is 1.5's answer, deliberately on the same contexts.** Riverbend's observational
    study made the Study Center look *harmful* ($65\%$ users against $80\%$ non-users); the
    experiment makes it look *helpful* ($75\%$ against $55\%$). Same school, same Study Center,
    opposite conclusions --- and **a smaller gap as the stronger evidence** is the closing item.
  - **Hook (notes page 1 + dark slide + plan, unresolved):** two quarters of the same Study
    Center --- *watched* $65\%$ against $80\%$ (looked harmful) against *assigned* $75\%$
    against $55\%$ (looks helpful). Which should the counselor believe? Circle one; re-voted at
    **problem 12**.
  - **Notes rows (17 problems):** 1. *Assign, don't watch* --- **Experiment** (1--4) · 2. *Four*
    --- **Principles** (5--7; problem 5 is the Cedar Ridge fill table and the lesson's one
    `\wordbank` / `\blank` cluster) · 3. *Two refinements* --- **Blinding \& Blocking** (8--9) ·
    4. *What buys the verb* --- **Caused** (10--13, the crux row) · 5. Guided Practice ---
    **Harbor Point Swim Times** (14--17). The teacher works 1, 6, 8 and 10.
  - **The trap is problem 4** --- new app against old packet: the packet group *is* the control
    group. **The crux is problem 13** --- a *watched* 35-point gap still earns only
    "association"; **problem 17 is it transferred** (25 watched points against 20 assigned).
  - Contexts: Riverbend HS (warm-up + notes; 120 volunteers split 60/60 by generator,
    $45/60 = 75\%$ against $33/60 = 55\%$, gap 20; block on last quarter's grades), **Harbor
    Point Community Pool (Guided Practice; 90 volunteers 45/45, $27/45 = 60\%$ against
    $18/45 = 40\%$, gap 20 against 1.5's watched gap of 25)**, Millbrook Public Library
    (homework; 1,200 card holders, 200 volunteers → 100/100). Bayside survives only as the
    debrief's **cold check**.
  - Homework: 6 items, 12 points --- 1 name the parts; 2 the two rates and the gap
    ($65\%$/$35\%$, 30); 3 pool and scale ($50\%$ → 600 as an estimate, spiral to 1.2);
    4 **the contrast pair** (watched against assigned --- association against caused); 5 block
    on age (120 → 60/60, 80 → 40/40) and why; 6 **the crux head-on** (a 48-point gap against
    30). Two pages. Packet night.
  - Page counts (12pt): cover 1, warmup 1/1, **notes 4/4**, homework 2/2; plan 7pp, deck 15
    frames. `make -C unit01/lesson06 all` and `check` both exit 0; per-page last lines compared
    blank↔key off the built PDFs for all three keyed components.
  - Keys generated with `templates/lesson/mkkey.py` from
    `templates/lesson/examples/lesson06_{warmup,notes,homework}_key.json`.
  - **One documented deviation:** `\termrowheight` is **2.15cm**, not 1.2's 2.3cm --- the 0.75cm
    it frees is what lets the table's first row start on page 1 and the notes close at four
    pages.
  - **Fitting lesson:** the inherited draft had never been compiled and ran **6pp**, with the
    row-3 and row-4 displays overflowing the Notes column (panel headers colliding,
    `\normalsize` rate lines spilling out of their boxes). Both displays were rebuilt, every
    figure rescaled, row 3's two grid sub-rows merged into one, prose and answer heights cut ---
    4pp, and the problem count fell 19 → 17. The **homework key ran 3pp against a 2pp blank**
    (long answers pushed the `spiralbox` over), fixed by shortening answers in the JSON.
- **Lesson 1.7 — "Comparing Studies and Choosing a Method" — is CURRENT** (regenerated
  2026-09-14 in the Main Ideas / Notes table shape, from the pre-EFFL legacy shape).
  - Components: `cover`, `warmup`(+key), `notes`(+key), `homework`(+key), `slides`.
    `activity/`, `activity_key/`, `exit_ticket/`, `exit_ticket_key/` deleted.
  - Standards: **PS.DC.3c, PS.DC.3d, PS.DC.3e** (PS.DC.1b carried forward).
  - Scope: the two study types **side by side**, the first row (*who decides which group each
    individual is in*) producing every other row, and the sentence each design earns (*is
    associated with* against *caused*); **when you cannot run an experiment** ---
    unethical / impossible / impractical, with the test *can you hand this out to a person?*,
    and the rule that an unavailable experiment is a reason for a **weaker verb**, not an excuse
    for a stronger one; **PS.DC.3d** --- the cycle used to plan a well-designed experiment, only
    the *Collect* row changing from *sampled* to *assigned*; and **PS.DC.3e** --- the five
    collection methods as a pre-filled reference table plus diagnostic rows.
  - **Built on the 1.5/1.6 pairs rather than new scenarios**: every context has already been run
    both ways, so the comparison is between studies students themselves computed.
  - **Hook (notes page 1 + dark slide + plan, unresolved):** a generator split 120 volunteers
    60/60, then the counselor *sat in the Study Center and watched*. A classmate says: "she just
    watched, so this quarter's study was an observational study." Circle agree / disagree;
    re-voted at **problem 15**.
  - **Notes rows (19 problems; problem 1 is the side-by-side fill table):** 1. Side by side ---
    **Two Designs** (1--5) · 2. When you cannot --- **Experiment** (6--9) · 3. Planning an
    experiment --- **The Cycle** (10--11) · 4. Five ways to collect --- **The Method** (12--15,
    the crux row) · 5. Guided Practice --- **Harbor Point** (16--19).
  - **The trap is problem 8** --- the 45-minute bus ride is *impossible*, not *unethical*; take
    a hand count before anyone writes. **The crux is problem 15** --- observation the *method*
    inside an experiment the *design*; the hook vote is re-taken there, and **problem 19** is it
    transferred.
  - Contexts: Riverbend HS (warm-up + notes; watched $65\%$/$80\%$ against assigned
    $75\%$/$55\%$), **Harbor Point Community Pool (Guided Practice; the 1.5 survey of 200 and
    the 1.6 experiment of 90 labelled, then a new water-aerobics experiment --- 120 volunteers
    60/60, $42/60 = 70\%$ against $30/60 = 50\%$, gap 20)**, Millbrook Public Library (homework;
    a third study --- 300 volunteers 150/150, $96/150 = 64\%$ against $60/150 = 40\%$, gap 24).
    Bayside Middle School (Study A / Study B, $90/150 = 60\%$) survives only as the debrief's
    **cold check**.
  - Homework: 6 items, 12 points --- 1 sort the two earlier designs; 2 rates, gap and the verb;
    3 the cycle (spiral to 1.5); 4 **the contrast pair** (a late fee is assignable, being read to
    as a toddler is impossible); 5 all five methods; 6(a) **the crux head-on** and 6(b) the
    48-point gap as the *weakest* evidence. Two pages. Packet night.
  - Page counts (12pt): cover 1, warmup 1/1, **notes 5/5**, homework 2/2; plan 7pp, deck 15
    frames. `make -C unit01/lesson07 all` and `check` both exit 0; per-page correspondence
    verified blank↔key, and every page of both packets, the plan and the deck rendered and
    inspected.
  - Keys generated with `templates/lesson/mkkey.py` from
    `templates/lesson/examples/lesson07_{warmup,notes,homework}_key.json`.
  - **OPEN — the notes are 5pp against the profile's 3--4pp budget.** Vocab rows were cut to
    1.7cm, every `\pcell` height reduced, all five figures rebuilt narrower, and the prose
    tightened throughout; reaching 4pp needs about 18cm more, which means **losing a
    standards-bearing row** --- either PS.DC.3d's cycle row or half of PS.DC.3e's methods row.
    The content was kept and the overrun flagged instead. **This is a decision for the user:**
    cut a row (and drop a standard's coverage in the notes), or raise the budget for a
    three-standard lesson. Twelve key answers also overflowed their `\pcell` boxes silently on
    the first pass and were shortened in the JSON.
- **Lesson 1.8 — "Project: Design and Conduct a Survey" — is CURRENT** (regenerated 2026-09-14
  in the Main Ideas / Notes table shape, from the pre-EFFL legacy shape).
  - Components: `cover`, `warmup`(+key), `notes`(+key), `homework`(+key), `slides`.
    `activity/`, `activity_key/`, `exit_ticket/`, `exit_ticket_key/` deleted. The project
    deliverable is **homework item 6**, not an `extensionbox` (retired course-wide).
  - Standards: **AFDA.DA.2d, 2h, 2i, 2j; PS.DC.2d**.
  - Scope: the unit **run forwards** --- students build a study instead of taking one apart. The
    four-stage cycle as a *deliverables checklist*; **the survey instrument**, the lesson's only
    genuinely new content, taught by repairing three broken items students met in 1.4 as
    response bias; **relative frequency** and a **pre-drawn, pre-scaled bar graph** read and
    annotated with `\labelbox` (AFDA.DA.2h --- nothing is sketched); scaling a sample percent to
    a population; and the **four-sentence report** the project is graded on.
  - **The lesson's pivot is that the class is a convenience sample.** The Student Council's
    stratified 60 may speak about all 900 students; the class of 25 may not. The two results are
    built to *nearly agree* so that near-agreement can be named as luck, not evidence --- chance
    never chose this class. Naming the limit is scored as part of the answer, not as an apology.
  - **Hook (notes page 1 + dark slide + plan, unresolved):** last spring's class of 25 in this
    room got $36\%$ for club funding against the council's stratified-60 result of $35\%$, and a
    student wrote *"we matched the council, so our class can speak for all 900 students too."*
    Circle agree / disagree; re-voted at **problem 13**.
  - **Notes rows (19 problems):** 1. **The Cycle** --- the deliverables checklist (1--4) ·
    2. **The Instrument** --- four rules taught by repair (5--6 plus the fill table) ·
    3. **Relative Frequency** --- the pre-drawn bar graph (7--11) · 4. **The Limit** (12--15,
    the crux row) · 5. Guided Practice --- **Our Class Survey** (16--19).
  - **The trap is problem 9** --- $9/25 = 36\%$ and $0.36 \times 900 = 324$ are both
    arithmetically right and the claim is still illegal. **The crux is problem 13** (the hook
    re-vote), **transferred to the class's own live data at problem 18**.
  - **The Guided Practice is the class's own survey**: the instrument is built live in a card of
    `\blank{}`s, then a tally table is filled from the room. **The key's 9/7/6/3 →
    $36$/$28$/$24$/$12\%$ is a worked exemplar** --- real class data will differ, and that
    warning is in the plan's `[Guided Notes \& Practice]` teacher note, never in the key.
  - Contexts: Riverbend Student Council \$3,000 grant (warm-up + notes; stratified 60 from 900
    at $1/15$ → 18/16/14/12), the class's own survey (Guided Practice), Millbrook Public Library
    (homework; an SRS of 80 by phone → 28/24/20/8 = $35$/$30$/$25$/$10\%$, $0.35 \times 1200 =
    420$, against a front-desk clipboard of 50 where 30 chose story hour = $60\%$). Bayside
    Middle School (homeroom of 30, 12/9/6/3, $0.40 \times 750 = 300$) survives only as the
    debrief's **cold check**.
  - Homework: 6 items, 12 points --- 1 relative frequencies; 2 read the bar graph and spiral to
    variable type; 3 **the contrast pair** (scale the SRS, the clipboard percent, which may be
    scaled at all); 4 **the crux head-on** (the clipboard's $13/50 = 26\%$ beside the SRS's
    $25\%$); 5 justification and instrument repair, spiralling to 1.4; **6 the project
    deliverable** --- the four-sentence report on the class's own tally. Two pages.
  - Page counts (12pt): cover 1, warmup 1/1, **notes 5/5**, homework 2/2; plan 6pp, deck 15
    frames, student and key packets 12pp each. `make -C unit01/lesson08 all` and `check` both
    exit 0; per-page headings compared blank↔key, and every page rendered and inspected (four
    figure overlaps found and fixed that way).
  - Keys generated with `templates/lesson/mkkey.py` from
    `templates/lesson/examples/lesson08_{warmup,notes,homework}_key.json`.
  - **OPEN — the notes are 5pp against the profile's 3--4pp budget**, as in 1.7. This is a
    project lesson whose Guided Practice row must carry a live instrument card *and* a tally
    table. After four trimming passes (vocab rows to 1.85cm, every figure rescaled, answer
    spaces to 1.6--1.8cm, prose compressed) 5pp was the floor without cutting problems below the
    shape's density rules. **The user's call**, together with 1.7's overrun.
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

0. **Decide the two 5pp notes** — 1.7 and 1.8 (see the two open items at the top). Either raise
   the profile's 3–4pp budget for a three-standard lesson and for the project lesson, or name the
   row to cut. **Nothing else in unit 1 is waiting on a decision.**
1. **Teach the shape and bring back what worked.** All nine unit-1 lessons are now in it, so a
   correction is a correction to the rule: **change `LESSON_SHAPE.md` first, then the lessons.**
   A change to the notes table now costs nine conversions, not one.
2. ~~Open questions for the user~~ — **all three decided 2026-09-06**: phases total 60
   (5 / 35 / 10 / 10); no `extensionbox` course-wide; homework due at the start of the first
   class after two study halls.
3. ~~Convert 1.0, 1.1, 1.3–1.8~~ — **done 2026-09-14.** Unit 1 is uniform.
4. **Units 2–8**: scaffold `notes` (only) into each lesson as authored and delete
   `experience`/`experience_key`; confirm the Unit 2 lesson map with the user before authoring.
   **Author them straight into the table shape** — there is no longer an older shape to convert
   from, and `templates/lesson/notes.tex` already emits it.
5. **Reuse the Unit 1 assessment set as the template for U2–U8** (blueprint 14/16/40/30, 33 items,
   6 pages; `\setlength{\workrowsep}{5pt}` in every test preamble; unit cover pair with scoring on
   the key's page 2). The tests were untouched by every redesign, including this one.
6. **The unit-1 tests are still 10pt** while every lesson component is 12pt. Not a defect — the
   tests were never part of the pilot — but worth a decision the next time they are opened.
7. **A course-wide final (`finals/`) is still not scaffolded.** Wait for more units.
8. **Promote into `shared/` on a run allowed to touch it:** the measured `\coverbanner` block and
   the `\vterm`/`\vtermans` pair, which every lesson currently copies into its own preamble, and
   the `\wordbank` strip. Three copies per lesson × nine lessons is the current cost. Doing so
   would also let the cover's 16.24pt overfull `\namedateperiod` line be fixed once.
9. Merged to `main`: lesson-1.0 + palette as PR #3; 1.1 as PR #4; 1.2 as PR #5; 1.3 as PR #6;
   1.4 as PR #7; 1.5 as PR #8; 1.6 as PR #9; the breakdown doc as PR #10; 1.7 as PR #11; 1.8 as
   PR #12; the EFFL port as PR #15; the 1.0 EFFL regen as PR #16; the gradual-release restoration
   as PR #17; the drop-the-activity skill rewrite as PR #18; the 1.1 notes-only conversion as
   PR #19; 1.1's classroom revision as PR #20; the shared-skill move as PR #21. **The 1.2 pilot +
   profile rewrite merged as PR #22** (2026-09-07); the 12pt follow-up is PR #23. **The 1.3
   regeneration is PR #26** and **the 1.4 regeneration PR #27** (2026-09-07). **The Main Ideas /
   Notes table + 1.2's conversion is PR #28** (2026-09-13). **This run — the whole of unit 1 into
   the table shape — is the PR opened 2026-09-14.**

## Gotchas found this session

### Converting eight lessons at once — what actually bit (found 2026-09-14)

Eight subagents, one lesson each, one shared brief. Every one of them hit the same three
problems, so these are properties of the table shape rather than of any lesson:

- **A `\pcell` answer longer than its fixed height overflows silently — no warning, no overfull
  box, nothing in the log.** It is invisible until you render the key and look at it. Six of the
  eight lessons shipped a first key with overflowing cells; 1.3's had **every** answer
  overflowing. **A keyred line holds about 28 characters in a half-column `\pcell`.** Write the
  answer first, then size H to it, then render the key and read it. This is the single most
  common defect in the shape and `make check` cannot see it.
- **TikZ `scale` shrinks coordinates but NOT font size.** Below about `scale=0.75`, captions
  stacked above a line, panel headers, and legend entries start colliding — and again nothing
  appears in the log. Every lesson that rescaled a figure to save a page produced at least one
  collision. Give nodes a bounded `text width`, set display labels `\tiny`, and re-render.
- **The first draft of a table always runs long.** Six of eight came in at 5–6pp against a 3–4pp
  budget. What recovers a page, in the order worth trying: shrink `\pcell` answer heights;
  rescale and rebuild the figures; cut `\termrowheight` from 2.3cm to ~2.1cm (this alone often
  decides whether the table's first row starts on page 1); trim printed prose; merge two grid
  sub-rows into one; and last, fold four problems into two — usually there is a duplicate pair.
  **Cutting problems is the last resort, not the first.**

**Two structural limits found.** A lesson carrying three standards (1.7: PS.DC.3c/3d/3e) and the
project lesson (1.8, whose Guided Practice needs a live instrument card *and* a tally table)
**cannot reach 4pp without dropping a standard's coverage**. The budget is a density rule, not a
physical law; where it and the standards disagree, flag it rather than quietly cutting.

**The homework key can run long while the blank does not** (found in 1.6): long key answers push
the closing `spiralbox` onto a third page against a two-page blank. Page-for-page is checked on
the **compiled components**, never on the merged packets — the pagination pass pads a mismatch
silently, so the packets agree while the components do not.

**Regenerating every key and diffing it against disk is a cheap, total proof** that no key was
hand-edited and none has drifted:

```
python3 templates/lesson/mkkey.py <blank> /tmp/out.tex <spec> && diff /tmp/out.tex <key>
```

Run it across the unit before opening a PR. All 24 unit-1 keys pass it as of 2026-09-14.


### Blank/key page alignment is NOT what `make check` verifies (found 2026-08-31)

The gate compares a component with its key by **total page count only**. Two files can both be
4 pages and still break in different places, so the teacher's page 3 is not the student's page 3.

**Cause.** In the guided notes' `vocabbox`, the blank's `\termblanklong{Term}` reserves two ruled
lines per term while the key's `\vocabans{Term}{definition}` prints a wrapped definition that is
usually shorter. The key's page 1 gains an inch or two, the first `notesbox` floats up onto it,
and every section after it sits one page early. **Lesson 1.1 shipped this way originally**, and the
2026-08-31 regeneration **fixed it**: `\boxguard[20]` now guards the first `notesbox` after the
`vocabbox` in both files, and all five notes pages were verified heading-for-heading. Do the same
in every conversion.

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
