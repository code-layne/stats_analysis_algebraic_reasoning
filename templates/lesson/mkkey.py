#!/usr/bin/env python3
"""Generate a _key main.tex from its blank: same bytes except the answers.

The page-for-page rule is easiest to keep when the key is never hand-edited: author the blank,
list the answers IN ORDER in a JSON spec, and generate. Re-run after every edit to the blank.

Usage:  python3 templates/lesson/mkkey.py unitXX/lessonYY/notes/main.tex \
            unitXX/lessonYY/notes_key/main.tex answers.json
SPEC: {"blanks": [...], "lines": [[...],[...]], "vocab": {"Term": "def"}, "title": "Guided Notes"}
Replaces, in order: every \\blank{W} -> \\ans{a}; every \\par\\writelines{n} / \\par\\writeline
-> \\par\\ansline{..} + \\ansline{..}; \\termblanklong{T} -> \\vocabans{T}{def};
-boxes -> -key; the pageheader title gets " --- Answer Key"; the %! header line too.
"""
import json, re, sys
blank, key, spec = sys.argv[1:4]
S = json.load(open(spec))
t = open(blank).read()
ans = iter(S["blanks"])
# Only substitute on non-comment lines; a \blank{} mentioned in a % comment must not count.
def code_sub(pattern, repl, text):
    out = []
    for line in text.split('\n'):
        if line.lstrip().startswith('%'):
            out.append(line)
        else:
            out.append(re.sub(pattern, repl, line))
    return '\n'.join(out)
n_blank = sum(len(re.findall(r'\\blank\{[^}]*\}', l)) for l in t.split('\n') if not l.lstrip().startswith('%'))
assert n_blank == len(S["blanks"]), f"{n_blank} blanks in file, {len(S['blanks'])} answers given"
t = code_sub(r'\\blank\{[^}]*\}', lambda m: '\\ans{' + next(ans) + '}', t)
lines = iter(S.get("lines", []))
def wl(m):
    n = int(m.group(1)) if m.group(1) else 1
    a = next(lines)
    assert len(a) == n, f"writelines{{{n}}} but {len(a)} answers: {a}"
    return '\\par\\ansline{' + a[0] + '}' + ''.join('\n\\ansline{' + x + '}' for x in a[1:])
t = code_sub(r'\\par\\writelines\{(\d+)\}|\\par\\writeline(?![a-z])', lambda m: wl(m), t)
assert next(lines, None) is None, "unused writeline answers"
for term, d in S.get("vocab", {}).items():
    hits = [o for o in ('\\termblanklong{' + term + '}', '\\termblank{' + term + '}') if o in t]
    assert hits, term
    t = t.replace(hits[0], '\\vocabans{' + term + '}{' + d + '}')
assert not any('\\termblank' in l for l in t.split('\n') if not l.lstrip().startswith('%')), "unfilled termblanklong"
t = t.replace('\\usepackage{saar-boxes}', '\\usepackage{saar-key}   % pulls in -boxes; do NOT also load -boxes', 1)
t = re.sub(r'(\\pageheader\{[^}]*\}\{[^}]*)\}', r'\1 --- Answer Key}', t, count=1)
t = re.sub(r'^(%!.*)$', r'\1 (Answer Key)', t, count=1, flags=re.M)
t = t.replace('% NAMESTRIP: no \\namedateperiod here. The student writes their name once, on the\n% cover this component is stapled behind.',
              '% NAMESTRIP: no \\namedateperiod here — mirrors the blank. NO teachernote here —\n% teacher prose lives in the lesson plan.')
open(key, 'w').write(t)
print("wrote", key, "blanks:", n_blank)
