install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:
	black *.py helper/*.py tests/*.py

test:
	python -m pytest -vv --cov=tests tests

lint:
	pylint --disable=R,C helper tests main.py

run:
	python main.py --question "What is the topic this paper highlights?"

all: install lint test format run