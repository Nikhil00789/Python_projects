import os
import datetime

# Database to store users and their contacts
users = {}         # { username: password }
contacts = {}      # { username: [ {id, first_name, last_name, email, phone}, ... ] }

# ─────────────────────────────────────────
#  HELPER FUNCTIONS
# ─────────────────────────────────────────

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_header(username):
    print(f"\n[User {username} logged in]")
    print(datetime.datetime.now().strftime("%a %b %d %H:%M:%S %Y"))
    print("-" * 30)

def get_next_id(username):
    contact_list = contacts[username]
    if len(contact_list) == 0:
        return 1
    return contact_list[-1]["id"] + 1

def show_menu():
    print("\nWhat do you want to do?")
    print("[view -a]  to view all contacts")
    print("[view]     to view a specific contact")
    print("[add]      to add a new contact")
    print("[del]      to delete a contact")
    print("[del -a]   to delete all contacts")
    print("[update]   to update a contact")
    print("[exit]     to logout")

# ─────────────────────────────────────────
#  CONTACT FUNCTIONS
# ─────────────────────────────────────────

def add_contact(username):
    print("\n--- Add New Contact ---")
    first_name = input("Enter First Name : ")
    last_name  = input("Enter Last Name  : ")
    email      = input("Enter Email      : ")
    phone      = input("Enter Phone No   : ")

    new_contact = {
        "id"         : get_next_id(username),
        "first_name" : first_name,
        "last_name"  : last_name,
        "email"      : email,
        "phone"      : phone
    }

    contacts[username].append(new_contact)
    print(f"\n✅ Contact '{first_name}' added successfully!")


def view_all_contacts(username):
    print("\n--- Your Contacts List ---")
    contact_list = contacts[username]

    if len(contact_list) == 0:
        print("No contacts found.")
        return

    print(f"{'ID':<5} {'First Name':<15} {'Last Name':<15} {'Email':<25} {'Phone':<15}")
    print("-" * 75)
    for c in contact_list:
        print(f"{c['id']:<5} {c['first_name']:<15} {c['last_name']:<15} {c['email']:<25} {c['phone']:<15}")


def view_specific_contact(username):
    print("\n--- View Specific Contact ---")
    contact_id = int(input("Enter Contact ID : "))

    contact_list = contacts[username]
    found = False

    for c in contact_list:
        if c["id"] == contact_id:
            print(f"\nContact ID   : {c['id']}")
            print(f"First Name   : {c['first_name']}")
            print(f"Last Name    : {c['last_name']}")
            print(f"Email        : {c['email']}")
            print(f"Phone Number : {c['phone']}")
            found = True
            break

    if not found:
        print("❌ Contact not found.")


def update_contact(username):
    print("\n--- Update Contact ---")
    contact_id = int(input("Enter Contact ID to update : "))

    contact_list = contacts[username]
    found = False

    for c in contact_list:
        if c["id"] == contact_id:
            print(f"\nUpdating contact: {c['first_name']} {c['last_name']}")
            print("(Press Enter to keep existing value)\n")

            new_first = input(f"First Name [{c['first_name']}] : ")
            new_last  = input(f"Last Name  [{c['last_name']}]  : ")
            new_email = input(f"Email      [{c['email']}]      : ")
            new_phone = input(f"Phone      [{c['phone']}]      : ")

            if new_first: c["first_name"] = new_first
            if new_last:  c["last_name"]  = new_last
            if new_email: c["email"]      = new_email
            if new_phone: c["phone"]      = new_phone

            print(f"\n✅ Contact updated successfully!")
            found = True
            break

    if not found:
        print("❌ Contact not found.")


def delete_contact(username):
    print("\n--- Delete Contact ---")
    contact_id = int(input("Enter Contact ID to delete : "))

    contact_list = contacts[username]
    found = False

    for c in contact_list:
        if c["id"] == contact_id:
            print(f"\nContact ID   : {c['id']}")
            print(f"First Name   : {c['first_name']}")
            print(f"Last Name    : {c['last_name']}")
            print(f"Email        : {c['email']}")
            print(f"Phone Number : {c['phone']}")

            confirm = input("\nAre you sure you want to delete? (yes/no) : ")
            if confirm.lower() == "yes":
                contact_list.remove(c)
                print(f"✅ Contact '{c['first_name']}' successfully deleted.")
            else:
                print("Deletion cancelled.")
            found = True
            break

    if not found:
        print("❌ Contact not found.")


def delete_all_contacts(username):
    print("\n--- Delete All Contacts ---")
    confirm = input("Are you sure you want to delete ALL contacts? (yes/no) : ")
    if confirm.lower() == "yes":
        contacts[username].clear()
        print("✅ All contacts deleted.")
    else:
        print("Deletion cancelled.")


# ─────────────────────────────────────────
#  AUTHENTICATION FUNCTIONS
# ─────────────────────────────────────────

def register():
    print("\n--- Register ---")
    username = input("Choose a Username : ")

    if username in users:
        print("❌ Username already exists. Please login.")
        return None

    password = input("Choose a Password : ")
    users[username] = password
    contacts[username] = []
    print(f"✅ Account created successfully! Welcome, {username}!")
    return username


def login():
    print("\n--- Login ---")
    username = input("Enter Username : ")
    password = input("Enter Password : ")

    if username in users and users[username] == password:
        print(f"✅ Login successful! Welcome back, {username}!")
        return username
    else:
        print("❌ Invalid username or password.")
        return None


# ─────────────────────────────────────────
#  MAIN PHONE BOOK MENU
# ─────────────────────────────────────────

def phonebook_menu(username):
    while True:
        clear()
        show_header(username)
        show_menu()

        choice = input("\n~$ ").strip().lower()

        if choice == "add":
            add_contact(username)
        elif choice == "view -a":
            view_all_contacts(username)
        elif choice == "view":
            view_specific_contact(username)
        elif choice == "update":
            update_contact(username)
        elif choice == "del":
            delete_contact(username)
        elif choice == "del -a":
            delete_all_contacts(username)
        elif choice == "exit":
            print(f"\nGoodbye, {username}! 👋")
            break
        else:
            print("❌ Invalid command. Please try again.")

        input("\nPress Enter to continue...")


# ─────────────────────────────────────────
#  MAIN ENTRY POINT
# ─────────────────────────────────────────

def main():
    print("=" * 40)
    print("   📞 Welcome to Digital Phone Book")
    print("=" * 40)

    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("\nEnter choice (1/2/3) : ").strip()

        if choice == "1":
            username = register()
            if username:
                phonebook_menu(username)
        elif choice == "2":
            username = login()
            if username:
                phonebook_menu(username)
        elif choice == "3":
            print("\nThank you for using Digital Phone Book. Goodbye! 👋")
            break
        else:
            print("❌ Invalid choice. Enter 1, 2 or 3.")

main()