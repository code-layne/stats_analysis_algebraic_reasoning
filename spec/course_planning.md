# Course Planning Log — Statistical Analysis & Algebraic Reasoning

**Last updated:** 2026-08-05 — Course map confirmed by the user and the **entire
course scaffolded**: all 8 units, 66 lesson dirs (lesson00 launch + content
lessons per unit), unit test/test_keys/sample_test dirs, root + unit Makefiles.
`make -C unit01/lesson01 all` and `make -C unit01/lesson01 check` both pass on
the raw skeletons.

## Current state

- `spec/statistical_analysis_algebraic_reasoning.md` is the **confirmed** course
  map: 8 units, 58 content lessons + one Lesson 0 per unit (66 lesson dirs),
  statistics-heavy (6 stats units, 2 algebra/modeling units), semester split after
  Unit 4.
- **Every lesson dir is scaffolded, none authored.** All components are unmodified
  skeletons: cover, warmup, notes, activity, exit_ticket, homework (+ their keys)
  and slides, per lesson. Unit tests/test keys are skeletons too. Nothing is
  committed to git yet — the whole tree is new files on branch
  `claude/stats-data-analysis-structure-dc9531`.
- Per-unit progress: U1–U8 scaffolded / 0 lessons authored / U1 L1 smoke-built.
- Key design decisions (user-confirmed 2026-08-05):
  - AFDA.AF.3 (linear programming) excluded — outside the course description.
  - No trig anywhere.
  - Polynomial and logarithmic content (named in the course description but absent
    from AFDA) cited from A2.F.1 / A2.F.2; curve-of-best-fit reach-ins from A2.ST.2;
    counting from AFDA.DA.3g–i / A2.ST.3.
  - Projects close Units 1, 5, 6, 7 and the Unit 8 capstone.
  - **Lesson 0 convention:** every unit gets a `lesson00/` unit-launch lesson,
    outside the 8-content-lesson cap; content lessons kept as proposed.
  - **Counting = two lessons** (3.7 techniques, 3.8 probability-with-counting);
    categorical displays merged into one lesson (3.1, PS.DS.4a–d) to stay at cap.

## Next steps

1. **Commit the scaffold** (and open a PR) — the user hasn't said to yet; ask or
   wait for their direction.
2. **Author Unit 1 Lesson 0 and Lesson 1** as the model lessons for the course
   (greenfield: these set the tone every later lesson mirrors). Read the
   PS.DC/AFDA.DA.2 "Understanding the Standards" pages first.
3. Then scale out through Unit 1, build + `make check` per lesson, and author the
   Unit 1 practice/actual tests once its lessons exist.
