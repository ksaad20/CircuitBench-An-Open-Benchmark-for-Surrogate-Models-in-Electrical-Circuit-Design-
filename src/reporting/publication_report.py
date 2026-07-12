"""
CircuitBench Publication Report
===============================

Generate publication-style benchmark reports.

Author
------
CircuitBench Development Team
"""

from __future__ import annotations

from datetime import datetime
import pandas as pd


class PublicationReport:

    @staticmethod
    def best_model(
        leaderboard,
        metric,
        ascending=False,
    ):

        leaderboard = leaderboard.sort_values(
            metric,
            ascending=ascending,
        )

        return leaderboard.iloc[0]


    @staticmethod
    def executive_summary(
        leaderboard,
        metric,
        ascending=False,
    ):

        best = PublicationReport.best_model(
            leaderboard,
            metric,
            ascending,
        )

        lines = []

        lines.append("# Executive Summary")
        lines.append("")
        lines.append(
            f"Generated: {datetime.now().isoformat()}"
        )
        lines.append("")
        lines.append(
            f"Models evaluated: {len(leaderboard)}"
        )
        lines.append("")
        lines.append(
            f"Best model: {best['Model']}"
        )
        lines.append("")
        lines.append(
            f"{metric}: {best[metric]:.6f}"
        )

        return "\n".join(lines)


    @staticmethod
    def methods():

        return """
# Methods

Benchmarking followed a standardized evaluation
pipeline including:

- Model training
- Independent evaluation
- Timing analysis
- Memory analysis
- Statistical comparison
- Calibration assessment
- Explainability analysis

All models were evaluated using identical
datasets and preprocessing.
"""


    @staticmethod
    def results_table(
        leaderboard,
    ):

        return leaderboard.to_markdown(
            index=False
        )


    @staticmethod
    def discussion():

        return """
# Discussion

The benchmark demonstrates comparative model
performance using standardized evaluation
procedures.

Differences between models should be interpreted
alongside confidence intervals and statistical
tests.
"""


    @staticmethod
    def generate(
        leaderboard,
        metric,
        ascending=False,
    ):

        sections = [

            PublicationReport.executive_summary(
                leaderboard,
                metric,
                ascending,
            ),

            PublicationReport.methods(),

            "# Results",

            PublicationReport.results_table(
                leaderboard,
            ),

            PublicationReport.discussion(),

        ]

        return "\n\n".join(sections)


    @staticmethod
    def save(
        leaderboard,
        filename,
        metric,
        ascending=False,
    ):

        report = PublicationReport.generate(

            leaderboard,

            metric,

            ascending,

        )

        with open(
            filename,
            "w",
            encoding="utf-8",
        ) as f:

            f.write(report)

