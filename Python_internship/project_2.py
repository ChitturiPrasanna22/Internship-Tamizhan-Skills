import json
from datetime import datetime, timedelta
import os

FILE_NAME = "library.json"
FINE_PER_DAY = 5  # Rs.5 per day

#  Load / Save Data 
def load_data():
    if not os.path.exists(FILE_NAME):
        return {}
    with open(FILE_NAME, "r") as file:
        return json.load(file)

def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

library = load_data()

#  Add Book 
def add_book():
    book_id = input("Enter Book ID: ")
    title = input("Enter Book Title: ")

    if book_id in library:
        print("Book already exists")
        return

    library[book_id] = {
        "title": title,
        "issued_to": None,
        "issue_date": None,
        "due_date": None
    }
    save_data(library)
    print("Book added successfully")

# Remove Book 
def remove_book():
    book_id = input("Enter Book ID to remove: ")

    if book_id not in library:
        print("Book not found")
        return

    del library[book_id]
    save_data(library)
    print("Book removed successfully")

# Issue Book
def issue_book():
    book_id = input("Enter Book ID: ")

    if book_id not in library:
        print("Book not found")
        return

    if library[book_id]["issued_to"] is not None:
        print("Book already issued")
        return

    student = input("Enter Student Name: ")
    issue_date = datetime.now()
    due_date = issue_date + timedelta(days=7)

    library[book_id]["issued_to"] = student
    library[book_id]["issue_date"] = issue_date.strftime("%Y-%m-%d")
    library[book_id]["due_date"] = due_date.strftime("%Y-%m-%d")

    save_data(library)
    print("Book issued successfully")
    print("Due Date:", due_date.strftime("%d-%m-%Y"))

# Return Book 
def return_book():
    book_id = input("Enter Book ID: ")

    if book_id not in library:
        print("Book not found")
        return

    if library[book_id]["issued_to"] is None:
        print("Book was not issued")
        return

    due_date = datetime.strptime(library[book_id]["due_date"], "%Y-%m-%d")
    return_date = datetime.now()

    fine = 0
    if return_date > due_date:
        days_late = (return_date - due_date).days
        fine = days_late * FINE_PER_DAY

    library[book_id]["issued_to"] = None
    library[book_id]["issue_date"] = None
    library[book_id]["due_date"] = None

    save_data(library)
    print("Book returned successfully")
    print("Fine Amount: Rs.", fine)

#  View Books 
def view_books():
    if not library:
        print("No books available")
        return

    for book_id, details in library.items():
        print("\nBook ID:", book_id)
        print("Title:", details["title"])
        print("Issued To:", details["issued_to"])
        print("Due Date:", details["due_date"])


while True:
    print("\n--- Library Book Management System ---")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. View Books")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        remove_book()
    elif choice == "3":
        issue_book()
    elif choice == "4":
        return_book()
    elif choice == "5":
        view_books()
    elif choice == "6":
        print("Exiting Library System")
        break
    else:
        print("Invalid choice")
