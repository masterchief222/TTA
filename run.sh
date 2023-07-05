#!/bin/bash

# Check if running as root
if [[ $EUID -ne 0 ]]; then
    echo "This script must be run as root."
    exit 1
fi

# Update apt package manager
apt update

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "Docker is not installed. Installing Docker..."

    # Install dependencies
    apt install -y curl

    # Install Docker
    curl -fsSL https://get.docker.com -o get-docker.sh
    sh get-docker.sh

    # Start Docker service
    systemctl start docker

    # Add current user to the docker group to run Docker without sudo
    usermod -aG docker $SUDO_USER

    echo "Docker has been installed and started."
else
    echo "Docker is already installed."
fi

# Create Docker image in current directory
docker build -t tta_project:1.0 .

# Run Docker image with -it argument
docker run -it tta_project:1.0
