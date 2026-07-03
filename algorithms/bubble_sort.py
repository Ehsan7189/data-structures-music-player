from algorithms.sorter import Sorter


class BubbleSort(Sorter):

    def __init__(self):

        super().__init__("Bubble Sort")

        print(self.__dict__)
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

                    left = getattr(current.song, key)
                    right = getattr(current.next.song, key)

                    self.swap(current, current.next)

                    self.show_step(
                        playlist,
                        f"Compare : {left} ↔ {right}\nResult  : Swap"
                    )

                    swapped = True

                current = current.next

            last_sorted = current