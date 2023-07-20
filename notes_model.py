import json
import datetime

class Note:
    def __init__(self, body):
        self.creation_date = datetime.datetime.now()
        self.modification_date = self.creation_date
        self.body = body[:2000]

    def update_body(self, new_body):
        self.body = new_body[:2000]
        self.modification_date = datetime.datetime.now()

class NotesManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.notes = self._load_notes()

    def _load_notes(self):
        try:
            with open(self.file_path, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def _save_notes(self):
        with open(self.file_path, "w") as file:
            json.dump(self.notes, file, cls=CustomJSONEncoder)

    def add_note(self, body):
        new_note = Note(body)
        self.notes.append(new_note)
        self._save_notes()

    def update_note_body(self, note_idx, new_body):
        if 0 <= note_idx < len(self.notes):
            self.notes[note_idx].update_body(new_body)
            self._save_notes()

    def delete_note(self, note_idx):
        if 0 <= note_idx < len(self.notes):
            del self.notes[note_idx]
            self._save_notes()

    def get_note_list(self):
        return [
            f"Creation Date: {note.creation_date}, "
            f"Modification Date: {note.modification_date}, "
            f"Body: {note.body[:100]}"
            for note in self.notes
        ]
class CustomJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime.datetime):
            return o.isoformat()  # Convert datetime to ISO 8601 format string
        return super().default(o)