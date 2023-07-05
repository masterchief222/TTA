# Use the official Debian 10 as the base image
FROM python:buster

# Set the working directory inside the container
WORKDIR /app

RUN apt-get update && apt-get install iputils-ping dnsutils systemd nftables sudo systemd-sysv dbus -y

# Set the TERM environment variable
ENV TERM=xterm

# Set systemd as the init system
ENV container docker

# Copy the Python script and any other required files to the working directory
COPY src/ .

# Copy the requirements.txt file to the working directory
COPY src/requirements.txt .

# Install the Python dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Define the command to run your Python script
CMD ["sudo","python3", "main.py"]
