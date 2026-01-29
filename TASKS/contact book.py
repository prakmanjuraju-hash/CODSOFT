def add_contact(contacts):
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()
    address = input("Enter address: ").strip()

    contacts[name] = {
        "phone": phone,
        "email": email,
        "address": address
    }

    print("Contact added successfully!\n")


def view_contacts(contacts):
    if not contacts:
        print("No contacts found.\n")
        return

    print("\n--- Contact List ---")
    for name, details in contacts.items():
        print(f"Name: {name} | Phone: {details['phone']}")
    print()


def search_contact(contacts):
    keyword = input("Enter name or phone number to search: ").strip()

    found = False
    for name, details in contacts.items():
        if keyword.lower() in name.lower() or keyword in details["phone"]:
            print("\nContact Found:")
            print(f"Name: {name}")
            print(f"Phone: {details['phone']}")
            print(f"Email: {details['email']}")
            print(f"Address: {details['address']}\n")
            found = True

    if not found:
        print("Contact not found.\n")


def update_contact(contacts):
    name = input("Enter the name of the contact to update: ").strip()

    if name not in contacts:
        print("Contact not found.\n")
        return

    print("Leave blank to keep existing value.")

    phone = input("New phone number: ").strip()
    email = input("New email: ").strip()
    address = input("New address: ").strip()

    if phone:
        contacts[name]["phone"] = phone
    if email:
        contacts[name]["email"] = email
    if address:
        contacts[name]["address"] = address

    print("Contact updated successfully!\n")


def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ").strip()

    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!\n")
    else:
        print("Contact not found.\n")


def main():
    contacts = {}

    while True:
        print("=== Contact Book ===")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            update_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "6":
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.\n")


if __name__ == "__main__":
    main()
