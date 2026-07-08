"""
Visualization.
"""

import matplotlib.pyplot as plt


def leaderboard(df):

    plt.figure(figsize=(8,5))

    plt.bar(df["Model"],df["Score"])

    plt.ylabel("Composite Score")

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.show()
