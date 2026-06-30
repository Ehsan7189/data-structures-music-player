from models.song import Song
from structures.playlist import Playlist

playlist = Playlist()

playlist.add_last(Song("music/Eminem - Mockingbird.mp3"))
playlist.add_last(Song("music/Adele - Hello.mp3"))
playlist.add_first(Song("music/Linkin Park - Numb.mp3"))

playlist.display()