"""
Efficiency metrics.
"""

import time


def throughput(samples, seconds):
    return samples / seconds


def samples_per_second(samples, runtime):
    return samples / runtime


def speedup(serial, parallel):
    return serial / parallel


def efficiency(speedup_value, processors):
    return speedup_value / processors
