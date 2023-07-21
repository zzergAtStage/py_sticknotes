import json
from notes_model import Note

class NoteService:
    def __init__(self, file_path):
        self.file_path = file_path
        self.notes = self._load_notes()


    def _load_notes(self):
        try:
            with open(self.file_path,'r') as file:
                notes_data = json.load(file)
                return [Note(note_data['body']) for note_data in notes_data]
        except FileNotFoundError:
            print(f"There is no file data found on {self.file_path}")
            return []
    
    def _save_notes(self):
        notes_data = [{'body' : note.body, 'creation_date': note.creation_date.isoformat(),
                      'modification_date': note.modification_date.isoformat()} for note in self.notes]
        with open(self.file_path, 'w') as file:
            json.dump(notes_data, file)
    
    def add_new_note(self, body):
        note = Note(body)
        self.notes.append(note)
        self._save_notes()

    def find_notes(self, keyword):
        found_notes = []
        for note in self.notes:
            if keyword.lower() in note.body.lower():
                found_notes.append(note)
        return found_notes

    def modify_note(self, note_index, new_body):
        if 0 <= note_index <= len(self.notes):
            self.notes[note_index].modify(new_body)
            self._save_notes()
    
    def delete_note(self, note_index):
        if 0<= note_index <= len(self.notes):
            del self.notes[note_index]
            self._save_notes()
    
    def show_all_notes(self):
        for idx, note in enumerate(self.notes):
            print(f"{idx+1}. Created: {note.creation_date}, Modified: {note.modification_date}, Body: {note.body}")

