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