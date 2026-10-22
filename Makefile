.PHONY: help install run dev build test lint clean

help:
	@echo "SmartERP Enterprise Makefile Targets:"
	@echo "  make install  - Install Python and Node dependencies"
	@echo "  make run      - Run backend server via entrypoint"
	@echo "  make dev      - Start development servers"
	@echo "  make build    - Build frontend production assets"
	@echo "  make test     - Execute pytest test suites"
	@echo "  make lint     - Run code quality analyzers"

install:
	pip install -r backend/requirements.txt
	cd frontend && npm install

run:
	python main.py

dev:
	start.bat

build:
	cd frontend && npm run build

test:
	pytest tests/

lint:
	ruff check backend/ || true
	cd frontend && npm run lint || true

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
