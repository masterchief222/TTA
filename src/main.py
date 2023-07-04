
from Menus.MainMenu import display_main_menu as main_menu
import colorama
import sys
import os


def create_file_and_directory(file_path):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)
    if not os.path.exists(file_path):
        open(file_path, 'w').close()


def initialize_interface_config():
    interface_file = "/etc/network/interfaces"
    create_file_and_directory(interface_file)
    try:
        with open(interface_file, "r") as file:
            lines = file.readlines()

        eth0_config_exists = False
        loopback_config_exists = False
        for line in lines:
            if line.startswith("auto eth0"):
                eth0_config_exists = True
            elif line.startswith("auto lo"):
                loopback_config_exists = True

        if not eth0_config_exists:
            lines.append("\n")
            lines.append("auto eth0\n")
            lines.append("iface eth0 inet dhcp\n")

        if not loopback_config_exists:
            lines.append("\n")
            lines.append("auto lo\n")
            lines.append("iface lo inet loopback\n")

        with open(interface_file, "w") as file:
            file.writelines(lines)

        print("eth0 and loopback interface configuration initialized.")
    except IOError:
        print(f"Error reading or writing file '{interface_file}'.")


def main():
    colorama.init()
    initialize_interface_config()
    input("press enter to go into main menu...")
    main_menu()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
