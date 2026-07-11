"""
Workflow execution engine.
"""

from concurrent.futures import ThreadPoolExecutor


class Workflow:

    def __init__(self, name="Workflow"):

        self.name = name

        self.tasks = []

    def add_task(self, function, *args, **kwargs):

        self.tasks.append((function, args, kwargs))

    def run(self):

        results = []

        for function, args, kwargs in self.tasks:

            results.append(function(*args, **kwargs))

        return results

    def run_parallel(self, workers=4):

        results = []

        with ThreadPoolExecutor(max_workers=workers) as executor:

            futures = [

                executor.submit(func, *args, **kwargs)

                for func, args, kwargs in self.tasks

            ]

            for future in futures:

                results.append(future.result())

        return results

    def clear(self):

        self.tasks.clear()

    def __len__(self):

        return len(self.tasks)
