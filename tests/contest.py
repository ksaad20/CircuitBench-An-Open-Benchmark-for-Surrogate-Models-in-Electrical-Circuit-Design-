"""
Shared fixtures for CircuitBench.
"""

import numpy as np
import pytest


@pytest.fixture
def sample_dataset():

    X = np.array(
        [
            [1, 2],
            [2, 3],
            [3, 4],
        ]
    )

    y = np.array(
        [
            3,
            5,
            7,
        ]
    )

    return X, y


@pytest.fixture
def random_seed():

    np.random.seed(42)
