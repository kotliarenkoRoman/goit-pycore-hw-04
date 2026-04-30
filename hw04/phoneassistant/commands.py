from colorama import Fore
import re
from . import data

def show_help():
    for name, cmd_data in COMMANDS.items():
        print(f"{Fore.LIGHTBLACK_EX}'{name}' - {cmd_data['description']}{Fore.RESET}")

def add_contact(args: list):
    cmdArgs = COMMANDS['add'].get('args')
    if len(args) != len(cmdArgs):
        print(f"{Fore.RED}Usage: add {' '.join(cmdArgs)}{Fore.RESET}")
        return
    data.users_list[args[0]] = args[1]
    print(f"{Fore.GREEN}Contact added{Fore.RESET}")

def change_contact(args: list):
    cmdArgs = COMMANDS['change'].get('args')
    if len(args) !=  len(cmdArgs):
        print(f"{Fore.RED}Usage: change {' '.join(cmdArgs)}{Fore.RESET}")
        return
    if args[0] in data.users_list:
        data.users_list[args[0]] = args[1]
        print(f"{Fore.GREEN}Contact changed{Fore.RESET}")
    else:
        print(f"{Fore.RED}Contact not found. Cant update phone number{Fore.RESET}")    

def show_phone(args: list):
    cmdArgs = COMMANDS['phone'].get('args')
    if len(args) !=  len(cmdArgs):
        print(f"{Fore.RED}Usage: phone {' '.join(cmdArgs)}{Fore.RESET}")
        return
    if args[0] in data.users_list:
        print(data.users_list[args[0]])
    else:
        print(f"{Fore.RED}Contact not found.{Fore.RESET}")    

def show_all():
    print(f"{Fore.YELLOW}List of contacts:{Fore.RESET}")
    if len(data.users_list) == 0:
        print(f"{Fore.LIGHTBLACK_EX}No users..{Fore.RESET}")
    else:
        for name, phone in data.users_list.items():
            print(f"{Fore.GREEN}{name}{Fore.RESET}: {Fore.BLUE}{phone}{Fore.RESET}")

def hello():
    print(f"{Fore.YELLOW}Hello, how can i help you?{Fore.RESET}")


COMMANDS = {
    "help":{"handler":show_help, "args":None, "description":"Show this help"},
    "close":{"handler":None, "args":None, "description":"Exit from program"},
    "exit":{"handler":None, "args":None, "description":"Exit from program"},
    "add":{"handler":add_contact, "args": ['name', 'phone_number'],"description":"Add contact. Example: 'add John 1234567890'"},
    "change":{"handler":change_contact, "args": ['name', 'phone_number'],"description":"Change existed contact. Example: 'change John 0987654321'"},
    "phone":{"handler":show_phone, "args": ['name'],"description":"Show phone number by name from contact list"},
    "all":{"handler":show_all, "args": None,"description":"Show full list of contacts"},
    "hello":{"handler":hello, "args": None,"description":"Just say hello"},
}