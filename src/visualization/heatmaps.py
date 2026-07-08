"""
Generate correlation and error heatmaps.
"""

import matplotlib.pyplot as plt


def correlation_heatmap(matrix):
    plt.imshow(matrix)
    plt.colorbar()
    plt.title("Correlation Matrix")
    plt.show()


def error_heatmap(error_matrix):
    plt.imshow(error_matrix)
    plt.colorbar()
    plt.title("Prediction Error")
    plt.show()
