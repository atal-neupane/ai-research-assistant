.DEFAULT_GOAL := help
.PHONY: help setup lint format test check validate-manifest clean

help: ## Show available commands
	@grep -E '^[a-zA-Z_-]+:.*?## ' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  %-20s %s\n", $$1, $$2}'

setup: ## Create the virtual environment and install dependencies from uv.lock
	uv sync

lint: ## Check code style and formatting (no changes made)
	uv run ruff check .
	uv run ruff format --check .

format: ## Auto-fix lint issues and format the code
	uv run ruff check --fix .
	uv run ruff format .

test: ## Run the test suite
	uv run pytest

check: lint test ## Run lint and tests together (same checks CI will run)

validate-manifest: ## Validate data/manifest.csv (needs scripts/validate_manifest.py)
	uv run python scripts/validate_manifest.py

clean: ## Remove caches and build artifacts (keeps .venv and data)
	rm -rf .pytest_cache .ruff_cache build dist
	find . -type d -name __pycache__ -not -path "./.venv/*" -prune -exec rm -rf {} +

# Added in later weeks:
# parse-eval: ## Compare PDF parsers against the gold data (Week 2-3)
# eval:       ## Run the full evaluation report (Week 5)