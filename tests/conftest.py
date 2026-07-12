"""
CircuitBench Test Fixtures
==========================

Shared pytest fixtures.
"""

from __future__ import annotations

import numpy as np
import pandas as pd
import pytest

from sklearn.datasets import make_regression
from sklearn.linear_model import LinearRegression


class DummyDataset:

    def __init__(self):

        X, y = make_regression(
            n_samples=200,
            n_features=10,
            noise=0.1,
            random_state=42,
        )

        self.name = "Dummy Dataset"

        self.X = X

        self.y = y

        self.X_train = X[:150]

        self.X_test = X[150:]

        self.y_train = y[:150]

        self.y_test = y[150:]

        self.feature_names = [f"feature_{i}" for i in range(X.shape[1])]


@pytest.fixture
def dataset():

    return DummyDataset()


@pytest.fixture
def model():

    model = LinearRegression()

    model.name = "Linear Regression"

    return model


@pytest.fixture
def predictions():

    rng = np.random.default_rng(42)

    return rng.normal(
        loc=0.0,
        scale=1.0,
        size=100,
    )


@pytest.fixture
def targets():

    rng = np.random.default_rng(123)

    return rng.normal(
        loc=0.0,
        scale=1.0,
        size=100,
    )


@pytest.fixture
def dataframe():

    return pd.DataFrame(
        {
            "RMSE": [
                0.12,
                0.15,
                0.10,
            ],
            "MAE": [
                0.07,
                0.08,
                0.06,
            ],
            "R2": [
                0.91,
                0.88,
                0.93,
            ],
        }
    )


@pytest.fixture
def classification_dataframe():

    return pd.DataFrame(
        {
            "Accuracy": [
                0.94,
                0.96,
                0.95,
            ],
            "Precision": [
                0.93,
                0.95,
                0.94,
            ],
            "Recall": [
                0.92,
                0.94,
                0.93,
            ],
            "F1": [
                0.925,
                0.945,
                0.935,
            ],
        }
    )


@pytest.fixture
def random_state():

    return 42


@pytest.fixture
def predictions():

    rng = np.random.default_rng(42)

    return rng.normal(
        loc=0.0,
        scale=1.0,
        size=100,
    )


@pytest.fixture
def targets():

    rng = np.random.default_rng(123)

    return rng.normal(
        loc=0.0,
        scale=1.0,
        size=100,
    )


@pytest.fixture
def dataframe():

    return pd.DataFrame(
        {
            "RMSE": [
                0.12,
                0.15,
                0.10,
            ],
            "MAE": [
                0.07,
                0.08,
                0.06,
            ],
            "R2": [
                0.91,
                0.88,
                0.93,
            ],
        }
    )


@pytest.fixture
def classification_dataframe():

    return pd.DataFrame(
        {
            "Accuracy": [
                0.94,
                0.96,
                0.95,
            ],
            "Precision": [
                0.93,
                0.95,
                0.94,
            ],
            "Recall": [
                0.92,
                0.94,
                0.93,
            ],
            "F1": [
                0.925,
                0.945,
                0.935,
            ],
        }
    )


@pytest.fixture
def random_state():

    return 42
