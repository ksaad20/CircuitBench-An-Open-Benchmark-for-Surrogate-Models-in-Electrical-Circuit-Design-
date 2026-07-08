"""
Explainability metrics.
"""

import numpy as np


def sparsity(values):

    values = np.asarray(values)

    return np.sum(values == 0) / len(values)


def explanation_entropy(weights):

    weights = np.asarray(weights)

    weights = weights / np.sum(weights)

    return -np.sum(
        weights *
        np.log2(weights)
    )


def importance_concentration(weights):

    weights = np.asarray(weights)

    return np.max(weights)


def normalized_importance(weights):

    weights = np.asarray(weights)

    return weights / np.sum(weights)
