#!/usr/bin/env python

import socket
import os
import sys

if os.name == "posix"
    IP_ADDR = '127.0.0.1'
elif os.name == "nt":   # Windows
    IP_ADDR = "192.168.137.181"
else:
    print "Unsupported operating system."
    sys.exit(1)

TCP_PORT = 5005
BUFFER_SIZE = 1024
MESSAGE = "Hello, World!"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP_ADDR, TCP_PORT))
s.send(MESSAGE)
data = s.recv(BUFFER_SIZE)
s.close()

print "received data:", data
