"""
CircuitBench SHAP Wrapper
=========================

Unified SHAP interface for supported models.

Author
------
CircuitBench Development Team
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd

try:
    import shap
    SHAP_AVAILABLE = True
except ImportError:
    SHAP_AVAILABLE = False


@dataclass
class SHAPResult:
    values: np.ndarray
    base_values: np.ndarray | float
    feature_names: list[str]


class SHAPWrapper:
    """
    Unified SHAP interface.
    """

    @staticmethod
    def available() -> bool:
        return SHAP_AVAILABLE

    @staticmethod
    def explain(
        model,
        X,
    ):
        """
        Compute SHAP values.
        """

        if not SHAP_AVAILABLE:
            raise ImportError(
                "Install shap with: pip install shap"
            )

        X = pd.DataFrame(X)

        try:

            explainer = shap.TreeExplainer(
                model
            )

        except Exception:

            try:

                explainer = shap.LinearExplainer(
                    model,
                    X,
                )

            except Exception:

                explainer = shap.Explainer(
                    model.predict,
                    X,
                )

        explanation = explainer(
            X
        )

        return SHAPResult(

            values=np.asarray(
                explanation.values
            ),

            base_values=explanation.base_values,

            feature_names=list(
                X.columns
            ),

        )

    @staticmethod
    def feature_importance(
        result: SHAPResult,
    ):
        """
        Mean absolute SHAP importance.
        """

        values = np.abs(
            result.values
        )

        if values.ndim == 3:
            values = values.mean(
                axis=2
            )

        importance = values.mean(
            axis=0
        )

        return (

            pd.DataFrame(

                {

                    "feature":
                        result.feature_names,

                    "importance":
                        importance,

                }

            )

            .sort_values(

                "importance",

                ascending=False,

            )

            .reset_index(

                drop=True,

            )

        )

    @staticmethod
    def summary_plot(
        result,
        X,
        show=True,
    ):
        """
        SHAP summary plot.
        """

        if not SHAP_AVAILABLE:
            raise ImportError(
                "Install shap first."
            )

        shap.summary_plot(

            result.values,

            X,

            feature_names=result.feature_names,

            show=show,

        )

    @staticmethod
    def bar_plot(
        result,
        X,
        show=True,
    ):
        """
        SHAP bar plot.
        """

        if not SHAP_AVAILABLE:
            raise ImportError(
                "Install shap first."
            )

        shap.summary_plot(

            result.values,

            X,

            feature_names=result.feature_names,

            plot_type="bar",

            show=show,

        )

