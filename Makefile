.PHONY: all lint
all: lint

lint:
	pycodestyle --exclude=venv .

fmt:
	black . -l 80 --exclude=venv

