"""
Memory benchmarking.
"""

import tracemalloc


def start():
    tracemalloc.start()


def stop():
    tracemalloc.stop()


def current_memory():
    current, peak = tracemalloc.get_traced_memory()
    return current


def peak_memory():
    current, peak = tracemalloc.get_traced_memory()
    return peak

__all__ = [
    "current_memory",
    "peak_memory",
    "memory_usage",
    "memory_delta",
    "memory_growth",
    "memory_per_sample",
    "memory_per_parameter",
    "memory_efficiency",
    "memory_bandwidth",
    "memory_utilization",
    "memory_fragmentation",
    "virtual_memory_usage",
    "resident_memory_usage",
    "shared_memory_usage",
    "gpu_memory_usage",
    "gpu_peak_memory",
    "cpu_memory_usage",
    "swap_memory_usage",
    "cache_memory_usage",
    "buffer_memory_usage",
    "available_memory",
    "free_memory",
    "total_memory",
    "allocated_memory",
    "reserved_memory",
    "memory_statistics",
    "memory_summary",
    "memory_report",
    "memory_dataframe",
    "normalize_memory",
    "compare_memory",
    "memory_percent",
    "memory_ratio",
    "memory_score",
    "memory_profile",
    "track_memory",
    "measure_memory",
    "measure_peak_memory",
    "memory_leak_check",
    "memory_snapshot",
]
