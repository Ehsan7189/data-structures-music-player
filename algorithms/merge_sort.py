from algorithms.sorter import Sorter
from models.node import Node


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
    
    def merge(self, left, right, key):

        dummy = Node(None)
        tail = dummy
        
        while left and right:
            
            if self.compare(left, right, key) <= 0:
                
                tail.next = left
                left.prev = tail

                tail = left
                left = left.next

            else:
                tail.next = right
                right.prev = tail

                tail = right
                right = right.next
                
    def merge_sort(self, head, key):

        if head is None or head.next is None:
            return head

        middle = self.get_middle(head)

        right = middle.next
        middle.next = None

        if right:
            right.prev = None

        left = head

        left = self.merge_sort(left, key)
        right = self.merge_sort(right, key)

        return self.merge(left, right, key)