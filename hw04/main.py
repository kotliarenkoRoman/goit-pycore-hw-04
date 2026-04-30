from phoneassistant import handler
from colorama import Fore

def main():
    print(f'{Fore.BLUE}Welcome to assistant bot!{Fore.RESET}')
    while True:
        response = input("Enter command: ").strip().lower()
        if not response:
            continue
        if response in ("exit","close"):
            print(f"{Fore.GREEN}Good bye!{Fore.RESET}")
            break

        handler.handle_command(response)   

if __name__ == "__main__":
    main()