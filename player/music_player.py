def get_progress(self):
    if self.state != "Playing" or self.playlist.current_song() is None:
        return None
    song = self.playlist.current_song()
    total = song.duration
    current = pygame.mixer.music.get_pos() // 1000  # milliseconds to seconds
    if current < 0:
        current = 0
    if current > total and total > 0:
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
    percent = int((current / total) * 20)
    bar = "[" + "=" * percent + ">" + " " * (20 - percent) + "]"
    print(f"\r{bar} {self._format_time(current)} / {self._format_time(total)}", end="")

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
    pygame.mixer.music.stop()
    pygame.mixer.music.play(start=seconds)
    self.state = "Playing"
    print(f"Seeked to {self._format_time(seconds)}")