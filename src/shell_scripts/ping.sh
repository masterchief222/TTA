#!/bin/bash

# Check if only one argument is passed
if [ $# -ne 1 ]; then
    echo "Please provide only one argument, the IP address."
    exit 1
fi

# Retrieve the IP address from the first argument
ip_address=$1

# Ping the provided IP address and capture the result
result=$(ping -c 4 $ip_address)

# Display the ping result
echo "$result"
