---
course: Statistical Analysis \& Algebraic Reasoning
prefix: saar
meeting_length: 60
reference_lesson: unit01/lesson01
components: [cover, warmup, notes, homework, slides]
keyed: [warmup, notes, homework]
one_page: [warmup]
doc_titles:
  warmup: Warm-Up
  notes: Guided Notes
  homework: Homework
  activity: Group Activity
  experience: Experience \& Formalize
  exit_ticket: Exit Ticket
note_labels:
  warmup: Warm-Up
  notes: Guided Notes
  homework: Homework
skeletons: templates/lesson
unit_tests: true
structure_source: standards
spec_dir: spec
course_index: spec/course_planning.md
check_target: true
point_size: 10
---

# Lesson Shape — Statistical Analysis & Algebraic Reasoning

This is the course profile the shared `lesson-planning` skill (`~/.claude/skills/lesson-planning/`)
reads before authoring anything. The skill carries the mechanism — build, LaTeX rules, workflow,
scripts; **this file carries the policy** — everything true of this course that is not
necessarily true of the others. Keep it current: when a convention changes, change it here first.
The frontmatter is machine-read by the scaffolder; the sections below are read by the skill at
Step 0. The skeletons, the per-component spec (`components.md`), and the standards-to-lesson
workflow (`course-workflow.md`) live in `templates/lesson/`.

## 1. The lesson shape

**This is a modeling- and applications-first secondary course** pairing statistical work with
algebraic reasoning, for a mid-track audience that has finished Algebra 1. Every component runs
the loop **compute → interpret → justify** ("what does this number mean here, and how do you
know?"): start from a context, compute, then interpret and justify — and cite the standard codes
the lesson covers. Scaffold heavily: a context first, small numbers, one new idea at a time, worked
examples, vocabulary support. Technology is assumed but pre-digested — calculator, Desmos, or
spreadsheet output is shown as a **pre-made figure to read**, and keystrokes belong in the We Do
(teacher driving) or the homework, never in the solo practice box.

**Every new lesson follows the gradual-release model, and the guided notes carry all of it** —
*I work one, we work one, you work some*. The teacher hooks the class, builds the ideas in the
**guided notes** with a class-filled vocabulary box and **4–6 numbered sections the teacher models**
(*I do*), works **one designated We Do example** jointly with the class (*we do*), then releases the
notes' **closing `practicebox` of 1–3 items students work silently and alone** for 10 minutes
(*you do*); a teacher-led **debrief** closes the loop and is the formative check.

| Phase | Minutes | Component |
| --- | --- | --- |
| Warm-Up | 5 | `warmup` |
| Guided Notes — I do (4–6 modeled sections) + We Do (one joint example) | 30 | `notes` |
| Independent Practice — the notes' closing `practicebox`, silently and alone | 10 | `notes` (its last box) |
| Debrief — whole class, teacher-led, walks the practice work | 7 | — (in the plan and the deck only) |
| Close & Assign | 3 | `homework` announced |

**Meeting-length discrepancy — flagged, not resolved.** `\MeetingLength` in
`shared/saar-article.sty` prints **60 minutes** (so `meeting_length` above is 60 and the plan's
*Lesson at a Glance* header reads "60 minutes"), but the user-confirmed phase table above sums to
**55**, and so did the earlier 5/20/18/7/5 split — the mismatch predates both redesigns. The old
skill described "the 55-minute period" while the style package says 60. **Author the phase table
as 5 / 30 / 10 / 7 / 3 exactly; do not stretch a phase to make the minutes reach 60, and do not
edit `shared/`.** The five unallocated minutes are passing/transition until the user decides
whether to set `\MeetingLength` to 55 or add a transition row to the table. Ask before doing
either.

**The release runs once per lesson, not once per section.** The numbered teaching sections are
the *I do* — the teacher holds the pen throughout, and their blanks are recording points, not
independent problems. **One designated We Do** follows them: the last numbered `notesbox`, worked
jointly, running the **same task the practice box will release, on different data**, with full
`work` space (budget 6–8 of the 30 minutes). Then the **single** closing `practicebox` is the
*you do*: **1–3 items, 10 minutes, worked silently and alone** — three is the ceiling, not the
target; an item needing more than ~3 minutes alone belongs in the homework; item 1 is the on-ramp
(startable within thirty seconds), the last item carries a *second instance of the lesson's trap*;
pre-work heavy arithmetic in a `work` block so the release is spent on classification and the
interpret-in-context sentence, which is what the debrief walks. Do not add a second practice box,
and do not release items inside the numbered sections. **The timebox rule:** the plan's Lesson box
carries a per-section minute budget that sums to 30 through the We Do; the notes run **≤ 6 pages**
blank and key; a part that runs over is cut or moved to the homework, never carried.

**Sequence the sections so the crux is earned, not announced:** set up the misconception, take a
vote or a commitment, *do not settle it*, then settle it in the crux section with a correct
computation that produces a worthless answer. Reuse one data set across several sections rather
than introducing a new one each time; the We Do runs on the notes' own data, the practice box on
a fresh study in the same setting is fine.

**The components:**

- **`cover`** — full-bleed cerulean banner, `\namedateperiod` (the one place it appears),
  `learningtargetbox` of "I can…" targets **naming the formal vocabulary outright**, a `tocbox`
  packet table of **three rows** (Warm-Up · Guided Notes · Homework — the independent practice
  has no handout of its own, so no row; it is named inside the Guided Notes description), every
  score cell a `\blank{1.2cm}`, and a `remindbox` *Keep in Mind* carrying the lesson's **content
  takeaway** — the rule, the test to apply, the trap to avoid, in the formal vocabulary — never
  the lesson's process. Standard codes stay off the cover.
- **`warmup`** — 3–5 spiral items on *prerequisite* skills, **exactly one page** blank and key,
  often a prefab PDF. Each item is a **tool the notes pick up again**; the plan's spiral-review box
  names which section reuses it. Lesson 1.1's enlarged sizing (`\large` body, `\workrowsep` 50pt,
  item spacing 22pt) is the model for handwriting room that still fits the page.
