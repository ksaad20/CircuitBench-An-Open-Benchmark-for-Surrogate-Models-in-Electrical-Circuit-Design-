"""
CircuitBench Benchmark Framework.
"""

from __future__ import annotations

from .benchmark_runner import BenchmarkRunner as LegacyBenchmarkRunner
from .benchmark_suite import BenchmarkSuite
from .experiment import Experiment
from .experiment_manager import ExperimentManager
from .leaderboard import Leaderboard
from .runner import BenchmarkRunner

AVAILABLE_BENCHMARKS = [
    "classification",
    "regression",
    "simulation",
    "optimization",
]

__all__ = [
    "AVAILABLE_BENCHMARKS",
    "BenchmarkRunner",
    "BenchmarkSuite",
    "Experiment",
    "ExperimentManager",
    "Leaderboard",
    "LegacyBenchmarkRunner",
]
