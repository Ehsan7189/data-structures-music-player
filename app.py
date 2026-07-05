from models.song import Song
from structures.playlist import Playlist
from algorithms.insertion_sort import InsertionSort


# ساخت پلی لیست
playlist = Playlist()

# اضافه کردن آهنگ ها (عمداً نامرتب)
playlist.add_last(Song("music/Metallica - One.mp3"))
playlist.add_last(Song("music/Adele - Hello.mp3"))
playlist.add_last(Song("music/Coldplay - Yellow.mp3"))
playlist.add_last(Song("music/Beatles - Hey Jude.mp3"))
playlist.add_last(Song("music/Queen - Bohemian Rhapsody.mp3"))
playlist.add_last(Song("music/Eminem - Mockingbird.mp3"))
playlist.add_last(Song("music/ABBA - Dancing Queen.mp3"))
playlist.add_last(Song("music/Linkin Park - Numb.mp3"))

print("========== Before Sort ==========")
playlist.display()

# ساخت الگوریتم Bubble Sort
insertion = InsertionSort()

insertion.trace = True

# مرتب سازی بر اساس نام آهنگ
result = insertion.measure(playlist, "artist")

print("\n========== After Sort ==========")
playlist.display()

print("\n========== Performance ==========")
print(f"Algorithm : {result['algorithm']}")
print(f"Sorted By : {result['sorted_by']}")
print(f"Time      : {result['time']:.8f} sec")
print(f"Memory    : {result['memory']} Bytes")