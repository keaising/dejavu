.PHONY: all lint
all: lint

lint:
	pycodestyle --show-source --exclude=venv .
