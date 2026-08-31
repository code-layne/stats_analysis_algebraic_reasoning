# Course Workflow — from the standards to lessons

The course structure will come from **`spec/statistical_analysis_algebraic_reasoning.md`** — the
design notes plus the **course map**. The mathematical **content** comes from the **standards
documents in `spec/`**: units are standard clusters and lessons are groups of the standards'
lettered Knowledge & Skills. This file explains how to turn the standards into lessons and how to
source and adapt them into each lesson's parts.

> **Status: the course is not mapped yet.** `spec/` currently holds only the source standards
> PDFs — there is no `spec/statistical_analysis_algebraic_reasoning.md` and no unit map. Until
> that file exists, **the unit/lesson map is an open question for the user, not something to
> infer from the PDFs on your own.** Propose, confirm, then author. When the map is settled,
> write it into `spec/statistical_analysis_algebraic_reasoning.md` and fill in "The course units"
> below to match.

## Course identity

This is **Statistical Analysis & Algebraic Reasoning**, a secondary course pairing statistical
work with algebraic reasoning. Author it as a **modeling and applications course**: start from a
context, compute, then **interpret and justify** — "what does this number mean here, and how do
you know?" Audience is secondary school, mid-track: students who need scaffolding, worked
examples, and vocabulary support. Small numbers, concrete contexts, one new idea at a time.

Two standing rules carry over from the courses this skill was ported from, and both hold here:

- **Technology is assumed but pre-digested.** Show calculator/Desmos/spreadsheet output as a
  **pre-made figure to read and interpret**; save student keystrokes for the activity, where a
  teacher is circulating.
- **Never ask students to sketch, draw, or construct a graph from a blank page.** Give a
  pre-drawn, pre-scaled axis system to complete, a figure to read, or a table to fill in. A
  standard that says "sketch" is satisfied by pre-drawn, pre-scaled axes — reconcile the two, do
  not choose between them.

## Where the content lives

- `spec/statistical_analysis_algebraic_reasoning.md` — course design notes, the standards
  inventory, and the unit map. **This is the unit/lesson map**;
  `spec/unit_lesson_breakdown.md` is the per-lesson index and status table.
- The **approved standards PDFs in `spec/`** — the authoritative standard text and its
  **lettered Knowledge & Skills**. Those letters are the codes a lesson cites.
- The **"Understanding the Standards" PDFs in `spec/`** — the clarifications: **scope limits,
  notation, and what is out of bounds**. Read the pages for the standard you are authoring
  *before* you write anything. The standard says *what*; this says *how far*.

A practical loop per lesson: find the standard's lettered skills in the approved standards PDF →
read the matching pages of the Understanding the Standards PDF for scope and notation → choose a
**data context students can work from prior knowledge alone** → build the Activity's two scenarios
around it (scenario 2 carries the crux question) → decide which formal terms the debrief attaches
in the guided notes → build the practice box and the homework around a
compute-then-interpret-then-justify spine.

## The course units

The authoritative map is `spec/statistical_analysis_algebraic_reasoning.md`, with
`spec/unit_lesson_breakdown.md` as the per-lesson index. Read them rather than reproducing them
here — a copy in this file goes stale.

## Decomposing a unit into lessons

**Convention: one lesson per Knowledge-and-Skills cluster** — *not* one per lettered bullet. The
letters are finer than a 60-minute class; group them into coherent chunks in the order the
standard lists them. Lesson id is `<unit>.<n>` where *n* counts lessons within the unit (Lesson
3.1, 3.2, …). Always **present the proposed lesson map for the unit and confirm it with the user
before authoring** — bullets merge and split depending on the class.

The confirmed map, per unit, is a table of this shape:

| Lesson | Standards | Topic | Likely context |
| --- | --- | --- | --- |
| 3.1 | *codes* | *topic* | *the real-world setting the lesson opens in* |

Pull each lesson's scope and notation from the matching "Understanding the Standards" pages, then
write in the course's contextual, modeling-first voice.

## Mapping content into a lesson

| Lesson element | Source |
| --- | --- |
| Lesson title (`\LessonNumberName`) | "Lesson X.Y: \<Topic\>" |
| **Primary Objective** (lesson plan) | What students will be able to *do / model / interpret / justify* with this topic, in student terms |
| **Priority Ideas & Skills** (gold box) | Left: the lettered Knowledge & Skills this lesson covers, in student language. Right: "Key Understandings" — the *why*, drawn from the matching "Understanding the Standards" pages |
| **Vocabulary, Concepts & Theorems** | Terms and notation the standard introduces (use `\TallMath{...}` for tall formulas) |
| **Guided-notes context** | A scenario from the course's application domains, reused across several notes sections so one data set carries the whole lesson |
| **Group-activity context** | A *second*, fresh scenario on the same skills, so the group work is transfer rather than repetition |
| **Vocabulary-box terms** | The formal vocabulary and notation, taught outright in the notes and listed in the plan's Vocabulary box |
| **Learning Targets** (cover, "I can…") | One target per lettered skill covered, reworded as "I can …" |
| Application / homework CYU contexts | Real or realistic data and scenarios — compute *then* interpret and justify |
| Connections line | The unit's core idea, **the standard codes covered**, and links to prior/next lessons (spiral) |

**Every lesson cites its standard codes.** That is the accountability spine of a standards-driven
course. Put the codes in the lesson plan's Priority Ideas box and in the Connections line.

## Graphs, sketching, and technology

- **Pre-draw and pre-scale the axes** — grid, tick labels, guides — and have students plot,
  label, or complete on them. That satisfies "sketch the graph" and removes the setup burden that
  eats a class period.
- **Technology output** (scatterplots, regression curves, distribution plots, parameter sweeps):
  show the result as a figure to read and interpret. Put the keystrokes in the activity, not the
  notes.

Never ask for a graph sketched from a blank page, and never make a component's core skill depend
on a device the class may not have in hand.
