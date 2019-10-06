.PHONY: all lint test docs install
all: lint test docs
gen: fmt table docs

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

table:
	python ./docs/table/user.py
	python ./docs/table/address.py

install:
	pip install -r requirements.txt
