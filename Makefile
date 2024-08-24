# Makefile variables
SRC_DIR := $(shell grep 'SRC_DIR' config.toml | sed 's/.*= *//')/
PYPROJECT_TOML := $(shell grep 'PYPROJECT_TOML' config.toml | sed 's/.*= *//')
GENERATE_DOTENV_PY := ./scripts/generate_dotenv/dotenv_from_toml.py

# Source code formatting, linting and testing
.PHONY: code.format \
		code.lint \
		code.check

code.format:
	isort $(SRC_DIR)
	black $(SRC_DIR)

code.lint: code.format
	bandit -r $(SRC_DIR) -c $(PYPROJECT_TOML)
	ruff check $(SRC_DIR)
	pylint $(SRC_DIR)
	mypy $(SRC_DIR)

code.check: code.lint

# Dotenv generation
dotenv:
	python $(GENERATE_DOTENV_PY)
