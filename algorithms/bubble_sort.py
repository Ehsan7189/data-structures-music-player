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

                left = getattr(current.song, key)
                right = getattr(current.next.song, key)

                compare_result = self.compare(current, current.next, key)

                if compare_result > 0:

                    self.swap(current, current.next)

                    self.show_step(
                        playlist,
                        key,
                        left,
                        right,
                        "Swap"
                    )

                    swapped = True

                else:

                    self.show_step(
                        playlist,
                        key,
                        left,
                        right,
                        "No Swap"
                    )

                current = current.next

            last_sorted = current