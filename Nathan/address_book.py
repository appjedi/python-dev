
contacts = []


def save_contacts(filename="address_book.txt"):
    global contacts
    try:
        with open(filename, "w") as f:
            for name, email, phone in contacts:
                f.write(f"{name},{email},{phone}\n")
    except:
        print("error saving contacts")


def read_contacts(filename="address_book.txt"):
    global contacts
    try:
        with open(filename, "r") as f:
            for line in f:
                print("line:", line)
                name, email, phone = line.strip().split(",")
                contacts.append((name, email, phone))
    except:
        print("error reading file")
    return


def enter_contacts():
    another = "y"
    while another == "y":
        name = input("Enter name: ")
        email = input("Enter email: ")
        phone = input("Enter phone number: ")

        contacts.append((name, email, phone))
        another = input("Add another? (y/n): ")


def show_contacts():
    if len(contacts) == 0:
        print("no contacts")
        return

    print("Name, Email, Phone")
    for name, email, phone in contacts:
        print(f"{name} : {email} : {phone}")


def main_menu():
    choice = 0
    while choice != 9:
        print("\nMenu:")
        print("1. Enter Contact")
        print("2. Show Contacts")
        print("3. Save Contacts to File")
        print("4. Read Contacts from File")
        print("9. Quit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            enter_contacts()
        elif choice == 2:
            show_contacts()
        elif choice == 3:
            save_contacts()
            print("Contacts saved to address_book.txt")
        elif choice == 4:
            read_contacts()
            print("Contacts loaded from address_book.txt")
        elif choice == 9:
            print("Exiting program.")
        else:
            print("Invalid choice. Please try again.")


def main():
    try:
        main_menu()
    except:
        print("error")


main()