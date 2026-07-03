from models.song import Song
from structures.playlist import Playlist
from algorithms.bubble_sort import BubbleSort


# ساخت پلی لیست
playlist = Playlist()

# اضافه کردن آهنگ ها (عمداً نامرتب)
playlist.add_last(Song("music/Linkin Park - Numb.mp3"))
playlist.add_last(Song("music/Adele - Hello.mp3"))
playlist.add_last(Song("music/Eminem - Mockingbird.mp3"))
playlist.add_last(Song("music/Coldplay - Yellow.mp3"))

print("========== Before Sort ==========")
playlist.display()

# ساخت الگوریتم Bubble Sort
bubble = BubbleSort()

bubble.trace = True

# مرتب سازی بر اساس نام آهنگ
result = bubble.measure(playlist, "artist")

print("\n========== After Sort ==========")
playlist.display()

print("\n========== Performance ==========")
print(f"Algorithm : {result['algorithm']}")
print(f"Sorted By : {result['sorted_by']}")
print(f"Time      : {result['time']:.8f} sec")
print(f"Memory    : {result['memory']} Bytes")