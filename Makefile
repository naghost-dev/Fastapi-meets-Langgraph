.PHONY: run
run:
	uvicorn src.app.main:app  --port 18080 --reload

.PHONY: install
install:
	poetry install

.PHONY: check-codestyle
check-codestyle:
	ruff check --fix .
