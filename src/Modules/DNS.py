import socket
from Modules.Display import show_delete_menu as delete_menu
from Modules.Validation import is_valid_ip
from Menus.OthersMenu import restart_networking_service
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


def toggle_eth0_configuration():
    interface_file = "/etc/network/interfaces"

    try:
        with open(interface_file, "r") as file:
            lines = file.readlines()

        eth0_index = -1
        for i, line in enumerate(lines):
            if line.startswith("iface eth0"):
                eth0_index = i
                break

        if eth0_index != -1:
            eth0_line = lines[eth0_index]
            if "dhcp" in eth0_line:
                # Current configuration is DHCP, change to static
                lines[eth0_index] = "iface eth0 inet static\n"
            else:
                # Current configuration is static, change to DHCP
                lines[eth0_index] = "iface eth0 inet dhcp\n"

        with open(interface_file, "w") as file:
            file.writelines(lines)

        print_info("eth0 configuration toggled successfully.")
    except IOError:
        print_error(f"Error reading or writing file '{interface_file}'.")


def add_dns_permanently():
    interface_file = "/etc/network/interfaces"

    try:
        with open(interface_file, "r") as file:
            lines = file.readlines()

        eth0_index = -1
        for i, line in enumerate(lines):
            if line.startswith("iface eth0"):
                eth0_index = i
                break

        if eth0_index != -1 and "inet static" in lines[eth0_index]:
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

            dns_line_index = -1
            for i, line in enumerate(lines):
                if line.startswith("    dns-nameservers"):
                    dns_line_index = i
                    break

            if dns_line_index != -1:
                existing_line = lines[dns_line_index].strip()
                lines[dns_line_index] = existing_line + \
                    " " + name_server + "\n"
            else:
                dns_line = f"    dns-nameservers {name_server}\n"
                lines.insert(eth0_index + 1, dns_line)

            with open(interface_file, "w") as file:
                file.writelines(lines)

            print_info(
                f"DNS server {name_server} added to eth0 configuration.")
            restart_networking_service()
        else:
            print_warning(
                "Cannot add DNS permanently. eth0 interface is not configured with static IP.")
    except IOError:
        print_error(f"Error reading or writing file '{interface_file}'.")
