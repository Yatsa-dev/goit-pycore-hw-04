def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def show_phone(args, contacts):
    name = args[0]
    phone = contacts.get(name)
    return f"Contact for name {name}: {phone}" if phone else f"Contact for name {name}: not found"
    
def change_phone(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return f"Contact with name '{name}' not found."
    
def get_all(contacts):
    return contacts
 

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "change":
            print(change_phone(args, contacts))
        elif command == "all":
            print(get_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
