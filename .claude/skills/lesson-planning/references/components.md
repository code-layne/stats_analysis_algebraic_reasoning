# Components

The spec for authoring each file after scaffolding. The scaffolder (`scripts/new_lesson.py`)
gives you a correctly-preambled skeleton with TODO markers; this file says what fills them.
**Always also open a real built EFFL lesson as the gold reference** — these specs summarize the
pattern, but the live project is authoritative. For macros and boxes
see `references/conventions.md`; for where content comes from, `references/course-workflow.md`.

Contents: [Lesson plan](#lesson-plan) · [Cover](#cover) · [Warm-up](#warm-up) ·
[**Experience & Formalize**](#experience--formalize) · [Homework](#homework) ·
[Slides](#slides) · [Legacy components](#legacy-components--pre-effl) ·
[Answer-key discipline](#answer-key-discipline)

**A new lesson is `cover` + `warmup` + `experience` + `homework` + `slides`.** That is the EFFL
(experience first, formalize later) shape. `notes`, `activity`, and `exit_ticket` are pre-EFFL —
the build still merges them so the 60+ legacy lessons keep working, but do not author new ones.
See [Legacy components](#legacy-components--pre-effl).

General rules:
- Student components preamble with `saar-article` + `saar-boxes`; keys with
  `saar-article` + `saar-key`. **The `experience` component is 12pt; everything else is 10pt.**
- **The spoiler rule:** nothing the student sees *before* the activity — the cover, the warm-up,
  the deck's learning-targets frame — may pre-name the vocabulary the debrief will attach. Write
  targets in plain language ("how spread out the values are", not "standard deviation"). The
  teacher-facing lesson plan keeps the formal vocabulary and the standard codes.
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
   (Phase / Min / Students / Teacher) carrying the five EFFL phases:
   **Warm-Up 5 · Experience & Formalize: Activity 22 · Debrief: Formalize 14 · Application 10 ·
   Close & Assign 4.** `fixedskillbox` because a `tabularx` must not split.
7. **Experience & Formalize — The Activity** — `skillbox{frost}`: the 2-minute launch script,
   then `multicols{2}` — *what students do* (the arc of the two scenarios, and which item is the
   **crux question**) beside *what the teacher does* (circulate; the questions, cues, and prompts
   to give instead of answers; which group work to display).
8. **Debrief — Formalize** — `skillbox{frost}`: the ordered "red ink" moves, each attaching a
   formal name to something a group already wrote, plus the QuickNotes walkthrough and why this
   order.
9. **Application** — `skillbox{frost}`: the one problem worked together, the three questions the
   teacher asks while students hold the pen, and how to sort the Interpret/What-if responses.
   **This is the lesson's formative check** — there is no exit ticket.
10. **Watch For** — `skillbox{redbox}`: misconceptions keyed to item numbers; cold-call prompts.
11. **Homework — Check Your Understanding** — `skillbox{goldbox}`: the ~6 CYU items and what each
    targets, how it is scored and when it is due, and **whether today's practice is the packet
    pages or the equivalent DeltaMath set** (see the Homework spec below).
12. **Close & Preview** — `skillbox{goldbox}`: name what changed today, the **Connections** line
    carrying the lettered standard codes covered, and a one-line preview of the next lesson.
13. **Teacher notes** — `\begin{teachernote}[Component]`, one per component in packet order:
    **[Warm-Up]**, **[Experience & Formalize]** (Activity / Debrief / Application), **[Homework]**.
    Three notes, not five. Teacher prose lives here and **never** in a `_key`.

## Cover

`cover/main.tex` — student-facing front page of the packet. No key. Structure:
- Full-bleed cerulean banner (tikz) with `\LARGE` course name, unit, and `Lesson <id>  <title>`.
- `\namedateperiod` — the cover is the **one** component that carries it (namestrip).
- `learningtargetbox` — an "I can…" list, one target per priority idea/skill, **spoiler-free**:
  plain-language descriptions of what students will be able to *do*, never the formal vocabulary
  the debrief will attach. The lettered standard codes belong in the lesson plan, not here.
- `tocbox` — a `tabularx` listing each packet component (#, Component, Description, Score blank)
  with a Total row. In an EFFL lesson that is **three rows**:

  | # | Component | Description | Score |
  |---|---|---|---|
  | 1 | Warm-Up | spoiler-free one-liner | `\blank{1.2cm}` |
  | 2 | Experience & Formalize | *Activity Title* — scenarios with your group, then QuickNotes and an application we work together | `\blank{1.2cm}` |
  | 3 | Homework | Check Your Understanding — practice in new contexts | `\blank{1.2cm}` |

  **Homework is scored**, so its score cell is a `\blank{}` — never `NA`. The row never changes
  with the packet-vs-DeltaMath choice; that is announced aloud at Close & Assign.
- `remindbox` ("Keep in Mind") — describes the **EFFL process only** and stops there. No content
  preview, no formal vocabulary: *"you and your group will work out … using what you already
  know — and only afterward will we name what you found."*

## Warm-up

`warmup/` (+ `warmup_key/`) — short spiral review of *prerequisite* skills (prior-course fluency,
prior lessons' skills). Frequently a **prefab PDF**: if so, drop it in as
`warmup/main.pdf` (and `warmup_key/main.pdf`) — `lesson.mk` merges it directly and the lesson
plan can embed its thumbnail. If authored: 3–5 quick problems with work space (`\vspace`), **no
name row** (namestrip), and the spiral review stays text-only in the plan. Key mirrors with `\ans`.
The warm-up must fit **one page**, blank and key.
**Spoiler rule:** the warm-up runs *before* the activity, so it reviews prerequisite skills and
plants seeds without naming any of the lesson's formal vocabulary. The lesson plan's spiral-review
box says which formal idea each item seeds; the student page does not.

## Experience & Formalize

**The component's name is "Experience & Formalize"** — that is what the cover, the packet header,
the deck, and the lesson plan call it. **The directory stays `experience/`**: it is a build
identifier listed in `shared/lesson.mk`'s `STUDENT_ORDER`/`KEYED_PAIRS`, and renaming it would
mean editing the build system. Directory `experience`, label *Experience & Formalize*.

`experience/` (+ `experience_key/`) — **the heart of the lesson**, one document, **three parts**,
in this order, on an explicit **page budget**:

| Part | Budget | What it is |
| --- | --- | --- |
| 1. Activity | **≤ 2 pages** | group work from prior knowledge only |
| 2. QuickNotes | **½ page** | the debrief fills it |
| 3. Application | **½–1 page** | one problem worked *together* — compute, interpret, justify |

Hold the budget: it is the whole point of the split. A part that runs over gets cut, not carried.
**There is no Check Your Understanding section in this component** — this course's CYU-style
practice is the `homework` component, and everything in `experience/` happens in class, together.

`\documentclass[12pt]{article}` (Math Medic sizing — the rest of the packet is 10pt),
`\pageheader{Unit X, Lesson Y.Z}{Experience \& Formalize: <Activity Title>}`, no name row.

The preamble defines `\answerspace{H}{answer}` (see `conventions.md`). The blank passes `{}`; the
key passes the answer, occupying the identical height — so the two files paginate identically by
construction. **No `\writelines` in Experience & Formalize** — answers go in open space. Short
inline `\blank{}`s remain for table cells and one-word fills. `\boxguard` counts here are
12pt-relative: use **~14–16**, not the 24–30 used in 10pt components.

1. **Activity** — a `headlinebox{frost}` framing one motivating **data context**, then **two
   `scenariobox`es** (`{cerulean}`; ~10–14 lettered sub-questions total, ~2 pages) that students
   work **from prior knowledge only**: complete a table, compute a value, circle/annotate a
   **pre-drawn** display, answer in the open space. Scenario 1 builds the toolkit on one data set;
   scenario 2 varies it (the contrast case) and carries the lesson's **crux question** — the one
   that surfaces the target misconception. **The timebox rule:** the activity must fit the
   22-minute block; extra examples belong to the debrief, the Application, or the homework CYU
   set. Never name the formal vocabulary here — students answer in their own words. Every display
   is pre-drawn; **never ask a student to sketch a graph from scratch.**
2. **QuickNotes** — one titled `tcolorbox` (frost/cerulean) the **debrief fills**: a small worked
   example or formula beside fill-in bullets covering the lesson's formal terms and notation. A
   summary of what the groups discovered, not a lecture; **half a page**. Blanks are `\blank{}`
   (key: `\ans{}`).
3. **Application** — a `notesbox{Application: <Title>}` with **one problem worked together**. This
   is the first place the just-named vocabulary is *used* and the lesson's only in-class practice,
   so it carries the whole arc: state the question in context, compute in a `work` block,
   **interpret the result in context**, then a "what if we change a number?" prompt that tests the
   concept rather than the procedure and demands a **justification**. Note `practicebox` takes
   **no argument** (its title is fixed as "Guided Practice"), so a titled Application uses
   `notesbox`.

   **The Application is the formative check.** With no exit ticket, the teacher reads the
   Interpret and What-if responses over shoulders and sorts them to decide how the next lesson
   opens; the lesson plan says into which categories.

Key mirrors exactly: same `\answerspace` macro and heights, answers in its second argument,
`\ans{}` in the blanks, `work` blocks carried over byte-identically, MC option tagged
`\textcolor{keyred}{\textbf{$\leftarrow$ correct}}`.

## Homework

`homework/` (+ `homework_key/`) — **this course's Check Your Understanding set.** Experience &
Formalize carries no practice section, so this is where the CYU-style problems live. It is the
lesson's practice *and* its graded work: the cover's score column carries a `\blank{}` for it,
never `NA`.

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

**Packet or DeltaMath.** The packet pages are authored for every lesson regardless. Which form the
assignment takes is decided **lesson by lesson** by the teacher at Close & Assign, based on whether
DeltaMath carries adequate content for that lesson's skills; when it does, students keep the packet
pages as a worked reference instead. Nothing about what you author changes — say the choice in the
lesson plan's Homework box and on the deck's closing frame, and leave the cover row alone.

## Legacy components — pre-EFFL

`notes/`, `activity/`, and `exit_ticket/` (with their `_key`s) predate the 2026-08 EFFL redesign.
`shared/lesson.mk` still merges them, so the 60+ legacy lessons keep building untouched, and the
scaffolder still accepts them by name (`--components ...,notes,activity,exit_ticket`) so a legacy
lesson can be patched. **Do not author them into a new lesson.** For how to regenerate a legacy
lesson in the EFFL shape, see the Retrofit section of `SKILL.md`. Their specs follow for reference
while converting.

## Guided notes

`notes/` (+ `notes_key/`) — the student's fill-in notes. Structure:
- `\pageheader{Unit X, Lesson Y.Z}{Guided Notes}` — **no name row** (namestrip).
- `objectivebox` — "By the end of this lesson, I will be able to…" **filled in, not blank.**
  State the objectives outright, one per priority idea/skill, worded exactly as the cover's
  learning targets. The student should be able to read what the lesson is for without waiting
  for it to be dictated, so this box is **not** a fill-in — no `\writeline`s here, and the key
  carries the identical text (which also makes it parity-proof).
- `vocabbox` — `\termblanklong{Term}` per key term (key uses `\vocabans{Term}{definition}`).
  Write the intro sentence plainly: the term macros carry their own `\par` (vocabpar is enforced
  in the package), so **do not** add `\par\vspace{2pt}` — it double-spaces the box.
- `hookbox` — the same hook as the plan, with write-lines for student responses.
- Direct-instruction sections in `notesbox{Title}` with blanks (`\blank`, `\writeline`) at the
  points where students record steps/definitions/results. Build the worked example from the standard's
  scope, in a context.
- Optional `practicebox` ("Guided Practice") with 1–2 worked-with-class problems.

## Activity

`activity/` (+ `activity_key/`) — differentiated group practice, ideally a small **applied
investigation** — a data set to analyze, a scenario to model, a measurement to solve for.
- `\pageheader{Unit X, Lesson Y.Z}{Group Activity}` — **no name row** (namestrip).
- Three `tcolorbox`es titled **Tier R — Remediate**, **Tier A — Approaching Proficiency**,
  **Tier E — Extension** (`colframe=black!40`), each with problems and generous `\vspace` work
  room. Tiers escalate in difficulty and align to the same skills; the top tier should reach an
  interpret/justify/critique-the-model task.
- Key mirrors exactly, filling answers with `\ans{...}` and marking correct MC options with
  `\textcolor{keyred}{\textbf{$\leftarrow$ correct}}`, plus brief worked steps.

## Exit ticket

`exit_ticket/` (+ `exit_ticket_key/`) — a short independent check (2–3 items), no notes.
`\pageheader{...}{Exit Ticket}` — **no name row** (namestrip); a tight `enumerate` with a little work
space. Include at least one "what does this result mean?" item. Key fills with `\ans`.

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

**The deck follows the EFFL flow (~9 frames):** title → learning targets (**spoiler-free**) →
warm-up → activity launch → 3–4 debrief frames (formal terms in "red ink", `\redink{}` =
`redacc`) → QuickNotes summary → application → close & assign. **Everything before the debrief
frames stays vocabulary-free** (the spoiler rule). The closing frame names the assignment and
says plainly which form it takes today — the packet's Check Your Understanding pages or the
equivalent DeltaMath set — with the due date and how it is scored. Written to the
secondary-school audience throughout.

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
