import json
from datetime import datetime

def create_new_book():
    try:
        with open("contact_book.json", "r") as file:
            pass
    except Exception:
        with open("contact_book.json", "w") as file:
            book = []
            json.dump(book, file, indent=4)

def is_saved(book, first, last):
    for c in book:
        if c["first name"] == first and c["last name"] == last:
            return True
    return False

def add_contact(book, name, family):
    if is_saved(book, name , family):
        print("\nThere is contact with the same name, press 'edit contact'\n")
        return

    book.append({"first name":name, "last name": family, "phone number": input("Enter phone number"), "email": input("Enter email")})
    sort_book(book)
    with open("contact_book.json", "w") as file:
        json.dump(book, file, indent= 4)

def show_all(book):
    to_show = "\n======== Contacts ========\n"
    for p in book:
        to_show += f"{p["first name"]} {p["last name"]}: {p["phone number"]}, email: {p['email']}\n"
    print(to_show)

def search_by_name(book, first_name):
    for c in book:
        if c["first name"] == first_name and c["last name"] == input("Enter last name"):
            return f"{c["first name"]} {c["last name"]}: {c["phone number"]}, email: {c['email']}"
    return "Contact not found"

def delete_contact(book, first_name, last_name):
    new_book = []
    flag = False
    for c in book:
        if (c["first name"] == first_name) and (c["last name"] == last_name):
            flag = True
            continue
        new_book.append(c)
    with open("contact_book.json", "w") as file:
        json.dump(new_book, file, indent= 4)
    print("\n== Contact deleted ==\n") if flag else print("\n== Contact not found ==\n")

def edit_contact(book):
    flag = False
    first_name = input("Enter first name ")
    last_name = input("Enter last name ")
    for c in book:
        if (c["first name"] == first_name) and (c["last name"] == last_name):
            choice = input("\nPress 1 for updating phone number or 2 for email")
            if choice == "1":
                c["phone number"] = input("Enter new phone number")
            elif choice == "2":
                c["email"] = input("Enter new email")
            flag = True
    if flag:
        print("\n== Contact updated ==\n")
        with open("contact_book.json", 'w') as file:
            json.dump(book, file, indent= 4)
    else:
        print("\nContact not found, choose 'add contact'\n")

def sort_book(book):
    for i in range(len(book)):
        mini = i
        for j in range(i + 1, len(book)):
            if book[j]["first name"] < book[mini]["first name"]:
                mini = j
        book[i], book[mini] = book[mini], book[i]

def backup(book):
    backup_name = f"backups/contact({datetime.now().strftime('%d.%m.%Y')}).json"
    with open(backup_name, 'w') as new_file:
        json.dump(book, new_file, indent= 4)
    print("\n= Backup created successfully =\n")

def main():
    create_new_book()
    add_contact("moshe", "israeli")
    delete_contact("moshe", "israeli")
    show_all()

if __name__ == "__main__":
    main()
