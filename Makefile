.PHONY: all lint test docs
all: lint test docs

lint:
	pycodestyle --exclude=venv . --max-line-length=80

test:
	python -m pytest test

fmt:
	black . -l 80 --exclude=venv

require:
	pip freeze > requirements.txt

docs:
	cd docs; make html; cd build/html; touch .nojekyll
