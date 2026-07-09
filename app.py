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


def show_menu():

    print("\n" + "=" * 35)
    print("        MUSIC PLAYER")
    print("=" * 35)
    print("1. Display Playlist")
    print("2. Play")
    print("3. Pause")
    print("4. Stop")
    print("5. Next")
    print("6. Previous")
    print("7. Toggle Shuffle")
    print("8. Sort Playlist")
    print("9. Show Performance")
    print("0. Exit")


def show_performance():

    global last_result

    if last_result is None:

        print("\n❌ No performance data available.")
        return

    print("\n===== Performance =====")
    print(f"Algorithm   : {last_result['algorithm']}")
    print(f"Sorted By   : {last_result['sorted_by']}")
    print(f"Time        : {last_result['time']:.8f} sec")
    print(f"Memory      : {last_result['memory']} Bytes")
    print(f"Comparisons : {last_result['comparisons']}")
    print(f"Movements   : {last_result['movements']}")


def sort_playlist():

    global last_result

    print("\n===== Sort Playlist =====")
    print("1. Bubble Sort")
    print("2. Insertion Sort")
    print("3. Merge Sort")

    algorithm = input("Choose Algorithm: ")

    if algorithm not in sorters:

        print("\n❌ Invalid choice.")
        return

    print("\n===== Sort By =====")
    print("1. Artist")
    print("2. Title")
    print("3. Format")

    field = input("Choose Field: ")

    if field not in fields:

        print("\n❌ Invalid choice.")
        return

    sorter = sorters[algorithm]()
    key = fields[field]

    last_result = sorter.measure(playlist, key)

    print("\n✅ Playlist Sorted Successfully!\n")

    playlist.display()

    show_performance()


while True:

    show_menu()

    choice = input("\nChoose: ")

    if choice == "0":

        print("\n👋 Goodbye!")
        break

    elif choice == "1":

        playlist.display()

    elif choice == "2":

        player.play()

    elif choice == "3":

        player.pause()

    elif choice == "4":

        player.stop()

    elif choice == "5":

        player.next()

    elif choice == "6":

        player.previous()

    elif choice == "7":

        player.shuffle()

    elif choice == "8":

        sort_playlist()

    elif choice == "9":

        show_performance()

    else:

        print("\n❌ Invalid choice.")