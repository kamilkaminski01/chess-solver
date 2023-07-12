.PHONY: build start clear stop lint

build:
	docker build -t chess-solver .

start:
	docker run -d -p 5000:5000 --name chess-solver chess-solver

run:
	cd app/ && python app.py

clear:
	docker stop chess-solver
	docker rm -f chess-solver

stop:
	docker stop chess-solver

lint:
	cd app/ && black . && isort . && mypy . && flake8 .
