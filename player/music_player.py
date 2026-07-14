import random
import pygame

class Player:

    def __init__(self, playlist):
        self.playlist = playlist
        self.state = "Stopped"
        self.shuffle_mode = False
        self.shuffle_order = []
        self.shuffle_index = 0
        pygame.mixer.init()

    def _play_current_song(self, message):
        song = self.playlist.current_song()
        if not song:
            print("Playlist is empty.")
            return
        self.state = "Playing"
        print(f"\n{message}")
        print(song)
        try:
            pygame.mixer.music.load(song.path)
            pygame.mixer.music.play()
        except Exception as e:
            print(f"❌ Error playing file: {e}")
            self.state = "Stopped"

    def play(self):
        if self.playlist.head is None:
            print("Playlist is empty.")
            return
        if self.state == "Playing" and not pygame.mixer.music.get_busy():
            self.next()
            return
        if self.state == "Playing":
            return
        if self.state == "Paused":
            pygame.mixer.music.unpause()
            self.state = "Playing"
            print("▶ Resumed")
            return
        self._play_current_song("▶ Now Playing")

    def pause(self):
        if self.state == "Playing":
            pygame.mixer.music.pause()
            self.state = "Paused"
            print("⏸ Paused")

    def stop(self):
        if self.playlist.head is None:
            return
        pygame.mixer.music.stop()
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
        pygame.mixer.music.stop()
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
        pygame.mixer.music.stop()
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
            if self.state == "Playing" or self.state == "Paused":
                self._play_current_song("🔀 Shuffle On")
            else:
                print("🔀 Shuffle On")
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

    def get_progress(self):
        if self.state != "Playing" or self.playlist.current_song() is None:
            return None
        song = self.playlist.current_song()
        total = song.duration
        current = pygame.mixer.music.get_pos() // 1000
        if current < 0:
            current = 0
        if total > 0 and current > total:
            current = total
        return current, total

    def show_progress(self):
        progress = self.get_progress()
        if progress is None:
            print("Not playing.")
            return
        current, total = progress
        if total == 0:
            print("Duration unknown.")
            return
        bar_length = 20
        filled = int((current / total) * bar_length)
        if filled >= bar_length:
            filled = bar_length - 1
        bar = "[" + "=" * filled + ">" + " " * (bar_length - filled - 1) + "]"
        print(f"\r{bar} {self._format_time(current)} / {self._format_time(total)}")

    def _format_time(self, seconds):
        m = seconds // 60
        s = seconds % 60
        return f"{m:02d}:{s:02d}"

    def seek(self, seconds):
        if self.state != "Playing":
            print("Not playing.")
            return
        song = self.playlist.current_song()
        if song.duration == 0:
            print("Cannot seek: duration unknown.")
            return
        if seconds < 0:
            seconds = 0
        elif seconds > song.duration:
            seconds = song.duration
        try:
            pygame.mixer.music.set_pos(seconds)
            self.state = "Playing"
            print(f"Seeked to {self._format_time(seconds)}")
        except Exception as e:
            print(f"set_pos failed: {e}, trying reload...")
            try:
                pygame.mixer.music.stop()
                pygame.mixer.music.load(song.path)
                pygame.mixer.music.play(start=seconds * 1000)
                self.state = "Playing"
                print(f"Seeked to {self._format_time(seconds)}")
            except Exception as e2:
                print(f"❌ Error seeking: {e2}")
                self.state = "Stopped"