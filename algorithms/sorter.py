import time
import tracemalloc


class Sorter:

    

    def __init__(self,algorithm_name):

        self.algorithm_name = algorithm_name
        self.trace = False
        self.step = 1

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
            "memory": peak,
            "sorted_by": key
        }

    def compare(self, node1, node2, key):

        left = getattr(node1.song, key).lower()
        right = getattr(node2.song, key).lower()

        if left > right:
            return 1
        elif left < right:
            return -1
        else:
            return 0
    
    def swap(self, node1, node2):

        node1.song, node2.song = node2.song, node1.song    

    def show_step(self, playlist, message):

        if not self.trace:
            return

        if playlist.size > 10:
            return

        print("\n" + "=" * 50)
        print(f"Step {self.step}")
        print(message)
        print("=" * 50)

        playlist.display()

        self.step += 1