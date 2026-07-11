class BenchmarkRegistry:

    def __init__(self):
        self._benchmarks = {}

    def register(self, benchmark):
        self._benchmarks[benchmark.name] = benchmark

    def unregister(self, name):
        self._benchmarks.pop(name, None)

    def list(self):
        return list(self._benchmarks.keys())

    def get(self, name):
        return self._benchmarks.get(name)

    def exists(self, name):
        return name in self._benchmarks
