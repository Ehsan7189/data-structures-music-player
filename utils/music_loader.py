import os
from models.song import Song

class MusicLoader:

    SUPPORTED_FORMATS = (".mp3", ".wav", ".flac", ".aac", ".ogg")

    @staticmethod
    def load_folder(path, playlist):

        if not os.path.isdir(path):
            print("\n❌ Folder not found.")
            return 0

        count = 0

        for file_name in os.listdir(path):

            full_path = os.path.join(path, file_name)

            if not os.path.isfile(full_path):
                continue

            _, extension = os.path.splitext(file_name)

            if extension.lower() not in MusicLoader.SUPPORTED_FORMATS:
                continue

            song = Song(full_path)
            playlist.append(song)
            count += 1

        return count