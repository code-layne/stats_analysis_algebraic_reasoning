# Conventions

Extracted from the `shared/saar-*.sty` packages. The live project is always the source of
truth — if the styles diverge from this, follow the package.

The style packages, the box vocabulary, and the five conventions below were ported from the
Algebra, Trigonometry, and Data Analysis course (2026-08-05) with the prefix changed to `saar`
and the course title changed; the royal-blue / gold palette carried over unchanged. That course
had in turn taken them from Linear Algebra and, before that, Algebra 2. The conventions are
battle-tested; adopt them from lesson 1.1 onward rather than rediscovering them.

## Style packages

| Package | Purpose | Required by |
| --- | --- | --- |
| `saar-colors` | Color palette (loads `xcolor`) | everything |
| `saar-article` | Article preamble: geometry, lists, fill-in helpers, page header, name rows, **course macros** | student components |
| `saar-boxes` | All `tcolorbox` environments, plus `\boxguard`, the `work` environment and `teachernote` | components + lesson plan |
| `saar-key` | Answer macros (`\ans`, `\ansline`, `\vocabans`) + makes `work` blocks visible; requires `-boxes` | answer keys |
| `saar-beamer` | Slide theme (`\royalheader{}`, `\sectionlabel[color]{}`) | `slides/` |

The `slides` component requires `shared/saar-beamer.sty`, which is already in place. If any
style file is ever copied in from another course, change its internal
`\ProvidesPackage`/`\RequirePackage` names to `saar-*` and its color names to this palette
before using it.

## Per-document-type preambles

**Student component** (warmup, notes, activity, exit_ticket, homework, cover):
```latex
\documentclass[10pt]{article}
\usepackage{saar-article}
\usepackage{saar-boxes}
% cover also: \usepackage{ltablex}\keepXColumns
```

**Answer key** (the matching `_key` directory):
```latex
\documentclass[10pt]{article}
\usepackage{saar-article}
\usepackage{saar-key}     % pulls in -boxes; do NOT also load -boxes
```

**Lesson plan** (`main.tex` at the lesson root): loads `-boxes` and `graphicx`. The course
macros `\CourseName` and `\MeetingLength` are defined in `saar-article.sty`, so
the plan defines only the lesson-specific ones:
```latex
\newcommand{\UnitNumberName}{Unit 3: <Unit Title> \quad}
\newcommand{\LessonNumberName}{Lesson 3.2: <Lesson Title>}
```

The `\TallMath` helper for tall inline math is defined per-document where needed (the
scaffolder includes it):
```latex
\newcommand{\TallMath}[1]{$\displaystyle #1\rule[-1.4em]{0pt}{3.2em}$}
```

## Fill-in helpers (from `-article`)

| Macro | Effect |
| --- | --- |
| `\blank{width}` | Underlined gap of the given width (e.g. `\blank{4.8cm}`) |
| `\writeline` | A full-width gray rule to write on |
| `\writelines{n}` | `n` stacked write-lines |
| `\termblank{Term}` | Bold royal term + inline blank, then a write-line |
| `\termblanklong{Term}` | Bold royal term on its own line + two write-lines (vocab style) |
| `\namedateperiod` | Name / Date / Period row — **cover and unit tests only** (Namestrip) |
| `\namepartnerperiod` | Name / Partner / Period row — **not used on components**; superseded by Namestrip |
| `\pageheader{Unit X, Lesson Y.Z}{Document Type}` | Full-width royal-blue banner header (prints `\CourseHeaderName`, "Stat Analysis & Algebraic Reasoning") |

**Course macros** (`-article`): `\CourseName` is the full title, *Statistical Analysis & Algebraic
Reasoning* — use it on covers and title slides. `\CourseHeaderName` is the short form the page
banner prints, so the banner and the lesson id fit on one line. `\MeetingLength` rounds out
the set.

