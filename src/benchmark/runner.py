"""
Benchmark Runner.
"""

from .evaluator import Evaluator


class Runner:

    def __init__(self):

        self.evaluator=Evaluator()

    def run(self,y_true,y_pred):

        return self.evaluator.evaluate(
            y_true,
            y_pred
        )
