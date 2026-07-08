"""
Classification metrics.
"""

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)


def evaluate_classification(
        y_true,
        y_pred):

    return {

        "Accuracy":
        accuracy_score(y_true, y_pred),

        "Precision":
        precision_score(
            y_true,
            y_pred,
            average="weighted"
        ),

        "Recall":
        recall_score(
            y_true,
            y_pred,
            average="weighted"
        ),

        "F1":
        f1_score(
            y_true,
            y_pred,
            average="weighted"
        )

    }
