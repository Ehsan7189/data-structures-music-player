import os
from mutagen import File

class Song:

    def __init__(self, file_path):

        self.path = file_path
        self.filename = os.path.basename(file_path)
        self.extension = os.path.splitext(self.filename)[1].lower()

        file_name = os.path.splitext(self.filename)[0]
        parts = file_name.split(" - ")

        if len(parts) == 2:
            self.artist = parts[0].strip()
            self.title = parts[1].strip()
        else:
            self.artist = "Unknown"
            self.title = file_name.strip()

        self.duration = self._get_duration()

    def _get_duration(self):
        try:
            audio = File(self.path)
            if audio is not None and hasattr(audio.info, 'length'):
                return int(audio.info.length)
        except Exception:
            pass
        return 0

    def __str__(self):
        return (
            f"Artist : {self.artist}\n"
            f"Title  : {self.title}\n"
            f"Format : {self.extension}"
        )