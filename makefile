.PHONY: test clean

test:
	poetry run coverage run --source=. -m pytest
	poetry run coverage report --skip-empty -m

clean:
	find . \( -type f -name "*.py[co]" -or -name ".coverage" \) -delete
	find . \( -type d -name "__pycache__" -or -name "*.egg-info" -or -name "*.pytest_cache" \) -exec rm -r {} +
