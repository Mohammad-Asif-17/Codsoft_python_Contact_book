class ContactManager:
    def __init__(self):
        self.contacts = {}

    def add_contact(self , name, phone_number, email, address):
        self.contacts[name] = {'phone_number': phone_number, 'email': email, 'address': address}

    def view_contact_list(self):
        if self.contacts:
            print("Contact List:")
            for name , details in self.contacts.items():
                print(f"Name:{name}, Phone Number:{details['phone_number']}, Email:{details['email']}, Address:{details['address']}")
        else:
            print("Contact list is empty.")

    def search_contact(self, serach_term):
        serach_result = []
        for name, details in self.contacts.items():
            if serach_term.lower() in name.lower() or serach_term in details['phone_number']:
                serach_result.append((name, details['phone_number']))
                if serach_result:
                    print("Search Results:")
                    for name, phone_number in serach_result:
                        print(f"Name:{name}, Phone Number:{phone_number}")
                else:
                    print("No matching contacts found.")

    def update_contact(self, name, phone_number, email, address):
        if name in self.contacts:
            self.contacts[name] = {'phone_number': phone_number, 'email': email, 'address':address}
            print("Contact update successfully.")
        else:
            print("Contact not found.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]

            print("Contact delete successfully.")

        else:
            print("Contact not found.")

def main():
    Contact_manager = ContactManager()
    while True:
        print("\n Contact Management System menu:")

        print("1. To Add Contact")
        print("2. To View Contact")
        print("3. To Search Contact")
        print("4. To Update Contact")
        print("5. To Delete Contact")
        print("6. To Exit")

        choice = input("Enter your choice:")

        if choice == '1':
            name = input("Enter your name:")
            phone_number = input("Enter your phone number:")
            email = input("Enter your email:")
            address = input("Enter your address:")

            Contact_manager.add_contact(name, phone_number, email, address)
        elif choice =='2':
            Contact_manager.view_contact_list()
        elif choice == '3':
            serach_term = input("Enter name or phone number to serach:")
            Contact_manager.search_contact(serach_term)
        elif choice == '4':
            name = input("Enter your name of the contact to update:")
            if name in Contact_manager.contacts:
                phone_number = input("Enter new phone number:")
                email = input("Enter new email:")
                address = input("Enter new address:")

                Contact_manager.update_contact(name, phone_number, email, address)
            else:
                print("Contact not found:")
        elif choice =='5':
            name = input("Enter name of contact to delete:")
            Contact_manager.delete_contact(name)
        elif choice == '6':
            print("Exiting....")
            break
        else:
            print("Invalid choice, please try again.")
if __name__=="__main__":
    main()