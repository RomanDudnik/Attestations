import csv
from datetime import datetime


class Note:

    def __init__(self, title, body):
        self.id = str(datetime.now())
        self.title = title
        self.body = body
        self.created_at = str(datetime.now())
        self.updated_at = str(datetime.now())


class Notes:

    def __init__(self):
        self.notes = {}

    def read_notes_csv(self, path):
        with open(path, "r") as f:
            reader = csv.reader(f, delimiter=";")
            for row in reader:
                if len(row) > 0:
                    note = Note(row[1], row[2])
                    note.id = row[0]
                    note.created_at = row[3]
                    note.updated_at = row[4]
                    self.notes[note.id] = note

    def add_note(self):
        title = input("Enter note title: ")
        body = input("Enter note body: ")
        note = Note(title, body)
        self.notes[note.id] = note

    def edit_note(self):
        note_id = input("Enter note id: ")
        if note_id in self.notes:
            title = input("Enter new title: ")
            body = input("Enter new body: ")
            note = self.notes[note_id]
            note.title = title
            note.body = body
            note.updated_at = str(datetime.now())
        else:
            print("Note not found")

    def delete_note(self):
        note_id = input("Enter note id: ")
        if note_id in self.notes:
            del self.notes[note_id]
        else:
            print("Note not found")

    def save_notes_csv(self, path):
        with open(path, "w") as f:
            writer = csv.writer(f, delimiter=";")
            for note_id in self.notes:
                note = self.notes[note_id]
                writer.writerow([note.id, note.title, note.body,
                                note.created_at, note.updated_at])

    def print_notes(self):
        for note_id in self.notes:
            note = self.notes[note_id]
            print(
                f"\n{note.id}\n{note.title}\n{note.body}\nCreated at: {note.created_at}\nUpdated at: {note.updated_at}\n")


if __name__ == "__main__":
    notes = Notes()
    path = "notes.csv"
    notes.read_notes_csv(path)
    print("The Notes app welcomes you! \nChoose an action.")

    while True:
        print("Menu: ")
        print("1. View notes")
        print("2. Add note")
        print("3. Edit note")
        print("4. Delete note")
        print("5. Save notes")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            notes.print_notes()
        elif choice == "2":
            notes.add_note()
        elif choice == "3":
            notes.edit_note()
        elif choice == "4":
            notes.delete_note()
        elif choice == "5":
            notes.save_notes_csv(path)
        elif choice == "6":
            break
