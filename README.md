# statistical_analysis_algebraic_reasoning

## Getting the source

`math-shared/` is a git submodule, [code-layne/math-shared](https://github.com/code-layne/math-shared),
which holds the grading package shared across the courses. It sits at the project root, not under
`shared/`: the build searches `shared/` recursively, and `math-shared/examples` holds `main.tex`
files a component build would pick up. Clone with it:

```bash
git clone --recurse-submodules https://github.com/code-layne/stats_analysis_algebraic_reasoning
```

In a clone made without `--recurse-submodules`, run `git submodule update --init` once. Ordinary
builds still work without the submodule. Only the grading targets below need it.

## Building from source

Requires [XeLaTeX](https://tug.org/xetex/), `latexmk`, `poppler` (`pdfunite`, `pdftoppm`,
`pdfinfo`), and `python3`.

```bash
make -C unit01/lesson02 all   # all five work products for one lesson
make -C unit01 student key    # merge a whole unit
make -C unit01/tests          # a unit's tests (and test_keys/ for their keys)
make all                      # build every unit
make student key              # merge the whole curriculum
```

Output lands in `target/`.

### Graded components

A component that loads `grading` (from `math-shared/grading.sty`) marks its graded answers with
`\gradedblank`. Each page then carries corner registration marks, a QR code, and a name strip.
Write each `\gradedblank` line identically in the blank and the key. The key prints the answer
inside the box (`saar-key` turns this on whenever a document loads `grading`). See
`math-shared/README.md` for the macros and `math-shared/grading-system-design.md` for the plan.

```bash
# a lesson component: manifest.json, and the check that blank and key agree
make -C unit01/lesson02 manifest COMP=homework
# one personalized copy of the lesson's student packet per student
make -C unit01/lesson02 roster-packets COMP=homework ROSTER=~/Rosters/saar/roster-map.csv

# a unit test or quiz (also runnable from tests/, test_keys/ or quiz01/ with the bare name)
make -C unit01 manifest COMP=tests/practice_test
make -C unit01 roster-packets COMP=quiz01/actual_quiz ROSTER=~/Rosters/saar/roster-map.csv
```

Roster builds put student names in their PDFs and logs. They stay under `target/`, which is never
committed. Keep `roster-map.csv` outside the repository.
