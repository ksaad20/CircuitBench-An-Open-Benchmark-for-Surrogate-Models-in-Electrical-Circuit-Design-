"""
latency.py
==========

Latency and throughput utilities for CircuitBench.

This module provides small, reusable helpers to measure execution time,
summarize repeated latency measurements, and compute throughput-style
performance metrics for benchmarking models and pipelines.

Author: CircuitBench
License: Apache 2.0
"""

from __future__ import annotations

from dataclasses import dataclass
import time
from typing import Any, Callable, Iterable, Sequence

import numpy as np

__all__ = [
    "LatencyResult",
    "measure_latency",
    "measure_repeated_latency",
    "measure_with_warmup",
    "throughput",
    "samples_per_second",
    "median_latency",
    "mean_latency",
    "std_latency",
    "percentile_latency",
    "latency_summary",
    "speedup",
    "relative_latency",
]


@dataclass(frozen=True)
class LatencyResult:
    """
    Container for latency measurements.

    Attributes
    ----------
    samples : np.ndarray
        Raw latency samples in seconds.
    warmup_runs : int
        Number of warmup runs used before collecting samples.
    repeats : int
        Number of measured repetitions.
    """

    samples: np.ndarray
    warmup_runs: int = 0
    repeats: int = 1

    @property
    def mean(self) -> float:
        return float(np.mean(self.samples))

    @property
    def median(self) -> float:
        return float(np.median(self.samples))

    @property
    def std(self) -> float:
        if self.samples.size < 2:
            return 0.0
        return float(np.std(self.samples, ddof=1))

    def percentile(self, q: float) -> float:
        return float(np.percentile(self.samples, q))


def _validate_callable(func: Callable[..., Any]) -> None:
    if not callable(func):
        raise TypeError("func must be callable.")


def _validate_repeats(repeats: int) -> None:
    if not isinstance(repeats, int) or repeats <= 0:
        raise ValueError("repeats must be a positive integer.")


def _validate_warmup_runs(warmup_runs: int) -> None:
    if not isinstance(warmup_runs, int) or warmup_runs < 0:
        raise ValueError("warmup_runs must be a non-negative integer.")


def measure_latency(
    func: Callable[..., Any],
    *args: Any,
    **kwargs: Any,
) -> float:
    """
    Measure the wall-clock execution time of a callable once.

    Parameters
    ----------
    func : callable
        Function to execute.
    *args, **kwargs :
        Arguments forwarded to the callable.

    Returns
    -------
    float
        Elapsed time in seconds.
    """
    _validate_callable(func)

    start = time.perf_counter()
    func(*args, **kwargs)
    end = time.perf_counter()

    return float(end - start)


def measure_repeated_latency(
    func: Callable[..., Any],
    *args: Any,
    repeats: int = 10,
    **kwargs: Any,
) -> LatencyResult:
    """
    Measure repeated latency and return all raw samples.

    Parameters
    ----------
    func : callable
        Function to execute.
    repeats : int
        Number of repetitions.
    *args, **kwargs :
        Arguments forwarded to the callable.

    Returns
    -------
    LatencyResult
        Dataclass containing latency samples.
    """
    _validate_callable(func)
    _validate_repeats(repeats)

    samples = np.empty(repeats, dtype=float)

    for i in range(repeats):
        samples[i] = measure_latency(func, *args, **kwargs)

    return LatencyResult(samples=samples, warmup_runs=0, repeats=repeats)


def measure_with_warmup(
    func: Callable[..., Any],
    *args: Any,
    warmup_runs: int = 3,
    repeats: int = 10,
    **kwargs: Any,
) -> LatencyResult:
    """
    Measure repeated latency after warmup runs.

    Warmup runs are executed but not recorded. This is useful when benchmarking
    JIT compilation, GPU kernels, lazy imports, caching, or model initialization.

    Parameters
    ----------
    func : callable
        Function to execute.
    warmup_runs : int
        Number of warmup iterations.
    repeats : int
        Number of measured repetitions.
    *args, **kwargs :
        Arguments forwarded to the callable.

    Returns
    -------
    LatencyResult
        Dataclass containing latency samples.
    """
    _validate_callable(func)
    _validate_warmup_runs(warmup_runs)
    _validate_repeats(repeats)

    for _ in range(warmup_runs):
        func(*args, **kwargs)

    samples = np.empty(repeats, dtype=float)

    for i in range(repeats):
        samples[i] = measure_latency(func, *args, **kwargs)

    return LatencyResult(samples=samples, warmup_runs=warmup_runs, repeats=repeats)


def mean_latency(values: Sequence[float]) -> float:
    """
    Mean latency in seconds.
    """
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        raise ValueError("values must not be empty.")
    return float(np.mean(arr))


def median_latency(values: Sequence[float]) -> float:
    """
    Median latency in seconds.
    """
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        raise ValueError("values must not be empty.")
    return float(np.median(arr))


def std_latency(values: Sequence[float]) -> float:
    """
    Sample standard deviation of latency in seconds.
    """
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        raise ValueError("values must not be empty.")
    if arr.size < 2:
        return 0.0
    return float(np.std(arr, ddof=1))


def percentile_latency(values: Sequence[float], q: float) -> float:
    """
    Compute a latency percentile.

    Parameters
    ----------
    values : Sequence[float]
        Latency samples in seconds.
    q : float
        Percentile in [0, 100].

    Returns
    -------
    float
        Percentile latency in seconds.
    """
    if not 0 <= q <= 100:
        raise ValueError("q must be between 0 and 100.")
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        raise ValueError("values must not be empty.")
    return float(np.percentile(arr, q))


def latency_summary(values: Sequence[float]) -> dict[str, float]:
    """
    Produce a compact latency summary.

    Returns
    -------
    dict
        Summary statistics including mean, median, std, p95, and p99.
    """
    arr = np.asarray(values, dtype=float)
    if arr.size == 0:
        raise ValueError("values must not be empty.")

    return {
        "count": float(arr.size),
        "mean": float(np.mean(arr)),
        "median": float(np.median(arr)),
        "std": float(np.std(arr, ddof=1)) if arr.size > 1 else 0.0,
        "min": float(np.min(arr)),
        "p90": float(np.percentile(arr, 90)),
        "p95": float(np.percentile(arr, 95)),
        "p99": float(np.percentile(arr, 99)),
        "max": float(np.max(arr)),
    }


def throughput(samples: int, seconds: float) -> float:
    """
    Compute throughput as samples per second.
    """
    if samples < 0:
        raise ValueError("samples must be non-negative.")
    if seconds <= 0:
        raise ValueError("seconds must be positive.")
    return float(samples / seconds)


def samples_per_second(samples: int, seconds: float) -> float:
    """
    Alias for throughput.
    """
    return throughput(samples, seconds)


def speedup(baseline_seconds: float, candidate_seconds: float) -> float:
    """
    Compute speedup relative to a baseline.

    A value > 1 means the candidate is faster.
    """
    if baseline_seconds <= 0 or candidate_seconds <= 0:
        raise ValueError("Time values must be positive.")
    return float(baseline_seconds / candidate_seconds)


def relative_latency(baseline_seconds: float, candidate_seconds: float) -> float:
    """
    Compute candidate latency relative to baseline.

    A value < 1 means the candidate is faster.
    """
    if baseline_seconds <= 0 or candidate_seconds <= 0:
        raise ValueError("Time values must be positive.")
    return float(candidate_seconds / baseline_seconds)
