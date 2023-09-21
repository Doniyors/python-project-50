lint: 
	poetry run flake8

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

pytest:
	pytest