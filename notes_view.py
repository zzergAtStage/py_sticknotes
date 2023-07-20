class NotesView:
    @staticmethod
    def display_menu():
        print("\n--- Menu ---")
        print("1. Add new note")
        print("2. Show all notes")
        print("3. Modify a note")
        print("4. Delete a note")
        print("0. Exit")

    @staticmethod
    def get_user_input(prompt):
        return input(prompt)

    @staticmethod
    def display_message(message):
        print(message)

    @staticmethod
    def display_notes(note_list):
        if note_list:
            print("\n--- Notes ---")
            for note in note_list:
                print(note)
        else:
            print("No notes found.")
