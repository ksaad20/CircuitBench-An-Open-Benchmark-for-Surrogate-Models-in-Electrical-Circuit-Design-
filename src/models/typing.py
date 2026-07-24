"""
CircuitBench Typing Definitions
===============================

Shared typing aliases used throughout the framework.
"""

from __future__ import annotations

import random
import time
from collections.abc import Callable, MutableMapping, Sequence
from pathlib import Path
from typing import (
    Any,
    Union,
)

import numpy as np

try:
    import pandas as pd
except ImportError:
    pd = None

# ==========================================================
# Generic Types
# ==========================================================

Number = Union[int, float]

PathLike = Union[str, Path]

Parameters = dict[str, Any]

Metadata = dict[str, Any]

History = dict[str, Any]

Config = dict[str, Any]

# ==========================================================
# Machine Learning Data
# ==========================================================

ArrayLike = Union[
    np.ndarray,
    Sequence[Number],
]

if pd is not None:
    DataFrameLike = Union[
        np.ndarray,
        pd.DataFrame,
        pd.Series,
    ]

else:
    DataFrameLike = np.ndarray

FeatureMatrix = DataFrameLike

TargetVector = ArrayLike

Prediction = ArrayLike

Probability = ArrayLike

# ==========================================================
# Registry
# ==========================================================

Registry = MutableMapping[str, type]

RegistryMetadata = MutableMapping[str, Metadata]

# ==========================================================
# Metrics
# ==========================================================

MetricResult = dict[str, float]

MetricFunction = Callable[..., float]

# ==========================================================
# Training
# ==========================================================

LossHistory = list[float]

ValidationHistory = list[float]

EpochHistory = dict[str, list[float]]

# ==========================================================
# Hyperparameter Optimization
# ==========================================================

SearchSpace = dict[str, Any]

TrialResult = dict[str, Any]

OptimizationHistory = list[TrialResult]

# ==========================================================
# Explainability
# ==========================================================

FeatureImportance = dict[str, float]

ShapValues = Any

# ==========================================================
# Export
# ==========================================================

__all__ = [
    "ArrayLike",
    "Config",
    "DataFrameLike",
    "EpochHistory",
    "FeatureImportance",
    "FeatureMatrix",
    "History",
    "LossHistory",
    "Metadata",
    "MetricFunction",
    "MetricResult",
    "Number",
    "OptimizationHistory",
    "Parameters",
    "PathLike",
    "Prediction",
    "Probability",
    "Registry",
    "RegistryMetadata",
    "SearchSpace",
    "ShapValues",
    "TargetVector",
    "TrialResult",
    "ValidationHistory",
]
# ==========================================================
# Randomness
# ==========================================================


def set_random_seed(seed: int = 42) -> None:
    """
    Set random seeds for reproducibility.
    """

    random.seed(seed)
    np.random.seed(seed)

    try:
        import torch

        torch.manual_seed(seed)
        torch.cuda.manual_seed_all(seed)

    except ImportError:
        pass


# ==========================================================
# Timing
# ==========================================================


class Timer:
    """
    Simple execution timer.
    """

    def __init__(self):

        self.start_time = None

    def __enter__(self):

        self.start_time = time.perf_counter()

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):

        self.elapsed = time.perf_counter() - self.start_time


# ==========================================================
# Filesystem
# ==========================================================


def ensure_directory(path: str | Path):

    path = Path(path)

    path.mkdir(
        parents=True,
        exist_ok=True,
    )

    return path


# ==========================================================
# Dictionaries
# ==========================================================


def merge_parameters(
    default: dict[str, Any],
    override: dict[str, Any],
):

    merged = default.copy()

    merged.update(override)

    return merged


# ==========================================================
# Validation
# ==========================================================


def is_fitted(model) -> bool:

    return getattr(model, "is_fitted", False)


# ==========================================================
# Pretty Printing
# ==========================================================


def print_header(title: str):

    line = "=" * 70

    print(line)

    print(title)

    print(line)


# ==========================================================
# Export
# ==========================================================

__all__ = [
    "Timer",
    "ensure_directory",
    "is_fitted",
    "merge_parameters",
    "print_header",
    "set_random_seed",
]
