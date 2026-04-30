from . import commands
import re
from colorama import Fore


def parse_input(response: str):
        params = re.split(r'\s{1,}', response.strip())
        command = params[0]
        args = params[1:]
        return command, args

def handle_command(response: str):
    commandName, args = parse_input(response)
    cmd = commands.COMMANDS.get(commandName)

    if not cmd:
        print(f"{Fore.RED}Invalid command '{commandName}' {Fore.RESET}")
    else:
        handler = cmd['handler']

        if cmd['args']:
            handler(args)
        else:
            handler()    