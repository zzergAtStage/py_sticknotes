from notes_presenter import NotesPresenter

def main():
    file_path = "notes.json"
    presenter = NotesPresenter(file_path)
    presenter.run()

if __name__ == "__main__":
    main()
