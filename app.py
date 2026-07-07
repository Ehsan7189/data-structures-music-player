from algorithms.bubble_sort import BubbleSort
from algorithms.insertion_sort import InsertionSort
from algorithms.merge_sort import MergeSort
from structures.playlist import Playlist
from player.music_player import Player

play_list = Playlist()
player = Player(play_list)

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

def sort_palylist():
    
    print("\n===== Sort Playlist =====")
    print("1. Bubble Sort")
    print("2. Insertion Sort")
    print("3. Merge Sort")

    algorithm = input("Choose Algorithm: ")



    if algorithm not in sorters:

        print("\n❌ Invalid choice.")

        continue

    sorter = sorters[algorithm]()
    print("\nSort By")
    print("1. Artist")
    print("2. Title")
    print("3. Format")



    field = input("Choose Field: ")

    if field not in fields:

        print("\n❌ Invalid choice.")

        continue
    
    key = fields[field]

    result = sorter.measure(playlist, key)

    print("\nSorted Successfully!")

    playlist.display()

    print("\n===== Performance =====")
    print(f"Algorithm   : {result['algorithm']}")
    print(f"Time        : {result['time']:.8f} sec")
    print(f"Memory      : {result['memory']} Bytes")
    print(f"Comparisons : {result['comparisons']}")
    print(f"Movements   : {result['movements']}")

while True:

    show_menu()

    choice = input("Choose : ")

    if choice == "0":

        print("Goodbye!")

        break

    elif choice == "1":

        Playlist.display()
    
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

        sort_palylist()

   