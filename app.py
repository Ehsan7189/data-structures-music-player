from structures.playlist import Playlist
from models.song import Song

# playlist = Playlist()

playlist = Playlist()

playlist.add_last(Song("music/Eminem - Mockingbird.mp3"))
playlist.add_last(Song("music/Adele - Hello.mp3"))

playlist.current_song()