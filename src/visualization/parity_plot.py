"""
True vs Predicted parity plots.
"""

import matplotlib.pyplot as plt


def parity(y_true, y_pred):

    plt.scatter(y_true, y_pred)

    minimum = min(min(y_true), min(y_pred))

    maximum = max(max(y_true), max(y_pred))

    plt.plot([minimum, maximum],
             [minimum, maximum],
             '--')

    plt.xlabel("Measured")

    plt.ylabel("Predicted")

    plt.show()
