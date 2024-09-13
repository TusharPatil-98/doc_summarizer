install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

run:
	python main.py

all: install run