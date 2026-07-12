"""
CircuitBench Calibration Metrics
================================

Calibration metrics for probabilistic machine learning models.

Author
------
CircuitBench Development Team
"""

from __future__ import annotations

import numpy as np

from sklearn.calibration import calibration_curve


class CalibrationMetrics:
    """
    Calibration metrics.
    """

    @staticmethod
    def expected_calibration_error(
        y_true,
        y_prob,
        n_bins=10,
    ):
        """
        Expected Calibration Error (ECE).
        """

        y_true = np.asarray(y_true)
        y_prob = np.asarray(y_prob)

        bins = np.linspace(
            0.0,
            1.0,
            n_bins + 1,
        )

        ece = 0.0

        for i in range(n_bins):
            mask = (y_prob >= bins[i]) & (y_prob < bins[i + 1])

            if np.any(mask):
                accuracy = np.mean(y_true[mask])

                confidence = np.mean(y_prob[mask])

                ece += (np.sum(mask) / len(y_true)) * abs(accuracy - confidence)

        return float(ece)

    @staticmethod
    def calibration_curve_data(
        y_true,
        y_prob,
        n_bins=10,
    ):
        """
        Returns calibration curve data.
        """

        return calibration_curve(
            y_true,
            y_prob,
            n_bins=n_bins,
        )

    @staticmethod
    def maximum_calibration_error(
        y_true,
        y_prob,
        n_bins=10,
    ):
        """
        Maximum Calibration Error (MCE).
        """

        y_true = np.asarray(y_true)
        y_prob = np.asarray(y_prob)

        bins = np.linspace(
            0.0,
            1.0,
            n_bins + 1,
        )

        max_error = 0.0

        for i in range(n_bins):
            mask = (y_prob >= bins[i]) & (y_prob < bins[i + 1])

            if np.any(mask):
                accuracy = np.mean(y_true[mask])

                confidence = np.mean(y_prob[mask])

                error = abs(accuracy - confidence)

                max_error = max(
                    max_error,
                    error,
                )

        return float(max_error)

    @staticmethod
    def brier_skill_score(
        y_true,
        y_prob,
    ):
        """
        Brier Skill Score.
        """

        y_true = np.asarray(y_true)

        y_prob = np.asarray(y_prob)

        climatology = np.mean(y_true)

        bs_model = np.mean((y_prob - y_true) ** 2)

        bs_reference = np.mean((climatology - y_true) ** 2)

        if bs_reference == 0:
            return 0.0

        return float(1.0 - (bs_model / bs_reference))

    @staticmethod
    def calibration_error(
        y_true,
        y_prob,
    ):
        """
        Mean absolute calibration error.
        """

        return float(np.mean(np.abs(np.asarray(y_true) - np.asarray(y_prob))))

    @classmethod
    def basic_report(
        cls,
        y_true,
        y_prob,
    ):
        """
        Basic calibration report.
        """

        return {
            "ECE": cls.expected_calibration_error(
                y_true,
                y_prob,
            ),
            "MCE": cls.maximum_calibration_error(
                y_true,
                y_prob,
            ),
            "CalibrationError": cls.calibration_error(
                y_true,
                y_prob,
            ),
            "BrierSkillScore": cls.brier_skill_score(
                y_true,
                y_prob,
            ),
        }