**No year on any document.** These materials are reused year over year, so nothing printed on a
lesson plan, packet, or test may carry a school year. There is deliberately **no `\SchoolYear`
macro** — the plan's title block is `\CourseName` alone. Do not reintroduce one.

**The `\noindent` trap is fixed in the package — `vocabpar` is automatic here.** `\termblank`,
`\termblanklong` (blank) and `\vocabans` (key) each open with their **own `\par`**, so a `vocabbox`
whose intro sentence is followed by a term can no longer collide. Two courses upstream this was a
per-lesson hand fix; it is structural in the packages this course inherited, so there is nothing to
do. **Do not add `\par\vspace{2pt}` after a vocab intro sentence** — it is now redundant, and
it adds a second paragraph break.

The macros also close with `\par\addvspace{…}` rather than the older `\\[…]`. A `\\` immediately
followed by the next term's `\par` emits an underfull `\hbox` per term; ending the paragraph
properly is quieter and correct.

## Box environments (from `-boxes`)

Lesson-plan boxes take a background color as the last argument (use the aliases `goldbox`,
`greenbox`, `redbox`, or palette colors like `mist`); the frame/header is royal by default:
```latex
\begin{skillbox}[Priority Ideas \& Skills]{goldbox} ... \end{skillbox}   % breakable
\begin{fixedskillbox}[Spiral Review]{mist} ... \end{fixedskillbox}      % no page break
```

Titled student boxes (title is fixed by the environment unless it takes an argument):

| Environment | Title / use | Arg |
| --- | --- | --- |
| `objectivebox` | "Primary Objective" | — |
| `learningtargetbox` | "Learning Targets — I Can…" (cover sheet) | — |
| `vocabbox` | "Vocabulary & Key Concepts" | — |
| `hookbox` | "Hook" | — |
| `notesbox{Title}` | generic titled notes section | title |
| `practicebox` | "Guided Practice" | — |
| `spiralbox` | "Connections & Big Ideas" | — |
| `scenariobox[Title]{color}` | activity/homework scenario | title, color |
| `headlinebox{color}` | colored callout strip | color |
| `blurbbox[Title]{color}` | study/excerpt blurb | title, color |
| `reflectionbox` | "Reflection" (homework) | — |
| `extensionbox` | "Extension — optional" | — |
| `tocbox` | "What's in This Packet" (cover) | — |
| `remindbox` | "Keep in Mind" (cover) | — |

## The five conventions — and the order they run in

Found the hard way on the Algebra 2 course, carried through Linear Algebra and Algebra/Trig/Data
Analysis, and ported here with the styles. They exist for one outcome: **every component is the
same number of pages blank and keyed**, so the student packet never carries a padding page, and no
box breaks leaving a stub.
This course starts with all five in force — the scaffolder emits namestripped skeletons and the
`work`/`teachernote`/`boxguard` machinery is already in `saar-boxes.sty`, so there is nothing to
retrofit as long as you author to them.

How each is enforced here:

| # | Convention | Enforcement |
| --- | --- | --- |
| 1 | **vocabpar** | **Automatic.** The term macros carry their own `\par` — it cannot be violated |
| 2 | **teachernote** | Scaffolder seeds the notes in the plan; **`make check` fails** on one in a key |
| 3 | **namestrip** | Scaffolder emits no name row; **`make check` fails** on one in a component |
| 4 | **work rule** | `work` is one code path for blank and key; **`make check` fails** on a page mismatch |
| 5 | **boxguard** | Judgment call — `\boxguard` is available everywhere, but **nothing detects a missed one** |

So four of the five are now caught by the build (see "The convention gate" below). **boxguard is
the one that still needs your eyes** — a stranded stub is not a page-count error, so `make check`
cannot see it. Look at the PDF.

**When reviewing or revising a lesson, execute them in this order:**

> **1. teachernote → 2. namestrip → 3. work rule → 4. boxguard**

