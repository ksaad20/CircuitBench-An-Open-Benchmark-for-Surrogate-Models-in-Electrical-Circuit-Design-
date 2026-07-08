"""
Metric calculation tests.
"""

import numpy as np


def mse(a, b):

    return np.mean((a - b) ** 2)


def test_zero_error():

    x = np.array([1, 2, 3])

    assert mse(x, x) == 0


def test_positive_error():

    x = np.array([1, 2])

    y = np.array([3, 4])

    assert mse(x, y) > 0
