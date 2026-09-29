# unit02/review/Makefile — build the Unit 2 test study guide (review only; no key).
#
# Self-contained, on the finals/ model (LESSON_SHAPE.md section 6): this review set is a
# STANDALONE deliverable merged into no packet, so it is NOT added to shared/unit.mk or
# shared/root.mk and it cannot reflow the pagination of unit 2's verified student/key packets.
# Every subdirectory holding a main.tex compiles to target/<unit>/review/<name>/main.pdf.

PROJECT_ROOT := $(abspath ../..)
UNIT         := $(notdir $(abspath ..))
TEXINPUTS    := $(PROJECT_ROOT)/shared//:
PDF_DIR      := $(PROJECT_ROOT)/target/$(UNIT)/review
LATEXFLAGS   := -xelatex -interaction=nonstopmode -halt-on-error -file-line-error

DOCS := $(patsubst %/main.tex,%,$(wildcard */main.tex))

.PHONY: all clean $(DOCS)
all: $(DOCS)
$(DOCS):
	@mkdir -p $(PDF_DIR)/$@
	cd $@ && TEXINPUTS="$(TEXINPUTS)" latexmk $(LATEXFLAGS) -outdir="$(PDF_DIR)/$@" main.tex
	@echo "OK  $(UNIT) review -> target/$(UNIT)/review/$@/main.pdf"

clean:
	rm -rf $(PDF_DIR)
