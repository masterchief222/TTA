import re
import socket


def is_valid_ip(ip):
    # Regular expression pattern for IP address validation
    pattern = r'^((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)\.?\b){4}$'

    if not re.match(pattern, ip):
        print("--ip is incorrect--")
        return False

    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        print("--ip is unreachable--")
        return False


def is_valid_hostname(hostname):
    # Regular expression pattern for hostname validation
    pattern = r'^[a-zA-Z0-9.-]+$'

    if not re.match(pattern, hostname):
        return False

    if len(hostname) > 255:
        return False

    if hostname[-1] == ".":
        hostname = hostname[:-1]

    if any(len(label) > 63 for label in hostname.split(".")):
        return False

    return True
