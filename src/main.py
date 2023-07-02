
from Menus.MainMenu import display_main_menu as main_menu
import colorama
import sys
import os


def main():
    colorama.init()
    main_menu()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
