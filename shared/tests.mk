# shared/tests.mk — build a unit's summative assessments (blank student copies).
# Included by each unitNN/tests/Makefile (`include ../../shared/tests.mk`).
# Every subdirectory holding a main.tex compiles to target/<unit>/tests/<name>/main.pdf.

PROJECT_ROOT := $(abspath ../..)
UNIT         := $(notdir $(abspath ..))
TEXINPUTS    := $(PROJECT_ROOT)/shared//:$(PROJECT_ROOT)/math-shared:
PDF_DIR      := $(PROJECT_ROOT)/target/$(UNIT)/tests
LATEXFLAGS   := -xelatex -interaction=nonstopmode -halt-on-error -file-line-error

TESTS := $(patsubst %/main.tex,%,$(wildcard */main.tex))

# The practice test doubles as the unit "sample test" drop-in: its compiled PDF is
# published to ../sample_test/main.pdf, which shared/unit.mk merges into BOTH the
# student and key packets. The actual test is never published into a packet.
DROP_SRC := practice_test
DROP_DST := ../sample_test/main.pdf

.PHONY: all clean drop $(TESTS)

all: $(TESTS) drop

$(TESTS):
	@mkdir -p $(PDF_DIR)/$@
	cd $@ && TEXINPUTS="$(TEXINPUTS)" latexmk $(LATEXFLAGS) \
	    -outdir="$(PDF_DIR)/$@" main.tex
	@echo "OK  $(UNIT) test -> target/$(UNIT)/tests/$@/main.pdf"

drop: $(DROP_SRC)
	@mkdir -p $(dir $(DROP_DST))
	cp $(PDF_DIR)/$(DROP_SRC)/main.pdf $(DROP_DST)
	@echo "OK  Published practice test -> $(UNIT)/sample_test/main.pdf (student packet)"

clean:
	rm -rf $(PDF_DIR)

# ── Grading ───────────────────────────────────────────────────────────────────
# `make manifest COMP=<name>` and `make roster-packets COMP=<name> ROSTER=<path>`
# run shared/unit.mk's grading targets for tests/<name> (a trailing _key is
# dropped, so the key directory's own name works too). See shared/unit.mk.
# ROSTER may start with ~/ and may be relative to this directory.
.PHONY: manifest roster-packets
manifest roster-packets:
	@$(MAKE) --no-print-directory -C .. $@ COMP=tests/$(patsubst %_key,%,$(COMP)) \
	    $(if $(ROSTER),ROSTER="$(abspath $(patsubst ~/%,$(HOME)/%,$(ROSTER)))")
