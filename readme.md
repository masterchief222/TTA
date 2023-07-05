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

- IP: The IP address to assign.
- interface: The network interface to assign the IP address to.

**Returns**
None
