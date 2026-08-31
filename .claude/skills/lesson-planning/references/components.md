# Components

The spec for authoring each file after scaffolding. The scaffolder (`scripts/new_lesson.py`)
gives you a correctly-preambled skeleton with TODO markers; this file says what fills them.
**Always also open lessons 1.0 and 1.1 as the gold reference** — these specs summarize the
pattern, but the live project is authoritative. For macros and boxes
see `references/conventions.md`; for where content comes from, `references/course-workflow.md`.

Contents: [Lesson plan](#lesson-plan) · [Cover](#cover) · [Warm-up](#warm-up) ·
[**Guided notes**](#guided-notes) · [Homework](#homework) ·
[Slides](#slides) · [Dead shapes](#dead-shapes) · [Answer-key discipline](#answer-key-discipline)

**A new lesson is `cover` + `warmup` + `notes` + `homework` + `slides`.** The **guided notes
carry the entire gradual release** — the teacher models the numbered sections (*I do*), works one
designated example with the class (*We Do*), then releases a closing practice box students work
alone (*you do*). **There is no group activity.** The **debrief is a phase, not a component** —
it lives in the lesson plan and the deck only — and **there is no exit ticket**. `activity/` (the
dropped group activity), `experience/` (the scrapped EFFL component), and `exit_ticket/` still
build if a lesson has them, but do not author any of them. See [Dead shapes](#dead-shapes).

General rules:
- Student components preamble with `saar-article` + `saar-boxes`; keys with
  `saar-article` + `saar-key`. **Every component is 10pt.**
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
  pre-drawn, pre-scaled axes — see `course-workflow.md`.)
- Use the project's boxes and fill-in macros rather than hand-rolling layout.

## Lesson plan

`main.tex` at the lesson root — teacher-facing, never handed to students. Canonical section
order:

1. **Title block** — `\CourseName` + `\UnitNumberName \LessonNumberName`. **No school year**
   — see "No year on any document" in `conventions.md`.
2. **Primary Objective** — a `tcolorbox` (frost/cerulean). One or two sentences in student terms
   stating what students will be able to do, interpret, and justify with the topic.
3. **Priority Ideas & Skills** — `skillbox{goldbox}`, two `minipage`s. Left: the priority
   ideas/skills for this topic. Right: "Key Understandings" — the *why*, drawn from the matching
   "Understanding the Standards" pages. Tag the lettered standard codes here.
4. **Vocabulary, Concepts & Theorems** — `skillbox{greenbox}`, a `tabularx` term/definition
   table (use `\TallMath{...}` for tall formulas).
5. **Activate Prior Knowledge & Spiral Review** — `fixedskillbox{frost}`; left lists the
   reviewed skills, right shows the warm-up thumbnail via `\includegraphics[page=1]{warmup/main}`
   **only if the warm-up is a prefab PDF** (authored warm-ups stay text-only).
6. **Lesson at a Glance — `\MeetingLength`** — `fixedskillbox{frost}`, a four-column `tabularx`
   (Phase / Min / Students / Teacher) carrying the five phases:
   **Warm-Up 5 · Guided Notes 30 · Independent Practice 10 · Debrief 7 · Close & Assign 3.**
   `fixedskillbox` because a `tabularx` must not split. Place it after the Vocabulary box and
   before Activate Prior Knowledge. **This table is a contract** — the Lesson box's per-section
   minutes must sum to 30 (the We Do included), and the practice box must be workable alone in 10.
7. **Hook** — `skillbox{frost}`: what goes on the board before anyone sits down, the question to
   ask, and what to do with the answers. End it *unresolved* when the lesson's crux is a
   misconception the notes will settle.
8. **Lesson — Guided Notes (30 min)** — `skillbox{frost}`, `multicols{2}`: one bolded paragraph
   per notes section, **each carrying its own minute budget**, saying exactly what the teacher
   models on the board and what students write. The last paragraph is the **We Do** — name the
   example, say what the teacher holds the pen for and what the class supplies, and budget it.
   The minutes must sum to **30**. Name which section is **the lesson** and which to compress if
   you run behind.
9. **Explicit Instruction: \<the core move\>** — `skillbox{frost}`, a two-column `tabularx`:
   numbered **steps to give verbatim** beside one fully **worked example**, plus a contrast case.
10. **Active Monitoring** — `skillbox{redbox}`: misconceptions keyed to item numbers across the
    notes sections *and* the practice box; the answers to reject; cold-call prompts.
11. **Independent Practice (10 min)** — `skillbox{redbox}`: **students work the notes' closing
    practice box silently and alone** — say so explicitly, since this is the phase most likely to
    drift into partner work. One paragraph on **the arc** of the 1–3 items (which is the on-ramp,
    which is the **crux**), then the **circulation prompts** (questions and cues, not answers)
    keyed to item numbers, the **two-minute check** (which item every student must have started
    by then), and **which student work to display for the debrief** — collected while circulating,
    with permission.
12. **Debrief (7 min) — what goes on the board** — `skillbox{frost}`: the ordered walkthrough of
    the displayed practice work (students correct their own in a second color), a **whole-class
    cold check for understanding** with its correct answer, and the **formative read** — the
    three piles to sort responses into and how the next lesson opens from them. This replaces the
    exit ticket.
13. **Reinforcement & Extension** — `skillbox{goldbox}`: the ~6 homework items and what each
    targets, how it is scored and when it is due, **whether tonight's assignment is the packet
    pages or the Desmos override** (and, if Desmos, which activity), the optional extension, the
    next-lesson preview, and the **Connections** line carrying the lettered standard codes covered.
14. **Teacher notes** — `\begin{teachernote}[Component]`, one per component in packet order:
    **[Warm-Up]**, **[Guided Notes]**, **[Homework]**. Three notes — there is no note for the
    debrief or the independent practice, which are fully specified in their own boxes. Teacher
    prose lives here and **never** in a `_key`.

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
  | 2 | Guided Notes | the ideas the notes build, in order, ending in the practice you work alone | `\blank{1.2cm}` |
  | 3 | Homework | the new context, one line | `\blank{1.2cm}` |

  **Three rows** — the independent practice is part of the Guided Notes row, not its own, because
  it has no separate handout. **Homework is scored**, so its score cell is a `\blank{}` — never
  `NA`. The row never changes with the packet-vs-Desmos choice; that is announced aloud at
  Close & Assign.
- `remindbox` ("Keep in Mind") — the lesson's **content takeaway** in three or four sentences:
  the rule, the test to apply, and the trap to avoid, stated in the formal vocabulary. This is
  the page a student flips back to while doing the homework.

## Warm-up

`warmup/` (+ `warmup_key/`) — short spiral review of *prerequisite* skills (prior-course fluency,
prior lessons' skills). Frequently a **prefab PDF**: if so, drop it in as
`warmup/main.pdf` (and `warmup_key/main.pdf`) — `lesson.mk` merges it directly and the lesson
plan can embed its thumbnail. If authored: 3–5 quick problems with work space (`\vspace`), **no
name row** (namestrip), and the spiral review stays text-only in the plan. Key mirrors with `\ans`.
The warm-up must fit **one page**, blank and key.
Each item should be a **tool the notes pick up again** — the plan's spiral-review box names which
notes section reuses it, so the warm-up reads as a running start rather than a detour. Say so when
you collect it.

## Guided notes

`notes/` (+ `notes_key/`) — **the lesson**: the direct-instruction handout that carries the whole
gradual release. Budget **≤ 6 pages** blank and key, and **40 minutes of the period** — 30 for
everything through the We Do, then 10 for the closing practice box, which is the *Independent
Practice* phase. Structure, in order:

- `\pageheader{Unit X, Lesson Y.Z}{Guided Notes}` — **no name row** (namestrip).
- `objectivebox` — "By the end of this lesson, I will be able to…" **filled in, not blank.** One
  per priority idea/skill, worded exactly as the cover's learning targets. Not a fill-in — no
  `\writeline`s here, and the key carries identical text (which also makes it parity-proof).
- `vocabbox` — `\termblanklong{Term}` per key term; the key uses `\vocabans{Term}{definition}`.
  Write the intro sentence plainly: the term macros carry their own `\par` (vocabpar is enforced
  in the package), so **do not** add `\par\vspace{2pt}` — it double-spaces the box.
- `hookbox` — the same hook as the plan, with `\writelines{2}` for the student response. When the
  hook is a claim the lesson will demolish, state it and **leave it unresolved**.
- **4–6 numbered teaching sections — the *I do*.** Each is a `notesbox{N. Title}`, with
  `\blank{}` and `\writeline` at the points where students record a definition, a step, or a
  result, and `work` blocks for multi-step computations. **The teacher holds the pen throughout**:
  every worked example in these sections is modeled at the board and copied down, so the blanks
  are recording points, not independent problems. Build every example from a **context**, and
  reuse one data set across several sections rather than introducing a new one each time.
  - Sequence them so the **crux section is earned, not announced**: set up the misconception,
    take a vote or a commitment, *do not settle it*, then settle it in the crux section with a
    correct computation that produces a worthless answer. The plan says which section is which.
  - Number them in the text (`1.`, `2.`, …) so the plan's Lesson box and the deck can refer to
    them by number.
- **One `notesbox{N. We Do — <task>}` — the *we do*.** A single example, the last numbered
  section, worked **jointly**: the class supplies the numbers, the reasoning, and the
  interpretation sentence while the teacher writes. It runs the **same task the practice box will
  release**, on different data, so students have a completed template in hand before they work
  alone. Give it full `work` space, not a summary — this is the last thing they see modeled.
  Budget 6–8 of the 30 minutes.
- **A closing `practicebox` — the *you do*, and the 10-minute Independent Practice phase.**
  `practicebox` takes **no argument** (its title is fixed as "Guided Practice"). **1–3 items,
  worked silently and alone** — three is the ceiling, not the target, and any item needing more
  than ~3 minutes alone belongs in the homework instead. Item 1 is the on-ramp and must be
  startable within thirty seconds of the release; the last item carries a *second instance of the
  lesson's trap*. Pre-work heavy arithmetic in a `work` block so the release is spent on the
  classification and the interpretation sentence, not on computation. End with an
  **interpret-in-context** line — that sentence is what the debrief walks.
  - Optionally close with an `extensionbox` ("Extension — optional") of one item for students who
    finish early. Expect a handful to reach it and none to finish it; the plan says to pose it
    aloud in the debrief if nobody got there.
  - **This is the only released work in the lesson.** Do not add a second practice box, and do
    not release items inside the numbered sections — the release happens once, here.

**Pagination.** Guard the first `notesbox` after the `vocabbox` with `\boxguard[20]` in **both**
files — the key's `\vocabans{}` runs shorter than the blank's `\termblanklong{}` rules and will
otherwise float that section onto page 1 in the key only, silently desynchronizing the packet.
Raise `\boxguard` to ~30–40 before any section opening with an unbreakable `tabularx`. Never let
a lead-in sentence be orphaned from the table it introduces — `\nopagebreak` after it.

## Homework

`homework/` (+ `homework_key/`) — authored for **every** lesson. It is the lesson's practice
*and* its graded work: the cover's score column carries a `\blank{}` for it, never `NA`.

`\pageheader{...}{Homework}` — **no name row** (namestrip). Budget **1–2 pages**, blank and key.
Structure:

- **~6 items in new contexts**, spanning the lesson's lettered Knowledge & Skills: the core
  procedure, a **deliberate contrast pair** (same task, opposite condition — the pair that
  surfaces the target misconception), an interpret-in-context item, and a justification item.
  Every item lands in a context, and every answer is phrased in that context.
- **One spiral item** reaching back to an earlier lesson.
- An optional `extensionbox` ("Extension — optional").
- A closing `spiralbox` (its title is fixed as "Connections & Big Ideas") previewing the next
  lesson.

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
can be patched. For how to convert such a lesson, see the Retrofit section of `SKILL.md`.

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

**The deck follows the gradual-release flow (~12 frames):** title → learning targets → warm-up
→ hook → **one frame per numbered notes section** (the crux section's frame flagged with
`\sectionlabel[redacc]{}`) → **We Do** → **independent-practice launch** → debrief → close &
assign. The notes frames carry the *answers* the class arrives at, so they are the board, not a
preview — advance them in step with the handout.

- The **We Do frame** is a live surface, not a completed one: it shows the task and the data with
  the reasoning left blank, and the teacher fills it in from what the class supplies. Do not ship
  it pre-answered.
- The **independent-practice launch frame** carries only the item range, the 10 minutes, and the
  standing rule — **silently, alone, every answer ends in a sentence**. **Do not put the practice
  items or their answers on a slide before the practice**; a deck that shows the answer pattern
  turns the release into copying.
- The **debrief frame** walks the displayed practice work, then the whole-class cold check.

The closing frame names what changed today, then the assignment and plainly which form it takes —
the packet pages or the **Desmos** override, named specifically — with the due date and how it is
scored. Written to the secondary-school audience throughout.

## Unit tests (summative assessments)

Unit-level, not per-lesson — scaffolded once per unit under `unitXX/tests/` and
`unitXX/test_keys/` (see SKILL "What a unit is" and `references/build.md`). Author **two blank
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
  component. See `references/conventions.md` ("The convention gate").
