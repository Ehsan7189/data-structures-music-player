from models.node import Node
from models.song import Song

class Playlist:
    
    def __init__(self):

        self.head = None # * first
        self.tail = None # * current 
        self.current = None #  * last 
        self.size = 0

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
        self.size += 1
    
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
        self.size += 1

    def display(self):

        if self.head is None:
            print("Playlist is empty.")
            return

        current = self.head

        while current is not None:

            print(current.song)
            print("-" * 30)

            current = current.next

    def search(self, title):
        current = self.head
        while current is not None:
            if current.song.title == title:
                return current
            current = current.next
        return None
    
    def delete(self, title):

        node = self.search(title)

        if node is None:
            return False

        if self.head == self.tail:

            self.head = None
            self.tail = None
            self.current = None

        elif node == self.head:

            self.head = node.next
            self.head.prev = None

        elif node == self.tail:

            self.tail = node.prev
            self.tail.next = None

        else:

            node.prev.next = node.next
            node.next.prev = node.prev

        if self.current == node:
            self.current = self.head

        return True
    
    def current_song(self):
        if self.current is None:
            print("Playlist is empty.")
            return
        return self.current.song
    
    def next_song(self):
        if self.current is None:
            return None 
        
        if self.current.next is not None:
            self.current = self.current.next

        else:

            self.current = self.head
        return self.current.song
    
    def previous_song(self):

        if self.current is None:
            return None 
        
        if self.current.prev is not None:
            self.current = self.current.prev

        else:

            self.current = self.tail
        return self.current.song
    
    def update_tail(self):

        if self.head is None:
            self.tail = None
            return

        current = self.head

        while current.next:
            current = current.next

        self.tail = current