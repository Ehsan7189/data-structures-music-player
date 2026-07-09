from models.node import Node

class Playlist:

    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None
        self.size = 0

    def append(self, song):
        self.add_last(song)

    def add_first(self, song):
        new_node = Node(song)

        if self.head is None:
            self.head = self.tail = self.current = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.size += 1

    def add_last(self, song):
        new_node = Node(song)

        if self.head is None:
            self.head = self.tail = self.current = new_node
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
        while current:
            print(current.song)
            print("-" * 30)
            current = current.next

    def search(self, title):
        current = self.head
        while current:
            if current.song.title.lower() == title.lower():
                return current
            current = current.next
        return None

    def delete(self, title):
        node = self.search(title)

        if node is None:
            return False

        if node == self.head and node == self.tail:
            self.head = self.tail = self.current = None

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

        self.size -= 1
        return True

    def current_song(self):
        if self.current:
            return self.current.song
        return None

    def next_song(self):
        if not self.current:
            return None

        self.current = self.current.next if self.current.next else self.head
        return self.current.song

    def previous_song(self):
        if not self.current:
            return None

        self.current = self.current.prev if self.current.prev else self.tail
        return self.current.song

    def update_tail(self):
        if not self.head:
            self.tail = None
            return

        current = self.head
        while current.next:
            current = current.next
        self.tail = current

    def clear(self):
        self.head = self.tail = self.current = None
        self.size = 0