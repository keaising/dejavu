.PHONY: all lint test
all: lint test

lint:
	pycodestyle --exclude=venv . --max-line-length=80

test:
	python -m pytest test

fmt:
	black . -l 80 --exclude=venv

require:
	pip freeze > requirements.txt
