SHELL=/bin/bash

.PHONY: deps
deps:
	pip install -r requirements.txt

database: 
	python3 db/initdb.py

start:
	flask run