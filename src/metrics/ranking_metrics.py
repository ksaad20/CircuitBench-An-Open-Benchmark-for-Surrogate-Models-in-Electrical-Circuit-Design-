"""
CircuitBench Ranking Metrics
============================

Comprehensive ranking and information retrieval metrics.

Author
------
CircuitBench Development Team
"""

from __future__ import annotations

import numpy as np


class RankingMetrics:
    """
    Comprehensive ranking metrics.
    """

    @staticmethod
    def precision_at_k(
        y_true,
        y_pred,
        k=10,
    ):
        """
        Precision@K.
        """

        y_true = set(y_true)

        retrieved = y_pred[:k]

        if k == 0:
            return 0.0

        hits = sum(
            item in y_true
            for item in retrieved
        )

        return float(
            hits / k
        )

    @staticmethod
    def recall_at_k(
        y_true,
        y_pred,
        k=10,
    ):
        """
        Recall@K.
        """

        y_true = set(y_true)

        if len(y_true) == 0:
            return 0.0

        retrieved = y_pred[:k]

        hits = sum(
            item in y_true
            for item in retrieved
        )

        return float(
            hits
            /
            len(y_true)
        )

    @staticmethod
    def hit_rate(
        y_true,
        y_pred,
        k=10,
    ):
        """
        Hit Rate.
        """

        y_true = set(y_true)

        return float(

            any(

                item in y_true

                for item in y_pred[:k]

            )

        )

    @staticmethod
    def reciprocal_rank(
        y_true,
        y_pred,
    ):
        """
        Reciprocal Rank.
        """

        y_true = set(y_true)

        for rank, item in enumerate(
            y_pred,
            start=1,
        ):

            if item in y_true:

                return float(
                    1.0 / rank
                )

        return 0.0

    @staticmethod
    def average_precision(
        y_true,
        y_pred,
    ):
        """
        Average Precision.
        """

        y_true = set(y_true)

        if len(y_true) == 0:
            return 0.0

        score = 0.0

        hits = 0

        for rank, item in enumerate(
            y_pred,
            start=1,
        ):

            if item in y_true:

                hits += 1

                score += hits / rank

        return float(
            score
            /
            len(y_true)
        )


    @staticmethod
    def mean_average_precision(
        truth_lists,
        prediction_lists,
    ):
        """
        Mean Average Precision (MAP).
        """

        scores = [

            RankingMetrics.average_precision(
                truth,
                pred,
            )

            for truth, pred in zip(
                truth_lists,
                prediction_lists,
            )

        ]

        if len(scores) == 0:
            return 0.0

        return float(
            np.mean(scores)
        )

    @staticmethod
    def mean_reciprocal_rank(
        truth_lists,
        prediction_lists,
    ):
        """
        Mean Reciprocal Rank (MRR).
        """

        scores = [

            RankingMetrics.reciprocal_rank(
                truth,
                pred,
            )

            for truth, pred in zip(
                truth_lists,
                prediction_lists,
            )

        ]

        if len(scores) == 0:
            return 0.0

        return float(
            np.mean(scores)
        )

    @staticmethod
    def cumulative_gain(
        relevance,
    ):
        """
        Cumulative Gain.
        """

        relevance = np.asarray(
            relevance,
            dtype=float,
        )

        return float(
            np.sum(
                relevance
            )
        )

    @staticmethod
    def discounted_cumulative_gain(
        relevance,
    ):
        """
        Discounted Cumulative Gain.
        """

        relevance = np.asarray(
            relevance,
            dtype=float,
        )

        if len(relevance) == 0:

            return 0.0

        discounts = np.log2(

            np.arange(

                2,

                len(relevance) + 2,

            )

        )

        return float(

            np.sum(

                relevance / discounts

            )

        )

    @staticmethod
    def normalized_discounted_cumulative_gain(
        relevance,
    ):
        """
        Normalized DCG.
        """

        relevance = np.asarray(
            relevance,
            dtype=float,
        )

        ideal = np.sort(
            relevance
        )[::-1]

        ideal_score = RankingMetrics.discounted_cumulative_gain(
            ideal,
        )

        if ideal_score == 0:

            return 0.0

        return float(

            RankingMetrics.discounted_cumulative_gain(

                relevance,

            )

            /

            ideal_score

        )


    @staticmethod
    def success_at_k(
        y_true,
        y_pred,
        k=10,
    ):
        """
        Success@K.
        """

        return float(

            RankingMetrics.hit_rate(

                y_true,

                y_pred,

                k,

            )

        )

    @staticmethod
    def r_precision(
        y_true,
        y_pred,
    ):
        """
        R-Precision.
        """

        r = len(y_true)

        if r == 0:

            return 0.0

        return RankingMetrics.precision_at_k(

            y_true,

            y_pred,

            k=r,

        )

    @staticmethod
    def f1_at_k(
        y_true,
        y_pred,
        k=10,
    ):
        """
        F1@K.
        """

        precision = RankingMetrics.precision_at_k(

            y_true,

            y_pred,

            k,

        )

        recall = RankingMetrics.recall_at_k(

            y_true,

            y_pred,

            k,

        )

        if precision + recall == 0:

            return 0.0

        return float(

            2.0

            * precision

            * recall

            /

            (

                precision

                + recall

            )

        )

    @staticmethod
    def coverage_at_k(
        truth_lists,
        prediction_lists,
        k=10,
    ):
        """
        Coverage@K.
        """

        relevant = set()

        retrieved = set()

        for truth, prediction in zip(

            truth_lists,

            prediction_lists,

        ):

            relevant.update(truth)

            retrieved.update(

                prediction[:k]

            )

        if len(relevant) == 0:

            return 0.0

        return float(

            len(

                relevant.intersection(

                    retrieved

                )

            )

            /

            len(relevant)

        )

    @classmethod
    def basic_report(
        cls,
        y_true,
        y_pred,
        k=10,
    ):
        """
        Basic ranking report.
        """

        return {

            "Precision@K":

                cls.precision_at_k(

                    y_true,

                    y_pred,

                    k,

                ),

            "Recall@K":

                cls.recall_at_k(

                    y_true,

                    y_pred,

                    k,

                ),

            "HitRate":

                cls.hit_rate(

                    y_true,

                    y_pred,

                    k,

                ),

            "ReciprocalRank":

                cls.reciprocal_rank(

                    y_true,

                    y_pred,

                ),

            "AveragePrecision":

                cls.average_precision(

                    y_true,

                    y_pred,

                ),

            "RPrecision":

                cls.r_precision(

                    y_true,

                    y_pred,

                ),

            "F1@K":

                cls.f1_at_k(

                    y_true,

                    y_pred,

                    k,

                ),

            "Success@K":

                cls.success_at_k(

                    y_true,

                    y_pred,

                    k,

                ),

        }


__all__ = [

    "RankingMetrics",

]

