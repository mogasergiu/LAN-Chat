#!/usr/bin/python3

import socket as sck
import sys

maxBuffSize = 1024

def confirm(sock):
    '''Prompts the user to confirm his input'''
    while True:
        sock.sendall(bytes("Confirm? [y/n]", "utf-8"))
        confirmation = sock.recv(maxBuffSize).decode("utf-8")[0]
        if confirmation == 'y' or confirmation == 'Y':
            return 1

        elif confirmation == 'n' or confirmation == 'N':
            return 0

        else:
            continue

def scanOpenPorts(ip = 0, connType = sck.SOCK_STREAM):
    '''If it finds an available socket, it returns it'''
    openPorts = []

    if ip == 0:
        print("Invalid use! Exiting program...")
        sys.exit()

    print("Scanning for open ports...")

    try:
        for port in range(1, 65535):
            s = sck.socket(sck.AF_INET, connType)
            sck.setdefaulttimeout(1)
            result = s.connect_ex((ip, port))
            if result == 0:
                print("Port {} is open.".format(port))
                openPorts.append(port)
    except KeyboardInterrupt:
        print("Exiting program...")
        sys.exit()

    except sck.error:
        print("Could not connect to host...\nExiting program...")
        sys.exit()

    return openPorts
