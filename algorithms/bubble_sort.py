from algorithms.sorter import Sorter


class BubbleSort(Sorter):

    def __init__(self):

        super().__init__("Bubble Sort")
    def sort(self, playlist, key):
        if playlist.head is None or playlist.head.next is None: 
            return
        swapped = True
        last_sorted = None
        while swapped:
            swapped = False
            current = playlist.head

            while current.next != last_sorted:

                if self.compare(current, current.next, key) > 0:

                    current.song, current.next.song = (
                        current.next.song,
                        current.song,
                    )

                    swapped = True

                current = current.next

            last_sorted = current