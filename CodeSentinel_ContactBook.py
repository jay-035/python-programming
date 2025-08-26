def add_contact(filename):
    name = input("Enter contact name: ").strip()
    phone = input("Enter phone number: ").strip()
    with open(filename, "a") as f:
        f.write(f"{name},{phone}\n")
    print("Contact added.\n")

def view_contacts(filename):
    try:
        with open(filename, "r") as f:
            lines = f.readlines()
            if not lines:
                print("No contacts found.")
                return
            print("Saved Contacts:-\n")
            for line in lines:
                name, phone = line.strip().split(",", 1)
                print(f"{name}: {phone}")
            print()
    except FileNotFoundError:
        print("No contacts found.")

filename = "contacts.txt"
while True:
    print("Contact Book")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Exit")
    choice = input("Choose an option: ").strip()
    if choice == "1":
        add_contact(filename)
    elif choice == "2":
        view_contacts(filename)
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.\n")