vocabpar is no longer a step — it is structural. The order of the rest is not arbitrary: the first
three all change how much vertical space a component takes, and **boxguard repairs the pagination
they disturb**, so it runs last. teachernote and namestrip both *remove* material; the work rule
re-matches blank to key once the lengths have settled. Re-measure after each step rather than
trusting a verdict recorded against earlier box heights — a "this guard costs a page" verdict is
only valid for the box heights it was measured against.

Each convention is documented in its own section below. The retrofit path in `SKILL.md` still
applies: if a lesson is ever authored before a convention is checked, bring it forward **by
name**, one lesson at a time. **There is no bulk sweep** — a project-wide pass would re-flow the
pagination of every already-verified lesson at once.

### 1. vocabpar — paragraph breaks in the vocab box — ENFORCED IN THE PACKAGE

A bare `\noindent` is a no-op mid-paragraph, so a `vocabbox` intro sentence and the **first** term
used to run together on one line, in the blank and the key alike, and every lesson carried a
two-line hand fix.

**That fix is now in the macros.** `\termblank`, `\termblanklong` ([saar-article.sty]) and
`\vocabans` ([saar-key.sty]) each open with their own `\par\addvspace{2pt}` and close with
`\par\addvspace{…}`. Write the vocab box plainly:

```latex
% blank and key alike — no \par\vspace needed, and adding one double-spaces the box
Fill in each term as we build it together.
\termblanklong{First term}        % \vocabans{First term}{…} in the key
```

It was made structural two ports back, in a course that had no built lessons at the time — upstream
of that, patching a shared macro would have re-flowed dozens of already-verified lessons at once.
It arrives here already fixed. Treat the term macros as frozen: this course will accumulate built
lessons, and re-flowing them is exactly the cost the fix was timed to avoid.

**Still watch for the same collision elsewhere**: anywhere an `\ansline` or `\writeline` is followed
by some *other* `\noindent`-opening construct, the run-together can recur. The term macros are
fixed; the pattern is not universally.

### 2. teachernote — teacher prose in the lesson plan, never in a key

A `teachernote` is the one block in a key with no counterpart in the blank, so it makes the key
longer than its blank for no student-facing reason. **Teacher-only prose belongs in the lesson
plan**, which is teacher-facing already and sits outside the page-matched packet.

The plan closes with one note per component, in packet order, each titled for it:

```latex
\begin{teachernote}[Warm-Up]        ... \end{teachernote}   % → "Teacher Note: Warm-Up"
\begin{teachernote}[Guided Notes]   ... \end{teachernote}
\begin{teachernote}[Group Activity] ... \end{teachernote}
\begin{teachernote}[Exit Ticket]    ... \end{teachernote}
\begin{teachernote}[Homework]       ... \end{teachernote}
```

**There is no exemption — this applies to assessment keys too.** A unit test's answer rationale
and Part D scoring go on **page 2 of `unitXX/unit_cover_key/main.tex`**, not at the foot of
`practice_test_key`/`actual_test_key`. That document shares its page 1 with the student cover by
`\input`-ing the same `unit_cover/body.tex` (so the two can never drift) and is merged by
`shared/unit.mk` into the **key packet only** — which matters, because the practice test *is*
bound into the student packet, and its rationale must not ride along. One unit, one notes page:
cover + notes = a single double-sided sheet. A unit with no `unit_cover_key/` falls back to the
plain cover in both packets. The course finals (`finals/*_key/`) are merged into no packet at
all and have no cover, so their scoring notes stay in the key.

The environment lives in **`saar-boxes`** (the lesson plan does not load `-key`) and the title
argument is **optional** — a bare `\begin{teachernote}` renders plain "Teacher Note". If a note
ever ends up in a `_key`, migrate that lesson:

```bash
python3 .claude/skills/lesson-planning/scripts/movenotes.py unit03/lesson02
```

It lifts the note out of each `_key`, appends it to the plan with the right title, and refuses to
run twice on the same lesson. `--check` reports without changing anything.

### 3. namestrip — the name/date/period row belongs on the cover only

