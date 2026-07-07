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

            title, extension = os.path.splitext(file_name)

            if extension.lower() not in MusicLoader.SUPPORTED_FORMATS:
                continue

            if " - " in title:

                artist, song_title = title.split(" - ", 1)

            else:

                artist = "Unknown Artist"
                song_title = title

            song = Song(
                artist=artist.strip(),
                title=song_title.strip(),
                format=extension.lower()
            )

            playlist.append(song)

            count += 1

        return count