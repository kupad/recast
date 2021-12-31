SRC = src
PY_FILES = $(shell find $(SRC) -type f -name '*.py')
PYTHON  = python3
PKG = recast

.DEFAULT_GOAL := build

.PHONY: build-deps
build-deps:
	$(PYTHON) -m pip install --upgrade build twine pytest

.PHONY: build
build: dist

dist: setup.py $(PY_FILES)
	$(PYTHON) -m build

.PHONY: test
test: $(PY_FILES)
	$(PYTHON) -m unittest discover tests

.PHONY: install
install: build
	$(PYTHON) -m pip install .

.PHONY: uninstall
uninstall:
	$(PYTHON) -m pip uninstall $(PKG)

.PHONY: push
push: dist
	$(PYTHON) -m twine upload dist/*

.PHONY: push-test
push-test: dist
	$(PYTHON) -m twine upload --repository testpypi dist/*

.PHONY: clean
clean:
	rm -rf build dist $(SRC)/*.egg-info $(SRC)/*.pyc
