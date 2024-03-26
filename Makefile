
.PHONY: install virtualenv ipython clean test test-watch testci lint

install:
	@echo "Instalando para desenvolvimento"
	@.venv/bin/python -m pip install -e '.[dev]'

virtualenv:
	@.venv/bin/python -m pip -m venv .venv

ipython:
	@.venv/bin/ipython

test:
	@.venv/bin/pytest -vv -s

testci:
	pytest -v --junitxml=./test-result.xml

lint:
	@.venv/bin/flake8 --exclude=.venv,build,dist,*.egg-info

fmt:
	@.venv/bin/isort taxi_gcp integration tests
	@.venv/bin/black taxi_gcp integration tests

test-watch:
	@.venv/bin/ptw -- -vv -s
clean:
	@find ./ -name '*.pyc' -exec rm -f {} \;
	@find ./ -name '__pycache__' -exec rm -rf {} \;
	@find ./ -name 'Thumbs.db' -exec rm -f {} \;
	@find ./ -name '*~' -exec rm -f {} \;
	@rm -rf .cache
	@rm -rf .pytest_cache
	@rm -rf .mypy_cache
	@rm -rf build
	@rm -rf dist
	@rm -rf *.egg-info
	@rm -rf htmlcov
	@rm -rf .tox/
	@rm -rf docs/_build
