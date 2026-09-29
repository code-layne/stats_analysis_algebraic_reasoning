# unit01/study_guide/Makefile — build the Unit 1 test study guide (no key, by design).
#
# Self-contained, on the finals/ model (LESSON_SHAPE.md section 6): the study guide is a
# STANDALONE deliverable merged into no packet, so it is NOT added to shared/unit.mk or
# shared/root.mk and it cannot reflow the pagination of unit 1's verified student/key packets.
# Every subdirectory holding a main.tex compiles to target/<unit>/study_guide/<name>/main.pdf.

PROJECT_ROOT := $(abspath ../..)
UNIT         := $(notdir $(abspath ..))
TEXINPUTS    := $(PROJECT_ROOT)/shared//:
PDF_DIR      := $(PROJECT_ROOT)/target/$(UNIT)/study_guide
LATEXFLAGS   := -xelatex -interaction=nonstopmode -halt-on-error -file-line-error

QUIZZES := $(patsubst %/main.tex,%,$(wildcard */main.tex))

.PHONY: all clean $(QUIZZES)
all: $(QUIZZES)
$(QUIZZES):
	@mkdir -p $(PDF_DIR)/$@
	cd $@ && TEXINPUTS="$(TEXINPUTS)" latexmk $(LATEXFLAGS) -outdir="$(PDF_DIR)/$@" main.tex
	@echo "OK  $(UNIT) study_guide -> target/$(UNIT)/study_guide/$@/main.pdf"

clean:
	rm -rf $(PDF_DIR)
