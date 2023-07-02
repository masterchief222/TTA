from Modules.Display import show_delete_menu as delete_menu
from Modules.Validation import is_valid_ip
import subprocess
from colorama import Fore, Style


def print_info(message):
    print(f"{Fore.BLUE}{message}{Style.RESET_ALL}")


def print_warning(message):
    print(f"{Fore.YELLOW}{message}{Style.RESET_ALL}")


def print_error(message):
    print(f"{Fore.RED}{message}{Style.RESET_ALL}")


def get_current_name_servers(_print=True):
    config_file = "/etc/resolv.conf"

    try:
        with open(config_file, "r") as file:
            lines = file.readlines()

        name_servers = []
        for line in lines:
            try:
                if line.startswith("nameserver"):
                    name_server = line.split()[1]
                    name_servers.append(name_server)
            except:
                print_error("you have wrong dns config!")

        if name_servers:
            if _print:
                print_info("Current name servers:")
                for name_server in name_servers:
                    print(name_server)
            return name_servers
        else:
            print_warning("No name servers found in the configuration file.")
    except FileNotFoundError:
        print_error(f"Configuration file '{config_file}' not found.")


def delete_name_server():
    name_servers = get_current_name_servers(False)
    if name_servers is None:
        return
    name_servers.append("Exit")
    chosen_name_server = delete_menu(name_servers)
    if chosen_name_server is None:
        return
    config_file = "/etc/resolv.conf"

    try:
        with open(config_file, "r") as file:
            lines = file.readlines()

        # Filter out the lines containing the chosen name server
        filtered_lines = [
            line for line in lines if not line.startswith("nameserver " + chosen_name_server)]

        with open(config_file, "w") as file:
            file.writelines(filtered_lines)

        print_info(f"Name server '{chosen_name_server}' deleted successfully.")
    except FileNotFoundError:
        print_error(f"Configuration file '{config_file}' not found.")
    except IOError:
        print_error(f"Error reading or writing file '{config_file}'.")


def add_name_server():
    current_dns = get_current_name_servers(False)
    while True:
        name_server = input("Enter the name server to add: ").strip()
        if name_server.lower() == "exit":
            return
        if current_dns is not None and name_server in current_dns:
            print_warning("Duplicate detected!")
            return
        validation = is_valid_ip(name_server)
        if validation:
            break

    file_path = "/etc/resolv.conf"

    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
            last_nameserver_index = max(
                (i for i, line in enumerate(lines) if line.startswith("nameserver ")), default=-1)
            if current_dns == None or last_nameserver_index == -1:
                # If 'nameserver' is not found, append the new entry at the end of the file
                lines.append(f"nameserver {name_server}\n")
            else:
                position = 0
                while position < 1 or position > len(current_dns) + 1:

                    inp = input(
                        f"Enter the position to add the name server (1-{len(current_dns) + 1}): ")
                    if inp.lower() == "exit":
                        return
                    try:
                        position = int(inp)
                    except ValueError:
                        print_error(
                            f"please input 1-{len(current_dns) + 1} or Exit only(press enter to continue)")

                if position == len(current_dns) + 1:
                    lines.append(f"nameserver {name_server}\n\n")
                else:
                    line_index = [i for i, line in enumerate(
                        lines) if current_dns[position - 1] in line][0]
                    lines.insert(line_index, f"nameserver {name_server}\n")
        for i, line in enumerate(lines):
            lines[i] = line.strip(" ")
        with open(file_path, "w") as file:
            file.writelines(lines)

        print_info(f"DNS server {name_server} added successfully.")
    except IOError:
        print_error(f"Error reading or writing file '{file_path}'.")


def clear_name_servers():
    file_path = "/etc/resolv.conf"

    try:
        with open(file_path, "r") as file:
            lines = file.readlines()

        # Filter out the lines containing 'nameserver'
        filtered_lines = [
            line for line in lines if not line.startswith("nameserver")]

        with open(file_path, "w") as file:
            file.writelines(filtered_lines)

        print_info("DNS servers cleared successfully.")
    except IOError:
        print_error(f"Error reading or writing file '{file_path}'.")


# def restart_name_server_services():
#     service_name = "name_server"

#     try:
#         # Check if the service exists
#         check_service = subprocess.run(
#             ["systemctl", "is-active", service_name], capture_output=True, text=True)

#         if check_service.returncode == 0:
#             # Restart the name server service
#             result = subprocess.run(
#                 ["systemctl", "restart", service_name], capture_output=True, text=True)

#             if result.returncode == 0:
#                 print("Name server services restarted successfully.")
#             else:
#                 print("Failed to restart name server services.")
#                 print("Error:", result.stderr)
#         else:
#             print(f"The '{service_name}' service does not exist.")

#     except FileNotFoundError:
#         print(f"Failed to restart name server services. 'systemctl' command not found.")
#     except Exception as e:
#         print("An error occurred:", str(e))
