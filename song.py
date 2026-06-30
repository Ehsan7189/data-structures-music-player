import os


class Song:

    def __init__(self, file_path):

        
        self.path = file_path

        
        self.filename = os.path.basename(file_path)

    
        self.extension = os.path.splitext(self.filename)[1]

       
        file_name = os.path.splitext(self.filename)[0]

      
        parts = file_name.split(" - ")

        if len(parts) == 2:
            self.artist = parts[0]
            self.title = parts[1]
        else:
            self.artist = "Unknown"
            self.title = file_name
