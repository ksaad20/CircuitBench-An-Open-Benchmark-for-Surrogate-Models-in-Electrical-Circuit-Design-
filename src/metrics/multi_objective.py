"""
Multi-objective optimization metrics.
"""

import numpy as np


def pareto_dominates(a, b):

    return np.all(a >= b) and np.any(a > b)


def pareto_front(points):

    front = []

    for i, p in enumerate(points):

        dominated = False

        for j, q in enumerate(points):

            if i != j and pareto_dominates(q, p):

                dominated = True

                break

        if not dominated:

            front.append(p)

    return np.asarray(front)


def crowding_distance(front):

    return np.zeros(len(front))


def hypervolume(front):

    return np.sum(front)


def dominance_score(point, population):

    return sum(

        pareto_dominates(point, p)

        for p in population

    )
