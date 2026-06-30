from models.song import Song
from models.node import Node

song = Song("music/Eminem - Mockingbird.mp3")
node = Node(song)

print(node.song)