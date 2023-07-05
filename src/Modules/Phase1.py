import socket
from Modules.Display import show_delete_menu as delete_menu
from Modules.Validation import is_valid_ip
import subprocess
from colorama import Fore, Style
import os


def print_info(message):
    print(f"{Fore.BLUE}{message}{Style.RESET_ALL}")


def print_warning(message):
    print(f"{Fore.YELLOW}{message}{Style.RESET_ALL}")


def print_error(message):
    print(f"{Fore.RED}{message}{Style.RESET_ALL}")
