from algorithms.sorter import Sorter

class BubbleSort(Sorter):

    def __init__(self):
        super().__init__("Bubble Sort")

    def sort(self, playlist, key):

        if playlist.head is None:
            return

        end = None

        while end != playlist.head:
            current = playlist.head

            while current.next != end:

                if self.compare(current, current.next, key) > 0:
                    self.swap(current, current.next)

                current = current.next

            end = current