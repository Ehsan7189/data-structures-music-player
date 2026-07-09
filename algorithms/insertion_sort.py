from algorithms.sorter import Sorter

class InsertionSort(Sorter):

    def __init__(self):
        super().__init__("Insertion Sort")

    def sort(self, playlist, key):

        if playlist.head is None:
            return

        current = playlist.head.next

        while current:

            key_node = current
            prev = current.prev

            while prev and self.compare(prev, key_node, key) > 0:
                self.swap(prev, key_node)
                key_node = prev
                prev = prev.prev

            current = current.next