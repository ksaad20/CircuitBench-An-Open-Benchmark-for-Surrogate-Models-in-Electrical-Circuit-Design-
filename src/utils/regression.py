"""
Regression metrics.
"""

from sklearn.metrics import (
    mean_squared_error,
    mean_absolute_error,
    r2_score
)

import numpy as np


def rmse(y_true, y_pred):

    return np.sqrt(
        mean_squared_error(
            y_true,
            y_pred
        )
    )


def mae(y_true,
        y_pred):

    return mean_absolute_error(
        y_true,
        y_pred
    )


def r2(y_true,
       y_pred):

    return r2_score(
        y_true,
        y_pred
    )


def evaluate_regression(
        y_true,
        y_pred):

    return {

        "RMSE": rmse(y_true, y_pred),

        "MAE": mae(y_true, y_pred),

        "R2": r2(y_true, y_pred)

    }
