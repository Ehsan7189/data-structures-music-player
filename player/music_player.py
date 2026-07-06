class Player:

    def __init__(self, playlist):

        self.playlist = playlist
        self.state = "Stopped"

    def play(self):

        if self.playlist.head is None:

            print("Playlist is empty.")
            return

        if self.state == "Playing":
            return
        
        song = self.playlist.current_song()

        if self.state == "Paused":

            self.state = "Playing"

            print("\n▶ Resumed")
            print(song)

            return
        

        self.state = "Playing"

        song = self.playlist.current_song()

        print("\n▶ Now Playing")
        print(song)

    def pause(self):

        if self.state != "Playing":
            return

        self.state = "Paused"

        print("⏸ Paused")