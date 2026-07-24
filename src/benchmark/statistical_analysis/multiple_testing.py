"""
CircuitBench Multiple Testing Correction
========================================

Multiple hypothesis testing correction procedures.

Author
------
CircuitBench Development Team
"""

from __future__ import annotations

import numpy as np
from statsmodels.stats.multitest import multipletests


class MultipleTesting:
    """
    Multiple hypothesis testing correction methods.
    """

    @staticmethod
    def bonferroni(p_values):

        p_values = np.asarray(p_values)

        reject, corrected, _, _ = multipletests(
            p_values,
            alpha=0.05,
            method="bonferroni",
        )

        return {
            "method": "bonferroni",
            "corrected_p_values": corrected,
            "reject": reject,
        }

    # --------------------------------------------------

    @staticmethod
    def holm(p_values):

        p_values = np.asarray(p_values)

        reject, corrected, _, _ = multipletests(
            p_values,
            alpha=0.05,
            method="holm",
        )

        return {
            "method": "holm",
            "corrected_p_values": corrected,
            "reject": reject,
        }

    # --------------------------------------------------

    @staticmethod
    def holm_sidak(p_values):

        p_values = np.asarray(p_values)

        reject, corrected, _, _ = multipletests(
            p_values,
            alpha=0.05,
            method="holm-sidak",
        )

        return {
            "method": "holm-sidak",
            "corrected_p_values": corrected,
            "reject": reject,
        }

    # --------------------------------------------------

    @staticmethod
    def benjamini_hochberg(p_values):

        p_values = np.asarray(p_values)

        reject, corrected, _, _ = multipletests(
            p_values,
            alpha=0.05,
            method="fdr_bh",
        )

        return {
            "method": "benjamini-hochberg",
            "corrected_p_values": corrected,
            "reject": reject,
        }

    # --------------------------------------------------

    @staticmethod
    def benjamini_yekutieli(p_values):

        p_values = np.asarray(p_values)

        reject, corrected, _, _ = multipletests(
            p_values,
            alpha=0.05,
            method="fdr_by",
        )

        return {
            "method": "benjamini-yekutieli",
            "corrected_p_values": corrected,
            "reject": reject,
        }

    # --------------------------------------------------

    @staticmethod
    def sidak(p_values):

        p_values = np.asarray(p_values)

        reject, corrected, _, _ = multipletests(
            p_values,
            alpha=0.05,
            method="sidak",
        )

        return {
            "method": "sidak",
            "corrected_p_values": corrected,
            "reject": reject,
        }

    # --------------------------------------------------

    @classmethod
    def compare_all(cls, p_values) -> dict:

        return {
            "bonferroni": cls.bonferroni(p_values),
            "holm": cls.holm(p_values),
            "holm_sidak": cls.holm_sidak(p_values),
            "benjamini_hochberg": cls.benjamini_hochberg(p_values),
            "benjamini_yekutieli": cls.benjamini_yekutieli(p_values),
            "sidak": cls.sidak(p_values),
        }


__all__ = [
    "MultipleTesting",
]
