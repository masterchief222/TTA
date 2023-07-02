
import subprocess
import sys
from Modules.Display import show


def display_others_menu():
    main_menu = {
        "print all file and folder in current directory": current_dir,
        "ping": ping,
        "Back": "Exit"
    }
    show(main_menu, "others functionality menu")


def current_dir():
    print("getting files and folders in current directory...")
    subprocess.call(['sh', "shell_scripts/cuDirectory.sh"])


def ping():
    ip = input("enter ip you want to ping: ")
    print(f"pinging {ip}...")
    subprocess.call(['sh', "shell_scripts/ping.sh", ip])
