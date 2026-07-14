import random

class Player:

    def __init__(self, playlist):
        self.playlist = playlist
        self.state = "Stopped"
        self.shuffle_mode = False
        self.shuffle_order = []
        self.shuffle_index = 0

    def _play_current_song(self, message):
        song = self.playlist.current_song()

        if not song:
            print("Playlist is empty.")
            return

        self.state = "Playing"
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

    def pause(self):

        if self.state == "Playing":
            self.state = "Paused"
            print("⏸ Paused")

    def stop(self):

        if self.playlist.head is None:
            return

        self.state = "Stopped"
        self.playlist.current = self.playlist.head

        if self.shuffle_mode and self.shuffle_order:
     
            try:
                self.shuffle_index = self.shuffle_order.index(self.playlist.head)
            except ValueError:
              
                self._build_shuffle_order()
                self.shuffle_index = 0
       

        print("\n⏹ Stopped")

    def next(self):

        if self.state == "Stopped":
            return

        if self.shuffle_mode:
            if not self.shuffle_order:
                return
            self.shuffle_index = (self.shuffle_index + 1) % len(self.shuffle_order)
            self.playlist.current = self.shuffle_order[self.shuffle_index]
        else:
            self.playlist.next_song()

        self._play_current_song("⏭ Next Song")

    def previous(self):

        if self.state == "Stopped":
            return

        if self.shuffle_mode:
            if not self.shuffle_order:
                return
            self.shuffle_index = (self.shuffle_index - 1) % len(self.shuffle_order)
            self.playlist.current = self.shuffle_order[self.shuffle_index]
        else:
            self.playlist.previous_song()

        self._play_current_song("⏮ Previous Song")

    def shuffle(self):

       
        if self.playlist.head is None:
            print("Playlist is empty. Cannot enable shuffle.")
            return
        

        self.shuffle_mode = not self.shuffle_mode

        if self.shuffle_mode:
            self._build_shuffle_order()
            self.playlist.current = self.shuffle_order[0]
            self._play_current_song("🔀 Shuffle On")
        else:
            print("➡ Shuffle Off")

    def _build_shuffle_order(self):

        self.shuffle_order = []

        current = self.playlist.head

        while current:
            self.shuffle_order.append(current)
            current = current.next

        random.shuffle(self.shuffle_order)
        self.shuffle_index = 0