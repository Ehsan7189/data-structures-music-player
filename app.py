from structures.playlist import Playlist
from models.song import Song

playlist = Playlist()

playlist.add_last(Song("music/Eminem - Mockingbird.mp3"))
playlist.add_last(Song("music/Adele - Hello.mp3"))
playlist.add_last(Song("music/Linkin Park - Numb.mp3"))

print("=== قبل از حذف ===")
playlist.display()

playlist.delete("Hello")

print("\n=== بعد از حذف ===")
playlist.display()