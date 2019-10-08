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
	cd docs; make html; cd build/html; touch .nojekyll; echo "eureka.shuxiao.wang" > CNAME

table:
	python ./docs/table/user.py
	python ./docs/table/address.py
	python ./docs/table/order.py
	python ./docs/table/order2.py

install:
	pip install -r requirements.txt
