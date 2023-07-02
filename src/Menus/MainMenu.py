
import sys
from Modules.Display import show
from Menus.OthersMenu import display_others_menu as Other
from Menus.PhaseOneMenu import display_phase_one_menu as phase1


def display_main_menu():
    main_menu = {
        "phase 1 menu": phase1,
        "phase 2 menu": phase2,
        "others menu": Other,
        "Exit": sys.exit
    }
    show(main_menu,"Main menu")


def phase2():
    print("phase 2--")
