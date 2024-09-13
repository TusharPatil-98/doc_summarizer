install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=tests tests

run:
	python main.py --question "What is the topic this paper highlights?"

all: install test run