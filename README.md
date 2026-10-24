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
`\gradedblank`. Each page then carries corner registration marks, a QR code, and an id strip.
Write each `\gradedblank` line identically in the blank and the key. The key prints the answer
inside the box (`saar-key` turns this on whenever a document loads `grading`). See
`math-shared/README.md` for the macros and `math-shared/grading-system-design.md` for the plan.

```bash
# a lesson component: manifest.json, and the check that blank and key agree
make -C unit01/lesson02 manifest COMP=homework
# per student: a name cover sheet, its blank back, then that student's copy of the lesson packet
make -C unit01/lesson02 roster-packets COMP=homework ROSTER=~/Rosters/saar/roster-map.csv

# a unit test or quiz (also runnable from tests/, test_keys/ or quiz01/ with the bare name)
make -C unit01 manifest COMP=tests/practice_test
make -C unit01 roster-packets COMP=quiz01/actual_quiz ROSTER=~/Rosters/saar/roster-map.csv
```

Scanned pages go to an outside service, so a graded page carries only the student's tracking id:
the strip reads `ID: K7QM2P`. The name is printed only on math-shared's cover sheet, which sits on
top of each student's copy and is removed before the copy is turned in. Each student's run (cover,
blank back, copy, and a blank page if the copy is odd) is even, so every cover starts on an odd page
when the roster PDF prints duplex. `SECTION=` builds one section. The roster PDF holds the names on
its covers, so it stays under `target/`, which is never committed; the build fails if a name reaches
a graded page. Keep `roster-map.csv` outside the repository.
