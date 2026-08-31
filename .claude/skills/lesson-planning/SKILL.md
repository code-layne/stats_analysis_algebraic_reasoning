---
name: lesson-planning
description: >-
  Author complete, build-ready lessons for the Statistical Analysis & Algebraic Reasoning LaTeX
  curriculum (a project with a shared/ style package — prefix saar — and a Makefile hierarchy
  that compiles components with latexmk and merges them with pdfunite).
  Use this whenever the user wants to create, draft, or build a lesson, a lesson plan, a
  unit, or any lesson component — warm-up, guided notes, group activity, homework, cover sheet,
  slides, or their answer keys. Lessons follow a gradual-release model (I do / we do / you do
  together): warm-up, guided notes and practice, one whole-class group activity, teacher-led debrief,
  close and assign. The course is defined by
  spec/statistical_analysis_algebraic_reasoning.md and the standards documents in spec/; units are
  standard clusters and lessons are groups of the standards' lettered Knowledge & Skills.
  Trigger this even when the user just says "make lesson 2.3" or
  "I need a warm-up and key for tomorrow," and even if they don't say "skill" or "LaTeX." Also
  use it to author unit-level tests and a cumulative, course-wide final exam (the `finals/`
  deliverable) — any "final," "final exam," or "cumulative assessment" for the whole course.
  Also use it to RETROFIT a lesson to a named convention — boxguard, namestrip, vocabpar, the
  work rule, teachernotes — or to CONVERT an older lesson into the gradual-release shape, as in
  "convert unit 2 back to guided notes." See the Retrofit section.
---

# Lesson Planning — Statistical Analysis & Algebraic Reasoning

This skill authors lessons for the **Statistical Analysis & Algebraic Reasoning** course and
produces print-ready PDFs through the project's own build system. **It builds around the
project's conventions — it does not invent its own.** The course is a **modeling- and
applications-first** secondary course pairing statistical work with algebraic reasoning. Author
every component in that spirit: start from a context, compute, then **interpret and justify** —
and cite the standard codes the lesson covers.

**Every new lesson follows the gradual-release model** — *I do, we do, you do together*. The
teacher hooks the class, builds the ideas in **guided notes** with worked examples and a
class-filled vocabulary box, releases a short practice box, then hands the work to **groups of
three working one common activity**; a teacher-led **debrief** closes the loop and is the formative check. The 55-minute
period runs **5 warm-up / 20 guided notes & practice / 18 group activity / 7 debrief /
5 close & assign**.

**The debrief is not a component.** It is a phase, and it lives *only* in the lesson plan's
Debrief box and the deck's debrief frame — there is no student page for it. **There is no exit
ticket**: the debrief's cold check, run whole-class while students correct their own work in a
second color, is what tells you whether the lesson landed.

> **History.** An "experience first, formalize later" (EFFL) trial ran from 2026-08-29 to
> 2026-08-31 and put a single `experience/` component (Activity · QuickNotes · Application) in
> place of notes and activity. It was **scrapped** — students rejected it. Do not author
> `experience/` into a new lesson; see Retrofit for converting one that still exists.

### What is different about this course

