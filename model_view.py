class ConsoleUI:
    def __init__(self, note_service):
        self.note_service = note_service

    def display_menu(self):
        print("------ Menu ------")
        print("1. Add a new note")
        print("2. Find notes")
        print("3. Modify a note")
        print("4. Delete a note")
        print("5. Show all notes")
        print("0. Exit")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")

            if choice == "1":
                body = input("Enter the note's body: ")
                self.note_service.add_new_note(body)
            elif choice == "2":
                keyword = input("Enter a keyword to search for: ")
                found_notes = self.note_service.find_notes(keyword)
                if found_notes:
                    print("Found notes:")
                    for note in found_notes:
                        print(f"{note}")
                else:
                    print("No notes found.")
            elif choice == "3":
                note_index = int(input("Enter the index of the note to modify: ")) - 1
                new_body = input("Enter the new body for the note: ")
                self.note_service.modify_note(note_index, new_body)
            elif choice == "4":
                note_index = int(input("Enter the index of the note to delete: ")) - 1
                self.note_service.delete_note(note_index)
            elif choice == "5":
                self.note_service.show_all_notes()
            elif choice == "0":
                print("Exiting the application. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
