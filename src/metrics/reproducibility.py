"""
Reproducibility metrics.
"""

import hashlib
import json


def hash_results(results):
    return hashlib.sha256(
        json.dumps(results, sort_keys=True).encode()
    ).hexdigest()


def identical(a, b):
    return a == b


def reproducibility_score(matches, total):
    return matches / total
