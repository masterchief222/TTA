from Modules.Display import show
from Modules.Route import add_route, delete_route, enable_routing, print_routing_policies


def display_route_menu():
    main_menu = {
        "add route": add_route,
        "delete route": delete_route,
        "enable routing": enable_routing,
        "get all routing routing": print_routing_policies,
        "Back": "Exit"
    }
    show(main_menu, "route menu")
