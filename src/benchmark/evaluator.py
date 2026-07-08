"""
Evaluator.
"""

from .metrics import *
from .scorer import CompositeScore


class Evaluator:

    def __init__(self):

        self.scorer=CompositeScore()

    def evaluate(self,
                 y_true,
                 y_pred):

        results={}

        results["MAE"]=mae(y_true,y_pred)

        results["MSE"]=mse(y_true,y_pred)

        results["RMSE"]=rmse(y_true,y_pred)

        results["R2"]=r2(y_true,y_pred)

        results["MAPE"]=mape(y_true,y_pred)

        results["Score"]=self.scorer.score(
            results["RMSE"],
            results["MAE"],
            results["R2"]
        )

        return results
