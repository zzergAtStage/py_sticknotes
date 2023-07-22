from notes_model import Note
from model_presenter import NoteService
from file_operations import NoteDataStorage
from model_view import ConsoleUI

def main():
    file_path = "notes.json"  # Specify the file path where notes will be stored
    file_storage = NoteDataStorage(file_path)
    note_service = NoteService(file_storage)
    console_ui = ConsoleUI(note_service)

    console_ui.run()

if __name__ == "__main__":
    main()