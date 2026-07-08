"""
Metrics used for plotting.
"""

import pandas as pd


def metric_table(metrics):

    return pd.DataFrame(
        metrics.items(),
        columns=["Metric","Value"]
    )


def leaderboard_table(results):

    return pd.DataFrame(results)


def radar_data(metrics):

    return list(metrics.values())


def heatmap_matrix(df):

    return df.corr(
        numeric_only=True
    )
