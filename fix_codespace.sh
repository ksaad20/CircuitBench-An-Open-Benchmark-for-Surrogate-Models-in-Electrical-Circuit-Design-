#!/usr/bin/env bash
set -e

python -m pip install -U pip
python -m pip install numpy scipy pandas scikit-learn pytest
python -m pip install -e .

python -m ruff check . --fix || true
python -m black .

python -m ruff check .
pytest
