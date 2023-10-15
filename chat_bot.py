def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args: list, contacts):
    if valid_arguments(args):
        name, phone  = args
        contacts[name] = phone
        return f"Contact {name} was added"
    return('Please provide only name and contact info')

def change_contact(args: list, contacts):
    if valid_arguments(args):
        name, phone = args
        if name in contacts:
            contacts[name] = phone
            return f'Contact {name} was updated with {phone}'
        else:
           return(add_if_not_exists(name, contacts))
    return('Please privide only name and contact info!')

def get_phone(args, contacts):
    name = args[0]
    if name in contacts:
        return contacts[name]
    else: 
        return(add_if_not_exists(name, contacts))

def add_if_not_exists(name, contacts_list):
    response = (input(f"{name} is not found in the contacts list. Would you like to add one now? y/n: ")).lower()
    if response in ['y', 'yes']:
        phone = input(f'Enter contact information for {name}: ').split()
        return(add_contact([name, phone[0]], contacts_list))
    elif response in ['n', 'no', 'not']:
        return 'As you wish, master'
    else:
        return 'I take it as NO'

def print_contacts(args, contacts_list):
    all_contacts ='\n{:<15}{}\n\n'.format('NAME', "CONTACT INFO")
    for contact, contact_info in contacts_list.items():
        all_contacts+=f'{contact:<15}: {contact_info}\n'
    return all_contacts

def valid_arguments(args):
    if len(args) != 2:
        return False
    return True

def main():
    contacts = {}
    COMMANDS = {
        'add': add_contact,
        'update': change_contact,
        'change':change_contact,
        'phone': get_phone,
        'all': print_contacts,
        'hello': lambda *_: 'How can I help you?'
    }

    print('Welome to the assistant bot!')
    while True:
        user_input = input('Enter the command: ').strip().lower()
        command, *args = parse_input(user_input)

        if command in ['close', 'exit', 'goodbye']:
            print('Goodbye!')
            break
        elif command in COMMANDS:
            resut = COMMANDS[command](args, contacts)
            if resut:
                print(resut)
        else:
            print('Invalid command')



if __name__ == "__main__":
    main()