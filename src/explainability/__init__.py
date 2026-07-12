"""
CircuitBench Explainability Package
===================================

Explainability and model interpretation utilities.

Modules
-------
- permutation_importance
- shap_wrapper
- partial_dependence
- ice
"""

from .permutation_importance import PermutationImportance

__all__ = [
    "PermutationImportance",
]
