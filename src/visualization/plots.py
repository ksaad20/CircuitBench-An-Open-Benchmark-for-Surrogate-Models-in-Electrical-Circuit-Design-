"""
Standard publication-quality plotting functions.
"""

import matplotlib.pyplot as plt


def plot_loss(train_loss, val_loss):
    plt.figure(figsize=(6,4))
    plt.plot(train_loss, label="Training")
    plt.plot(val_loss, label="Validation")
    plt.xlabel("Epoch")
    plt.ylabel("Loss")
    plt.legend()
    plt.tight_layout()
    plt.show()


def scatter_prediction(y_true, y_pred):
    plt.figure(figsize=(5,5))
    plt.scatter(y_true, y_pred)
    plt.xlabel("True")
    plt.ylabel("Predicted")
    plt.tight_layout()
    plt.show()


def histogram_errors(errors):
    plt.figure(figsize=(6,4))
    plt.hist(errors, bins=30)
    plt.xlabel("Prediction Error")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.show()
