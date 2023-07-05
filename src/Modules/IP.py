import subprocess
from Menus.OthersMenu import all_interfaces, restart_networking_service
from Modules.Validation import is_valid_ip
from Modules.Display import show_delete_menu
from colorama import Fore, Style


def print_info(message):
    print(f"{Fore.BLUE}{message}{Style.RESET_ALL}")


def print_warning(message):
    print(f"{Fore.YELLOW}{message}{Style.RESET_ALL}")


def print_error(message):
    print(f"{Fore.RED}{message}{Style.RESET_ALL}")


def assign_temporary_ip():
    interfaces = all_interfaces()
    interfaces.append("Exit")
    ip = ""
    while True:
        ip = input("Enter the IP to assign: ").strip()
        if ip.lower() == "exit":
            return
        validation = is_valid_ip(ip)
        if validation:
            break
    choosen = show_delete_menu(interfaces)
    if choosen is None:
        return
    command = ['sudo', 'ip', 'addr', 'add', ip, 'dev', choosen]
    try:
        subprocess.run(command, check=True)
        print_info("IP address assigned successfully.")
    except subprocess.CalledProcessError as e:
        print_error(
            f"Error: Failed to assign IP temporarily. Return code: {e.returncode}")
        print(e.output.decode())


def assign_permanent_ip():
    interfaces = all_interfaces()
    interfaces.append("Exit")
    ip_address = ""
    while True:
        ip_address = input("Enter the IP to assign: ").strip()
        if ip_address.lower() == "exit":
            return
        validation = is_valid_ip(ip_address)
        if validation:
            break
    interface = show_delete_menu(interfaces)
    if interface is None:
        return
    # Read the current network configuration file
    with open('/etc/network/interfaces', 'r') as config_file:
        config_lines = config_file.readlines()
    new_config_lines = []
    found_interface = False
    after_iface = False
    int_index = -1
    for i, line in enumerate(config_lines):
        if line.startswith(f"iface {interface}"):
            int_index = i
            break

    if not (int_index != -1 and "inet static" in config_lines[int_index]):
        print_warning(
            f"Cannot assign IP. {interface} interface is not configured with a static IP.")
        return

    # Process each line in the configuration file
    for line in config_lines:
        line = line.strip()
        # Check if the line defines the interface we want to modify
        if line.startswith('iface') and line.split()[1] == interface:
            new_config_lines.append(line)  # Append the 'iface' line
            new_config_lines.append(f'    address {ip_address}')
            found_interface = True
            after_iface = True
        elif found_interface and line.startswith('address') and after_iface:
            after_iface = False
        else:
            new_config_lines.append(line)

    # If the specified interface was not found in the configuration file, add it with the new IP
    if not found_interface:
        new_config_lines.append(f'auto {interface}')
        new_config_lines.append(f'iface {interface} inet static')
        new_config_lines.append(f'    address {ip_address}')

    # Write the updated configuration back to the file
    with open('/etc/network/interfaces', 'w') as config_file:
        config_file.write('\n'.join(new_config_lines))

    restart_networking_service()
    print_info("IP address assigned permanently and networking service restarted.")
