MDBOOK ?= mdbook
PYTHON ?= python

SPEC_JSON := spec.json

.PHONY: all generated-files validate specification dev
all: generated-files validate specification

generated-files: $(SPEC_JSON)
	$(PYTHON) scripts/generate.py

validate: generated-files
	$(PYTHON) scripts/validate.py

specification: generated-files
	$(MDBOOK) build
dev: generated-files
	$(MDBOOK) serve
