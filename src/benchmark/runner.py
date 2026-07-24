"""
CircuitBench Benchmark Runner

Core benchmark execution engine.

Author: CircuitBench
License: Apache-2.0
"""

from __future__ import annotations

import logging
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

logger = logging.getLogger(__name__)


@dataclass
class BenchmarkResult:
    """Stores the result of a single benchmark execution."""

    model_name: str
    dataset_name: str
    metrics: dict[str, float]
    runtime: float = 0.0
    memory: float = 0.0
    metadata: dict[str, Any] = field(default_factory=dict)


class BenchmarkRunner:
    def __init__(
        self,
        metrics: list | None = None,
        *,
        random_state: int | None = None,
        output_directory: str | Path | None = None,
        **kwargs: Any,
    ):
        """
        Initialize a benchmark runner.

        Parameters
        ----------
        metrics
            List of metric objects.
        random_state
            Random seed used for reproducibility.
        output_directory
            Directory for exported benchmark results.
        """

        self.metrics = metrics if metrics is not None else []

        self.random_state = random_state

        self.output_directory = (
            Path(output_directory)
            if output_directory is not None
            else Path("benchmark_results")
        )

        self.output_directory.mkdir(
            parents=True,
            exist_ok=True,
        )

        self.datasets = []
        self.models = []
        self.results = []
