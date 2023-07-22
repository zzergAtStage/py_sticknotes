import datetime


class ConsoleUI:
    def __init__(self, note_service):
        """Provide the view functions and offer to the user application's abilities"""
        self.note_service = note_service
    def _display_search_results(self, found_notes):
        if found_notes:
            print("Found notes:")
            self.note_service.show_selected_notes(found_notes)
        else:
            print("No notes found.")

    def display_menu(self):
        print("\n------ Menu ------")
        print("1. Add a new note")
        print("2. Find notes")
        print("3. Modify a note")
        print("4. Delete a note")
        print("5. Show all notes")
        print("0. Exit")

    def _get_search_type(self):
        while (True):
            print("\n------- Search Type ------")
            print("1. Plain Text Search")
            print("2. Date-Based Search")
            print("0. Back to Main Menu")
            choice = input("Enter your choice: ")
            if choice == "1":
                search_text = input("Enter the text to search in notes' body: ")
                found_notes = self.note_service.find_notes(search_text=search_text)
                self._display_search_results(found_notes)
                break
            elif choice == "2":
                search_date_input = input("Enter the date to search (DD/MM/YYYY): ")
                try:#trying to convert date to datetime object ignore time
                    search_date = datetime.datetime.strptime(search_date_input, "%d/%m/%Y")
                    print(f"Debug: search_date: {search_date}")
                    found_notes = self.note_service.find_notes(search_date=search_date)
                    self._display_search_results(found_notes)
                    break
                except ValueError:
                    print("Invalid date format. Please enter a valid date in the format DD/MM/YYYY")
            elif choice == "0":
                break
            else:
                print("Invalid choice. Please try again.")

 
    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")

            if choice == "1":
                body = input("Enter the note's body: ")
                self.note_service.add_new_note(body)
            elif choice == "2":
               self._get_search_type()
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
