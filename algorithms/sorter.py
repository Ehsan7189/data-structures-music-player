import time
import tracemalloc


class Sorter:

    def __init__(self,algorithm_name):

        self.algorithm_name = algorithm_name

    def measure(self, playlist, key):
        start_time = time.perf_counter()
        tracemalloc.start()
        self.sort(playlist, key)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        end_time = time.perf_counter()
        return {
            "algorithm": self.algorithm_name,
            "time": end_time - start_time,
            "memory": peak
        }