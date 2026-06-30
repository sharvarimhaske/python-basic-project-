import json
import os

FILE_NAME = "library.json"

def load_books():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

def save_books(books):
    with open(FILE_NAME, "w") as file:
        json.dump(books, file, indent=4)

def add_book():
    books = load_books()

    book_id = input("Enter Book ID: ")
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")

    book = {
        "id": book_id,
        "title": title,
        "author": author,
        "issued": False
    }

    books.append(book)
    save_books(books)

    print(" Book Added Successfully!")

def view_books():
    books = load_books()

    if not books:
        print("No Books Available.")
        return

    print("\n===== LIBRARY BOOKS =====")

    for book in books:
        status = "Issued" if book["issued"] else "Available"

        print("-" * 40)
        print("Book ID :", book["id"])
        print("Title   :", book["title"])
        print("Author  :", book["author"])
        print("Status  :", status)

def search_book():
    search_id = input("Enter Book ID: ")

    books = load_books()

    for book in books:
        if book["id"] == search_id:
            print("\nBook Found")
            print(book)
            return

    print("Book Not Found")

def issue_book():
    book_id = input("Enter Book ID to Issue: ")

    books = load_books()

    for book in books:
        if book["id"] == book_id:
            if not book["issued"]:
                book["issued"] = True
                save_books(books)
                print("Book Issued Successfully")
            else:
                print(" Book Already Issued")
            return

    print(" Book Not Found")

def return_book():
    book_id = input("Enter Book ID to Return: ")

    books = load_books()

    for book in books:
        if book["id"] == book_id:
            if book["issued"]:
                book["issued"] = False
                save_books(books)
                print("Book Returned Successfully")
            else:
                print("Book was not issued")
            return

    print(" Book Not Found")

def delete_book():
    book_id = input("Enter Book ID to Delete: ")

    books = load_books()

    books = [book for book in books if book["id"] != book_id]

    save_books(books)

    print(" Book Deleted Successfully")

while True:
    print("\n====== LIBRARY MANAGEMENT SYSTEM ======")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Delete Book")
    print("7. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        view_books()
    elif choice == "3":
        search_book()
    elif choice == "4":
        issue_book()
    elif choice == "5":
        return_book()
    elif choice == "6":
        delete_book()
    elif choice == "7":
        print("Thank You!")
        break
    else:
        print("Invalid Choice")



