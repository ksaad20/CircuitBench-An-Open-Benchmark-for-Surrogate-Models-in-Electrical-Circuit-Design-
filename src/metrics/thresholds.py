"""
Threshold definitions used throughout CircuitBench.
"""

EXCELLENT = 0.95
VERY_GOOD = 0.90
GOOD = 0.80
FAIR = 0.70
POOR = 0.60


def grade(score: float) -> str:
    if score >= EXCELLENT:
        return "Excellent"
    elif score >= VERY_GOOD:
        return "Very Good"
    elif score >= GOOD:
        return "Good"
    elif score >= FAIR:
        return "Fair"
    elif score >= POOR:
        return "Poor"
    return "Fail"