- **`notes`** — *the lesson*: `\pageheader{…}{Guided Notes}` → `objectivebox` (**filled in, not
  blank**, worded exactly as the cover's targets; the key carries identical text) → `vocabbox` of
  `\termblanklong{Term}` per term (key: `\vocabans{Term}{definition}`) → `hookbox` with
  `\writelines{2}` (leave the hook *unresolved* when it plants the crux) → 4–6 numbered
  `notesbox{N. Title}` sections → `notesbox{N. We Do --- <task>}` → closing `practicebox` →
  optionally one `extensionbox`. Number the sections in the text so the plan and deck can refer
  to them.
- **`homework`** — authored for **every** lesson, 1–2 pages: ~6 items in **new contexts**
  spanning the lesson's lettered skills — the core procedure, a **deliberate contrast pair** (same
  task, opposite condition — the pair that surfaces the target misconception), an
  interpret-in-context item, a justification item — plus **one spiral item** reaching back, an
  optional `extensionbox`, and a closing `spiralbox` previewing the next lesson. Every answer is
  phrased in its context.
- **`slides`** — the required Beamer deck, ~12 frames: title → learning targets → warm-up → hook →
  **one frame per numbered notes section** (crux frame flagged `\sectionlabel[redacc]{}`) → **We
  Do, a live surface left un-answered** → **independent-practice launch carrying only the item
  range, the 10 minutes, and the rule** (never the items or their answers) → debrief → close &
  assign (what changed today; the assignment and plainly which form — packet pages or a named
  Desmos activity; due date; how scored).

**There is no spoiler rule.** The vocabulary is taught, not discovered: the cover, the warm-up,
the notes' `vocabbox`, and every slide may name the formal terms outright. Say the word, define
it, then use it.

**What this course does not have — do not re-add any of it:**

- **No group activity, no group work at all.** No groups of three, no tiers, no `activity/`
  component. The release is individual. Differentiate by **depth inside the practice box** (1–3
  items ramping to the crux, plus an optional `extensionbox`), never with Tier R / Tier A / Tier E
  boxes.
- **No exit ticket.** The debrief's whole-class cold check — run while students correct their own
  work in a second color — is the formative read; it sorts responses into three piles that decide
  how the next lesson opens.
- **The debrief is not a component**, and **independent practice is a phase with a page, not a
  component**: neither gets a directory, and neither gets a cover row.
- **No 12pt component and no `\answerspace`.** Both died with EFFL; every component is 10pt and
  answer space is `\writeline` / `\writelines{n}` / `\blank{}` (section 4).
- **No per-section I-do/we-do/you-do mini-cycles, no second practice box.**
- **The extension block is an open question.** Lesson 1.1's `extensionbox`es were removed on
  request (2026-08-31) and its plan sends early finishers back to check their conclusions;
  `components.md` still lists an optional `extensionbox`. **Ask before authoring the next lesson**
  whether it is gone course-wide or 1.1 is the exception.

**History.** An "experience first, formalize later" (EFFL) trial ran 2026-08-29 → 2026-08-31 with a
single 12pt `experience/` component (Activity · QuickNotes · Application) in place of notes and
activity; students rejected it. Gradual release was restored 2026-08-31 with a separate 18-minute
**group activity** (`activity/`), and that activity was **dropped the same day** in favor of
individual release inside the notes. The current shape is the notes-only gradual release above.

**`unit01/lesson01` is the reference implementation** (converted 2026-08-31, revised from
classroom feedback the same day). Mirror its preamble, box usage, pacing, and tone; the live
lesson overrides every document, this one included. **Lesson 1.0 is not a model** — it still
carries `activity/`. A lesson is current only when it has `notes/` and **none of** `activity/`,
`experience/`, or `exit_ticket/`, and its plan's *Lesson at a Glance* reads 5 / 30 / 10 / 7 / 3.

## 2. Grading and homework policy

- **Every score cell on the cover is a `\blank{}`** — Warm-Up, Guided Notes, and Homework rows
  plus the Total. Nothing prints `NA`.
