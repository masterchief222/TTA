

import re
import subprocess
from Modules.Display import show_delete_menu as delete_menu
from Modules.Validation import is_valid_ip


def add_route():
    while True:
        destination_ip = input("Enter the destination IP: ").strip()
        if destination_ip.lower() == "exit":
            return
        if is_valid_ip(destination_ip):
            break
    while True:
        destination_ip_mask = input("Enter the destination IP mask: ").strip()
        try:
            if 0<int(destination_ip_mask)<=32:
                break
        except:
            print("wrong netmask try again!")


    while True:
        gateway = input("Enter the gateway IP: ").strip()
        if gateway.lower() == "exit":
            return
        if is_valid_ip(gateway):
            break

    try:
        # Execute the `ip route add` command to add the route
        subprocess.run(["ip", "route", "add", destination_ip,
                       "via", gateway], check=True)
        print("Route added successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to add route: {e}")


def enable_routing():
    try:
        # Execute the sysctl command to enable IP forwarding
        subprocess.run(["sysctl", "net.ipv4.ip_forward=1"], check=True)
        print("Routing enabled successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to enable routing: {e}")


def print_routing_policies():
    routing = get_routing_policies()
    if routing == []:
        print("no routing policy found!")
    else:
        print(routing)


def get_routing_policies():
    try:
        # Execute the `ip route` command to get the routing policies
        result = subprocess.run(
            ["ip", "route"], capture_output=True, text=True)
        output = result.stdout.strip()

        # Parse the output to extract destination IP and gateway for each route
        routing_policies = re.findall(
            r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+via\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})", output)

        return routing_policies
    except subprocess.CalledProcessError as e:
        print(f"Failed to retrieve routing policies: {e}")
        return []


def delete_route(destination_ip, gateway):
    name_servers = get_routing_policies()
    if name_servers is []:
        print("no routing policy found!")
        return
    name_servers.append("Exit")
    chosen_name_server = delete_menu(name_servers)
    if chosen_name_server is None:
        return
    try:
        # Execute the `ip route delete` command to delete the specific route
        subprocess.run(["ip", "route", "delete", destination_ip,
                       "via", gateway], check=True)
        print(
            f"Route deleted successfully: Destination IP: {destination_ip}, Gateway: {gateway}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to delete route: {e}")

# Example usage:
# Get the list of routing policies
# routing_policies = get_routing_policies()
# print("Routing Policies:")
# for destination_ip, gateway in routing_policies:
#     print(f"Destination IP: {destination_ip}, Gateway: {gateway}")
