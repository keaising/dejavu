.PHONY: all lint
all: lint

lint:
	pycodestyle --exclude=venv .

fmt:
	black handler dal model -l 80

