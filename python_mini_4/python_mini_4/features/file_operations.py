import os

class FileOperations:
    def create_file(self, filename="new_file.txt"):
        try:
            with open(filename, "w") as f:
                f.write("Created by Voice Assistant")
            return True
        except Exception:
            return False