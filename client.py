#!/usr/bin/env python
import socket

# For Windows Machines, must enable IPv4 Ping Response in Advanded Firewall Settings

#TCP_IP = '127.0.0.1'
#TCP_IP = 'localhost'
TCP_IP = '10.214.152.157'
TCP_PORT = 50525
BUFFER_SIZE = 1024
MESSAGE = "Hello, World!"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE)
data = s.recv(BUFFER_SIZE)
s.close()

print "received data:", data
