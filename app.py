from structures import playlist
from player import music_player
import player


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

while True:

    show_menu()

    choice = input("Choose : ")

    if choice == "0":

        print("Goodbye!")

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

        print("\n===== Sort Playlist =====")
        print("1. Bubble Sort")
        print("2. Insertion Sort")
        print("3. Merge Sort")

        algorithm = input("Choose Algorithm: ")

        print("\nSort By")
        print("1. Artist")
        print("2. Title")
        print("3. Format")

        field = input("Choose Field: ")