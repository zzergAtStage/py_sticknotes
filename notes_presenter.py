from notes_model import NotesManager
from notes_view import NotesView

class NotesPresenter:
    def __init__(self, file_path):
        self.notes_manager = NotesManager(file_path)
        self.view = NotesView()

    def run(self):
        while True:
            self.view.display_menu()
            choice = self.view.get_user_input("Enter your choice: ")

            if choice == "1":
                self.add_note()
            elif choice == "2":
                self.show_all_notes()
            elif choice == "3":
                self.modify_note()
            elif choice == "4":
                self.delete_note()
            elif choice == "0":
                break
            else:
                self.view.display_message("Invalid choice. Try again.")

    def add_note(self):
        note_body = self.view.get_user_input("Enter the note's body: ")
        self.notes_manager.add_note(note_body)
        self.view.display_message("Note added successfully.")

    def show_all_notes(self):
        note_list = self.notes_manager.get_note_list()
        self.view.display_notes(note_list)

    def modify_note(self):
        note_list = self.notes_manager.get_note_list()
        self.view.display_notes(note_list)
        note_idx = self.view.get_user_input("Enter the index of the note to modify: ")
        new_body = self.view.get_user_input("Enter the new body for the note: ")
        self.notes_manager.update_note_body(int(note_idx), new_body)
        self.view.display_message("Note modified successfully.")

    def delete_note(self):
        note_list = self.notes_manager.get_note_list()
        self.view.display_notes(note_list)
        note_idx = self.view.get_user_input("Enter the index of the note to delete: ")
        self.notes_manager.delete_note(int(note_idx))
        self.view.display_message("Note deleted successfully.")
