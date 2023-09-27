help:
	@echo Makefile doc for koodu
	@echo
	@grep -E '^[ .a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'
	@echo

install:  # Install requirements
	poetry install

build-docs:  # Build the documentation
	mkdocs build

deploy-docs:  # Deploy the documentation
	mkdocs build

release:  # Build a new version and release it
	poetry build
	poetry publish

mypy: # Run a static syntax check
	poetry run mypy src/

lint: # Format the code correctly
	poetry run black .
	poetry run ruff --fix .

clean:  # Clear any cache files and test files
	rm -rf .mypy_cache
	rm -rf .pytest_cache
	rm -rf .ruff_cache
	rm -rf test_output
	rm -rf site/
	rm -rf dist/
	rm -rf **/__pycache__
	rm -rf **/*.pyc

test:  # Run tests
	pytest -vv
