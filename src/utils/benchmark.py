"""
Benchmark score aggregation.
"""

import pandas as pd


def rank_models(results):

    df = pd.DataFrame(results)

    return df.sort_values(
        by="Score",
        ascending=False
    )


def best_model(results):

    ranking = rank_models(results)

    return ranking.iloc[0]


def leaderboard(results):

    return rank_models(results)
