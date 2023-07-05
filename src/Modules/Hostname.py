import subprocess
import os
from colorama import Fore, Style


def print_info(message):
    print(f"{Fore.BLUE}{message}{Style.RESET_ALL}")


def print_warning(message):
    print(f"{Fore.YELLOW}{message}{Style.RESET_ALL}")


def print_error(message):
    print(f"{Fore.RED}{message}{Style.RESET_ALL}")


def change_hostname():
    new_hostname = input("Enter the new hostname: ")
    try:
        # Write the new hostname to the /etc/hostname file
        with open("/etc/hostname", "w") as file:
            file.write(new_hostname)

        # Apply the hostname change using subprocess.run()
        subprocess.run(['hostnamectl', 'set-hostname',
                       new_hostname], check=True)

        print_info("Hostname changed successfully.")
    except subprocess.CalledProcessError as e:
        print_error(
            f"Error: Failed to change hostname. Return code: {e.returncode}")
        print(e.output.decode())
    except Exception as e:
        print_error(f"Failed to change hostname: {e}")


def get_current_hostname():
    try:
        with open("/etc/hostname", "r") as file:
            return file.read().strip()
    except FileNotFoundError:
        return ""


def get_hostname():
    try:
        result = subprocess.run(["hostname"], capture_output=True, text=True)
        current_hostname = result.stdout.strip()
        print_info("Current hostname: " + current_hostname)
    except subprocess.CalledProcessError as e:
        print_error(f"Failed to get current hostname: {e}")
