import logging
from .registry import BenchmarkRegistry


class BenchmarkRunner:
    def __init__(self):
        self.registry = BenchmarkRegistry()

        logging.basicConfig(level=logging.INFO, format="%(levelname)s | %(message)s")

    def register(self, benchmark):
        self.registry.register(benchmark)

    def run(self, benchmark_name):
        benchmark = self.registry.get(benchmark_name)

        if benchmark is None:
            raise ValueError(f"Benchmark '{benchmark_name}' not found.")

        logging.info(f"Running {benchmark.name}")

        X = benchmark.load_dataset()
        X = benchmark.preprocess(X)
        benchmark.train()
        metrics = benchmark.evaluate()
        benchmark.leaderboard()

        logging.info("Finished.")

        return metrics
