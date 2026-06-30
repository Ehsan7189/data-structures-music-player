from models.song import Song


class Node:

    def __init__(self, song: Song):

        self.prev = None
        self.song = song
        self.next = None