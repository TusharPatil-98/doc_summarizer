install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt &&\
		pip install torch --index-url https://download.pytorch.org/whl/cu121
		
run:
	python main.py

all: install run