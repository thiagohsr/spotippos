setup: setup-env setup-jsonserver ## Install dependencies

setup-env:  ## Install python requirements
	pip install -r requirements.txt

setup-jsonserver:
	cd json_server && npm install

run: run-jsonserver run-spotippos_app ## Run json-server and Spotippos_app API

run-jsonserver:
	cd json_server && npm run start &

run-spotippos_app:
	python spotippos_app/app.py

test:
	pytest