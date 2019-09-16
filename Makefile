.PHONY: all
all: lint

.PHONY: lint
lint:
	@pycodestyle --show-source --exclude=venv .

