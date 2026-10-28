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
# per student: the lesson packet with her name on the cover and her copy of every graded component
make -C unit01/lesson02 roster-packets ROSTER=~/Mathematics/rosters/roster-map.csv \
    SECTION="Statistical Analysis & Algebraic Reasoning"

# a unit test or quiz (also runnable from tests/, test_keys/ or quiz01/ with the bare name)
make -C unit01 manifest COMP=tests/practice_test
make -C unit01 roster-packets COMP=quiz01/actual_quiz ROSTER=~/Mathematics/rosters/roster-map.csv

# the same from the root
make roster-packets LESSON=unit01/lesson02 ROSTER=~/Mathematics/rosters/roster-map.csv
make roster-packets COMP=unit01/tests/actual_test ROSTER=~/Mathematics/rosters/roster-map.csv
make manifest COMP=unit01/lesson02/homework
```

Scanned pages go to an outside service, so a graded page carries only the student's tracking id:
the strip reads `ID: K7QM2P`. In a lesson packet the name is printed on the Name line of the lesson
cover. Every graded component starts on a fresh sheet, so the student tears those sheets out and
turns them in, and the cover stays in her packet. The lesson's roster PDF is
`target/compiled/unitXX/lessonYY_roster.pdf`, one packet per student in roster order, paginated like
`make student`. A quiz or test instead gets math-shared's tear-off name sheet: each student's run
(name sheet, blank back, copy, and a blank page if the copy is odd) is even, so every name sheet
starts on an odd page when the roster PDF prints duplex. Both builds write each graded component's
`manifest.json` first, which `grading ingest` reads. `SECTION=` builds one section. The roster PDFs
hold names, so they stay under `target/`, which is never committed; the build fails if a name
reaches a graded page. Keep `roster-map.csv` outside the repository.
