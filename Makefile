install:
	@echo "Installing dependencies..."
	poetry install
	poetry run pre-commit install

activate:
	@echo "Activating virtual environment..."
	poetry shell

download:
	@echo "Downloading the data..."
	mkdir data
	cd data/ && { curl -O https://stone-data-challenge.s3.amazonaws.com/portfolio_clientes.csv ; cd -; }
	cd data/ && { curl -O https://stone-data-challenge.s3.amazonaws.com/portfolio_comunicados.csv ; cd -; }
	cd data/ && { curl -O https://stone-data-challenge.s3.amazonaws.com/portfolio_geral.csv ; cd -; }
	cd data/ && { curl -O https://stone-data-challenge.s3.amazonaws.com/portfolio_tpv.csv ; cd -; }
	cd data/ && { curl -O https://stone-data-challenge.s3.amazonaws.com/estados_regioes.csv ; cd -; }

setup: download activate install