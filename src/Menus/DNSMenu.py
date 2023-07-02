
import sys
from Modules.Display import show
from Modules.Phase1 import add_name_server, clear_name_servers, delete_name_server, get_current_name_servers


def display_DNS_menu():
    main_menu = {
        "Get current name servers of the OS": get_current_name_servers,
        "Delete a name server": delete_name_server,
        "Add a name server in a chosen position": add_name_server,
        "Clear all name servers": clear_name_servers,
        # "restart DNS services": restart_name_server_services,
        "Back": "Exit"
    }
    show(main_menu, "DNS handle menu")
