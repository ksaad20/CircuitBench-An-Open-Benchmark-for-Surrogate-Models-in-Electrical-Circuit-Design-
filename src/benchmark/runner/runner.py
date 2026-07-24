"""
Core benchmark runner.

This module provides a lightweight implementation of the benchmark runner
used by Circuit-Bench. It can be extended later with dataset loading,
metrics, reporting and visualization.
"""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass, field
from time import perf_counter
from typing import Any


@dataclass
class BenchmarkResult:
    """Stores the result of a benchmark execution."""

    name: str
    success: bool
    execution_time: float
    metrics: dict[str, Any] = field(default_factory=dict)
    metadata: dict[str, Any] = field(default_factory=dict)


class BenchmarkRunner:
    """Generic benchmark runner."""

    def __init__(self) -> None:
        self.results: list[BenchmarkResult] = []

    def run(
        self,
        name: str,
        benchmark: Callable[..., Any],
        *args: Any,
        **kwargs: Any,
    ) -> BenchmarkResult:
        """Execute a benchmark function."""

        start = perf_counter()

        success = True
        metrics: dict[str, Any] = {}

        try:
            output = benchmark(*args, **kwargs)
            if isinstance(output, dict):
                metrics = output
        except Exception as exc:
            success = False
            metrics["error"] = str(exc)

        execution_time = perf_counter() - start

        result = BenchmarkResult(
            name=name,
            success=success,
            execution_time=execution_time,
            metrics=metrics,
        )

        self.results.append(result)
        return result
