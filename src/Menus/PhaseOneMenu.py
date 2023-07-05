import subprocess
from Modules.Display import show
from Menus.DNSMenu import display_DNS_menu
import Modules.Phase1
from Menus.HostnameMenu import display_Hostname_menu
from Menus.IpMenu import display_IP_menu
import sys


def display_phase_one_menu():
    main_menu = {
        "DNS menu": display_DNS_menu,
        "Hostname menu": display_Hostname_menu,
        "IP menu": display_IP_menu,
        "route menu": route,
        "back": "Exit"
    }
    show(main_menu, "Phase 1 menu")


def route():
    pass
