from functions import show_all, add_contact, search_by_name, delete_contact, create_new_book, edit_contact

create_new_book()

interface = ("====== Hello ======\n"
             "1. Show all contacts\n"
             "2. Add new contact\n"
             "3. Search contact\n"
             "4. Delete contact\n"
             "5. Edit contact\n"
             "0. Quit\n")

while True:
    print(interface)
    choice = input("Select an option")
    if choice == "0":
        break
    elif choice == "1":
        show_all()
    elif choice == "2":
        name = input("Enter first name")
        family = input("Enter last name")
        add_contact(name, family)
    elif choice == "3":
        first_name = input("Enter first name")
        print(search_by_name(first_name))
    elif choice == "4":
        first_name = input("Enter first name")
        last_name = input("Enter last name")
        delete_contact(first_name, last_name)
    elif choice == "5":
        edit_contact()
    else:
        print("Invalid choice, please try again")