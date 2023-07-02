import subprocess
from Modules.Display import show
from Menus.DNSMenu import display_DNS_menu
import Modules.Phase1
import sys


def display_phase_one_menu():
    main_menu = {
        "DNS": display_DNS_menu,
        "Hostname": Hostname,
        "IP": Ip,
        "route": route,
        "back": "Exit"
    }
    show(main_menu, "Phase 1 menu")


def Hostname():
    pass


def Ip():
    pass


def route():
    pass
