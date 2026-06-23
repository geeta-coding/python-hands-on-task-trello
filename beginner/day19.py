import json
import re
import os

FILE_NAME = "contacts.json"


# ----------------------------
# File Handling
# ----------------------------

def load_contacts():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)


# ----------------------------
# Validation
# ----------------------------

def validate_phone(phone):
    return phone.isdigit() and len(phone) == 10


def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)


# ----------------------------
# Add Contact
# ----------------------------

def add_contact(contacts):
    name = input("Enter Name: ")

    while True:
        phone = input("Enter Phone (10 digits): ")
        if validate_phone(phone):
            break
        print("Invalid phone number!")

    while True:
        email = input("Enter Email: ")
        if validate_email(email):
            break
        print("Invalid email format!")

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "favorite": False
    }

    contacts.append(contact)
    save_contacts(contacts)

    print("Contact added successfully!")


# ----------------------------
# Display Contacts
# ----------------------------

def display_contacts(contacts):
    if not contacts:
        print("\nNo contacts found.")
        return

    print("\n" + "=" * 80)
    print(f"{'Name':20} {'Phone':15} {'Email':30} {'Favorite'}")
    print("=" * 80)

    for contact in contacts:
        fav = "★" if contact["favorite"] else "-"
        print(
            f"{contact['name']:20} "
            f"{contact['phone']:15} "
            f"{contact['email']:30} "
            f"{fav}"
        )

    print("=" * 80)


# ----------------------------
# Search Contact
# ----------------------------

def search_contact(contacts):
    keyword = input("Enter name to search: ").lower()

    found = False

    for contact in contacts:
        if keyword in contact["name"].lower():
            print("\nFound:")
            print(contact)
            found = True

    if not found:
        print("No matching contacts found.")


# ----------------------------
# Update Contact
# ----------------------------

def update_contact(contacts):
    name = input("Enter contact name to update: ").lower()

    for contact in contacts:
        if contact["name"].lower() == name:

            new_name = input(
                f"New Name ({contact['name']}): "
            ) or contact["name"]

            while True:
                new_phone = input(
                    f"New Phone ({contact['phone']}): "
                )

                if new_phone == "":
                    new_phone = contact["phone"]
                    break

                if validate_phone(new_phone):
                    break

                print("Invalid phone number!")

            while True:
                new_email = input(
                    f"New Email ({contact['email']}): "
                )

                if new_email == "":
                    new_email = contact["email"]
                    break

                if validate_email(new_email):
                    break

                print("Invalid email!")

            contact["name"] = new_name
            contact["phone"] = new_phone
            contact["email"] = new_email

            save_contacts(contacts)

            print("Contact updated successfully!")
            return

    print("Contact not found.")


# ----------------------------
# Delete Contact
# ----------------------------

def delete_contact(contacts):
    name = input("Enter contact name to delete: ").lower()

    for contact in contacts:
        if contact["name"].lower() == name:
            contacts.remove(contact)
            save_contacts(contacts)

            print("Contact deleted successfully!")
            return

    print("Contact not found.")


# ----------------------------
# Favorites Feature
# ----------------------------

def toggle_favorite(contacts):
    name = input("Enter contact name: ").lower()

    for contact in contacts:
        if contact["name"].lower() == name:
            contact["favorite"] = not contact["favorite"]

            status = (
                "marked as favorite"
                if contact["favorite"]
                else "removed from favorites"
            )

            save_contacts(contacts)

            print(f"Contact {status}.")
            return

    print("Contact not found.")


def show_favorites(contacts):
    favorites = [c for c in contacts if c["favorite"]]

    if not favorites:
        print("No favorite contacts.")
        return

    display_contacts(favorites)


# ----------------------------
# Main Menu
# ----------------------------

def main():
    contacts = load_contacts()

    while True:
        print("\n===== CONTACT BOOK =====")
        print("1. Add Contact")
        print("2. Display All Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Mark/Unmark Favorite")
        print("7. Show Favorites")
        print("8. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_contact(contacts)

        elif choice == "2":
            display_contacts(contacts)

        elif choice == "3":
            search_contact(contacts)

        elif choice == "4":
            update_contact(contacts)

        elif choice == "5":
            delete_contact(contacts)

        elif choice == "6":
            toggle_favorite(contacts)

        elif choice == "7":
            show_favorites(contacts)

        elif choice == "8":
            print("Goodbye!")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()