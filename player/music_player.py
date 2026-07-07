import random

class Player:

    def __init__(self, playlist):

        self.playlist = playlist
        self.state = "Stopped"
        self.shuffle_mode = False
        self.shuffle_order = None
        self.shuffle_index = 0

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

        if self.shuffle_mode:

            self.shuffle_index = (self.shuffle_index + 1) % len(self.shuffle_order)

            self.playlist.current = self.shuffle_order[self.shuffle_index]
        else:

            self.playlist.next_song()

        self._play_current_song("⏭ Next Song")

    def previous(self):

        if self.playlist.head is None:
            return

        if self.state == "Stopped":
            return
        
        if self.shuffle_mode:

            self.shuffle_index = (self.shuffle_index - 1) % len(self.shuffle_order)

            self.playlist.current = self.shuffle_order[self.shuffle_index]

        else:

            self.playlist.previous_song()

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

            self.playlist.current = self.shuffle_order[0]

            self._play_current_song("🔀 Shuffle On")

        else:

            self.shuffle_order = None
            self.shuffle_index = 0
            
            print("➡ Shuffle Off")

    def build_shuffle_order(self):

        self.shuffle_order = []

        current = self.playlist.head

        while current is not None:

            self.shuffle_order.append(current)

            current = current.next

        random.shuffle(self.shuffle_order)

        self.shuffle_index = 0

