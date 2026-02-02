import json

def create_new_book():
    try:
        with open("contact_book.json", "r") as file:
            pass
    except Exception:
        with open("contact_book.json", "w") as file:
            book = []
            json.dump(book, file, indent=4)

def add_contact(name, family, number):
    with open("contact_book.json", "r") as file:
        book = json.load(file)

    book.append({"first name":name, "last name": family, "phone number": number, "email": input("Enter email")})
    with open("contact_book.json", "w") as file:
        json.dump(book, file, indent= 4)

def show_all():
    with open("contact_book.json", "r") as file:
        book = json.load(file)

    to_show = "======== Contacts ========\n"
    for p in book:
        to_show += f"{p["first name"]} {p["last name"]}: {p["phone number"]}, email: {p['email']}\n"
    print(to_show)

def search_by_name(first_name):
    with open("contact_book.json", "r") as file:
        book = json.load(file)

    for c in book:
        if c["first name"] == first_name and c["last name"] == input("Enter last name"):
            return f"{c["first name"]} {c["last name"]}: {c["phone number"]}, email: {c['email']}"
    return "Contact not found"

def delete_contact(first_name, last_name):
    new_book = []
    flag = False
    with open("contact_book.json", "r") as file:
        book = json.load(file)
    for c in book:
        if (c["first name"] == first_name) and (c["last name"] == last_name):
            flag = True
            continue
        new_book.append(c)
    with open("contact_book.json", "w") as file:
        json.dump(new_book, file, indent= 4)
    print("Contact deleted") if flag else print("Contact not found")

def update_contact():
    flag = False
    with open("contact_book.json", "r") as file:
        book = json.load(file)
    first_name = input("Enter first name ")
    last_name = input("Enter last name ")
    for c in book:
        if (c["first name"] == first_name) and (c["last name"] == last_name):
            choice = input("Press 1 for updating phone number or 2 for email")
            if choice == "1":
                c["phone number"] = input("Enter new phone number")
            elif choice == "2":
                c["email"] = input("Enter new email")
            flag = True
    if flag:
        print("Contact updated")
        with open("contact_book.json", 'w') as file:
            json.dump(book, file, indent= 4)
    else:
        print("Contact not found, choose 'add contact'")


def main():
    create_new_book()
    add_contact("moshe", "israeli", "0555332332")
    delete_contact("moshe", "israeli")
    show_all()

if __name__ == "__main__":
    main()
