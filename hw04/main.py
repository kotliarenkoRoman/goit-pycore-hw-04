from colorama import Fore
import re

def add_contact(args: list, contacts: dict) -> str:
    if len(args) != 2:
        return f"{Fore.RED}Usage: add [name] [phone]{Fore.RESET}"
    contacts[args[0]] = args[1]
    return f"{Fore.GREEN}Contact added{Fore.RESET}"

def change_contact(args: list, contacts: dict) -> str:
    if len(args) != 2:
        return f"{Fore.RED}Usage: change [name] [phone] {Fore.RESET}"
    if args[0] in contacts:
        contacts[args[0]] = args[1]
        return f"{Fore.GREEN}Contact changed{Fore.RESET}"
    else:
        return f"{Fore.RED}Contact not found. Cant update phone number{Fore.RESET}"   

def show_phone(args: list, contacts: dict) -> str:
    if len(args) !=  1:
        return f"{Fore.RED}Usage: phone [name] {Fore.RESET}"
    if args[0] in contacts:
        return f"{Fore.BLUE}{contacts[args[0]]}{Fore.RESET}"
    else:
        return f"{Fore.RED}Contact not found.{Fore.RESET}"    

def hello():
    return f"{Fore.YELLOW}Hello, how can i help you?{Fore.RESET}"

def parse_input(response: str):
        params = re.split(r'\s{1,}', response.strip())
        command = params[0]
        args = params[1:]
        return command, args

def main():
    contacts = {}
    print(f'{Fore.BLUE}Welcome to assistant bot!{Fore.RESET}')
    while True:
        response = input("Enter command: ").strip().lower()
        if not response:
            continue
        if response in ("exit","close"):
            print(f"{Fore.GREEN}Good bye!{Fore.RESET}")
            break

        cmd, args = parse_input(response)
        if cmd == 'hello':
            print(hello())
        elif cmd == 'add':
            print(add_contact(args, contacts))
        elif cmd == 'change':
            print(change_contact(args, contacts))
        elif cmd == 'phone':
            print(show_phone(args, contacts))
        elif cmd == 'all':
            print(f"{Fore.YELLOW}List of contacts:{Fore.RESET}")
            if len(contacts) == 0:
                print(f"{Fore.LIGHTBLACK_EX}No users..{Fore.RESET}")
            else:
                for name, phone in contacts.items():
                    print(f"{Fore.GREEN}{name}{Fore.RESET}: {Fore.BLUE}{phone}{Fore.RESET}")
        else:
            print(f"{Fore.RED}Invalid command{Fore.RESET}")            

if __name__ == "__main__":
    main()