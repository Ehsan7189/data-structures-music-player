from algorithms.bubble_sort import BubbleSort
from algorithms.insertion_sort import InsertionSort
from algorithms.merge_sort import MergeSort
from structures.playlist import Playlist
from player.music_player import Player
from utils.music_loader import MusicLoader

playlist = Playlist()
player = Player(playlist)

last_result = None



while True:

    path = input("Enter music folder: ")

    playlist.clear()

    count = MusicLoader.load_folder(path, playlist)

    if count > 0:

        print(f"\n✅ {count} song(s) loaded.")
        break

    print("\n❌ Folder not found or no supported music files.")



sorters = {
    "1": BubbleSort,
    "2": InsertionSort,
    "3": MergeSort
}

fields = {
    "1": "artist",
    "2": "title",
    "3": "format"
}