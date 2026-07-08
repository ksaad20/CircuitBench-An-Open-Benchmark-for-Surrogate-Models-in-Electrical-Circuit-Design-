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