- **Homework is authored for every lesson, and it is scored.** ~6 items in new contexts, each
  ending in an interpretation or a justification. Algebra 2 dropped homework entirely and AP
  Statistics keeps a separate unscored in-class practice set — **copy neither.** Scoring guidance
  goes in the plan's `\begin{teachernote}[Homework]`, never in the key.
- **Packet or Desmos is a per-lesson teacher decision, made at Close & Assign.** The packet pages
  are authored either way and are the default. **Desmos Classroom's coverage of this course's
  standards is uneven** — stronger on function modeling and regression, thinner on inference and
  study design — so it is checked lesson by lesson and never assumed. When a Desmos activity
  carries the lesson's skills, it replaces the assignment and students keep the packet pages as a
  worked reference. Nothing about what you author changes: the plan's Reinforcement box and the
  deck's closing frame say which form the assignment takes (naming the specific Desmos activity
  when that is the call); the cover row and its score cell never change. (Desmos replaced
  DeltaMath as the override on 2026-08-31 — do not write DeltaMath anywhere.)
- **No course-wide due-date rule.** The plan's Reinforcement box and the deck's closing frame
  state, per lesson, how the homework is scored and when it is due.
- The independent practice has no cover row and no score cell of its own — it is part of the
  Guided Notes row, because it has no separate handout.

## 3. Where structure comes from

**Structure** comes from **`spec/statistical_analysis_algebraic_reasoning.md`** — the design
notes and the **confirmed course map** (approved 2026-08-05): 8 units, 58 content lessons plus one
**Lesson 0** per unit (a unit-launch lesson — hook context, vocabulary preview, prerequisite
review — that sits outside the eight-content-lesson cap), **66 lesson directories** in all;
semester split after Unit 4 (S1 *data and chance*, S2 *models and decisions*); projects with real
data in Units 1, 5, 6, and 8 (lessons 1.8, 5.7, 6.8, 8.6). Units are standard clusters; lessons
are groups of a standard's lettered Knowledge & Skills. **AFDA.AF.3 (linear programming) is
excluded; there is no trigonometry.** `spec/unit_lesson_breakdown.md` is the per-lesson index and
status table (it still describes the EFFL component set — two redesigns stale; fix it on the next
run that touches it).

**Content** comes from the **standards documents in `spec/`**: the approved 2023 SOL PDFs
(**PS.\*** primary; **AFDA.\*** for function families, the data cycle, probability, the normal
distribution; **A2.\*** cited only where the course exceeds AFDA) give the standard text and its
**lettered Knowledge & Skills** — the codes a lesson cites; the **"Understanding the Standards"**
PDFs give the scope limits, notation, and what is out of bounds — **read the matching pages before
authoring anything.** The standard says *what*; this says *how far*. Do not invent scope the
standard does not carry.

**One lesson per Knowledge-and-Skills cluster**, not per lettered bullet — group the letters into
coherent 60-minute chunks in listed order; lesson id `<unit>.<n>`. **Present the proposed lesson
map for the unit and confirm it with the user before authoring** — bullets merge and split
depending on the class. The content-mapping table (which standard element feeds which lesson
element), the technology rule, and the pre-drawn-axes rule are in
`templates/lesson/course-workflow.md`; the skill's `references/standards-workflow.md` is the
generic path this course follows.

**Every lesson cites its standard codes** — in the plan's Primary Objective box, its Priority
Ideas & Skills box, and its Connections line. That is the accountability spine of a
standards-driven course.

**The planning log — `spec/course_planning.md` — bookends every run.** Read it at Step 0 (after
this file): it records the current build state, which lessons are in which shape, the confirmed
lesson maps, the open questions for the user, and the gotchas found so far. **Update it at the end
of every run, even a partial one**, so the next invocation — often a fresh worktree after the
sync — picks up exactly where this one left off: **Last updated** (today's absolute date plus a
one-line summary of the run), **Current state** (per-unit/per-lesson build status kept in sync
with what is on disk; which components are authored vs skeleton vs built; confirmed maps), and
**Next steps** (the concrete next actions and any decisions pending from the user). Keep it terse
and current — overwrite stale entries rather than appending a changelog. Also keep the status
column of `spec/unit_lesson_breakdown.md` in sync when a lesson lands.

## 4. Style notes

- **Prefix `saar`** — `shared/saar-{colors,article,boxes,key,beamer}.sty`, ported from
  Algebra/Trig/Data Analysis on 2026-08-05 (which took them from Linear Algebra, and before that
  Algebra 2). Any style file copied in from another course must have its
  `\ProvidesPackage`/`\RequirePackage` names changed to `saar-*` and its colors to this palette
  before use.
