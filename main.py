from functions import show_all, add_contact, search_by_name, delete_contact, create_new_book, edit_contact, backup
import json

create_new_book()

interface = ("====== Hello ======\n"
             "1. Show all contacts\n"
             "2. Add new contact\n"
             "3. Search contact\n"
             "4. Delete contact\n"
             "5. Edit contact\n"
             "6. Create backup file\n"
             "0. Quit\n")

with open("contact_book.json", "r") as file:
    book = json.load(file)

while True:
    print(interface)
    choice = input("Select an option")
    if choice == "0":
        break
    elif choice == "1":
        show_all(book)
    elif choice == "2":
        name = input("Enter first name")
        family = input("Enter last name")
        add_contact(book, name, family)
    elif choice == "3":
        first_name = input("Enter first name")
        print(search_by_name(book, first_name))
    elif choice == "4":
        first_name = input("Enter first name")
        last_name = input("Enter last name")
        delete_contact(book, first_name, last_name)
    elif choice == "5":
        edit_contact(book)
    elif choice == "6":
        backup(book)
    else:
        print("Invalid choice, please try again")
    input("press ENTER to continue\n")