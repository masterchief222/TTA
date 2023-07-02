from Modules.Display import show
import sys


def display_phase_one_menu():
    main_menu = {
        "DNS": DNS,
        "Hostname": Hostname,
        "IP": Ip,
        "route": route,
        "back": "Exit"
    }
    show(main_menu)


def DNS():
    pass


def Hostname():
    pass


def Ip():
    pass


def route():
    pass
