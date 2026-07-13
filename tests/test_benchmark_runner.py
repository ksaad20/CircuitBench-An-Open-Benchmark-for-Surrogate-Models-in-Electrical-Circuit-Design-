"""
Compatibility layer.

The canonical BenchmarkRunner implementation now lives in
src.benchmark.runner.runner.
"""

from __future__ import annotations

from benchmark.runner.runner import (
    BenchmarkRunner,
    BenchmarkResult,
)

__all__ = [
    "BenchmarkRunner",
    "BenchmarkResult",
]
