ENV := test

default: help

# cli: make help ENV=live
help:
	@uv -h
	@echo "\nEnv: $(ENV)"

run-main:
	uv run main.py

run-eg:
	uv run examples/py_base.py

dep-tree:
	uv tree

dump-requirements:
	uv export --format requirements.txt > requirements.txt
