import json
from notes_model import Note

class NoteDataStorage:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_notes(self):
        try:
            with open(self.file_path, 'r') as file:
                notes_data = json.load(file)
                return [Note(note_data['body']) for note_data in notes_data]
        except FileNotFoundError:
            print(f"Error: There is no data by path: {self.file_path}")
            return []

    def save_notes(self, notes_data):
        with open(self.file_path, 'w') as file:
            json.dump(notes_data, file)