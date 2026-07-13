"""
Compatibility layer.

The canonical BenchmarkRunner implementation now lives in
src.benchmark.runner.runner.
"""

from __future__ import annotations

from .runner.runner import BenchmarkRunner
from .runner.runner import BenchmarkResult

__all__ = [
    "BenchmarkRunner",
    "BenchmarkResult",
]
