#!/bin/bash

echo "Running Ruff auto-fix..."
python -m ruff check . --fix

echo "Running Black..."
python -m black .

echo "Sorting imports..."
python -m isort .

echo "Checking remaining Ruff errors..."
python -m ruff check .

echo "Running pytest..."
pytest
