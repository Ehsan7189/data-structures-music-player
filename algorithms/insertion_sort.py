from algorithms.sorter import Sorter


class InsertionSort(Sorter):

    def __init__(self):
        super().__init__("Insertion Sort")

    def sort(self, playlist, key):

        if playlist.head is None or playlist.head.next is None:
            return

        current = playlist.head.next

        while current:

            temp = current.song
            next_node = current.next
            position = current.prev

            while position and self.compare(position, temp, key) > 0:

                position.next.song = position.song
                position = position.prev

            if position is None:
                playlist.head.song = temp
            else:
                position.next.song = temp

            current = next_node