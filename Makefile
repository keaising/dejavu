.PHONY: all lint test
all: lint test

lint:
	pycodestyle --exclude=venv .

test:
	python -m pytest

fmt:
	black . -l 80 --exclude=venv
