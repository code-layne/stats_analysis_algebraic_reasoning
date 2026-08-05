---
name: lesson-planning
description: >-
  Author complete, build-ready lessons for the Statistical Analysis & Algebraic Reasoning LaTeX
  curriculum (a project with a shared/ style package — prefix saar — and a Makefile hierarchy
  that compiles components with latexmk and merges them with pdfunite).
  Use this whenever the user wants to create, draft, or build a lesson, a lesson plan, a
  unit, or any lesson component — warm-up, guided notes, activity, exit ticket, homework,
  cover sheet, or their answer keys. The course will be defined by
  spec/statistical_analysis_algebraic_reasoning.md and the standards documents in spec/; units are
  standard clusters and lessons are groups of the standards' lettered Knowledge & Skills.
  Trigger this even when the user just says "make lesson 2.3" or
  "I need a warm-up and key for tomorrow," and even if they don't say "skill" or "LaTeX." Also
  use it to author unit-level tests and a cumulative, course-wide final exam (the `finals/`
  deliverable) — any "final," "final exam," or "cumulative assessment" for the whole course.
---

# Lesson Planning — Statistical Analysis & Algebraic Reasoning

This skill authors lessons for the **Statistical Analysis & Algebraic Reasoning** course and
produces print-ready PDFs through the project's own build system. **It builds around the
project's conventions — it does not invent its own.** The course is a **modeling- and
applications-first** secondary course pairing statistical work with algebraic reasoning. Author
every component in that spirit: start from a context, compute, then **interpret and justify** —
and cite the standard codes the lesson covers.

> **The course is not mapped yet.** `spec/` holds the source standards PDFs and nothing else —
> there is no `spec/statistical_analysis_algebraic_reasoning.md`, no unit map, and no built
> lesson. The build system, the style packages, and the five conventions are all in place and
> ready. **Do not infer a unit/lesson map on your own** — propose one, confirm it with the user,
> and write it into that spec file (see `references/course-workflow.md`).

## The course at a glance

- **Structure** will come from `spec/statistical_analysis_algebraic_reasoning.md` — the guiding
  philosophy and the **course map**: one unit per standard cluster, each lesson grouping a
  standard's lettered Knowledge & Skills. **That file does not exist yet**; writing it (with the
  user) is the first real course-planning task.
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
  `cover`, `warmup`, `notes`, `activity`, `exit_ticket`, `homework`, and optional `slides`.
- An **answer key** for each keyed component, as a *separate* sibling directory:
  `warmup_key`, `notes_key`, `activity_key`, `exit_ticket_key`, `homework_key`.
  (`cover` has no key.)

`shared/lesson.mk` discovers a component if it has a `main.tex` **or** a `main.pdf` and
compiles the `main.tex` ones with `latexmk -xelatex`; a prefab `main.pdf` is used as-is from
the source tree with no compile step (Step 4). It then builds **five work products** into
`target/compiled/unitXX/`:

| Product | Contents |
|---|---|
| `lessonYY_plan.pdf` | the lesson plan (the lesson-root `main.tex`), on its own |
| `lessonYY_slides.pdf` | the Beamer deck **printed** — 3 slides per page, each with a ruled notes column beside it |
| `lessonYY_slides.pptx` | the same deck wrapped for PowerPoint (one full-page image per slide) — the **projected** form |
| `lessonYY_student.pdf` | cover + the **blank** warmup, notes, activity, exit ticket, homework, in that order |
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
5. **Find a model lesson — or recognize there isn't one yet.** If a built lesson already
   exists, open it and mirror its preamble, box usage, and tone. **This is a greenfield
   course**: if no lesson exists yet, `references/conventions.md` and
   `references/components.md` are your reference, and the *first* lesson you author becomes
   the model for the rest — build and proofread it carefully before scaling out.

### Step 1 — Map the unit into lessons, then gather the lesson's content

The content path is always `references/course-workflow.md`:

- **Decompose the unit into lessons** from `spec/statistical_analysis_algebraic_reasoning.md`
  (once it exists — until then the course map itself is the thing to settle with the user). The
  convention is **one lesson per Knowledge-and-Skills cluster** — group the standard's lettered
  bullets into coherent 55-minute chunks, in listed order (Lesson `<unit>.<n>`). Present the
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
  --title "<Lesson Title>" --unit-title "<Unit Title>" \
  --components cover,warmup,notes,activity,exit_ticket,homework,slides
```

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
  `\usepackage{saar-article}` + `\usepackage{saar-boxes}`.
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
- Structure comes from `spec/statistical_analysis_algebraic_reasoning.md` (**not written yet** —
  settle the course map with the user, never infer it); content comes from the **standards
  documents in `spec/`** — read the matching "Understanding the Standards" pages for scope
  before authoring. Don't invent scope the standard does not carry.
- **Cite the standard codes** in every lesson plan (Priority Ideas box and Connections line).
- Audience is secondary school, mid-track: context first, small numbers, one new idea at a time,
  heavy scaffolding.
- Greenfield: there may be no existing lesson to mirror; lean on the reference docs and make
  the first lesson a clean model.
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