- **Course macros live in the style package.** `saar-article.sty` defines `\CourseName`
  (*Statistical Analysis \& Algebraic Reasoning* — covers and title slides), `\CourseHeaderName`
  (*Stat Analysis \& Algebraic Reasoning* — the short form `\pageheader` prints so the banner and
  the lesson id fit on one line), and `\MeetingLength` (*60 minutes* — see the flag in section 1).
  A lesson plan defines only `\UnitNumberName` and `\LessonNumberName`, and loads `graphicx`
  itself (`-article` does not). **There is deliberately no `\SchoolYear` macro — no year on any
  document.** These materials are reused year over year; the plan's title block is `\CourseName`
  alone. Do not reintroduce one.
- **Every component is 10pt** — cover, warm-up, notes, homework, tests, and the plan alike:
  `\documentclass[10pt]{article}` + `saar-article` + `saar-boxes` (cover also `ltablex` +
  `\keepXColumns`). That is the frontmatter's `point_size: 10` — most sibling courses are 12pt;
  the only 12pt document this course ever had was EFFL's `experience/`, which is retired.
  `\boxguard` counts were tuned at 10pt (default 16; ~20 after a `vocabbox`; 30 before a box
  opening with an unbreakable TikZ/pgfplots figure or `tabularx`).
- **Palette — cerulean with gold accents** (`cerulean` #0B6FA4 is the dominant color, the third
  blue across the stats-family courses, separated by hue so it survives a photocopy; the deck
  overrides it to a brighter #1785BF). Defined: `cerulean ceruleanlight frost frostmid charcoal
  slate linegray graybg goldacc goldbg hookbg greenacc greenbg redacc redbg plumacc plumbg keyred`
  plus the lesson-plan background aliases `frostbox goldbox greenbox redbox plumbox`. **Undefined
  here — translate any material pasted in from another course:** `royal`, `royallight`, `mist`,
  `mistmid`, `bluebox`, `\royalheader` (renamed tree-wide 2026-08-05, no deprecated aliases —
  a stale name fails loudly), `burgundy`, `navy`, `navylight`, `sky`, `skymid`, and Algebra 2's
  whole `forest` family. Mapping when porting: `royal`/`navy`/`forest` → `cerulean`,
  `mist`/`sky`/`forestbg` → `frost`, `mistmid`/`skymid` → `frostmid`. `keyred` is the answer color;
  `practicebox` is deliberately plum, not blue; `graybg` is the teachernote background.
- **This course HAS `fixedskillbox`** (AP Statistics does not): `\begin{fixedskillbox}[Title]{color}`
  never splits — use it where a lesson-plan `tabularx` must stay intact on one page (*Lesson at a
  Glance*, *Activate Prior Knowledge & Spiral Review*); use breakable `skillbox[Title]{color}` +
  `\boxguard` everywhere else. Lesson-plan boxes take the background as the **last** argument
  (`goldbox`, `greenbox`, `redbox`, or a palette color such as `frost`); the frame is cerulean by
  default.
- **Box catalog** (`saar-boxes.sty`): `objectivebox` ("Primary Objective"), `learningtargetbox`
  ("Learning Targets — I Can…", cover), `vocabbox` ("Vocabulary & Key Concepts"), `hookbox`
  ("Hook"), `notesbox{Title}`, `practicebox` (**no argument** — title fixed as "Guided Practice";
  a titled box is `notesbox{Title}`), `spiralbox` ("Connections & Big Ideas"),
  `scenariobox[Title]{color}`, `headlinebox{color}` (callout strip; the tests' `\parthead` wraps
  it), `blurbbox[Title]{color}`, `reflectionbox` ("Reflection" — exists, but the current shape has
  no use for it), `extensionbox` ("Extension — optional"), `tocbox` ("What's in This Packet",
  cover), `remindbox` ("Keep in Mind", cover), `teachernote[Title]` (plan only), and `work` (**no
  argument**; body is an amsmath `aligned` — one statement per line, `&` immediately before the
  relation; `\workrowsep` adds leading and moves blank and key together). `\tierbox` and
  `\componenttable` do not exist here.
- **Key macros (`saar-key.sty`): `\ans{}`, `\ansline{}`, and `\vocabans{Term}{definition}`.**
  **`\termans` is undefined in this course** — the shared skill's `\termblank` ↔ `\termans` pair is
  `\termblanklong{Term}` (bold cerulean term + two write-lines) ↔ `\vocabans{Term}{def}` here;
  `\termblank{Term}` (term + inline blank + one write-line) also exists in the blank. **vocabpar is
  automatic**: `\termblank`, `\termblanklong`, and `\vocabans` each open with their own `\par`, so
  write the vocab intro sentence plainly and **do not add `\par\vspace{2pt}`** — it double-spaces
  the box. Treat the term macros as frozen.
- **`\writelines{n}` occupies n+1 line slots here** (it still ends in `\\`; the upstream fix the
  shared conventions describe was never ported), so raising one is not free — re-measure the
  blank. **A `\writeline` / `\writelines{n}` / `\ansline` opening on its own source line still
  continues the paragraph**, rendering the first rule as a stub at the end of the prompt: author
  it as **`\par\writeline`**, and in a key put the `\par` on only the *first* `\ansline` of a
  consecutive run, or the key grows taller than its blank.
- **`\answerspace` is gone.** It was EFFL's macro (12pt, open white space instead of rules) and
  survives only in `templates/lesson/experience*.tex` and the untouched `experience/` skeletons of
  units 2–8. Leave it alone there; never introduce it into a new component.
- **Page-for-page alignment beyond the gate.** The key's `\vocabans{}` runs shorter than the
  blank's `\termblanklong{}` rules, so the first `notesbox` after the `vocabbox` floats onto page 1
  in the key only, and every section thereafter is a page early with the totals unchanged. **Guard
  the first `notesbox` after the `vocabbox` with `\boxguard[20]` in both files** and **verify by
  comparing per-page headings**, not page counts. `\boxguard` is inert inside a breakable
  `tcolorbox` — to force a split inside one, mirror tcolorbox's `\tcbbreak` in blank and key.
  Never let a lead-in sentence be orphaned from the table it introduces (`\nopagebreak`). A tall
  table closing the last box strands a page; splitting a long box (e.g. `notesbox{Practice}` /
  `notesbox{Practice, continued}`) is how the homework aligns.
- **Authoring traps found in 1.1's classroom revision:** a list with a wide custom `label=`
  needs `leftmargin=*, labelindent=0pt, align=left, labelsep=0.6em` or the label hangs outside a
  `scenariobox` border; set tables at `\linewidth` (not `0.92\linewidth` inside a `center`) and
  widen answer blanks to the column; use `>{\raggedright\arraybackslash}X` to stop hyphenation in
  a narrow reason column; give practice items spaced lines (`\par\vspace{6pt}`) rather than
  pressing Variable / Type / How-do-you-know together.
- **Beamer:** `\documentclass[aspectratio=169,11pt]{beamer}` + `saar-beamer`, which provides
  `\ceruleanheader{Title}` and `\sectionlabel[color]{LABEL}`. `\CourseName` is **not** defined in
  beamer (`saar-beamer` does not load `saar-article`) — write the course name literally.
  `saar-beamer` does not load `tcolorbox` — use beamer's `\begin{block}{}`; beamer's `itemize` does
  not accept `[leftmargin=…]` — use `\setlength{\itemsep}{…}`.
- `\TallMath{…}` for tall inline math is defined per document (the skeletons include it).
  `\namedateperiod` on the cover and the unit tests/finals only; `\namepartnerperiod` is unused.

## 5. Lesson-plan section order

Title block (`\CourseName` + `\UnitNumberName \LessonNumberName` — no year) → **Primary Objective**
(frost/cerulean `tcolorbox`; one or two sentences in student terms — do, interpret, justify — plus
the **Standards** line with the lettered codes) → **Priority Ideas & Skills** (`skillbox{goldbox}`,
two columns: the lettered skills in student language with their codes · *Key Understandings*, the
why, with the **target misconception named**) → **Vocabulary, Concepts & Theorems**
(`skillbox{greenbox}`, term/definition `tabularx`) → **Lesson at a Glance — `\MeetingLength`**
(`fixedskillbox{frost}`, Phase / Min / Students / Teacher, **5 / 30 / 10 / 7 / 3**; the table is a
contract — the Lesson box's minutes sum to 30 and the practice box is workable alone in 10) →
**Activate Prior Knowledge & Spiral Review** (`fixedskillbox{frost}`; which notes section picks each
warm-up item up again; `\includegraphics[page=1]{warmup/main}` **only** for a prefab warm-up) →
**Hook** (`skillbox{frost}`; what is on the board before anyone sits down; leave the crux
unresolved and name which section settles it) → **Lesson — Guided Notes (30 min)** (`skillbox{frost}`,
`multicols{2}`; one bold paragraph per numbered section, **each with its own minute budget**, the
last being the **We Do**; name which section *is* the lesson and which to compress) → **Explicit
Instruction: <the core move>** (`skillbox{frost}`; verbatim steps beside one worked example and a
contrast case) → **Active Monitoring** (`skillbox{redbox}`; misconceptions keyed to section *and*
practice-item numbers; the reasons-that-are-not-reasons to reject; cold-call prompts) →
**Independent Practice (10 min)** (`skillbox{redbox}`; **"silently and alone" said explicitly**;
the arc of the 1–3 items — on-ramp, crux; the two-minute check; circulation prompts keyed to
items; which work to collect, with permission, for the debrief — two *disagreeing* answers for the
crux) → **Debrief (7 min) — what goes on the board** (`skillbox{frost}`; the displayed practice
work in order while students correct in a second color; the whole-class cold check with its
correct answer — *this replaces the exit ticket*; the **formative read** into three piles and how
the next lesson opens from pile (b)) → **Reinforcement & Extension** (`skillbox{goldbox}`; the ~6
homework items and what each targets, scoring and due date, **packet or Desmos** with the activity
named, the optional extension, the next-lesson preview, and the **Connections & Big Ideas** line
carrying the standard codes) → **Teacher Notes, three of them in packet order:** `[Warm-Up]`,
`[Guided Notes]`, `[Homework]`. There is no note for the debrief or the independent practice — both
are fully specified in their own boxes. No *Group Work & Differentiation* box, no *Individual Work
& Assessment* box, no *Exit Ticket* anything.

## 6. Unit-level and course-level assessments

**Unit tests** — scaffolded automatically the first time a unit is created (`--tests` re-runs
idempotently, `--no-tests` skips). A unit holds `tests/` (`practice_test/`, `actual_test/`;
`include ../../shared/tests.mk`; its `drop` publishes the *practice* test to
`sample_test/main.pdf`), `test_keys/` (`practice_test_key/`, `actual_test_key/`; `drop` publishes
to `sample_test_key/main.pdf`), and the two `sample_test*` drop-in dirs `shared/unit.mk` merges
into the unit student / key packets. **The actual test and its key are never merged into any
packet.** Tests are taken in a testing setting, so they **keep `\namedateperiod`**, use
`\pageheader{Unit X: <Title>}{…}`, and are organized by `\parthead{Part …}` strips: **A Vocabulary
(matching) · B Multiple Choice · C Short Answer & Computation · D Extended Response** —
interpret-and-justify in D. Practice and actual are **parallel forms**: same blueprint and ideas,
different numbers and contexts, reshuffled vocabulary letters. Sample every lettered skill the
unit's lessons taught. **Unit 1's set is the template for units 2–8:** 14 / 16 / 40 / 30 points,
33 items, 6 pages, with `\setlength{\workrowsep}{5pt}` in every test preamble (identical in blank
and key) for handwriting room. The tests have no pedagogy in them and were untouched by both
redesigns. Build: `make -C unitXX/tests all && make -C unitXX/test_keys all` **before** the unit
packet, so the `sample_test` prefab exists when `unit.mk` merges it.

**The unit cover pair** — `unit_cover/` (student packet) and `unit_cover_key/` (key packet); both
wrappers `\input` one shared **`unit_cover/body.tex`** so page 1 cannot drift — edit the cover
there, never in a wrapper. Page 1: banner, overview, lesson table, big ideas — student-facing, no
scoring information. **Page 2 of `unit_cover_key/main.tex` is where a unit test's answer rationale
and Part D scoring live** (as `\begin{teachernote}[Practice Test --- Part B]` blocks under a
`headlinebox`), because the practice test rides in the *student* packet and its key must carry no
`teachernote` and paginate exactly like its blank. Keep it to one page — cover + notes is a single
double-sided sheet. A unit with no `unit_cover_key/` gets the plain cover in both packets. Unit 1's
pair (authored 2026-08-07) is the pattern.

**Tests are outside `make check`** (the gate walks `unitXX/lessonMM/` only). That is a limit of
the checker, not an exemption: a test key still carries no `teachernote` and still matches its
blank page for page — check both by hand. **Verify every number in pure Python before authoring**
any assessment, both forms.

**The course final — `finals/` — is not yet scaffolded** (wait until more units exist so it can
actually be cumulative). When the user asks for a **final exam** / **cumulative assessment**, this
replaces the per-lesson workflow (still bookended by Step 0 and the planning-log update). The newest
unit's `tests/` and `test_keys/` are the format model — read them first and mirror their preamble,
`\parthead` strips, box usage, and key style.

1. **Scaffold `finals/` by hand** — the scaffolder does not create finals. A top-level directory,
   sibling of the `unitXX/` dirs, with **four flat subdirectories** each holding a `main.tex`:
   `practice_final/` (blank study copy with the `remindbox` "this is a practice final" banner),
   `practice_final_key/`, `final/` (the real exam, plain *Instructions* line), `final_key/`.
   **No `sample_final*` drop-in dirs and no `drop`/publish step** — the final is a standalone
   deliverable merged into no packet. Do not add `finals` to `shared/root.mk` or `unit.mk`; it
   builds only via its own self-contained `finals/Makefile`, which globs `*/main.tex` and compiles
   each to `target/finals/<name>/main.pdf`:

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

   `make -C finals all` builds all four; `make -C finals clean` removes `target/finals`.
2. **Design a genuinely cumulative blueprint.** Sweep every unit's `practice_test` Part A vocab and
   Part C spines so the final samples the whole course roughly evenly; **balance the statistical
   strand against the algebraic one**, and do not let the freshest units crowd out the early ones.
   The proven shape (50 questions / 100 pts), mirroring the unit tests:

   | Part | Items | Pts | Coverage rule |
   | --- | --- | --- | --- |
   | A — Vocabulary (two matching sets) | 16 | 16 | one set per strand of the course |
   | B — Multiple Choice | 12 | 24 | ~1 concept check per unit |
   | C — Short Answer & Computation | 16 | 48 | **at least one computational item per unit**, weighted toward the heaviest standards |
   | D — Extended Response | 6 | 12 | cross-unit **synthesis** — pull an idea from one unit into another and justify the choice |

   Scale the counts to the course, but keep Part C's per-unit spine. Reuse the unit tests'
   hand-verified numeric spines where you can.
3. **Author the four files blank-and-key in lockstep** — blanks `saar-boxes`, keys `saar-key` with
   every answer in `\ans{}`; define every math macro the body uses in each preamble (a local
   `\parthead` plus the course's notation). **Final keys are the one exemption from the
   teachernote rule** — they are merged into no packet and have no cover, so their `teachernote`
   blocks (vocab answer-letter summary, per-item MC rationale, Part C/D scoring) stay in the key.
   Practice and actual are parallel forms: different numbers, reshuffled vocab letters, same
   structure.
4. **Verify all arithmetic in pure Python before authoring, for both forms** — every summary
   statistic, regression coefficient, probability, and algebraic solution; check any edge or
   ambiguous case explicitly. Non-negotiable, exactly as for unit tests.
5. **Build and QA.** `make -C finals all`; scan all four logs for `^!` / file-line errors; grep
   for `\ans` inside `$...$` (must be zero); check overfull `\hbox > 15pt` (the standard
   `\pageheader` banner's ~10.8pt is fine); page-count each PDF with `pdftoppm`; visually
   spot-check at least one page of each **key** so the red answers render with no tofu.
6. **Update the planning log** with the `finals/` deliverable, the blueprint, and both forms' Part
   C spines, so a later run can reproduce or revise it.

## 7. Legacy shapes and regeneration

Recognize the shape by the component directories:

| Shape | Has | Notes |
| --- | --- | --- |
| **current** (notes-only gradual release, 2026-08-31) | `notes/`, no `activity/` / `experience/` / `exit_ticket/`; plan reads 5 / 30 / 10 / 7 / 3 | `unit01/lesson01` — the target |
| **group-activity** (2026-08-31, morning) | `notes/` + `activity/`, no `exit_ticket/` | `unit01/lesson00` |
| **EFFL** (2026-08-29 → 31) | `experience/` (12pt, `\answerspace`), no `notes/` | units 02–08, empty skeletons |
| **pre-EFFL legacy** (2026-08-06) | `notes/` + `activity/` + `exit_ticket/`, Tier R / A / E boxes in the activity | `unit01/lesson02`–`lesson08` |

`shared/lesson.mk`'s `STUDENT_ORDER` (`cover warmup experience notes activity exit_ticket
homework`) was **deliberately left alone** — it merges the current set in the right order and
still merges the retired dirs, so every older lesson keeps building. The scaffolder still accepts
`activity`, `experience`, and `exit_ticket` by name (`--components …`) so an older lesson can be
patched, and `make check` still holds a legacy `exit_ticket` to one page. **Do not patch one in
place** — when asked to touch such a lesson, **ask whether to convert it** to the current shape.
**There is no bulk sweep**: converting every lesson at once would re-flow the pagination of every
verified lesson; convert one at a time as each comes up, and rebuild that lesson's unit packet.
Whatever the starting shape, the destination is `cover` + `warmup` + `notes` + `homework` +
`slides`, a 5 / 30 / 10 / 7 / 3 phase table, and the whole release inside the notes.

**From the group-activity shape** (1.0; 1.1's conversion is the worked example):

1. **Fold the activity into the notes — do not just delete it.** Its items are the raw material
   for expanding the notes from 20 minutes to 30: on-ramp items become worked examples inside the
   numbered sections, its **crux item becomes the We Do**, one or two later items become the
   closing `practicebox`, and the rest is cut or moved to the homework — an 18-minute group block
   becomes 10 minutes of solo work, so most of it does not survive. Material trimmed to reach the
   old 20-minute notes block goes back here (check the lesson's planning-log entry before
   inventing new content).
2. **Re-set what you keep in the notes' own context** — the activity used a fresh context for
   transfer; folded in, the point is release, so the We Do runs on the notes' data. Keeping the
   activity's context for the practice box is fine when it is the same setting, a different study.
3. `git rm -r activity activity_key`, **and delete `.stamps/unitXX/lessonYY` + `target/unitXX/lessonYY`.**
4. Keep the homework; it needs no reshaping. DeltaMath → Desmos everywhere it appears.
5. Rewrite the cover's packet table to **three rows**; the plan (phase table, *Lesson — Guided
   Notes (30 min)* with per-section minutes, **Independent Practice (10 min)** in place of *Group
   Work & Differentiation*, **Debrief** now walking the practice items, Reinforcement; **three**
   teacher notes — drop `[Group Activity]`); and the deck (hook → notes frames → We Do left
   un-answered → practice launch carrying only the item range and the rule → debrief → close).

**From the EFFL shape** (units 2–8 — empty skeletons, so nothing is lost; do it as part of
authoring each unit, never as a sweep):

1. Scaffold `notes` + `notes_key` into the existing lesson dir (`--components notes`; do **not**
   scaffold `activity`).
2. **Unfold the three EFFL parts.** QuickNotes becomes the spine of the guided notes, expanded
   back into 4–6 taught sections with worked examples (a QuickNotes bullet is a summary, not a
   lesson); the EFFL Activity's richest scenario becomes the **We Do**; the EFFL Application
   becomes the closing `practicebox`; remaining Activity scenarios are cut or moved to the
   homework.
3. Keep the homework; it needs no reshaping.
4. Delete `experience/` + `experience_key/` and the stale stamps/target dirs.
5. Rewrite the cover (three rows), the plan (phase table, Hook, Lesson, Explicit Instruction,
   Active Monitoring, **Independent Practice**, **Debrief**, Reinforcement; three teacher notes),
   and the deck.

**From the pre-EFFL legacy shape** (1.2–1.8, which carry both `exit_ticket/` and `activity/`):
delete `exit_ticket/` + `exit_ticket_key/` (and their stamps/target dirs); drop the Exit Ticket
cover row and its teacher note; replace the plan's *Individual Work & Assessment* box with a
**Debrief (7 min)** box that folds the exit ticket's conceptual item in as the whole-class cold
check; add the *Lesson at a Glance* table; then run the group-activity conversion above —
**the three tiers collapse into the We Do plus a 1–3 item practice box; cut, do not
concatenate.** Re-time the notes to the 30-minute block — expand or trim so they fit; do not let
the phase table lie.

Either way, a stale stamp under `.stamps/unitXX/lessonYY/` makes `make` skip recompiling a sibling
whose PDF was cleaned and `pdfunite` then fails on a missing file — remove the stamps with the
target dir. Finish with the evidence per lesson: `make -C unitXX/lessonYY all` **and**
`make -C unitXX/lessonYY check` exit 0, blank and key verified page-for-page by per-page heading,
the PDF eyeballed for stranded boxes, then the planning-log update.

**Scoreboard (2026-09):** 66 lesson directories. **1 current** (`unit01/lesson01`); **1
group-activity** (`unit01/lesson00`, authored and complete — the next highest-value conversion);
**7 pre-EFFL legacy** (`unit01/lesson02`–`lesson08`, authored, built, and gated in their old
shape); **57 EFFL** (units 02–08, empty skeletons). The five conventions are already clean
tree-wide: no live `\namedateperiod` off the cover, no live `teachernote` in any `_key`, and every
lesson has a deck — the shape conversions are what remain. Unit 1's assessments and cover pair are
complete; units 2–8 have scaffolded test skeletons only.

## 8. Review order

The conventions have been in force since lesson 1.1 — the scaffolder emits namestripped skeletons
with the teacher notes pre-stubbed in the plan, `work` / `teachernote` / `\boxguard` live in
`saar-boxes.sty`, vocabpar is baked into the term macros, and `make check` fails the build on
four of the five. When the user brings a lesson forward by name
(`/lesson-planning apply boxguard namestrip retrofit to 8.1 and 8.3`), apply only the conventions
named — all if none are named — and if the lesson is in an older shape, convert it first
(section 7) and author the deck if one is missing.

**Whenever you review or revise a lesson, execute the conventions in this order:**

> **1. teachernote → 2. namestrip → 3. work rule → 4. boxguard**

vocabpar is not a step — it is structural. The first three each change how much vertical space a
component takes; **boxguard runs last because it repairs the pagination the other three disturb**.
Re-measure after each step — a "this guard costs a page" verdict is valid only for the box heights
it was measured against.

| # | Convention | Enforcement here | Apply with |
| --- | --- | --- | --- |
| — | **vocabpar** | **Automatic** — the term macros carry their own `\par` | nothing to do |
| 1 | **teachernote** | scaffolder seeds the notes in the plan; **`make check` fails** on one in a lesson `_key`; a test key's rationale goes on p2 of `unit_cover_key/` (by hand); only `finals/*_key/` keeps its notes | `movenotes.py unitNN/lessonMM` (`--check` previews) |
| 2 | **namestrip** | scaffolder emits no name row; **`make check` fails** on a live one on a component; cover, tests, and finals keep it | `namestrip.py --project . --unit NN --lesson MM` (`--check` previews) |
| 3 | **work rule** | `work` is one code path for blank and key; **`make check` fails** on a page mismatch (totals only — compare per-page headings yourself) | `work` blocks byte-identical; `\writelines{n}` only for prose `\ansline` drift |
| 4 | **boxguard** | **eyes only** — a stranded stub changes no page count | `\boxguard` / `\boxguard[n]` before the `\begin{...}`, blank **and** key |

**`make check` is the gate, and it is not optional.** `make -C unitXX/lessonYY check` (also
`make -C unitXX check`, `make check` at the root) builds first, then `shared/lesson_check.py`
reports every violation in one pass and exits 1: page parity per keyed component, `warmup` (and a
legacy `exit_ticket`) exactly one page blank and key, no `\ans` / `\ansline` / `\vocabans` inside
`$…$` / `\[…\]` / `\(…\)`, no `teachernote` in a lesson `_key`, no live name row on a component.
The source checks skip comments and understand `\$`; run them alone with
`python3 shared/lesson_check.py unitXX/lessonYY --no-pages`. **Always finish with the evidence**:
`make all` and `make check` both exit 0 (quote the gate's output rather than re-deriving page
counts), per-page headings compared between blank and key, the PDF eyeballed for stranded boxes,
any unresolved violation named with the reason — and then the planning-log update.