When a review says "lesson 3.2 needs a namestrip," the name/date/period row is repeating on
components stapled *behind* the cover sheet. The student writes their name once; every repeat costs
vertical space at the top of a page — space that matters most on the warm-up and exit ticket, which
are held to one page.

Strip `\namedateperiod`/`\namepartnerperiod` from `warmup`, `notes`, `activity`, `exit_ticket`,
`homework` **and from all five `_key` files**, which stay in lockstep. Two exemptions:

- **`cover/`** — the one place the row belongs. Never strip it.
- **`unitXX/tests/` and `test_keys/`** (and `finals/`) — taken in a testing setting, not stapled
  behind a lesson cover, so they keep the row.

Apply it with the script — it skips `cover/`, hits blanks and keys together, and is idempotent:

```bash
python3 .claude/skills/lesson-planning/scripts/namestrip.py --project . --unit 03 --lesson 02
python3 .claude/skills/lesson-planning/scripts/namestrip.py --project . --unit 03 --lesson 02 --check
```

`--check` writes nothing and exits 1 if it finds anything, so it doubles as a review gate. Rebuild
afterward and confirm the warm-up and exit ticket are **still 1 page**, blank *and* key.

**Going forward this is automatic:** `new_lesson.py` and the worksheet skeletons no longer emit a
name row, so newly scaffolded lessons are born namestripped. Namestrip is **not always free** —
on a retrofit it can reclaim enough space that the *key* fits a box the blank still pushes, opening
a mismatch that a `\boxguard` then closes. That is why it runs before boxguard, never after.

### 4. The work rule — `\begin{work}` (defined in `-boxes`, visible under `-key`)

