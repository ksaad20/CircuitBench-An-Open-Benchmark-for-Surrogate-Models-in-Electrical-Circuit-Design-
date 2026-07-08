"""
Generate benchmark summary dashboards.
"""

from dataclasses import dataclass


@dataclass
class DashboardMetrics:

    model_name: str
    mae: float
    rmse: float
    r2: float
    inference_time: float
    memory: float


def summarize(metrics):

    print("="*40)

    print(metrics.model_name)

    print("="*40)

    print(f"MAE : {metrics.mae}")

    print(f"RMSE: {metrics.rmse}")

    print(f"R²  : {metrics.r2}")

    print(f"Latency : {metrics.inference_time}")

    print(f"Memory  : {metrics.memory}")
