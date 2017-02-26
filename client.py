#!/usr/bin/env python
import socket
import os
import sys

if os.name == "posix"
    IP_ADDR = '10.42.0.52'
elif os.name == "nt":   # Windows
    IP_ADDR = "192.168.137.181"
    # For Windows Machines, must enable IPv4 Ping Response in Advanded Firewall Settings
    #IP_ADDR = '127.0.0.1'
    #IP_ADDR = 'localhost'
    #IP_ADDR = '10.214.152.157'
else:
    print "Unsupported operating system."
    sys.exit(1)

TCP_PORT = 50525
BUFFER_SIZE = 1024
MESSAGE = "Hello, World!"

# Asks the user for an integer using the sting in prompt,
#   checks to see if it is an integer in the specified range
#   and prompts the user again if not
def get_int(prompt, min_val, max_val):
    while True:
        num = raw_input(prompt)

        try:
            num = int(num)
            if num > max_val or num < min_val:
                print "Error: input not within range."
        except ValueError:
            print "Error: input must be an integer."
        return num

if __name__ == "__main__":
    # Open up a socket to the Pi
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP_ADDR, TCP_PORT))
    s.send(MESSAGE)

    # Ask the user for input
    while True:
        n1 = get_int("Please input parameter 1 (integer): ")
        n2 = get_int("Please input parameter 2 (integer): ")
        n3 = get_int("Please input parameter 3 (integer): ")
        n4 = get_int("Please input parameter 4 (integer): ")

        s.send("command:%d %d %d %d" % (n1, n2, n3, n4))
        print "Command Sent!"

    #data = s.recv(BUFFER_SIZE)
    #s.close()

    print "received data:", data
