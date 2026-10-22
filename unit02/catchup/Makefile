# unit02/catchup/Makefile — build the Unit 2 exchange-student catch-up packet (review only; no key).
#
# Self-contained, on the finals/ model (LESSON_SHAPE.md section 6): this catch-up packet is a
# STANDALONE deliverable merged into no packet, so it is NOT added to shared/unit.mk or
# shared/root.mk and it cannot reflow the pagination of unit 2's verified student/key packets.
# Every subdirectory holding a main.tex compiles to target/<unit>/catchup/<name>/main.pdf.

PROJECT_ROOT := $(abspath ../..)
UNIT         := $(notdir $(abspath ..))
TEXINPUTS    := $(PROJECT_ROOT)/shared//:
PDF_DIR      := $(PROJECT_ROOT)/target/$(UNIT)/catchup
LATEXFLAGS   := -xelatex -interaction=nonstopmode -halt-on-error -file-line-error

DOCS := $(patsubst %/main.tex,%,$(wildcard */main.tex))

.PHONY: all clean $(DOCS)
all: $(DOCS)
$(DOCS):
	@mkdir -p $(PDF_DIR)/$@
	cd $@ && TEXINPUTS="$(TEXINPUTS)" latexmk $(LATEXFLAGS) -outdir="$(PDF_DIR)/$@" main.tex
	@echo "OK  $(UNIT) catchup -> target/$(UNIT)/catchup/$@/main.pdf"

clean:
	rm -rf $(PDF_DIR)
