import pathlib, sys
from colorama import Fore

MAX_LEVEL = 10
IDENT = 2

def get_styled_item_name(item: pathlib.Path) -> str: 
    if item.is_dir():
        return f"{Fore.BLUE} {item.name}/ {Fore.RESET}"
    return f"{Fore.LIGHTBLACK_EX} {item.name} {Fore.RESET}"

def show_directory_tree(path: pathlib.Path, level: int = 0):
    for item in path.iterdir():
        item_name = get_styled_item_name(item)
        shift = len(item_name) + level * IDENT
        print(f"{item_name:>{shift}}")
        if item.is_dir() and level <= MAX_LEVEL:
            show_directory_tree(item, level + 1)

def main():
    args = sys.argv
    if len(args) == 1: #no args 
        print(f"{Fore.RED}Directory path empty.{Fore.RESET}")
        return
    
    dirpath = pathlib.Path(args[1])
    
    if not dirpath.exists():
       print(f"{Fore.RED}Directory {dirpath} is not exists.{Fore.RESET}")
       return
     
    if not dirpath.is_dir():
       print(f"{Fore.RED} {dirpath} is not directory.{Fore.RESET}")         
       return

    show_directory_tree(dirpath)

if __name__ == '__main__':
    main()