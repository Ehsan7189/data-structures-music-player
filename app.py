from algorithms.bubble_sort import BubbleSort
from algorithms.insertion_sort import InsertionSort
from algorithms.merge_sort import MergeSort
from structures.playlist import Playlist
from player.music_player import Player
from utils.music_loader import MusicLoader
import os
import pygame

playlist = Playlist()
player = Player(playlist)

last_result = None

while True:

    path = input("Enter music folder: ")

    playlist.clear()

    count = MusicLoader.load_folder(path, playlist)

    if count > 0:

        print(f"\n✅ {count} song(s) loaded.")

        if player.shuffle_mode:
            player.shuffle_mode = False
            player.shuffle_order = []
            player.shuffle_index = 0
            print("🔀 Shuffle disabled due to playlist reload.")

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
    print("10. Rename Files")
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

    playlist.current = playlist.head

    playlist.display()

    show_performance()

    if player.shuffle_mode:
        player._build_shuffle_order()
        try:
            player.shuffle_index = player.shuffle_order.index(playlist.head)
        except ValueError:
            player.shuffle_index = 0
        print("🔀 Shuffle order re-synchronized after sorting.")


def rename_files():

    if playlist.head is None:
        print("\n❌ Playlist is empty.")
        return

    if player.state != "Stopped":
        pygame.mixer.music.stop()
        player.state = "Stopped"
        print("\n⏹ Player stopped before renaming.")

    print("\n===== Rename Files =====")
    print("This will rename all files in the playlist to:")
    print("  Artist - Title.extension")
    print("Files with 'Unknown' artist will be renamed to Title.extension")
    confirm = input("Proceed? (y/n): ").lower()

    if confirm != "y":
        print("❌ Rename cancelled.")
        return

    renamed = 0
    skipped = 0
    errors = 0

    current = playlist.head
    while current:
        song = current.song

        if song.artist.lower() == "unknown":
            new_name = f"{song.title}{song.extension}"
        else:
            new_name = f"{song.artist} - {song.title}{song.extension}"

        current_filename = os.path.basename(song.path)

        if current_filename == new_name:
            current = current.next
            skipped += 1
            continue

        new_path = os.path.join(os.path.dirname(song.path), new_name)

        if os.path.exists(new_path):
            base_name = os.path.splitext(new_name)[0]
            ext = os.path.splitext(new_name)[1]
            counter = 1
            while True:
                test_name = f"{base_name}_{counter}{ext}"
                test_path = os.path.join(os.path.dirname(song.path), test_name)
                if not os.path.exists(test_path):
                    new_path = test_path
                    break
                counter += 1

        try:
            os.rename(song.path, new_path)
            song.path = new_path
            song.filename = os.path.basename(new_path)
            renamed += 1
            print(f"✅ Renamed: {current_filename} → {os.path.basename(new_path)}")
        except Exception as e:
            print(f"❌ Error renaming {current_filename}: {e}")
            errors += 1

        current = current.next

    print("\n===== Rename Summary =====")
    print(f"Renamed: {renamed}")
    print(f"Skipped (already correct): {skipped}")
    print(f"Errors: {errors}")

    if renamed > 0:
        print("✅ Playlist paths updated.")


while True:

    show_menu()

    choice = input("\nChoose: ")

    if choice == "0":

        pygame.mixer.quit()
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

    elif choice == "10":

        rename_files()

    else:

        print("\n❌ Invalid choice.")