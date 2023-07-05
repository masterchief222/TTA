import sys
from Modules.Display import show
from Modules.Hostname import change_hostname, get_hostname


def display_Hostname_menu():
    main_menu = {
        "current hostname": get_hostname,
        "change hostname": change_hostname,
        "Back": "Exit"
    }
    show(main_menu, "Hostname handle menu")
