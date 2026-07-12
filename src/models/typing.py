"""
CircuitBench Typing Definitions
===============================

Shared typing aliases used throughout the framework.
"""
from __future__ import annotations

import random
import time
from pathlib import Path
from typing import Any, Dict
import numpy as np
from pathlib import Path
from typing import (
    Any,
    Callable,
    Dict,
    List,
    MutableMapping,
    Sequence,
    Type,
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

Parameters = Dict[str, Any]

Metadata = Dict[str, Any]

History = Dict[str, Any]

Config = Dict[str, Any]

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

Registry = MutableMapping[str, Type]

RegistryMetadata = MutableMapping[str, Metadata]

# ==========================================================
# Metrics
# ==========================================================

MetricResult = Dict[str, float]

MetricFunction = Callable[..., float]

# ==========================================================
# Training
# ==========================================================

LossHistory = List[float]

ValidationHistory = List[float]

EpochHistory = Dict[str, List[float]]

# ==========================================================
# Hyperparameter Optimization
# ==========================================================

SearchSpace = Dict[str, Any]

TrialResult = Dict[str, Any]

OptimizationHistory = List[TrialResult]

# ==========================================================
# Explainability
# ==========================================================

FeatureImportance = Dict[str, float]

ShapValues = Any

# ==========================================================
# Export
# ==========================================================

__all__ = [
    "Number",
    "PathLike",
    "Parameters",
    "Metadata",
    "History",
    "Config",
    "ArrayLike",
    "DataFrameLike",
    "FeatureMatrix",
    "TargetVector",
    "Prediction",
    "Probability",
    "Registry",
    "RegistryMetadata",
    "MetricResult",
    "MetricFunction",
    "LossHistory",
    "ValidationHistory",
    "EpochHistory",
    "SearchSpace",
    "TrialResult",
    "OptimizationHistory",
    "FeatureImportance",
    "ShapValues",
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
    default: Dict[str, Any],
    override: Dict[str, Any],
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
    "set_random_seed",
    "ensure_directory",
    "merge_parameters",
    "is_fitted",
    "print_header",
]
