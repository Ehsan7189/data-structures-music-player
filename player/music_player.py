class Player:

    def __init__(self, playlist):

        self.playlist = playlist
        self.state = "Stopped"
        self.shuffle_mode = False
        self.shuffle_order = []

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

    def stop(self):

        if self.playlist.head is None:
            return

        if self.state == "Stopped":
            return

        self.state = "Stopped"

        self.playlist.current = self.playlist.head

        print("\n⏹ Stopped")

    def next(self):

        if self.playlist.head is None:
            return

        if self.state == "Stopped":
            return


        self.playlist.next_song()

        self._play_current_song("⏭ Next Song")

    def previous(self):

        if self.playlist.head is None:
            return

        if self.state == "Stopped":
            return

        song = self.playlist.previous_song()

        self._play_current_song("⏮ Previous Song")

    def _play_current_song(self, message):

        self.state = "Playing"

        song = self.playlist.current_song()

        print(f"\n{message}")
        print(song)

    def play(self):

        if self.playlist.head is None:
            print("Playlist is empty.")
            return

        if self.state == "Playing":
            return

        if self.state == "Paused":

            self._play_current_song("▶ Resumed")
            return

        self._play_current_song("▶ Now Playing")

    def shuffle(self):

        self.shuffle_mode = not self.shuffle_mode

        if self.shuffle_mode:

            self.build_shuffle_order()

            print("🔀 Shuffle On")

        else:

            print("➡ Shuffle Off")



