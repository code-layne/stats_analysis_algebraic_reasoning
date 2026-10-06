# unit02/warmups/Makefile — standalone extra warm-ups (e.g. a Day 2 re-entry warm-up when a
# lesson runs over). On the quiz01 model (LESSON_SHAPE.md section 6): merged into NO packet,
# NOT listed in shared/unit.mk or shared/root.mk, so the unit's verified packets never reflow.
# Every subdirectory holding a main.tex compiles to target/<unit>/warmups/<name>/main.pdf.

PROJECT_ROOT := $(abspath ../..)
UNIT         := $(notdir $(abspath ..))
TEXINPUTS    := $(PROJECT_ROOT)/shared//:
PDF_DIR      := $(PROJECT_ROOT)/target/$(UNIT)/warmups
LATEXFLAGS   := -xelatex -interaction=nonstopmode -halt-on-error -file-line-error

WARMUPS := $(patsubst %/main.tex,%,$(wildcard */main.tex))

.PHONY: all clean $(WARMUPS)
all: $(WARMUPS)
$(WARMUPS):
	@mkdir -p $(PDF_DIR)/$@
	cd $@ && TEXINPUTS="$(TEXINPUTS)" latexmk $(LATEXFLAGS) -outdir="$(PDF_DIR)/$@" main.tex
	@echo "OK  $(UNIT) warmups -> target/$(UNIT)/warmups/$@/main.pdf"

clean:
	rm -rf $(PDF_DIR)
