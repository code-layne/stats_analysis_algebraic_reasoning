# Components

The spec for authoring each file after scaffolding. The scaffolder
(`~/.claude/skills/lesson-planning/scripts/new_lesson.py`) gives you a correctly-preambled
skeleton with TODO markers from the `.tex` files beside this one; this file says what fills them.
**Always also open lesson 1.2 — the pilot — as the gold reference** — these specs summarize
the pattern, but the live project is authoritative. For macros and boxes
see the shared skill's `references/conventions.md` (`~/.claude/skills/lesson-planning/`) and
section 4 of `LESSON_SHAPE.md`; for where content comes from, `templates/lesson/course-workflow.md`.

Contents: [Lesson plan](#lesson-plan) · [Cover](#cover) · [Warm-up](#warm-up) ·
[**Guided notes & practice**](#guided-notes--practice) · [Homework](#homework) ·
[Slides](#slides) · [Dead shapes](#dead-shapes) · [Answer-key discipline](#answer-key-discipline)

**A new lesson is `cover` + `warmup` + `notes` + `homework` + `slides`** (the PILOT shape,
2026-09-06, modeled on AP Statistics lesson 1.4 minus its AP Practice page). The **guided notes
carry the release** — the teacher models **exactly two** long sections (*I do*), then works one
**Guided Practice** with the class holding the pen (*we do*) — and **the homework is the individual
practice** (*you do*), started in class in the last ten minutes. **There is no group activity and
no solo practice set in the notes.** The **debrief is spoken — a phase, not a component** — it lives
in the lesson plan and the deck only — and **there is no exit ticket**. `activity/` (the
dropped group activity), `experience/` (the scrapped EFFL component), and `exit_ticket/` still
build if a lesson has them, but do not author any of them. See [Dead shapes](#dead-shapes).

General rules:
- Student components preamble with `saar-article` + `saar-boxes`; keys with
  `saar-article` + `saar-key`. **Every student component is 12pt** (cover, warm-up, notes,
  homework, keys); the lesson plan is 10pt and the deck 11pt.
- **There is no spoiler rule.** The vocabulary is taught, so the cover, the warm-up, the notes,
  and the slides may all name it outright.
- Keep the **key structurally identical** to its blank — it is the blank with answers filled in.
- **Secondary-school audience, standards-sourced.** Take the scope from the standard's lettered
  Knowledge & Skills and the matching "Understanding the Standards" pages, then write to level:
  a context first, small numbers, one new idea at a time, heavy scaffolding.
- **Cite the standard codes** the component covers in the lesson plan's Priority Ideas box and
  Connections line.
- Every component runs the loop **compute → interpret → justify** ("what does this mean here,
  and how do you know?"). Never ask students to *sketch/draw/construct* a graph from a blank
  page — give a pre-drawn, pre-scaled axis system to complete, a figure to read, a table to
  fill in, or a computation/interpretation task. (A standard that says "sketch" is satisfied by
  pre-drawn, pre-scaled axes — see `templates/lesson/course-workflow.md`.)
- Use the project's boxes and fill-in macros rather than hand-rolling layout.

## Lesson plan

`main.tex` at the lesson root — teacher-facing, never handed to students. Canonical section
order:

1. **Title block** — `\CourseName` + `\UnitNumberName \LessonNumberName`. **No school year**
   — see "No year on any document" in section 4 of `LESSON_SHAPE.md`.
2. **Primary Objective** — a `tcolorbox` (frost/cerulean). One or two sentences in student terms
   stating what students will be able to do, interpret, and justify with the topic.
3. **Priority Ideas & Skills** — `skillbox{goldbox}`, two `minipage`s. Left: the priority
   ideas/skills for this topic. Right: "Key Understandings" — the *why*, drawn from the matching
   "Understanding the Standards" pages. Tag the lettered standard codes here.
4. **Vocabulary, Concepts & Theorems** — `skillbox{greenbox}`, a `tabularx` term/definition
   table (use `\TallMath{...}` for tall formulas).
5. **Lesson at a Glance — `\MeetingLength`** — `fixedskillbox{frost}`, a four-column `tabularx`
   (Phase / Min / Students / Teacher) carrying the four phases:
   **Warm-Up 5 · Guided Notes & Practice 35 · Debrief 10 · Close & Assign 10.**
   `fixedskillbox` because a `tabularx` must not split. **This table is a contract** — the I do is
   about 20 of the 35 and the Guided Practice about 14; the debrief is spoken; the homework start
   is the second formative read.
6. **Warm-Up — Activate Prior Knowledge (5 min)** — `fixedskillbox{frost}`, two columns: *the three
   items and what each seeds* (which notes section picks each one up) · *running it* (which item
   to debrief aloud, what to leave on the board, which item is the tell).
   `\includegraphics[page=1]{warmup/main}` **only** if the warm-up is a prefab PDF.
7. **Hook — before anyone sits down** — `skillbox{frost}`: the claim on the board, the vote, and
   **do not settle it** — name where it settles (the second half of section 2).
8. **Guided Notes & Practice — I do, then we do (35 min)** — `skillbox{frost}`, `multicols{2}`.
   Left column, *I do (about 20 min)*: one paragraph per section, each in two moves with its
   minutes, saying what the teacher models and what students write; name which section **is the
   lesson** (section 2) and where to take the vote before anyone writes. Right column, *we do
   (about 15 min)*: the Guided Practice by name, the questions the teacher asks per lettered part,
   the circulation prompts (reasons, not words), and which two papers to collect for the debrief.
9. **Debrief — whole class, spoken (10 min)** — `skillbox{frost}`, `multicols{2}`: the ordered walk
   of what goes back on the board (students answer aloud, nothing to fill in), the **cold check**
   asked cold with its correct answer (*this replaces the exit ticket*), the **formative read** into
   three piles and how the next lesson opens from pile (c), and what to cut if it runs short.
10. **Homework — scored, started in class, due after two study halls** — `skillbox{goldbox}`: the ~6 items and
    what each targets (name the contrast pair, the crux head-on, and the spiral item), scoring
    (2 per item), **packet or Desmos** with the activity named if Desmos, the next-lesson preview,
    and the **Connections & Big Ideas** line carrying the lettered standard codes.
11. **Watch For (while circulating)** — `skillbox{redbox}`: misconceptions keyed to notes section,
    Guided Practice part, *and* homework item, each with a probe; cold-call prompts.
12. **Close & Assign (10 min)** — `skillbox{goldbox}`: the homework launch, which items to start in
    class and which to let go home, the three-pile sort while circulating and the reteach trigger,
    the one-line "what changed today," the preview.
13. **Teacher notes** — `\begin{teachernote}[Component]`, one per component in packet order:
    **[Warm-Up]**, **[Guided Notes \& Practice]**, **[Homework]**. Three notes — none for the
    debrief or the homework start, which are fully specified in their own boxes. Teacher prose
    lives here and **never** in a `_key`.

## Cover

`cover/main.tex` — student-facing front page of the packet. No key. Structure:
- Full-bleed cerulean banner (tikz) with `\LARGE` course name, unit, and `Lesson <id>  <title>`.
- `\namedateperiod` — the cover is the **one** component that carries it (namestrip).
- `learningtargetbox` — an "I can…" list, one target per priority idea/skill, **naming the
  formal vocabulary outright**. The lettered standard codes belong in the lesson plan, not here.
- `tocbox` — a `tabularx` listing each packet component (#, Component, Description, Score blank)
  with a Total row — **three rows**:

  | # | Component | Description | Score |
  |---|---|---|---|
  | 1 | Warm-Up | what the spiral items rehearse | `\blank{1.2cm}` |
  | 2 | Guided Notes & Practice | the ideas the two sections build, then the one survey worked together | `\blank{1.2cm}` |
  | 3 | Homework | the new context, one line — *scored, started in class, due the first class after two study halls* | `\blank{1.2cm}` |

  **Three rows** — the Guided Practice is inside the Guided Notes & Practice row, not its own,
  because it has no separate handout. **Homework is scored**, so its score cell is a `\blank{}` —
  never `NA`. The row never changes with the packet-vs-Desmos choice; that is announced aloud at
  Close & Assign.
- `remindbox` ("Keep in Mind") — the lesson's **content takeaway** in three or four sentences:
  the rule, the test to apply, and the trap to avoid, stated in the formal vocabulary. This is
  the page a student flips back to while doing the homework.

## Warm-up

`warmup/` (+ `warmup_key/`) — short spiral review of *prerequisite* skills (prior-course fluency,
prior lessons' skills). Frequently a **prefab PDF**: if so, drop it in as
`warmup/main.pdf` (and `warmup_key/main.pdf`) — `lesson.mk` merges it directly and the lesson
plan can embed its thumbnail. If authored: **three** items at 12pt (`\setlength{\workrowsep}{50pt}`, `itemsep=22pt`, tables at
`\arraystretch` 2.6–3.3) so each item gets real handwriting room, **no name row** (namestrip), and the spiral review stays text-only in
the plan. Key mirrors with `\ans` (generate it with `mkkey.py`). The warm-up must fit **one page**,
blank and key — do not add a fourth item.
Each item should be a **tool the notes pick up again** — the plan's spiral-review box names which
notes section reuses it, so the warm-up reads as a running start rather than a detour. Say so when
you collect it.

## Guided notes & practice

`notes/` (+ `notes_key/`) — **the direct-instruction centrepiece, 35 minutes**, in two moves.
`\pageheader{Unit X, Lesson Y.Z}{Guided Notes \& Practice}` — **no name row** (namestrip). Target
**4 pages** at 12pt, blank and key, `\small` inside every box as the stats model does. **It runs short on purpose**: the period ends with students
starting the homework, which is where the individual practice lives.

**I do (~20 min)** — **exactly two** numbered notes sections. Each is long, carrying two moves:
the second is introduced by a bold run-in heading, `\textbf{\textcolor{cerulean}{Its Title.}}`, not
by a third box. **The crux lives in the second half of section 2.**
- **Page plan (fixed):** page 1 = `vocabbox` + `hookbox`; page 2 = section 1; page 3 = section 2 (`\newpage` before each section); page 4 = the Guided Practice alone. **No `objectivebox`** — the cover carries the targets.
- Every fill-in cluster opens with a `\wordbank{…}` strip (defined in the preamble; copy from 1.2) listing every word and number its blanks take.
- `vocabbox` — one `\vterm{Term}` per key term (4–5 of them): a **fixed-height 1.6cm row** with the
  term and one full-width blank and **no rule line**, as the stats course does. The box says
  **"Fill in each term as we name it in the notes below"** — filled during instruction, never
  front-loaded. The key uses `\vtermans{Term}{definition}`, which fills exactly the same height
  (keep definitions to two lines), so the box cannot drift blank vs. keyed. The `\vterm` /
  `\vtermans` pair is defined in the notes preamble — copy the block from lesson 1.2; `mkkey.py`
  maps one to the other. Do not use `\termblank` / `\termblanklong` / `\vocabans` in a new lesson.
- `hookbox` on page 1, under the vocab box: the claim, a circle-one vote, `\par\writelines{2}` for the reason — **left unresolved**; the same hook is a dark slide and a plan box.
- Two `notesbox{N. Title}` sections. Each opens in the warm-up's own context, carries a short piece
  of exposition, a **pre-drawn** table or display with `\blank{W}` fills at the points where students
  record the definition or the conclusion, and any computation in a `work` block (byte-identical in
  the key). Put a trap where it is broken in a `\fcolorbox{redacc}{redbg}{\parbox{0.94\linewidth}{…}}`
  callout (section 1's second half may carry a second trap; section 2's second half carries the
  target misconception in a `\fcolorbox{cerulean}{frost}` rule box). Sequence them so the crux is
  earned: the hook plants it and takes a vote, section 1 builds the vocabulary, the second half of
  section 2 re-takes the vote and settles it with a correct computation. Reuse one data set across
  both sections.

**We do (~15 min)**
- One `practicebox` — **takes no argument**, its title is fixed as "Guided Practice". Open with "**Title — we work this one together**" in a **second context**, alone on page 4. Four or five lettered parts: the
  setup/identification move, the computation with its labels (`work` block), **the part that is the
  point of the box** — the one that tests the misconception on new ground — and optionally one
  short closing part. `\par\writelines{n}` for prose answers (the key: `\par\ansline{}` on the first
  line of a run only). Students hold the pen; the questions the teacher asks belong in the plan.

**The notes end at Guided Practice.** No solo practice box, no *Putting It Together*, no
`extensionbox`, no `reflectionbox`. The debrief is spoken and lives in the plan; the individual
practice is `homework/`, started in class in the last ten minutes.

**Page lockstep:** generate the key from the blank with `templates/lesson/mkkey.py` and an
answers-in-order JSON spec (`templates/lesson/examples/` holds lesson 1.2's); it refuses to run if
the blank count and the answer count disagree. **Size each `\blank{}` close to its answer** — a
4.4cm blank replaced by a 2cm answer rewraps the paragraph and silently costs a page. Verify by
comparing **per-page headings** of the compiled blank and key, not just totals.

## Homework

`homework/` (+ `homework_key/`) — authored for **every** lesson. It is the lesson's **individual
practice** *and* its graded work: the cover's score column carries a `\blank{}` for it, never `NA`,
and **students start it in class in the last ten minutes of the period**, alone, while the
teacher circulates for the second formative read.

`\pageheader{...}{Homework}` — **no name row** (namestrip). Budget **2–3 pages** at 12pt, blank
and key; the practice boxes at full size (`\small` only in the opening `remindbox`).
Structure, in order:

- A `remindbox` — "**This is your graded homework.** It is scored out of N and due …; you will
  start it in the last minutes of the period …" — identical in blank and key.
- A `scenariobox[Context]{cerulean}` giving the **third context** (notes = first, Guided Practice =
  second) and its data.
- **~6 items in a `notesbox`**, spanning the lesson's lettered Knowledge & Skills: the core
  procedure, **one spiral item** reaching back to an earlier lesson, an interpret-in-context item,
  a **deliberate contrast pair** (same task, opposite condition — the pair that surfaces the target
  misconception), the **crux head-on**, and a justification item. Every answer is phrased in its
  context. Split into `notesbox{…, continued}` boxes so that **no item breaks across a page** and
  no lead-in sentence is stranded from its table — three boxes at 12pt is normal.
- A closing `spiralbox` (its title is fixed as "Connections & Big Ideas") previewing the next
  lesson. No `extensionbox`.

Multi-step solutions go in `work` blocks authored byte-identically here and in the key. Key fills
with `\ans`, carries every `work` block and `\boxguard` over unchanged, and tags the correct MC
option. Scoring guidance goes in the lesson plan's `\begin{teachernote}[Homework]`, **not** in the
key.

**Packet or Desmos.** The packet pages are authored for every lesson regardless. Which form the
assignment takes is decided **lesson by lesson** by the teacher at Close & Assign, based on whether
**Desmos** carries an activity adequate to that lesson's skills; when it does, students keep the
packet pages as a worked reference instead. Desmos Classroom's coverage of this course's standards
is uneven — strong on function modeling and regression, thinner on the inference and study-design
standards — so it is checked per lesson and never assumed. Nothing about what you author changes:
say the choice in the lesson plan's Homework box and on the deck's closing frame, name the specific
Desmos activity there if that is the call, and leave the cover row alone.

## Dead shapes

Three component shapes survive in the tree but must never be authored into a new lesson.
`shared/lesson.mk` still merges all of them, so any lesson carrying them keeps building, and the
scaffolder still accepts them by name (`--components ...,activity,experience,exit_ticket`) so one
can be patched. For how to convert such a lesson, see section 7 of `LESSON_SHAPE.md` (Legacy shapes and regeneration).

- **`activity/` (+ `activity_key/`)** — the dropped group activity: ~6–7 items over one shared
  data set, worked in groups of three for 18 minutes after the notes, in a context fresh from the
  notes'. Dropped 2026-08-31 — the release is individual now and lives in the notes' practice box.
  When converting, its on-ramp items become worked examples in the numbered sections, its **crux
  item becomes the We Do**, one or two later items become the `practicebox`, and the rest is cut
  or moved to the homework. Do not preserve it by renaming it.
- **`experience/` (+ `experience_key/`)** — the scrapped EFFL in-class component: one 12pt
  document in three parts (Activity · QuickNotes · Application) using an `\answerspace{H}{}`
  macro instead of write-lines. The EFFL trial ran 2026-08-29 to 2026-08-31 and was rejected by
  students. When converting, QuickNotes expands back into taught notes sections, the Activity's
  richest scenario becomes the **We Do**, and the Application becomes the `practicebox`.
- **`exit_ticket/` (+ `exit_ticket_key/`)** — a short independent check (2–3 items), no notes,
  one page. Replaced by the debrief's whole-class cold check. When converting, fold the exit
  ticket's conceptual item into the plan's Debrief box as that cold check.

## Slides

`slides/` — **required** teacher Beamer deck (it feeds two of the five work products, so every
lesson owes one). No key. Requires `shared/saar-beamer.sty`.
Preamble: `\documentclass[aspectratio=169,11pt]{beamer}` + `\usepackage{saar-beamer}`.
The title slide is hand-built (cerulean background canvas + minipage); content slides use
`\ceruleanheader{Title}` and `\sectionlabel[color]{LABEL}`. Note `\CourseName` is **not** defined
in beamer (`saar-beamer` does not load `saar-article`) — write "Statistical Analysis \& Algebraic
Reasoning" literally. `saar-beamer` also does **not** load `tcolorbox`: use beamer's native
`\begin{block}{}` for a highlighted box inside a frame, and note `\begin{itemize}` in beamer
does not accept `[leftmargin=…]` — set `\setlength{\itemsep}{…}` instead.

**The deck follows the gradual-release flow (~14 frames):** title → learning targets (with a
*How today works* block) → warm-up → **hook, dark frame, left unresolved** → **I-do divider,
dark frame** → two or three frames per notes section (the crux frame flagged
`\sectionlabel[redacc]{}`) → **Guided Practice** → **debrief** with the cold check → **You do:
start the homework** → close, dark frame. The notes frames carry the *answers* the class arrives
at, so they are the board, not a preview — advance them in step with the handout.

- The **Guided Practice frame** is a live surface, not a completed one: it shows the task and the
  data with the reasoning left blank, and the teacher fills it in from what the class supplies. Do
  not ship it pre-answered.
- The **You do frame** names the homework context and the item themes (never the answers), the
  standing rule — **silent and alone, I am circulating** — which items to start in class, and
  plainly which form the assignment takes (the packet pages, or a named Desmos activity), the
  points, and the due date.
- There is **no independent-practice launch frame** and no exit-ticket frame.

## Unit tests (summative assessments)

Unit-level, not per-lesson — scaffolded once per unit under `unitXX/tests/` and
`unitXX/test_keys/` (see section 6 of `LESSON_SHAPE.md` and the shared skill's `references/build.md`). Author **two blank
tests and their two keys**, all with `\pageheader{Unit X: <Title>}{...}` + `\namedateperiod` — tests
are taken in a testing setting, not stapled behind a lesson cover, so they keep the name row:

- **`tests/practice_test/main.tex`** — the study copy students keep. Opens with a `remindbox`
  telling students it mirrors the real test in format and ideas but uses different numbers.
  Organize into `\parthead{Part …}` sections (vocabulary, multiple choice, short
  answer/computation, extended response) with `\vspace` work room. This test is **published as
  the unit's `sample_test`** and lands in the student packet.
- **`tests/actual_test/main.tex`** — the real test given at test time. Same format, parts, and
  difficulty as the practice test, **different numbers/contexts**; no "this is practice" box.
  It is **never** merged into a packet — it is distributed separately.
- **`test_keys/practice_test_key/main.tex`**, **`test_keys/actual_test_key/main.tex`** — the
  keys, each mirroring its blank test exactly (preamble swaps `-boxes` for `-key`), answers in
  `\ans{...}`, correct MC options tagged, worked solutions in byte-identical `work` blocks. **No
  `teachernote`** — a test key's answer rationale and extended-response scoring go on page 2 of
  `unitXX/unit_cover_key/`, so they reach the key packet only; the practice key is published as
  `sample_test_key` and its blank rides in the *student* packet.

Content comes from across the whole unit's standards (it is summative) — sample every lettered
skill the unit's lessons taught. Cover the same
priority ideas the lessons taught; keep the interpret-and-justify emphasis in the extended
response. The practice and actual versions must stay parallel so the practice test is honest
preparation. Build/publish with `make -C unitXX/tests all` and `make -C unitXX/test_keys all`.

## Unit cover (optional pair)

`unitXX/unit_cover/` and `unitXX/unit_cover_key/` — the front matter of the unit packets,
discovered by `shared/unit.mk` and merged ahead of the lesson packets. The student cover goes
into the student packet; the key cover replaces it in the key packet (a unit with no
`unit_cover_key/` gets the plain cover in both).

The sheet itself lives in **`unit_cover/body.tex`**; both wrappers `\input` it, so page 1 cannot
drift between them. Edit the cover there, never in a wrapper.

```latex
% unit_cover/main.tex — 1pp student cover
\documentclass[10pt]{article}
\usepackage{saar-article}
\usepackage{saar-boxes}
\begin{document}
\input{body.tex}
\end{document}

% unit_cover_key/main.tex — the same page 1, plus one page of scoring notes
\documentclass[10pt]{article}
\usepackage{saar-article}
\usepackage{saar-boxes}
\begin{document}
\input{../unit_cover/body.tex}
\newpage
\begin{headlinebox}{cerulean}{\color{white}\bfseries Unit X --- Exam Scoring Notes (Teacher Copy)}\end{headlinebox}
\begin{teachernote}[Practice Test --- Part B] ... \end{teachernote}
\end{document}
```

Page 1 carries the unit banner, an overview, a lesson table, and the unit's big ideas — student
facing, so no scoring information. Page 2 is teacher-only: the answer rationale and Part D
scoring for **both** unit assessments, the prose that must not sit in a `*_test_key` (the
practice test is bound into the student packet). Keep it to one page — cover + notes is a single
double-sided sheet.

## Answer-key discipline

There is no key toggle — every key is a separate file under `<comp>_key/` (this applies to the
test keys too):
- Copy the blank component **verbatim**, then swap `\usepackage{saar-boxes}` for
  `\usepackage{saar-key}`.
- Replace each blank/write-line with `\ans{answer}` (inline) or `\ansline{answer}` (fills a
  write-line). Title becomes "<DocTitle> — Answer Key".
- For multiple choice, keep all options and tag the correct one
  (`\textcolor{keyred}{\textbf{$\leftarrow$ correct}}`), then show the reasoning in a short
  `itemize`.
- `\ans` is text-mode: never put it inside `$...$` — wrap math fragments instead
  (`\ans{$\hat v$}`) — and never let it span a blank line.
- **Worked solutions go in a `\begin{work}` block, authored byte-identically in the blank and
  the key** (the work rule). The blank reserves the block's exact height and prints nothing; the
  key prints the same block in `keyred`, so the two cannot drift.
- **No `teachernote` in any key — lesson component, unit test, or final.** It is the one block
  with no counterpart in the blank, so it makes the key longer than the blank. Teacher prose goes
  in the lesson plan as `\begin{teachernote}[Component]`; a unit test's answer rationale and
  scoring go on **page 2 of `unitXX/unit_cover_key/main.tex`**, which reaches the key packet only.
- Because the key matches the blank line-for-line, the two paginate identically. **Verify with
  `make -C unitXX/lessonYY check`**, which fails on a blank/key page mismatch, a warm-up or exit
  ticket over one page, `\ans` inside math, a `teachernote` in a key, and a name row on a
  component. See section 8 of `LESSON_SHAPE.md` (the convention gate).
