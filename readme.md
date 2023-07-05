# taktour andaz linux project

Brief description of the project.

## How to Run

### Method 1: Clone from Git, Build Locally, and Run

1. Clone the project repository from Git:\
   git clone https://github.com/masterchief222/TTA.git

2. Navigate to the project directory:\
   cd <project_directory>

3. Build the Docker image locally:\
   docker build -t tta_project:1.0 .

4. Run the Docker container:\
   docker run tta_project:1.0

### Method 2: Pull Image from Docker Hub and Run

1. Pull the Docker image from Docker Hub:

2. Run the Docker container:

# document

- [IP](#IP.py)
- [DNS](#DNS.py)
- [Validation](#Validation.py)
- [Hostname](#Hostname.py)
- [Route](#Route.py)
- [Menu](#Menus)
- [Display](#Display.py)

# IP.py

## assign_temporary_ip

**Purpose:**
This function allows the user to assign a temporary IP address to a network interface.

**Command:**

```shell
sudo ip addr add [IP] dev [interface]
```

**Parameters**

- IP: The IP address to assign.
- interface: The network interface to assign the IP address to.

**Returns**
None

## assign_permanent_ip

**Purpose**
This function allows the user to assign a permanent IP address to a network interface by modifying the network configuration file.

**Command**
change the content of /etc/network/interfaces

**Parameters**

- **IP**: The IP address to assign.
- **interface**: The network interface to assign the IP address to.

**Returns**
None

# DNS.py

## get_current_name_servers

**Purpose:**
This function retrieves the current name servers from the DNS configuration file.

**Command:**

read the content of /etc/resolv.conf

**Returns**
List of current name servers.

## delete_name_server

**Purpose:**
This function deletes a name server from the DNS configuration file.

**Command:**

delete configuration in /etc/resolv.conf

**Returns**
None

## add_name_server

**Purpose:**
This function adds a name server to the DNS configuration file.

**Command:**

add configuration in /etc/resolv.conf

**Returns**
None

## clear_name_servers

**Purpose:**
This function clears all name servers from the DNS configuration file.

**Command:**

delete configuration in /etc/resolv.conf

**Returns**
None

## toggle_eth0_configuration

**Purpose:**
This function toggles the configuration of the **'eth0'** interface between static and DHCP.

**Command:**

change the content of /etc/network/interfaces

**Returns**
None

## add_dns_permanently

**Purpose:**
This function adds a DNS server permanently to the **'eth0'** configuration.

**Command:**

change the content of /etc/network/interfaces

**Returns**
None

# Validation.py

## is_valid_ip

**Purpose:**
This function validates whether an IP address is valid or not.

**Command:**

use `regex` library to achive this

**Parameters**

- **ip**: The IP address to validate.

**Returns**
True | False

## is_valid_hostname

**Purpose**
This function validates whether a hostname is valid or not.

**Command**

use `regex` library to achive this

**Parameters**

- **hostname**: The hostname to validate.

**Returns**
True | False

# Hostname.py

## change_hostname

**Purpose:**
This function allows the user to change the hostname of the system.

**Command:**

change the content of /etc/hostname

**Parameters**

- **new_hostname**: The hostname to be set.

**Returns**
None

## get_current_hostname

**Purpose**
This function retrieves the current hostname of the system.

**Command**

read the content of /etc/hostname

**Returns**
The current hostname as a string.

## get_hostname

**Purpose**
This function retrieves and displays the current hostname of the system.

**Command**

```shell
hostname
```

**Returns**
None

# Route.py

## add_route

**Purpose:**
This function allows the user to add a new route to the system's routing table.

**Command:**

```shell
ip route add [destination_ip]\\[mask] via [gateway]
```

**Parameters**

- **destination_ip**: destination ip address of incompings packet.
- **mask**: destination ip address mask of incompings packet.
- **gateway**: ip gateway to forward incomping packet.

**Returns**
None

## enable_routing

**Purpose**
This function enables IP forwarding to allow the system to act as a router.

**Command**

```shell
sysctl net.ipv4.ip_forward=1
```

**Returns**
None

## print_routing_policies

**Purpose**
This function retrieves and displays the routing policies in the system's routing table (for using in display dictionary).

**Command**

call get_routing_policies() function.

**Returns**
None

## get_routing_policies

**Purpose**
This function retrieves the routing policies in the system's routing table.

**Command**

call get_routing_policies() function.

**Returns**
A list of tuples containing the destination IP and gateway for each route.

## delete_route

**Purpose:**
This function allows the user to delete a specific route from the system's routing table.

**Command:**

```shell
ip route delete [destination_ip] via [gateway]
```

**Parameters**

- **destination_ip**: destination ip address of incompings packet.
- **mask**: destination ip address mask of incompings packet.
- **gateway**: ip gateway to forward incomping packet.

**Returns**
None

# Menus

## [X]Menus

**Purpose:**
contain the dictionary for x menu and call the show().

**Parameters**

- a **dictionary** that has **command name** in the key and **function** for value.

# Display.py

This module provides functions for displaying menus and handling user input.

## Functions

### `display_menu(selected_row: int, menu_options: dict) -> None`

Displays the menu options with the selected row highlighted.

- `selected_row` (int): The index of the selected row.
- `menu_options` (dict): A dictionary mapping menu item names to their corresponding functions.

### `perform_task(task: str, menu_options: dict) -> Union[str, None]`

Executes the selected task.

- `task` (str): The name of the task to be performed.
- `menu_options` (dict): A dictionary mapping menu item names to their corresponding functions.

Returns:

- str or None: If the task is not a "Exit" task, returns the input prompt. Otherwise, returns None to exit the current menu level.

### `show(menu: dict, menu_name: str = "") -> None`

Displays the menu and handles user input.

- `menu` (dict): A dictionary mapping menu item names to their corresponding functions.
- `menu_name` (str, optional): The name of the menu. Defaults to an empty string.

### `show_delete_menu(menu: list) -> Union[str, None]`

Displays the delete menu and handles user input for deletion confirmation.

- `menu` (list): A list of menu item names.

Returns:

- str or None: Returns the selected menu item if confirmed for deletion, None otherwise.

### `display_delete_menu(selected_row: int, menu_options: list) -> None`

Displays the delete menu options with the selected row highlighted.

- `selected_row` (int): The index of the selected row.
- `menu_options` (list): A list of menu item names.

## Dependencies

- `readchar`: Reads a character from the console.
- `colorama`: Allows the use of ANSI escape sequences to display colored text.
