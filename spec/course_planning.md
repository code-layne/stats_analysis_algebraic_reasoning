# Course Planning Log — Statistical Analysis & Algebraic Reasoning

**Last updated:** 2026-08-05 — **Lesson 1.0 authored, built, and gated** (the course's first
real lesson and the model for the rest), and the **course palette was replaced**: royal blue
→ **cerulean**, renamed across the whole tree.

## Current state

### Palette — CHANGED 2026-08-05 (user decision)

The scaffold had copied Algebra/Trig/Data Analysis's royal blue (`#1D3F94`) **verbatim**, so the
two courses were visually identical. The dominant color is now **cerulean `#0B6FA4`** — the third
blue across the stats-family courses, separated by *hue* so it survives a photocopy:

| Course | Dominant | Hex |
|---|---|---|
| AP Statistics | navy | `#1F3A5F` |
| Algebra, Trig & Data Analysis | royal | `#1D3F94` |
| **Statistical Analysis & Algebraic Reasoning** | **cerulean** | **`#0B6FA4`** |
| Algebra 2 | forest | `#1E5631` |
| Precalculus | plum | `#4B2A6C` |
| Linear Algebra | burgundy | `#6B2137` |

- Names renamed tree-wide (895 files): `royal`→`cerulean`, `royallight`→`ceruleanlight`,
  `mist`→`frost`, `mistmid`→`frostmid`, `bluebox`→`frostbox`, `\royalheader`→`\ceruleanheader`.
- **No deprecated aliases** — the old names are undefined, so a stale reference fails loudly.
- Unchanged: gold accent, green vocab, red, plum `practicebox` (deliberately not blue),
  `graybg` teachernote, `keyred`.
- Beamer override: brighter cerulean `#1785BF` for dark slides.
- Contrast checked: white on cerulean **5.49:1** (WCAG AA, normal text).
- `.claude/skills/lesson-planning/` docs (SKILL.md, conventions.md, components.md) and
  `new_lesson.py` were all updated to match — new scaffolds emit cerulean.

*(An earlier pass in this session briefly ported Linear Algebra's burgundy palette before the
user redirected to a third blue. No burgundy remains in the tree.)*

### Lessons

- `spec/statistical_analysis_algebraic_reasoning.md` is the **confirmed** course map: 8 units,
  58 content lessons + one Lesson 0 per unit (66 lesson dirs), semester split after Unit 4.
- **Lesson 1.0 — "Unit Launch: Study Design" — is COMPLETE.** All components authored, built,
  and passing the gate. It is the **model lesson**; mirror its structure and voice.
  - Standards: **PS.DC.1a–c; AFDA.DA.2a** (previews PS.DC.1d–e, PS.DC.2, PS.DC.3).
  - Scope: data-in-context (who/what/units), individuals vs. variables, **categorical vs.
    quantitative**, the numbers-that-are-really-labels trap (grade level, jersey #, ZIP),
    statistical questions, and a preview of the 4-stage data cycle. The cycle is *previewed*
    only — Lesson 1.1 teaches it formally.
  - Contexts: Riverbend HS Student Life Survey (notes), Riverbend Athletics (activity),
    Northgate Recreation Center (homework). All arithmetic verified in Python.
  - Page counts: warmup 1/1, notes 4/4, activity 2/2, exit ticket 1/1, homework 2/2;
    plan 5pp, slides 9 frames.
  - `make -C unit01/lesson00 all` exits 0; `make -C unit01/lesson00 check` **passes**.
- **All other 65 lesson dirs are unmodified skeletons** (now cerulean). Unit tests/test keys
  are skeletons too.
- Per-unit progress: **U1: 1 of 9 authored (lesson00)**; U2–U8 scaffolded, 0 authored.
- Key design decisions (user-confirmed 2026-08-05): AFDA.AF.3 excluded; no trig; polynomial/log
  from A2.F.1/A2.F.2; counting = two lessons (3.7, 3.8); projects close U1, U5, U6, U7 + U8
  capstone; every unit gets a `lesson00/` launch outside the 8-content-lesson cap.

## Next steps

1. **Author Unit 1 Lesson 1.1** — "The statistical cycle; formulating questions; types of data"
   (PS.DC.1a–c; AFDA.DA.2a). Mirror lesson00's structure. It must teach the **four stages
   formally** (lesson00 only previewed them) and can assume the vocabulary lesson00 established:
   individual, variable, categorical, quantitative, statistical question.
2. Then scale out through Unit 1 (1.2–1.8), building + `make check` per lesson.
3. Author the Unit 1 practice/actual tests once its lessons exist, plus `unit01/unit_cover/` and
   `unit_cover_key/` (the test rationale/scoring page).
4. Open a PR for the lesson-1.0 + palette work on branch `claude/lesson-planning-generate-3d9e93`.

## Gotchas found this session

- **`sed -i '' -e 's/\bfoo\b/'` silently does nothing on macOS** — BSD sed has no `\b`. Use
  `perl -pi -e` for any word-boundary rename.
- `\ansline` answers longer than ~90 characters wrap and break blank/key page parity. Keep them
  to one line, or reserve a second `\writeline` in the blank.
- `\boxguard` defaults to 16 baselines, which over-refuses for a short box. Size it to the box:
  `\boxguard[12]` for a ~10-line box like `hookbox`.
