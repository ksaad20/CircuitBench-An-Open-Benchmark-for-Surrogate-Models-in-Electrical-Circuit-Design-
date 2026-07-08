"""
Regression evaluation metrics for CircuitBench.
"""

from __future__ import annotations

import numpy as np
from sklearn.metrics import (
    mean_absolute_error as sk_mae,
    mean_squared_error as sk_mse,
    median_absolute_error as sk_median_ae,
    max_error as sk_max_error,
    mean_squared_log_error
)

def weighted_mean_absolute_percentage_error(
        y_true,
        y_pred):
    """
    Weighted Mean Absolute Percentage Error (WMAPE).
    """

    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)

    denominator = np.sum(np.abs(y_true))

    if denominator == 0:
        return np.nan

    return float(

        np.sum(

            np.abs(y_true - y_pred)

        )

        /

        denominator

        * 100

    )

def mean_absolute_scaled_error(
        y_true,
        y_pred):

    """
    Mean Absolute Scaled Error (MASE).
    """

    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)

    numerator = np.mean(

        np.abs(y_true - y_pred)

    )

    denominator = np.mean(

        np.abs(

            np.diff(y_true)

        )

    )

    if denominator == 0:

        return np.nan

    return float(

        numerator / denominator

          )

def normalized_root_mean_squared_error(
        y_true,
        y_pred,
        method="range"):

    """
    Normalized RMSE.

    Methods
    -------
    range
    mean
    std
    """

    rmse = root_mean_squared_error(
        y_true,
        y_pred
    )

    y_true = np.asarray(y_true)

    if method == "range":

        denom = np.max(y_true) - np.min(y_true)

    elif method == "mean":

        denom = np.mean(y_true)

    elif method == "std":

        denom = np.std(y_true)

    else:

        raise ValueError(

            "Unknown normalization method."

        )

    if denom == 0:

        return np.nan

    return float(

        rmse / denom

    )


def normalized_root_mean_squared_error(
        y_true,
        y_pred,
        method="range"):

    """
    Normalized RMSE.

    Methods
    -------
    range
    mean
    std
    """

    rmse = root_mean_squared_error(
        y_true,
        y_pred
    )

    y_true = np.asarray(y_true)

    if method == "range":

        denom = np.max(y_true) - np.min(y_true)

    elif method == "mean":

        denom = np.mean(y_true)

    elif method == "std":

        denom = np.std(y_true)

    else:

        raise ValueError(

            "Unknown normalization method."

        )

    if denom == 0:

        return np.nan

    return float(

        rmse / denom

      )


def relative_absolute_error(
        y_true,
        y_pred):

    """
    Relative Absolute Error.
    """

    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)

    numerator = np.sum(

        np.abs(

            y_true - y_pred

        )

    )

    denominator = np.sum(

        np.abs(

            y_true -

            np.mean(y_true)

        )

    )

    if denominator == 0:

        return np.nan

    return float(

        numerator /

        denominator

          )


def relative_squared_error(
        y_true,
        y_pred):

    """
    Relative Squared Error.
    """

    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)

    numerator = np.sum(

        (y_true - y_pred) ** 2

    )

    denominator = np.sum(

        (

            y_true -

            np.mean(y_true)

        ) ** 2

    )

    if denominator == 0:

        return np.nan

    return float(

        numerator /

        denominator

    )


def root_relative_squared_error(
        y_true,
        y_pred):

    """
    Root Relative Squared Error.
    """

    return float(

        np.sqrt(

            relative_squared_error(

                y_true,

                y_pred

            )

        )

          )


def mean_squared_log_error_metric(
        y_true,
        y_pred):

    """
    Mean Squared Log Error.
    """

    y_true = np.clip(

        np.asarray(y_true),

        0,

        None

    )

    y_pred = np.clip(

        np.asarray(y_pred),

        0,

        None

    )

    return float(

        mean_squared_log_error(

            y_true,

            y_pred

        )

    )

def log_cosh_loss(
        y_true,
        y_pred):

    """
    Log-Cosh Loss.
    """

    error = np.asarray(

        y_pred

    ) - np.asarray(

        y_true

    )

    return float(

        np.mean(

            np.log(

                np.cosh(

                    error

                )

            )

        )

    )

def huber_loss(
        y_true,
        y_pred,
        delta=1.0):

    """
    Huber Loss.
    """

    error = np.asarray(

        y_true

    ) - np.asarray(

        y_pred

    )

    absolute = np.abs(error)

    quadratic = np.minimum(

        absolute,

        delta

    )

    linear = absolute - quadratic

    return float(

        np.mean(

            0.5 *

            quadratic ** 2 +

            delta *

            linear

        )

    )

def quantile_loss(
        y_true,
        y_pred,
        q=0.5):

    """
    Quantile (Pinball) Loss.
    """

    error = np.asarray(

        y_true

    ) - np.asarray(

        y_pred

    )

    return float(

        np.mean(

            np.maximum(

                q * error,

                (q - 1) * error

            )

        )

    )


