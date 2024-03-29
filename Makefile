install:  # Install requirements
	poetry install

update-lock:  # Update poetry.lock file
	poetry lock

build-docs:  # Build the documentation
	mkdocs build

deploy-docs:  # Deploy the documentation
	mkdocs gh-deploy

release:  # Build a new version and release it
	poetry build
	poetry publish

lint: # Format the code correctly
	poetry run black koodu tests
	poetry run ruff --fix koodu tests

clean:  # Clear any cache files and test files
	rm -rf .pytest_cache
	rm -rf .ruff_cache
	rm -rf test_output
	rm -rf site/
	rm -rf dist/
	rm -rf **/__pycache__
	rm -rf **/*.pyc

test:  # Run tests
	pytest -vv

##help: show help
help:
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'
