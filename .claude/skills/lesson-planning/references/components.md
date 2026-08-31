# Components

The spec for authoring each file after scaffolding. The scaffolder (`scripts/new_lesson.py`)
gives you a correctly-preambled skeleton with TODO markers; this file says what fills them.
**Always also open lessons 1.0 and 1.1 as the gold reference** — these specs summarize the
pattern, but the live project is authoritative. For macros and boxes
see `references/conventions.md`; for where content comes from, `references/course-workflow.md`.

Contents: [Lesson plan](#lesson-plan) · [Cover](#cover) · [Warm-up](#warm-up) ·
[**Guided notes**](#guided-notes) · [**Group activity**](#group-activity) · [Homework](#homework) ·
[Slides](#slides) · [Dead shapes](#dead-shapes) · [Answer-key discipline](#answer-key-discipline)

**A new lesson is `cover` + `warmup` + `notes` + `activity` + `homework` + `slides`.** That is
the gradual-release shape. The **debrief is a phase, not a component** — it lives in the lesson
plan and the deck only — and **there is no exit ticket**. `experience/` (the scrapped EFFL
component) and `exit_ticket/` still build if a lesson has them, but do not author either.
See [Dead shapes](#dead-shapes).

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
   **Warm-Up 5 · Guided Notes & Practice 20 · Group Activity 18 · Debrief 7 · Close & Assign 5.**
   `fixedskillbox` because a `tabularx` must not split. Place it after the Vocabulary box and
   before Activate Prior Knowledge. **This table is a contract** — the Lesson box's per-section
   minutes must sum to 20, and the activity must be workable in 18.
7. **Hook** — `skillbox{frost}`: what goes on the board before anyone sits down, the question to
   ask, and what to do with the answers. End it *unresolved* when the lesson's crux is a
   misconception the notes will settle.
8. **Lesson — Guided Notes (20 min)** — `skillbox{frost}`, `multicols{2}`: one bolded paragraph
   per notes section, **each carrying its own minute budget**, saying what to model (*I do*),
   what to fill in with the class (*we do*), and what to release (*you do*). Name which section
   is **the lesson** and which to compress if you run behind.
9. **Explicit Instruction: \<the core move\>** — `skillbox{frost}`, a two-column `tabularx`:
   numbered **steps to give verbatim** beside one fully **worked example**, plus a contrast case.
10. **Active Monitoring** — `skillbox{redbox}`: misconceptions keyed to item numbers across the
    notes *and* the activity; the answers to reject; cold-call prompts.
11. **Group Work (18 min)** — `skillbox{redbox}`: one paragraph on **the arc** (which items are
    the fast on-ramp, which is the **crux**, which is hardest), then the **circulation prompts**
    (questions and cues, not answers) keyed to item numbers, and **which student work to display
    for the debrief**. No tiers to describe — everyone works the same items.
12. **Debrief (7 min) — what goes on the board** — `skillbox{frost}`: the ordered walkthrough of
    the displayed work (students correct their own in a second color), a **whole-class cold check
    for understanding** with its correct answer, and the **formative read** — the three piles to
    sort responses into and how the next lesson opens from them. This replaces the exit ticket.
13. **Reinforcement & Extension** — `skillbox{goldbox}`: the ~6 homework items and what each
    targets, how it is scored and when it is due, **whether today's practice is the packet pages
    or the DeltaMath override**, the optional extension, the next-lesson preview, and the
    **Connections** line carrying the lettered standard codes covered.
14. **Teacher notes** — `\begin{teachernote}[Component]`, one per component in packet order:
    **[Warm-Up]**, **[Guided Notes]**, **[Group Activity]**, **[Homework]**. Four notes — there is
    no note for the debrief, which is fully specified in its own box. Teacher prose lives here and
    **never** in a `_key`.

## Cover

`cover/main.tex` — student-facing front page of the packet. No key. Structure:
- Full-bleed cerulean banner (tikz) with `\LARGE` course name, unit, and `Lesson <id>  <title>`.
- `\namedateperiod` — the cover is the **one** component that carries it (namestrip).
- `learningtargetbox` — an "I can…" list, one target per priority idea/skill, **naming the
  formal vocabulary outright**. The lettered standard codes belong in the lesson plan, not here.
- `tocbox` — a `tabularx` listing each packet component (#, Component, Description, Score blank)
  with a Total row — **four rows**:

  | # | Component | Description | Score |
  |---|---|---|---|
  | 1 | Warm-Up | what the spiral items rehearse | `\blank{1.2cm}` |
  | 2 | Guided Notes | the ideas the notes build, in order | `\blank{1.2cm}` |
  | 3 | Group Activity | *Activity Title* — the data set or scenario | `\blank{1.2cm}` |
  | 4 | Homework | the new context, one line | `\blank{1.2cm}` |

  **Homework is scored**, so its score cell is a `\blank{}` — never `NA`. The row never changes
  with the packet-vs-DeltaMath choice; that is announced aloud at Close & Assign.
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

`notes/` (+ `notes_key/`) — **the heart of the lesson**: the direct-instruction handout the class
fills in together. Budget **≤ 4 pages**, **20 minutes**, blank and key. Structure, in order:

- `\pageheader{Unit X, Lesson Y.Z}{Guided Notes}` — **no name row** (namestrip).
- `objectivebox` — "By the end of this lesson, I will be able to…" **filled in, not blank.** One
  per priority idea/skill, worded exactly as the cover's learning targets. Not a fill-in — no
  `\writeline`s here, and the key carries identical text (which also makes it parity-proof).
- `vocabbox` — `\termblanklong{Term}` per key term; the key uses `\vocabans{Term}{definition}`.
  Write the intro sentence plainly: the term macros carry their own `\par` (vocabpar is enforced
  in the package), so **do not** add `\par\vspace{2pt}` — it double-spaces the box.
- `hookbox` — the same hook as the plan, with `\writelines{2}` for the student response. When the
  hook is a claim the lesson will demolish, state it and **leave it unresolved**.
- **4–6 numbered teaching sections**, each a `notesbox{N. Title}`, with `\blank{}` and
  `\writeline` at the points where students record a definition, a step, or a result, and
  `work` blocks for multi-step computations. Build every example from a **context**, and reuse
  one data set across several sections rather than introducing a new one each time.
  - Sequence them so the **crux section is earned, not announced**: set up the misconception,
    take a vote or a commitment, *do not settle it*, then settle it in the crux section with a
    correct computation that produces a worthless answer. The plan says which section is which.
  - Number them in the text (`1.`, `2.`, …) so the plan's Lesson box and the deck can refer to
    them by number.
- A closing `practicebox` — the **you-do** release. `practicebox` takes **no argument** (its
  title is fixed as "Guided Practice"). Put a *second instance of the lesson's trap* here, and
  pre-work the arithmetic in a `work` block so the release is spent on the classification and
  the interpretation sentence, not on computation. End with an **interpret-in-context** line.

**Pagination.** Guard the first `notesbox` after the `vocabbox` with `\boxguard[20]` in **both**
files — the key's `\vocabans{}` runs shorter than the blank's `\termblanklong{}` rules and will
otherwise float that section onto page 1 in the key only, silently desynchronizing the packet.
Raise `\boxguard` to ~30–40 before any section opening with an unbreakable `tabularx`. Never let
a lead-in sentence be orphaned from the table it introduces — `\nopagebreak` after it.

## Group activity

`activity/` (+ `activity_key/`) — **one activity for the whole class**, worked in **groups of
three**, **18 minutes**, *after* the notes, so students already hold the vocabulary. Budget
**≤ 2 pages**, blank and key. **There are no tiers**: nothing is assigned, nothing is sorted, and
every group works the same items.

- `\pageheader{Unit X, Lesson Y.Z}{Group Activity}` — **no name row** (namestrip).
- A `headlinebox{frost}` naming the investigation and stating the two standing rules: **every
  answer needs a reason**, and **every conclusion names the group it applies to**.
- **One shared data set**, printed once, above the item boxes.
- Set it in a **fresh context** — not the one the notes just worked. Same skills, new data.
- **~6–7 items in two labelled `tcolorbox`es** (`colback=white, colframe=black!40, breakable`),
  split at a real phase change — *Part 1 — Read the data* / *Part 2 — Judge the claim*, or
  *Part 1 — Run the cycle* / *Part 2 — A second study, then two that failed*. Continue the
  numbering with `\begin{enumerate}[..., start=N]`.
  - **Put `\boxguard[30]` before Part 2.** That split is what lets the blank and the key break
    in the same place; with one long box there is no lever, because `\boxguard` is inert inside
    a breakable `tcolorbox`.
- **Differentiate by depth, not by handout.** Items 1–2 must be readable straight off the data so
  every group is writing within two minutes; the middle items compute and demand a sentence
  naming the group and the units; then **the crux item**, which is the misconception the notes
  set up. Put the single hardest item last.
- Close with an optional **`extensionbox`** ("Extension — optional") of one or two items for
  groups that finish early. Expect two or three groups to reach it and none to finish it. The
  lesson plan says to pose its best item aloud in the debrief if nobody got there.
- **Size it for one group, not three.** Everyone works the same set, so ~6–7 items is the 18-minute
  budget. A merged three-tier activity (12+ items) is roughly triple what the block holds.
- Prefer inline blanks over tall tables at the end of a box: a 5-row `tabularx` closing the last
  box is the single most common cause of a stranded one-inch stub on a third page.
- Key mirrors exactly, filling with `\ans{...}`, carrying every `work` block and `\boxguard`
  over unchanged, and marking correct MC options with
  `\textcolor{keyred}{\textbf{$\leftarrow$ correct}}`.

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

**Packet or DeltaMath.** The packet pages are authored for every lesson regardless. Which form the
assignment takes is decided **lesson by lesson** by the teacher at Close & Assign, based on whether
DeltaMath carries adequate content for that lesson's skills; when it does, students keep the packet
pages as a worked reference instead. Nothing about what you author changes — say the choice in the
lesson plan's Homework box and on the deck's closing frame, and leave the cover row alone.

## Dead shapes

Two component shapes survive in the tree but must never be authored into a new lesson.
`shared/lesson.mk` still merges both, so any lesson carrying them keeps building, and the
scaffolder still accepts them by name (`--components ...,experience,exit_ticket`) so one can be
patched. For how to convert such a lesson, see the Retrofit section of `SKILL.md`.

- **`experience/` (+ `experience_key/`)** — the scrapped EFFL in-class component: one 12pt
  document in three parts (Activity · QuickNotes · Application) using an `\answerspace{H}{}`
  macro instead of write-lines. The EFFL trial ran 2026-08-29 to 2026-08-31 and was rejected by
  students. When converting, QuickNotes expands back into taught notes sections, the Application
  becomes the notes' `practicebox`, and the Activity becomes the group activity in a fresh
  context.
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
`\sectionlabel[redacc]{}`) → practice → group-activity launch (the shared data set, the item
range and timing, the two standing rules) → debrief → close & assign. The notes frames carry the *answers*
the class arrives at, so they are the board, not a preview — advance them in step with the
handout. **Do not put the group activity's own items on a slide before the activity**; a deck
that lists the answers pattern turns the activity into copying. The closing frame names what changed
today, then the assignment and plainly which form it takes — the packet pages or the DeltaMath
override — with the due date and how it is scored. Written to the secondary-school audience
throughout.

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