**Any worked solution goes in a `work` block, and that block is byte-identical in the blank and the
key.** The package swap decides only whether it is shipped: under `-boxes` the blank builds the box
and emits a `\vphantom` of it (exact height, no ink and nothing in the PDF's text layer); under
`-key` the same box prints in `keyred`. The two therefore *cannot* drift — which is what keeps a
component the same length on both sides.

```latex
% notes/main.tex AND notes_key/main.tex — the same lines in both files
\begin{work}
  \tan 34^\circ &= \dfrac{h}{62} \\
              h &= 62\tan 34^\circ \\
              h &\approx 41.8 \text{ feet}
\end{work}
```

Format, non-negotiable:

- **One statement per line.** Never two steps on one row, and never an inline
  `a=b \Rightarrow c=d` chain — that is the idiom this rule replaces.
- **The `&` goes immediately before the relation**, so every relation in the block lands in one
  column. Works for `=`, `<`, `>`, `\le`, `\ge`, `\Rightarrow`.
- **Simplifying:** row 1 is the original expression, the relation, and the first simplification;
  every later row starts at the `&=` and aligns to the one above.
- **Solving:** one row per step, each aligned on its relation.

Do not wrap a `work` block in `\[ \]`, `align`, or `equation` — it supplies its own display. It is
set flush left (2em indent), not centered.

**When it applies:** a task that asks for multi-step work. A table cell holding a single final
answer is already the same size in both files — leave those as `\blank{}`/`\ans{}`. `work` blocks
do not go inside table cells; if a table asks for real work, pull the items out of the table.

`\workrowsep` (default `0pt`) adds leading between rows. It moves the blank and the key together,
so raising it for handwriting room can never break the match.

**Reach for `work` before `\writelines`.** The other place lengths drift is a prose `\ansline` that
wraps to four lines against a one-line `\writeline`; the fix there is `\writelines{n}` in the blank,
sized from the key's true wrapped length. But if the answer is a multi-step computation, `work`
fixes it correctly and cannot come apart, while a lengthened write-line only papers over it. Note
`\writelines{n}` occupies **n+1** line slots (it ends in `\\`), so raising one is not free —
re-measure the blank after any change.

### 5. boxguard — the page-break rule

When a review says "lesson 6.2 has a boxguard problem on page 4," a box broke across a page leaving
roughly an inch — a title plus a line or two — at the **top or bottom** of a page. **Push the whole
box to the next page.** Breaking a box is fine only when each side of the break gets a substantial
chunk. The white space you give up is cheaper than a stub that reads as a printing mistake.

`\boxguard` is defined in `shared/saar-boxes.sty` (so it reaches every key through
`saar-key.sty`) — no per-file preamble needed:

```latex
\boxguard                      % default: needs 16 lines of room, else break
\begin{notesbox}{2. ...}

\boxguard[30]                  % box OPENS with an unbreakable TikZ/pgfplots figure or tabularx
\begin{notesbox}{3. ...}
```

Prefer `\boxguard` to a hard `\newpage` — it self-adjusts when content above it changes. Apply
every guard to the blank **and** its `_key`, then rebuild and confirm the page counts did not move.

Two limits, both learned on the Algebra 2 course:

1. **`\boxguard` is inert inside a breakable `tcolorbox`** — `\needspace` measures the outer page
   while tcolorbox splits its own assembled vbox afterwards. To force a split at a chosen point
   *inside* a breakable box, use tcolorbox's own **`\tcbbreak`**. It is unconditional, so mirror it
   in the blank and the key and re-check both page counts.
2. **A guard that costs a page also costs the blank/key match — but the page can often be bought
   back.** Before declining a guard, measure the overflow: a few lines of mirrored table stretch
   (`\arraystretch` 1.7→1.5, `itemsep` 4pt→3pt) is usually cheaper than the stub.

**Boxguard is opt-in and nothing detects a missed one — this is the one convention `make check`
cannot enforce.** A stranded stub is not a compile error, does not change any page count, and
`make` still exits 0, so violations surface only when someone looks at the PDF. **Look at the
PDF.** A "guard costs a page" verdict is valid only for the box heights it was measured against —
re-measure rather than trusting a prior refusal.

## The convention gate — `make check`

`make all` exits 0 on a key that runs a page longer than its blank, on a two-page exit ticket, and
on `\ans` buried in math. `make check` is what turns those into build failures:

```bash
make -C unit03/lesson02 check     # one lesson
make -C unit03 check              # every lesson in the unit
make check                        # the whole curriculum
```

It builds first (the page checks read the compiled per-component PDFs), then reports **every**
violation in one pass and exits 1 — so it works as a review gate, not just a smoke test. What it
enforces, all defined in `shared/lesson_check.py`:

| Check | Fails when |
| --- | --- |
| **page parity** | a keyed component's page count ≠ its `_key`'s (the work rule's observable consequence) |
| **one-pagers** | `warmup` or `exit_ticket` is not exactly 1 page, blank **or** key |
| **ans-in-math** | `\ans` / `\ansline` / `\vocabans` appears inside `$…$`, `\[…\]`, or `\(…\)` |
| **teachernote** | `\begin{teachernote}` appears in a lesson component's `_key` |
| **namestrip** | a live `\namedateperiod` / `\namepartnerperiod` appears on a worksheet component |

The source checks skip LaTeX comments and understand escaped `\$`, so legitimate usage —
`\ans{$\sqrt{n}$}`, `\ansline{$41.8$ feet}`, `\$5` — does not trip them. `vocabpar` is not checked
because it cannot be violated; `boxguard` is not checked because it is invisible to any count.

Run it standalone (source checks only, no build required) with:

```bash
python3 shared/lesson_check.py unit03/lesson02 --no-pages
```

**Unit tests and `finals/` are outside the gate** by design — the gate walks `unitXX/lessonMM/`
only, and those blanks legitimately carry a name row. That is a limit of the checker, **not an
exemption from the conventions**: a unit test key must still carry no `teachernote` (its scoring
notes belong on page 2 of `unitXX/unit_cover_key/`) and must still paginate identically to its
blank, because `unit.mk` swaps `sample_test_key` in for `sample_test` at the tail of the key
packet. Check both by hand. Only `finals/*_key/`, merged into no packet at all, keeps its
scoring notes in a `teachernote`.

## Answer-key macros (from `-key`)

| Macro / env | Effect |
| --- | --- |
| `\ans{text}` | Inline answer in bold `keyred`; use in place of a blank |
| `\ansline{text}` | Bold `keyred` answer that fills a write-line with a dotted trail |
| `\vocabans{Term}{definition}` | Keyed vocabulary entry — the counterpart of `\termblanklong` |
| `work` (env) | Worked steps — **defined in `-boxes`**, authored identically in both files; see the work rule |

**`teachernote` is no longer a key macro.** It lives in `-boxes` and belongs in the **lesson plan**
— see convention 2 above.

`\ans` is a **text-mode** macro (`\textcolor{keyred}{\textbf{#1}}`). Never place it inside
`$...$`; wrap math fragments instead (`\ans{$\hat v$}`, `\ans{$\sqrt{n}$}`), and never let it
span a blank line.

**Key-authoring rule:** copy the blank component verbatim, then replace each blank/`\writeline`
with `\ans{…}`/`\ansline{…}` and mark correct multiple-choice options, e.g.
`\textcolor{keyred}{\textbf{$\leftarrow$ correct}}`. The key and blank must stay structurally
identical so they paginate the same way.

## Color palette (from `-colors`)

**Royal blue is the dominant color; gold is the secondary accent.** This is the *only* set of
defined colors — using any other name is a compile error:

- **Royal family (primary):** `royal` (#1D3F94), `royallight` (#3A62C4) — box frames/headers,
  the `\pageheader` banner, and term labels.
- **Mist tints (paired backgrounds):** `mist` (#EEF3FC), `mistmid` (#BFD3EF) — light backgrounds
  under royal frames (objective / learning-target / reflection boxes) and the banner subtitle.
- **Gold:** `goldacc` (#C8860D), `goldbg`, `hookbg` (#FDF4E3) — Hook, Extension, Keep-in-Mind.
- **Plum:** `plumacc` (#6B3FA0) on `plumbg` (#F3EEFA) — `practicebox` ("Guided Practice"). It is
  deliberately *not* blue, so guided practice reads as distinct from the royal notes boxes.
- **Green:** `greenbg`/`greenacc` — Vocabulary.
- **Red:** `redbg`/`redacc` — available as a `scenariobox`/`blurbbox` color.
- **Neutrals:** `charcoal`, `slate`, `graybg` (#F1F4F8, the `teachernote` background),
  `linegray`. **Answer red:** `keyred` (#CC0000).
- **Lesson-plan background aliases:** `bluebox`, `goldbox`, `greenbox`, `redbox`, `plumbox`.

There are **no deprecated aliases** — `burgundy`, `blush`, `navy`, `sky`, `royalblue`, and
`skyblue` are all undefined here. If you paste material in from another course, translate its
colors first.

The **Beamer theme overrides three colors** for dark slide backgrounds: a brighter `royal`
(#27509F), `goldacc` (#F5A623), and `hookbg` (#D4820A). That is intentional — do not sync them
back to `-colors`.

## Lesson-plan section order (canonical)

Primary Objective → Priority Ideas & Skills → Vocabulary, Concepts & Theorems → Activate
Prior Knowledge & Spiral Review (embeds the warm-up thumbnail if prefab) → Hook → Lesson (and
"Lesson (cont.)") → Explicit Instruction (one box per technique) → Active Monitoring →
Group Work & Differentiation (Tiers R / A / E) → Individual Work & Assessment (Exit Ticket +
a conceptual/justification check) → Reinforcement & Extension (Homework + Extension +
Preview). Keep the Primary Objective in plain student terms — what they can do, model,
interpret, and justify with the topic.

**Tag the standards.** This is a standards-driven course: the Priority Ideas & Skills box and the
Connections line both carry the lettered standard codes the lesson covers. The course map and the
code set it draws on are still being planned — see `course-workflow.md`.
