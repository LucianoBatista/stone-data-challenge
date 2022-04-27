install:
	@echo "Installing dependencies..."
	poetry install

activate:
	@echo "Activating virtual environment..."
	poetry shell

setup: activate install