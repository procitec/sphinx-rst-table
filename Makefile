UV ?= uv
SRC_FILES := sphinx_rst_table tests
DOCS_DIR := docs
DOCS_BUILD_DIR := $(DOCS_DIR)/_build

.PHONY: list
list:
	@$(MAKE) -pRrq -f $(lastword $(MAKEFILE_LIST)) : 2>/dev/null \
		| awk -v RS= -F: '/^# File/,/^# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}' \
		| sort \
		| egrep -v -e '^[^[:alnum:]]' -e '^$@$$'

.PHONY: sync
sync:
	$(UV) sync --all-groups

.PHONY: lock
lock:
	$(UV) lock

.PHONY: lint
lint:
	$(UV) run --only-group lint ruff check $(SRC_FILES)
	$(UV) run --only-group lint ruff format --check $(SRC_FILES)

.PHONY: format
format:
	$(UV) run --only-group lint ruff format $(SRC_FILES)
	$(UV) run --only-group lint ruff check --fix $(SRC_FILES)

.PHONY: test
test:
	$(UV) run --group test python -m pytest -n auto tests/

.PHONY: test-short
test-short:
	$(UV) run --group test python -m pytest -n auto --ignore-glob="*official*" tests/

.PHONY: test-matrix
test-matrix:
	$(UV) run --with tox --with tox-uv tox

.PHONY: docs-html
docs-html:
	$(UV) run --group docs sphinx-build -a -E -j auto -b html $(DOCS_DIR)/ $(DOCS_BUILD_DIR)/html

.PHONY: docs-html-fast
docs-html-fast:
	$(UV) run --group docs sphinx-build -j auto -b html $(DOCS_DIR)/ $(DOCS_BUILD_DIR)/html

.PHONY: docs-linkcheck
docs-linkcheck:
	$(UV) run --group docs sphinx-build -j auto -b linkcheck $(DOCS_DIR)/ $(DOCS_BUILD_DIR)/linkcheck

.PHONY: docs-pdf
docs-pdf:
	$(UV) run --group docs sphinx-build -b latex $(DOCS_DIR)/ $(DOCS_BUILD_DIR)/latex
	$(MAKE) -C $(DOCS_BUILD_DIR)/latex all-pdf

.PHONY: build
build:
	rm -rf dist/
	$(UV) build

.PHONY: publish
publish: build
	$(UV) publish

.PHONY: clean
clean:
	rm -rf .pytest_cache .ruff_cache .tox .venv dist build $(DOCS_BUILD_DIR)
	find . -type d -name __pycache__ -prune -exec rm -rf {} +
