# Components

The spec for authoring each file after scaffolding. The scaffolder (`scripts/new_lesson.py`)
gives you a correctly-preambled skeleton with TODO markers; this file says what fills them.
Once one lesson is built, **also open it as the gold reference** — this is a greenfield
course, so the first lesson you build becomes the model for the rest. For macros and boxes
see `references/conventions.md`; for where content comes from, `references/course-workflow.md`.

Contents: [Lesson plan](#lesson-plan) · [Cover](#cover) · [Warm-up](#warm-up) ·
[Guided notes](#guided-notes) · [Activity](#activity) · [Exit ticket](#exit-ticket) ·
[Homework](#homework) · [Slides](#slides) · [Answer-key discipline](#answer-key-discipline)

General rules:
- Student components preamble with `saar-article` + `saar-boxes`; keys with
  `saar-article` + `saar-key`.
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
6. **Hook** — `skillbox{frost}`: an entry question/scenario from the course's application
   domains.
7. **Lesson** (and optional **Lesson (cont.)**) — `skillbox{frost}` with `\begin{multicols}{2}`;
   the worked instructional progression, bolding the questions you'll pose. Context and
   numbers first, then the general statement.
8. **Explicit Instruction: <technique>** — one `skillbox{frost}` per technique, two columns:
   numbered steps on the left, a worked example (often a Desmos/calculator screenshot for
   transformation or regression work) on the right.
9. **Active Monitoring** — `skillbox{redbox}`: what to circulate and check; cold-call prompts.
10. **Group Work & Differentiation** — `skillbox{redbox}`: a `multicols{3}` with **Tier R —
    Remediate / Tier A — Approaching Proficiency / Tier E — Extension** bullet lists that
    mirror the activity tiers.
11. **Individual Work & Assessment** — `skillbox{redbox}`: exit-ticket items + a short
    **conceptual/justification check** (interpret-a-result item), with a note on collecting
    and using results.
12. **Reinforcement & Extension** — `skillbox{goldbox}`: homework overview, an extension, and a
    preview of the next lesson.

## Cover

`cover/main.tex` — student-facing front page of the packet. No key. Structure:
- Full-bleed cerulean banner (tikz) with `\LARGE` course name, unit, and `Lesson <id>  <title>`.
- `\namedateperiod` — the cover is the **one** component that carries it (namestrip).
- `learningtargetbox` — an "I can…" list, one target per priority idea/skill.
- `tocbox` — a `tabularx` listing each packet component (#, Component, Description, Score blank)
  with a Total row. Keep the rows aligned with the components you actually scaffolded.
- Optionally mirror the lesson plan's Priority Ideas & Vocabulary for student reference.

## Warm-up

`warmup/` (+ `warmup_key/`) — short spiral review of *prerequisite* skills (prior-course fluency,
prior lessons' skills). Frequently a **prefab PDF**: if so, drop it in as
`warmup/main.pdf` (and `warmup_key/main.pdf`) — `lesson.mk` merges it directly and the lesson
plan can embed its thumbnail. If authored: 3–5 quick problems with work space (`\vspace`), **no
name row** (namestrip), and the spiral review stays text-only in the plan. Key mirrors with `\ans`.
The warm-up must fit **one page**, blank and key.

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

## Homework

`homework/` (+ `homework_key/`) — independent practice + stretch.
`\pageheader{...}{Homework}` — **no name row** (namestrip); a numbered practice set (problems written to the
standard's lettered skills, in context), an `extensionbox` ("Extension — optional"), and
a short preview of the next lesson. Key fills with `\ans` and shows worked steps for the
harder items.

## Slides

`slides/` — optional teacher Beamer deck. No key. Requires `shared/saar-beamer.sty`.
Preamble: `\documentclass[aspectratio=169,11pt]{beamer}` + `\usepackage{saar-beamer}`.
The title slide is hand-built (cerulean background canvas + minipage); content slides use
`\ceruleanheader{Title}` and `\sectionlabel[color]{LABEL}`. Note `\CourseName` is **not** defined
in beamer (`saar-beamer` does not load `saar-article`) — write "Statistical Analysis \& Algebraic
Reasoning" literally. `saar-beamer` also does **not** load `tcolorbox`: use beamer's native
`\begin{block}{}` for a highlighted box inside a frame, and note `\begin{itemize}` in beamer
does not accept `[leftmargin=…]` — set `\setlength{\itemsep}{…}` instead. Keep slides aligned to
the lesson's instructional progression and written to the secondary-school audience.

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
