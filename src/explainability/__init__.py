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

from .ice import ICEPlots
from .partial_dependence import PartialDependence
from .permutation_importance import PermutationImportance
from .shap_wrapper import SHAPWrapper

__all__ = [
    "ICEPlots",
    "PartialDependence",
    "PermutationImportance",
    "SHAPWrapper",
]
