from models.node import Node
from models.song import Song

class Playlist:
    def __init__(self):

        self.head = None # * first
        self.tail = None # * current 
        self.current = None #  * last 
    def add_first(self, song: Song):
        new_node = Node(song)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.current = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    def add_last(self, song: Song):
        new_node = Node(song)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.current = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def display(self):

        if self.head is None:
            print("Playlist is empty.")
            return

        current = self.head

        while current is not None:

            print(current.song)
            print("-" * 30)

            current = current.next