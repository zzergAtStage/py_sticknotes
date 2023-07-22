import json
from notes_model import Note
from file_operations import NoteDataStorage

class NoteService:
    def __init__(self, file_storage):
        self.file_storage = file_storage
        self.notes = self.file_storage.load_notes()

    def _save_notes(self):
        """Save note data to the object, that will be saved with external methods"""
        notes_data = [{'body': note.body, 'creation_date': note.creation_date.isoformat(),
                       'modification_date': note.modification_date.isoformat()} for note in self.notes]
        self.file_storage.save_notes(notes_data)
    
    def add_new_note(self, body):
        note = Note(body)
        self.notes.append(note)
        self._save_notes()

    def find_notes(self, search_text=None, search_date=None):
        found_notes = []
        for note in self.notes:
            if search_text and search_text.lower() in note.body.lower():
                found_notes.append(note)
            if search_date:
                print(f"Debug: .find_notes note_date: {note.creation_date.date()}")
                # Compare the search_date with creation_date and modification_date (ignoring time)
                if (note.creation_date.date() == search_date.date() or
                    note.modification_date.date() == search_date.date()):
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

    def show_selected_notes(self, found_notes):
        for idx, note in enumerate(found_notes):
            print(f"{idx+1}. Created: {note.creation_date}, Modified: {note.modification_date}, Body: {note.body}")

