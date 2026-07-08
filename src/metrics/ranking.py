"""
Ranking metrics for CircuitBench.
"""

from __future__ import annotations

import numpy as np


def rank_models(scores: dict, reverse: bool = True) -> list:
    """
    Rank models by score.

    Parameters
    ----------
    scores : dict
        {"RandomForest":0.91, "XGBoost":0.95}

    reverse : bool
        True = larger is better

    Returns
    -------
    list
        Sorted list of tuples.
    """
    return sorted(scores.items(), key=lambda x: x[1], reverse=reverse)


def leaderboard(scores: dict) -> list[dict]:
    ranked = rank_models(scores)

    board = []

    for i, (name, score) in enumerate(ranked, start=1):
        board.append({
            "Rank": i,
            "Model": name,
            "Score": score
        })

    return board


def average_rank(rankings: list[list[int]]) -> np.ndarray:
    rankings = np.asarray(rankings)

    return np.mean(rankings, axis=0)


def weighted_rank(scores: dict, weights: dict) -> dict:

    output = {}

    for model in scores:

        output[model] = scores[model] * weights.get(model, 1.0)

    return output


def top_k(scores: dict, k: int = 5):

    return rank_models(scores)[:k]


def bottom_k(scores: dict, k: int = 5):

    return rank_models(scores)[-k:]


def best_model(scores: dict):

    return rank_models(scores)[0]


def worst_model(scores: dict):

    return rank_models(scores)[-1]


def percentile_rank(values):

    values = np.asarray(values)

    return np.argsort(np.argsort(values)) / len(values)


def score_gap(scores: dict):

    ranked = rank_models(scores)

    return ranked[0][1] - ranked[-1][1]
