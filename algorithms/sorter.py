import time
import tracemalloc
from models.node import Node   # اضافه کردن import


class Sorter:

    def __init__(self, algorithm_name):

        self.algorithm_name = algorithm_name
        self.trace = False
        self.step = 1
        self.comparisons = 0
        self.movements = 0

    def measure(self, playlist, key):

        self.comparisons = 0
        self.movements = 0
        self.step = 1

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
            "sorted_by": key,
            "comparisons": self.comparisons,
            "movements": self.movements
        }

    def get_value(self, item, key):

        # ===== اصلاح: استفاده از isinstance =====
        if isinstance(item, Node):
            value = getattr(item.song, key)
        else:
            value = getattr(item, key)
        # ===== پایان اصلاح =====

        return value.lower()

    def compare(self, node1, node2, key):

        self.comparisons += 1

        left = self.get_value(node1, key)
        right = self.get_value(node2, key)

        if left > right:
            return 1
        elif left < right:
            return -1
        else:
            return 0

    def swap(self, node1, node2):

        node1.song, node2.song = node2.song, node1.song
        self.movements += 1

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