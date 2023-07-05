import subprocess
from Modules.Display import show
from Modules.IP import *


def display_IP_menu():
    main_menu = {
        "assign ip address to interface(temp)": assign_temporary_ip,
        "assign ip address to interface(perm)": assign_permanent_ip,
        "release dhcp ip": release_dhcp_ip,
        "set ip to dhcp": set_dhcp,
        "Back": "Exit"
    }
    show(main_menu, "IP handle menu")


def release_dhcp_ip():
    interfaces = all_interfaces()
    interfaces.append("Exit")
    interface = show_delete_menu(interfaces)
    if interface is None:
        return
    try:
        # Run the 'dhclient' command to release the DHCP IP address of the specified interface
        subprocess.run(['sudo', 'dhclient', '-r', interface], check=True)
        print("DHCP IP address released successfully.")
    except subprocess.CalledProcessError as e:
        print(
            f"Error: Failed to release DHCP IP address. Return code: {e.returncode}")
        print(e.output.decode())
    except Exception as e:
        print(f"Failed to release DHCP IP address: {e}")


def set_dhcp():
    interfaces = all_interfaces()
    interfaces.append("Exit")
    interface = show_delete_menu(interfaces)
    if interface is None:
        return
    try:
        # Edit the /etc/network/interfaces file to set the interface to DHCP mode
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

        if int_index != -1 and "dhcp" in config_lines[int_index]:
            print_warning(
                f"{interface} interface is already configured with a dhcp IP.")
            return
        for line in config_lines:
            if line.startswith(f"iface {interface}"):
                new_config_lines.append(
                    " ".join(line.split(" ")[:-1].append("dhcp")))
                found_interface = True
                after_iface = True
            elif found_interface and line.startswith('address') and after_iface:
                after_iface = False
            else:
                new_config_lines.append(line)

        if not found_interface:
            new_config_lines.append(f'auto {interface}')
            new_config_lines.append(f'iface {interface} inet dhcp\n')

        with open('/etc/network/interfaces', 'w') as config_file:
            config_file.write(''.join(new_config_lines))

        print("Interface set to DHCP mode successfully.")
    except Exception as e:
        print(f"Failed to set interface to DHCP mode: {e}")
