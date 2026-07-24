"""
CircuitBench Permutation Importance
==================================

Production-quality permutation feature importance.

Author
------
CircuitBench Development Team
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd
from sklearn.metrics import get_scorer


@dataclass
class PermutationImportanceResult:
    feature_names: list[str]
    importances_mean: np.ndarray
    importances_std: np.ndarray
    raw_importances: np.ndarray


class PermutationImportance:
    @staticmethod
    def compute(
        model,
        X,
        y,
        scoring="r2",
        n_repeats=20,
        random_state=42,
    ):
        """
        Compute permutation feature importance.
        """

        X = pd.DataFrame(X).copy()

        scorer = get_scorer(scoring)

        rng = np.random.default_rng(random_state)

        baseline = scorer(
            model,
            X,
            y,
        )

        raw = np.zeros(
            (
                X.shape[1],
                n_repeats,
            ),
            dtype=float,
        )

        for feature in range(X.shape[1]):
            column = X.iloc[
                :,
                feature,
            ].copy()

            for repeat in range(n_repeats):
                shuffled = column.sample(
                    frac=1.0,
                    random_state=int(rng.integers(1_000_000)),
                ).to_numpy()

                X.iloc[
                    :,
                    feature,
                ] = shuffled

                score = scorer(
                    model,
                    X,
                    y,
                )

                raw[
                    feature,
                    repeat,
                ] = baseline - score

            X.iloc[
                :,
                feature,
            ] = column

        return PermutationImportanceResult(
            feature_names=list(X.columns),
            importances_mean=np.mean(
                raw,
                axis=1,
            ),
            importances_std=np.std(
                raw,
                axis=1,
            ),
            raw_importances=raw,
        )

    @staticmethod
    def to_dataframe(
        result,
    ):
        """
        Convert importance result to DataFrame.
        """

        return (
            pd.DataFrame(
                {
                    "feature": result.feature_names,
                    "importance": result.importances_mean,
                    "std": result.importances_std,
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
