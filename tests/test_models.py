"""
Machine-learning model tests.
"""

from sklearn.linear_model import LinearRegression
import numpy as np


def test_linear_regression_fit():

    X = np.array([[1], [2], [3]])

    y = np.array([2, 4, 6])

    model = LinearRegression()

    model.fit(X, y)

    prediction = model.predict([[4]])

    assert prediction[0] > 7
