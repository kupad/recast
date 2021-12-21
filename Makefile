SRC = src
PYTHON  = python3

.DEFAULT: build

.PHONY: build
build: setup.py $(SRC)
	$(PYTHON) setup.py sdist bdist_wheel

dist: build

.PHONY: test
test: $(SRC)
	$(PYTHON) -m unittest discover tests

.PHONY: install
install: build
	sudo $(PYTHON) setup.py install --record .install-files

.PHONY: uninstall
uninstall: setup.py .install-files
	cat .install-files | xargs -o sudo rm -ri && rm -f .install-files

.PHONY: push
push: dist
	twine upload dist/*

.PHONY: push-test
push-test: dist
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*

.PHONY: clean
clean:
	rm -rf build dist $(SRC)/*.egg-info $(SRC)/*.pyc
