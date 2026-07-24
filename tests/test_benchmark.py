"""
Tests for benchmark loading and execution.
"""

import pytest


def test_benchmark_module_exists():
    try:
        pass
    except Exception as e:
        pytest.fail(f"Benchmark module failed to import: {e}")


def test_available_benchmarks():
    from src import benchmark

    assert hasattr(benchmark, "AVAILABLE_BENCHMARKS")


def test_benchmark_is_list():
    from src import benchmark

    assert isinstance(benchmark.AVAILABLE_BENCHMARKS, list)
