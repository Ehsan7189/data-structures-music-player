from algorithms.sorter import Sorter


class BubbleSort(Sorter):

    def __init__(self):

        super().__init__("Bubble Sort")
    def sort(self, playlist, key):
        if playlist.head is None or playlist.head.next is None: 
            return
        swapped = True
        while swapped:
            swapped = False
            current = playlist.head
            while current.next:
                left = getattr(current.song, key)
                right = getattr(current.next.song, key)
                if left > right:
                    current.song, current.next.song = current.next.song, current.song
                    swapped = True

                current = current.next