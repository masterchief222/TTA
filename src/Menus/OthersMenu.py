
import subprocess
import sys
from Modules.Display import show
import netifaces


def display_others_menu():
    main_menu = {
        "print all file and folder in current directory": current_dir,
        "ping": ping,
        "print_resolve_conf": print_resolve_conf,
        "print_interface_conf": print_interface_conf,
        "all interfaces": print_all_interfaces,
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


def print_resolve_conf():
    config_file = "/etc/resolv.conf"

    try:
        with open(config_file, "r") as file:
            content = file.read()

        print(f"Content of {config_file}:")
        print(content)
    except FileNotFoundError:
        print(f"Configuration file '{config_file}' not found.")
    except IOError:
        print(f"Error reading file '{config_file}'.")


def print_interface_conf():
    interface_file = "/etc/network/interfaces"

    try:
        with open(interface_file, "r") as file:
            content = file.read()

        print(f"Content of {interface_file}:")
        print(content)
    except FileNotFoundError:
        print(f"Interface file '{interface_file}' not found.")
    except IOError:
        print(f"Error reading file '{interface_file}'.")


def print_all_interfaces():
    print(all_interfaces())


def all_interfaces():
    interfaces = netifaces.interfaces()
    return interfaces


def restart_networking_service():
    try:
        subprocess.run(['sudo', 'systemctl', 'restart',
                       'networking'], check=True)
    except subprocess.CalledProcessError as e:
        print(
            f"Error: Failed to restart networking service. Return code: {e.returncode}")
        print(e.output.decode())
