.PHONY: lint test

lint:
	poetry run isort ./
	poetry run black ./
	poetry run pflake8 ./
	poetry run mypy ./
	# poetry run sqlfluff

test:
	poetry run pytest -v --cov=python_app --cov-report=html --cov-report=xml

clean:
	rm -rf ./htmlcov ./.coverage ./coverage.xml
