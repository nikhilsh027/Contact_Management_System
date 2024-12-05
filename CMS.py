class Contact:
    def __init__(self, name, ph_number, email):
        self.name = name
        self.ph_number = ph_number
        self.email = email

    def __str__(self):
        return f"Name: {self.name}, Phone Number: {self.ph_number}, Email: {self.email}"


class ContactManager:
    def __init__(self):
        self.ContactList = []

    def add_contact(self, contact):
        self.ContactList.append(contact)

    def display_contacts(self):
        if not self.ContactList:
            print("No contacts available.")
            return
        for contact in self.ContactList:
            print(contact)  

    def search_contact(self, search_name):
        found_contacts = [contact for contact in self.ContactList if search_name.lower() in contact.name.lower()]
        if found_contacts:
            print("Found Contacts:")
            for contact in found_contacts:
                print(contact)
        else:
            print("Contact not found.")


def main():
    cm = ContactManager()

    while True:
        print("\nContact Menu")
        print("1. Add New Contact")
        print("2. Search Contact")
        print("3. Display Contacts")
        print("4. Exit")

        choice = input("\nChoose an option (1-4): ")

        if choice == '1':
            name = input("Enter the name of the contact: ")
            ph_number = input("Enter phone number of the contact: ")
            email = input("Enter email of the contact: ")
            cm.add_contact(Contact(name, ph_number, email))
            print(f"Contact of {name} has been added.")

        elif choice == '2':
            search_name = input("Input name to search: ")
            cm.search_contact(search_name)

        elif choice == '3':
            print("\nAll Contacts:")
            cm.display_contacts()

        elif choice == '4':
            print("Exiting the program.")
            break

        else:
            print("Invalid option. Please choose a number between 1 and 4.")


if __name__ == "__main__":
    main()
