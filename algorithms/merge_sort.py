from algorithms.sorter import Sorter


class MergeSort(Sorter):

    def __init__(self):
        super().__init__("Merge Sort")

    def sort(self, playlist, key):

        if playlist.head is None or playlist.head.next is None:
            return

        playlist.head = self.merge_sort(playlist.head, key)

    def get_middle(self, head):

        slow = head
        fast = head

        while fast.next and fast.next.next:

            slow = slow.next
            fast = fast.next.next

        return slow