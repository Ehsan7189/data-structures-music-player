from models.node import Node
from models.song import Song

class Playlist:
    def __init__(self):

        self.head = None # * first
        self.tail = None # * current 
        self.current = None #  * last 