1. **Homework is authored for every lesson, and it is scored.** ~6 items in new contexts
   spanning the lesson's lettered skills, each ending in an interpretation or a justification
   (the cover's score column carries a `\blank{}`, never `NA`). Algebra 2 dropped homework
   entirely and AP Statistics keeps a separate unscored in-class CYU — **do not copy either.**
2. **Packet or DeltaMath is a per-lesson teacher decision.** The packet pages are authored for
   every lesson regardless. **DeltaMath's statistics coverage is thin, so the packet is the
   default**; at Close & Assign the teacher may override it with the equivalent DeltaMath set
   where DeltaMath actually carries this lesson's skills. Nothing in the packet changes either
   way; the lesson plan's Homework box and the deck's closing frame carry the choice.
3. **Group work is NOT tiered.** One activity, the whole class, groups of three — nothing to
   assign or sort. Differentiate by **depth, not by handout**: the items ramp from readable-off-
   the-data to the crux, and an optional `extensionbox` at the end absorbs groups that finish
   early. Do not author Tier R / Tier A / Tier E boxes.
4. **This course HAS `fixedskillbox`** (AP Statistics does not). Use it where a lesson-plan
   `tabularx` must stay intact on one page; use `skillbox` + `\boxguard` everywhere else.

## The course at a glance

- **Structure** comes from `spec/statistical_analysis_algebraic_reasoning.md` — the guiding
  philosophy and the **course map**: one unit per standard cluster, each lesson grouping a
  standard's lettered Knowledge & Skills. `spec/unit_lesson_breakdown.md` is the per-lesson index
  and status table; `spec/course_planning.md` is the running handoff log.
- **Content** comes from the **standards documents in `spec/`**: the approved standards PDFs give
  the standard text and its lettered skills (the codes a lesson cites); the **"Understanding the
  Standards"** PDFs give the scope limits and notation — read the relevant pages *before*
  authoring. See `references/course-workflow.md`.
- **Audience is secondary school**, mid-track. Scaffold heavily — a context first, small numbers,
  one new idea at a time, worked examples, vocabulary support.
- **Every lesson cites its standards.** This is a standards-driven course; the lesson plan's
  Priority Ideas box and the Connections line both carry the lettered codes covered.
- **Style prefix is `saar`** — `shared/saar-{colors,article,boxes,key,beamer}.sty`. The palette
  is **cerulean with gold accents** (the third blue across the stats-family courses; see
  `references/conventions.md`); `royal`, `mist`, `burgundy`, `navy` and friends are undefined
  here. A teacher **slide deck** (`slides`) is supported — `shared/saar-beamer.sty` is in place.

## What a lesson is

A lesson lives in `unitXX/lessonYY/` and consists of:

- **`main.tex`** — the teacher-facing **lesson plan** (the root document of the lesson dir).
- A set of **student components**, each its own subdirectory containing **either** a
  `main.tex` (authored, compiled to a PDF) **or** a `main.pdf` (a prefab PDF, used as-is):
  `cover`, `warmup`, `notes`, `activity`, `homework`, and `slides`.
- An **answer key** for each keyed component, as a *separate* sibling directory:
  `warmup_key`, `notes_key`, `activity_key`, `homework_key`. (`cover` and `slides` have no key.)
- **`notes` — the guided notes — is the heart of the lesson.** Objectives, a `vocabbox` the
  class fills in together, a `hookbox`, **4–6 numbered `notesbox` teaching sections** (I do /
  we do), and a closing `practicebox` (you do). Budget **≤4pp**, ~20 minutes.
- **`activity` is one group activity for the whole class**, worked in groups of three *after*
  the notes, so students already hold the vocabulary. One shared data set, ~6–7 items in two
  labelled parts, then an optional `extensionbox`. Budget **≤2pp**, 18 minutes.
- **`homework` is authored for every lesson and is scored** — ~6 items in new contexts spanning
  the lesson's lettered skills, assigned from the packet by default or overridden with DeltaMath
  lesson by lesson.
- *Dead shape:* `experience/` (and `experience_key/`) is the scrapped EFFL component;
  `exit_ticket/` predates both redesigns. The build still merges both, so any lesson carrying
  them keeps building untouched. When asked to touch such a lesson, **ask whether to regenerate
  it in the gradual-release shape** rather than patching it — see Retrofit.

`shared/lesson.mk` discovers a component if it has a `main.tex` **or** a `main.pdf` and
compiles the `main.tex` ones with `latexmk -xelatex`; a prefab `main.pdf` is used as-is from
the source tree with no compile step (Step 4). It then builds **five work products** into
`target/compiled/unitXX/`:

| Product | Contents |
|---|---|
| `lessonYY_plan.pdf` | the lesson plan (the lesson-root `main.tex`), on its own |
| `lessonYY_slides.pdf` | the Beamer deck **printed** — 3 slides per page, each with a ruled notes column beside it |
| `lessonYY_slides.pptx` | the same deck wrapped for PowerPoint (one full-page image per slide) — the **projected** form |
| `lessonYY_student.pdf` | cover + the **blank** warmup, notes, activity, homework, in that order |
| `lessonYY_key.pdf` | cover + the **key** version of each, in the same order |

The student and key packets are paginated as one pair: numbers run lesson-wide, each component
starts on a recto page, and the two are **page-for-page identical** (the shorter of a
blank/key pair is padded to match). Never edit the slide products — the deck at
`slides/main.tex` is the source of truth for both. Details in `references/build.md`.

## What a unit is

A unit (`unitXX/`) holds its lessons plus **unit-level summative assessments**, scaffolded
automatically when the unit is first created (Step 2):

- **`tests/`** — the blank tests, one subdir each: **`practice_test/`** (a study copy students
  keep) and **`actual_test/`** (the real test given in a testing setting). Its `Makefile`
  (`include ../../shared/tests.mk`) compiles both and its `drop` target publishes the
  *practice* test to `sample_test/main.pdf`.
- **`test_keys/`** — the matching answer keys: **`practice_test_key/`** and
  **`actual_test_key/`**; its `drop` publishes the *practice* test key to `sample_test_key/main.pdf`.
- **`sample_test/`** and **`sample_test_key/`** — prefab drop-in dirs that receive those
  published PDFs. `shared/unit.mk` merges `sample_test` into the unit **student** packet and
  `sample_test_key` into the unit **key** packet. The **actual** test and its key are never
  merged into any packet — they stay out of student hands.

So the practice test is what students study from (in the packet); the actual test is authored
alongside it, shares the format, but is distributed separately at test time.

A unit may also carry an optional **cover pair**, discovered by `shared/unit.mk` and merged ahead
of the lesson packets. Both wrappers `\input` one shared **`unit_cover/body.tex`**, so page 1
cannot drift between them:

- **`unit_cover/`** — the 1-page student cover (banner, overview, lesson table, big ideas), merged
  into the unit **student** packet.
- **`unit_cover_key/`** — the same page 1 plus a **page 2 of exam scoring notes** (answer rationale
  and Part D scoring for both tests), merged into the unit **key** packet only. This is where a
  test's teacher prose lives — never at the foot of a `*_test_key`, which would put the rationale
  in front of students via the bound practice test. Keep it to one notes page: cover + notes = one
  double-sided sheet. A unit with no `unit_cover_key/` falls back to the plain cover in both packets.

## What a course final is

A **cumulative final exam** for the whole course lives in a single top-level **`finals/`**
directory, a sibling of the `unitXX/` dirs (not inside any unit). It follows the unit-test
practice/actual pattern but as **four flat subdirectories**, each with its own `main.tex`:

- **`practice_final/`** — the study copy (blank), carrying the `remindbox` "this is a practice
  final" banner.
- **`practice_final_key/`** — its answer key.
- **`final/`** — the real exam (blank), carrying the plain **Instructions** line.
- **`final_key/`** — its answer key.

`practice_final` and `final` are **parallel forms**: same blueprint and ideas, different numbers
and reshuffled vocabulary letters. `finals/` has its own **standalone `finals/Makefile`** (it is
*not* produced by the scaffolder, and it does *not* reuse `shared/tests.mk`) and, unlike unit
tests, has **no `sample_*` drop-in dirs and no `drop`/publish step** — the final is a standalone
deliverable, merged into no packet. See "Authoring a course-wide final exam" below.

## Workflow

Follow these steps in order. Read the referenced files as you reach each step rather than
all upfront.

### Step 0 — Sync with upstream, then detect project context (always do this first)

**Sync the worktree first — before reading or writing anything.** This skill runs in a git
worktree; start *every* invocation by pulling the latest upstream changes so you author
against the current shared styles, spec, and lesson map. Do this automatically — the user
should never have to ask:

```bash
git fetch origin
# Integrate the latest default branch (usually main) into this worktree's branch:
DEFAULT=$(git symbolic-ref --quiet --short refs/remotes/origin/HEAD 2>/dev/null | sed 's@^origin/@@')
git merge --no-edit "origin/${DEFAULT:-main}"
```

If the working tree is dirty or the merge reports conflicts, **stop and surface it to the
user** — never force, reset, or discard changes to make the sync succeed. Once the sync is
clean, detect project context:

1. **Read the planning log.** Open `spec/course_planning.md` (the running handoff log) for the
   current build state and the next steps left by the previous run. It orients the whole
   session; you update it at the end (Step 6). If it does not exist yet, this is the first run.
2. **Confirm the prefix.** `ls shared/*-colors.sty` → it is `saar`. All
   `\usepackage{saar-article}` etc. use it.
3. **Course macros live in `shared/`.** `saar-article.sty` defines `\CourseName`,
   `\CourseHeaderName`, `\MeetingLength`, so a lesson plan defines only
   `\UnitNumberName` and `\LessonNumberName` (the scaffolder handles this).
4. **Find the insertion point.** List `unit*/lesson*` to find the next unit/lesson number
   and whether the target lesson already exists.
5. **Find a model lesson — and check its shape.** Open a built lesson and mirror its preamble,
   box usage, and tone. **Mirror a current gradual-release lesson.** A lesson is current when it
   has `notes/` + `activity/`, **no `exit_ticket/`**, and a *Lesson at a Glance* phase table in
   its plan. A lesson with `experience/` is the scrapped EFFL shape; a lesson with
   `exit_ticket/` predates the current design. `spec/course_planning.md` records which lessons
   have been converted. **Lessons 1.0 and 1.1 are the models** — mirror them.

### Step 1 — Map the unit into lessons, then gather the lesson's content

The content path is always `references/course-workflow.md`:

- **Decompose the unit into lessons** from `spec/statistical_analysis_algebraic_reasoning.md`
  and `spec/unit_lesson_breakdown.md`. The
  convention is **one lesson per Knowledge-and-Skills cluster** — group the standard's lettered
  bullets into coherent 60-minute chunks, in listed order (Lesson `<unit>.<n>`). Present the
  proposed lesson map for the unit and **confirm it with the user before authoring** — bullets
  merge and split depending on the class.
- **Gather the lesson's content**: the lettered skills from the approved standards PDF, the scope
  limits and notation from the matching **"Understanding the Standards"** pages, and a context
  from the course's application domains.

See `references/course-workflow.md` for the decomposition rules and the content-mapping table.

### Step 2 — Scaffold the lesson directory

Run the scaffold script. It creates the lesson directory, the one-line lesson `Makefile`,
the component subdirectories you request, **and (if missing) the root `Makefile` and the
unit `Makefile`** so the unit/curriculum builds work:

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/new_lesson.py --project . --unit 03 --lesson 02 \
  --title "<Lesson Title>" --unit-title "<Unit Title>"
```

`--components` defaults to the gradual-release set —
**`cover,warmup,notes,activity,homework,slides`** — so omit the flag. `experience` and
`exit_ticket` are still scaffoldable by name so an older lesson can be patched, but **never
author either into a new lesson.**

The script is bundled with the skill, so it is invoked via `${CLAUDE_SKILL_DIR}` (the
working directory at runtime is the user's project, not the skill folder); `--project .`
is the project root. It auto-detects the prefix and writes each authored component's
`main.tex` as a correctly-preambled skeleton (and the matching `_key` skeleton for keyed
components). Pass `--prefab warmup` to create that component as an empty drop-in directory
instead (Step 4). `slides` is part of the default component list — every lesson ships a deck,
and the deck is the source for two of the five work products — so scaffold it unless the
lesson genuinely has none; it requires `shared/saar-beamer.sty` and errors clearly if that
is missing. Then fill in the skeletons.

**Unit assessments scaffold automatically.** When the run creates a *new* unit, the scaffolder
also lays down that unit's `tests/`, `test_keys/`, `sample_test/`, and `sample_test_key/` dirs
(practice + actual test skeletons and their keys, plus thin-include Makefiles) — see
"What a unit is." It never clobbers authored tests on later lessons. Use `--no-tests` to skip
them, or `--tests` to (re)scaffold them for a unit that already exists (idempotent).

### Step 3 — Author the lesson plan and components

**Before writing any component, do a full `Read` on each scaffolded `main.tex` skeleton you
are about to replace.** Use the `Read` tool on the actual file — a `cat`/`bash` dump does
**not** register the file with the editor and the first write will fail ("file has not been
read yet"). Read every skeleton you intend to author (each component and its `_key`) up front,
then write them. This is mandatory, not optional.

Author each file following `references/components.md`, which gives the required section
structure and a worked skeleton for every component and its key. Hold to these invariants:

- **Student components** preamble with `\documentclass[10pt]{article}` +
  `\usepackage{saar-article}` + `\usepackage{saar-boxes}`. Every component is 10pt; there is no
  12pt component any more (that was EFFL's `experience/`). Use `\writeline` / `\writelines{n}`
  and `\blank{}` for student answer space — **`\answerspace` was an EFFL macro and is gone.**
- **The vocabulary is taught, not discovered.** Gradual release has no spoiler rule: the cover's
  learning targets, the warm-up, the notes' `vocabbox`, and every slide may name the formal
  terms outright. Say the word, define it, then use it.
- **The timebox rule.** Each phase must fit its block. Guided notes: 4–6 sections plus a
  practice box, ≤4pp, 20 minutes — the plan's Lesson box carries a **per-section minute budget**
  that has to sum to 20. Group activity: **~6–7 items** over one shared data set, ≤2pp, 18
  minutes — everyone works the same set, so it must be sized for one group, not split three ways.
  A part that runs over gets cut or moved to the homework, not carried.
- **Every lesson plan carries a *Lesson at a Glance* phase table** (`fixedskillbox`) with the
  five phases, their minutes, what students do, and what the teacher does. It goes after the
  Vocabulary box and before Activate Prior Knowledge.
- **Blank and key must align page-for-page, not just page-count-for-page-count.** The gate only
  compares totals. A key runs more compact than its blank wherever `\vocabans{}` replaces
  `\termblanklong{}`, which can float a whole section onto an earlier page. Guard the *first*
  `notesbox` after the `vocabbox` with `\boxguard[20]` in **both** files so the break lands in
  the same place. Verify by comparing per-page headings, not page counts.
- **Answer keys** are *separate files* that swap `-boxes` for `\usepackage{saar-key}`
  and wrap every answer in `\ans{...}` (inline) or `\ansline{...}` (fills a write-line).
  Mirror the blank document exactly, then fill the blanks with `\ans`. There is **no**
  answer-key toggle — never try to build one.
- **Author to the five conventions from the start** (full spec in `references/conventions.md`):
  worked solutions go in byte-identical `\begin{work}` blocks in the blank and the key (the
  **work rule**); teacher prose goes in the lesson plan as `\begin{teachernote}[Component]`,
  never in a `_key`; components carry **no** name/date/period row (**namestrip** — cover and
  tests only); and `\boxguard` goes before any breakable box that would otherwise strand a
  stub, in the blank and the key both (**boxguard**). **vocabpar is automatic** — the term
  macros carry their own `\par`, so do *not* add `\par\vspace{2pt}` after a vocab intro
  sentence; it double-spaces the box. `make check` (Step 5) enforces all but boxguard.
- Use the project's box vocabulary (`skillbox`, `objectivebox`, `learningtargetbox`,
  `vocabbox`, `hookbox`, `notesbox`, `practicebox`, `scenariobox`, `tocbox`, etc.) and
  fill-in helpers (`\blank`, `\writeline`, `\termblanklong`) rather than reinventing layout.
  The full catalog — and the **cerulean/gold palette**, the only colors defined — is in
  `references/conventions.md`.
- **Match the course pedagogy.** Start from a context, then extract the mathematics; compute
  *then* interpret and justify. **Cite the standard codes.**
- **Never ask students to sketch a graph from a blank page.** Where a standard says "sketch,"
  satisfy it with a **pre-drawn, pre-scaled axis system** students complete, a pre-drawn figure
  to read, or a table to fill in. Show calculator/Desmos output as a figure.
- If the warm-up is a **prefab** PDF (`warmup/main.pdf` in the source tree), the lesson plan
  may embed its thumbnail via `\includegraphics[page=1]{warmup/main}`. **Authored** warm-ups
  compile to `target/` and have no source PDF to embed, so keep the spiral review text-only;
  the scaffolder picks the right form automatically.

### Step 4 — Handle prefab components

When the user supplies a ready-made PDF for a component, just drop it in — no wrapper needed:

1. Place the PDF as `<comp>/main.pdf` (e.g. `warmup/main.pdf`).
2. If the key is also a prefab PDF, place it as `<comp>_key/main.pdf`.

`shared/lesson.mk` discovers the component by its `main.pdf` and feeds it straight to
`pdfunite`, skipping compilation. Use `--prefab <comp>` when scaffolding to create the empty
drop-in directory.

### Step 5 — Build

Build from the lesson directory (or the unit/root for wider packets):

```bash
make -C unit03/lesson02 all       # all five products (this is the normal build)
make -C unit03/lesson02 plan      # the lesson plan          → lessonYY_plan.pdf
make -C unit03/lesson02 slides    # 3-up deck + notes column → lessonYY_slides.pdf
make -C unit03/lesson02 pptx      # projectable deck         → lessonYY_slides.pptx
make -C unit03/lesson02 student   # cover + blank components → lessonYY_student.pdf
make -C unit03/lesson02 key       # cover + key components   → lessonYY_key.pdf
make -C unit03/lesson02 check     # the convention gate — MUST pass before you report done
```

`make -C unit03 student|key` merges a unit; `make student|key` at the root merges the whole
curriculum (the plan and slide products stay per-lesson). Output lands in `target/compiled/`.
The build needs XeLaTeX, `latexmk`, `pdfunite`, and `pdfinfo`/`pdftoppm` (poppler) for the
pagination, handout, and PPTX passes; if a compile fails, surface the `.log` and fix the
offending `.tex` rather than editing the build system. Details and troubleshooting in
`references/build.md`.

**After building, run the gate — this is not optional.** `make all` exits 0 on a key that runs a
page longer than its blank, a two-page exit ticket, or `\ans` buried in math; `make check` is what
catches them. It builds first, reports every violation in one pass, and exits 1:

```bash
make -C unit03/lesson02 check
```

It enforces page parity per component, the one-page warm-up and exit ticket, `\ans` outside math,
no `teachernote` in a key, and no name row on a component. **`boxguard` is the one convention it
cannot see** — a stranded stub changes no page count — so also look at the built PDF. Details in
`references/conventions.md` ("The convention gate"). Unit tests and `finals/` are outside the gate
(it walks lesson dirs only) — but the conventions still bind a unit test: no `teachernote` in its
key, and its key paginates like its blank. Check those by hand.

### Step 6 — Update the course planning log (always do this last)

**Before you finish, record progress in `spec/course_planning.md`.** This is the running
handoff log that lets the next invocation — often in a fresh worktree after the Step 0 sync —
pick up exactly where this one left off. Do this at the **end of every execution of this
skill**, even a partial one; the user should never have to ask.

Update the file to reflect reality *now*:

- **Last updated** — today's date (absolute), and a one-line summary of what this run did.
- **Current state** — the unit/lesson build status: which units/lessons are scaffolded, which
  components are authored vs. still skeleton vs. built, and any confirmed lesson maps. Keep the
  per-unit progress table in sync with what actually exists on disk.
- **Next steps** — the concrete next actions (e.g. "author Unit 8 Lesson 8.2 notes + key",
  "confirm the Unit 9 lesson map with the user"), plus any open questions or decisions pending
  from the user.

Keep it terse and current — overwrite stale entries rather than appending a changelog. If the
file does not exist yet, create it with these sections. Since it lives in `spec/`, it is
tracked and travels with the branch, so the Step 0 sync always brings the latest state forward.

## Retrofit — converting a lesson to the gradual-release shape

Two older shapes exist in the tree, and `shared/lesson.mk` still merges both, so every such
lesson keeps building untouched. **Do not patch one in place** — when the user asks you to touch
it, ask whether to convert it instead. There is **no bulk sweep**; lessons are converted one at a
time as they come up.

**Converting an EFFL lesson** (it has `experience/`):

1. Create `notes/` + `notes_key/` and `activity/` + `activity_key/` (scaffold with
   `--components notes,activity`).
2. **Unfold the three EFFL parts.** QuickNotes becomes the spine of the **guided notes**, but
   expand it back into 4–6 taught sections with worked examples — a QuickNotes bullet is a
   summary, not a lesson. The EFFL Application becomes the notes' closing `practicebox`. The
   EFFL Activity's scenarios become the **group activity**, re-set in a
   *fresh context* so it does not repeat what the notes just worked.
3. Keep the homework; it needs no reshaping.
4. Delete `experience/` and `experience_key/`.
5. Rewrite the cover's packet table (four rows), the lesson plan (phase table, Hook, Lesson,
   Explicit Instruction, Active Monitoring, Group Work & Differentiation, **Debrief**,
   Reinforcement; four teacher notes — Warm-Up, Guided Notes, Group Activity, Homework), and the
   deck (hook → notes frames → activity launch → debrief → close & assign).

**Converting a pre-EFFL lesson** (it has `exit_ticket/`): the notes and activity are already the
right shape. Delete `exit_ticket/` + `exit_ticket_key/`, drop the Exit Ticket row from the cover
and its teacher note from the plan, replace the plan's *Individual Work & Assessment* box with a
**Debrief** box that folds the exit ticket's conceptual item in as a whole-class cold check, add
the *Lesson at a Glance* phase table, and re-time the notes to the 20-minute block — **trim if
they do not fit; do not let the phase table lie.**

**Build gotcha when deleting a component:** a stale stamp under `.stamps/unitXX/lessonYY/` makes
`make` skip recompiling a *sibling* whose PDF was cleaned, and `pdfunite` then fails on a missing
file. Remove `.stamps/<unit>/<lesson>` alongside `target/<unit>/<lesson>`.

## Reviewing or revising a lesson — the five conventions, in order

The conventions are in force from lesson 1.1 — the scaffolder emits namestripped skeletons,
`work`/`teachernote`/`boxguard` live in `saar-boxes.sty`, vocabpar is baked into the term macros,
and `make check` fails the build on four of the five. But a lesson can still drift, and the user
brings one forward by name:

> `/lesson-planning apply boxguard namestrip retrofit to 8.1 and 8.3`

Apply **only the conventions named** — all five if none are named — to the lessons named.

**Whenever you review or revise a lesson, execute the conventions in this order:**

> **1. teachernote → 2. namestrip → 3. work rule → 4. boxguard**

vocabpar is not a step here — it is structural, enforced by the term macros themselves. The first
three each change how much vertical space a component takes; **boxguard runs last because it
repairs the pagination the other three disturb**. Re-measure after each step — a "this guard costs
a page" verdict is only valid for the box heights it was measured against.

| # | Name | The rule | How to apply | Gated? |
| --- | --- | --- | --- | --- |
| — | **vocabpar** | `\par` before the first term in a `vocabbox` | **Nothing to do** — the term macros carry it | n/a |
| 1 | **teachernote** | Teacher prose in the lesson plan, one titled note per component — never in a `_key`. A unit test's rationale/scoring goes on p2 of `unitXX/unit_cover_key/` (key packet only) | `python3 .claude/skills/lesson-planning/scripts/movenotes.py unitNN/lessonMM` (`--check` to preview); test keys by hand | ✅ (lessons only) |
| 2 | **namestrip** | Name/date/period row on the cover (and tests) only | `python3 .claude/skills/lesson-planning/scripts/namestrip.py --project . --unit NN --lesson MM` (`--check` to preview) | ✅ |
| 3 | **work rule** | A component is the same length blank and keyed | `work` blocks authored byte-identically in both files; `\writelines{n}` only for prose `\ansline` drift | ✅ |
| 4 | **boxguard** | No box stranded as a ~1in sliver across a page break | `\boxguard` (or `\boxguard[n]`) on its own line before the `\begin{...}` — blank **and** key | ❌ **eyes only** |

Full spec for each: `references/conventions.md` ("The five conventions").

**There is no bulk sweep.** Retrofitting every lesson at once would re-flow the pagination of
every verified lesson; do them lesson-by-lesson as they are reviewed.

**Always finish with the evidence**, per lesson: `make -C unitXX/lessonYY all` exits 0 **and
`make -C unitXX/lessonYY check` exits 0**. The gate is the evidence for page parity and the
one-pagers — quote its output rather than re-deriving page counts by hand. Report any violation you
could not resolve and why, and confirm you eyeballed the PDF for stranded boxes (the one thing the
gate cannot see). Then Step 6.

## Authoring a course-wide final exam

When the user asks for a **final exam** / **cumulative assessment for the whole course**, follow
this workflow instead of the per-lesson one. It still bookends with Step 0 (sync + read the
planning log) and Step 6 (update the planning log). The unit `tests/` and `test_keys/` are the
**format model** — read the newest unit's `practice_test`, `actual_test`, and their keys first
and mirror their preamble, `\parthead` strips, box usage, and key style.

**1. Scaffold `finals/` by hand.** The `new_lesson.py` scaffolder does *not* create finals.
Make the four subdirectories and a standalone Makefile at the project root:

```bash
mkdir -p finals/practice_final finals/practice_final_key finals/final finals/final_key
```

Write `finals/Makefile` (it mirrors `shared/tests.mk` but is self-contained, globs `*/main.tex`,
compiles each to `target/finals/<name>/main.pdf`, and has **no** `drop`/publish step):

```make
# finals/Makefile — build the cumulative course final exam.
PROJECT_ROOT := $(abspath ..)
TEXINPUTS    := $(PROJECT_ROOT)/shared//:
PDF_DIR      := $(PROJECT_ROOT)/target/finals
LATEXFLAGS   := -xelatex -interaction=nonstopmode -halt-on-error -file-line-error

FINALS := $(patsubst %/main.tex,%,$(wildcard */main.tex))

.PHONY: all clean $(FINALS)
all: $(FINALS)
$(FINALS):
	@mkdir -p $(PDF_DIR)/$@
	cd $@ && TEXINPUTS="$(TEXINPUTS)" latexmk $(LATEXFLAGS) -outdir="$(PDF_DIR)/$@" main.tex
	@echo "OK  final -> target/finals/$@/main.pdf"
clean:
	rm -rf $(PDF_DIR)
```

Unless the user says otherwise, **do not** create `sample_final*` drop-in dirs or PDFs — the
final is standalone and merged into no packet. (Don't add `finals` to any unit/root packet
Makefile in `shared/`.)

**2. Design the blueprint — genuinely cumulative.** Sweep every unit's `practice_test` Part A
vocab and Part C spines so the final samples the whole course, roughly evenly. **Balance the
statistical strand against the algebraic one**, and do not let the last units, which are
freshest, crowd out the early ones. The proven shape (50 questions / 100 pts) is four parts,
mirroring the unit tests:

| Part | Items | Pts | Coverage rule |
|---|---|---|---|
| A — Vocabulary (two matching sets) | 16 | 16 | one set per strand of the course |
| B — Multiple Choice | 12 | 24 | ~1 concept check per unit |
| C — Short Answer & Computation | 16 | 48 | **at least one computational item per unit**, weighted toward the heaviest standards |
| D — Extended Response | 6 | 12 | cross-unit **synthesis** — items that make a student pull an idea from one unit into another and justify the choice |

Scale the counts to the course, but keep Part C's per-unit spine — it is what makes the exam
cumulative. Reuse the unit tests' already-hand-verified numeric spines where you can.

**3. Author the four files, blank-and-key in lockstep.** Same invariants as any component:
blanks use `\usepackage{saar-boxes}`, keys swap in `\usepackage{saar-key}` and wrap every
answer in `\ans{...}`. Define in each preamble every math macro the body uses (a local
`\parthead`, plus whatever the course's notation needs). Give the keys `teachernote` blocks with the vocab
answer-letter summary, per-item MC rationale, and Part C/D scoring. Practice and actual are
parallel forms — **different numbers and reshuffled vocab letters**, same structure.

**4. Verify all arithmetic in pure Python before authoring**, for *both* forms — every summary
statistic, regression coefficient, probability, and algebraic solution the exam asserts. This is
non-negotiable, exactly as for unit tests. Check any item with a known edge or ambiguous case
explicitly.

**5. Build and QA.** `make -C finals all`. Then scan all four logs for `^!`/file-line errors,
grep for `\ans` inside `$...$` (must be zero), check overfull `\hbox > 15pt` (the standard
pageheader banner ~10.8pt is fine), and page-count each PDF with `pdftoppm`. Visually spot-check
at least one page of each **key** to confirm red answers render with no tofu.

**6. Update the planning log** (Step 6) noting the `finals/` deliverable, the blueprint, and both
forms' Part C spines, so a later run can reproduce or revise it.

## Reference files

- `references/conventions.md` — the style packages, every box environment, the fill-in and
  answer-key macros, the cerulean/gold color palette, per-document-type preambles, and **the five
  conventions** (vocabpar, teachernote, namestrip, work rule, boxguard). Read before authoring.
- `references/components.md` — section-by-section spec and a skeleton for the lesson plan and
  each component + key.
- `references/course-workflow.md` — decomposing `spec/statistical_analysis_algebraic_reasoning.md` into units
  and lessons, the unit map, the content-mapping table, and the sketching/technology rule.
- `references/build.md` — the Makefile hierarchy, scaffolding, prefab PDFs, build commands,
  and troubleshooting.

## Guardrails

- **Bookend every run with the planning log:** read `spec/course_planning.md` at the start
  (Step 0) and update its current-state + next-steps at the end (Step 6). Never skip the
  end-of-run update, even for a partial run.
- **Full `Read` each skeleton before writing it** (Step 3). A `bash`/`cat` dump does not
  register the file with the editor, so the write fails; always use the `Read` tool first.
- Structure comes from `spec/statistical_analysis_algebraic_reasoning.md` and
  `spec/unit_lesson_breakdown.md`; content comes from the **standards
  documents in `spec/`** — read the matching "Understanding the Standards" pages for scope
  before authoring. Don't invent scope the standard does not carry.
- **Cite the standard codes** in every lesson plan (Priority Ideas box and Connections line).
- Audience is secondary school, mid-track: context first, small numbers, one new idea at a time,
  heavy scaffolding.
- **Every new lesson is gradual release:** `cover`, `warmup`, `notes` (guided notes +
  practice), `activity` (one whole-class group activity), `homework` (scored), `slides`. The **debrief is a
  phase, not a component**, and there is **no exit ticket**. Never author `experience` or
  `exit_ticket` into a new lesson; when an older lesson needs work, ask whether to convert it
  (see "Retrofit").
- **Mirror lessons 1.0 and 1.1.** A lesson with `experience/` is the scrapped EFFL shape; one
  with `exit_ticket/` predates the current design. Neither is the model.
- **There is no spoiler rule** — name the vocabulary on the cover, in the notes, and on the
  slides. **Obey the timebox rule:** notes ≤4pp / 20 min with a per-section minute budget that
  sums to 20; activity ≤2pp / 18 min.
- **Every plan carries a *Lesson at a Glance* phase table** — 5 / 20 / 18 / 7 / 5.
- **Homework is scored.** The cover's score column carries a `\blank{}` for it, never `NA`.
  Author the packet pages for every lesson; DeltaMath is the teacher's override at Close &
  Assign and does not change what you author.
- **Check page-for-page alignment, not just page counts.** `make check` compares totals only;
  a key can float a section onto an earlier page. Compare per-page headings between blank and
  key, and guard the first `notesbox` after the `vocabbox` with `\boxguard[20]` in both.
- Keep blank and key documents in lockstep — the key is the blank with answers filled in, and it
  must come out the **same number of pages**. Worked solutions live in shared `work` blocks (the
  work rule); a key that runs long costs the student packet a blank padding page.
- **Run `make check` after every build** and before reporting a lesson done — it is the gate for
  page parity, the one-page warm-up/exit ticket, `\ans`-in-math, `teachernote`-in-a-key, and
  namestrip. **It cannot see boxguard**, so look at the PDF too.
- **When reviewing or revising a lesson, run the conventions in order:** teachernote → namestrip →
  work rule → boxguard. Boxguard is always last — it repairs the pagination the other three
  disturb. vocabpar is structural and is not a step. See "Reviewing or revising a lesson."
- A **course final** is the `finals/` deliverable (four flat subdirs + a standalone Makefile,
  no `sample_*` drops); build it via `make -C finals all`. See "Authoring a course-wide final
  exam." Verify all arithmetic in Python for both the practice and actual forms before authoring.
- This is a modeling and applications course: context first, compute *then* interpret and
  justify. **No "sketch from a blank page" questions** — pre-draw and pre-scale the axes, even
  where the standard says "sketch."
- Only the cerulean/gold palette colors are defined. `royal`, `mist`, `burgundy`, `navy`, and
  `sky` are **not** — translate any material pasted in from another course.
- Don't modify `shared/` or the Makefiles to make a lesson build; fix the lesson's `.tex`.
