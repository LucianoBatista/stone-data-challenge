install:
	@echo "Installing dependencies..."
	poetry install
	poetry run pre-commit install

activate:
	@echo "Activating virtual environment..."
	poetry shell

setup: activate install