#!/usr/bin/env python

import socket

# For Windows Machines, must enable IPv4 Ping Response in Advanced Firewall Settings
 
# TCP_IP = '127.0.0.1'
#TCP_IP = 'localhost'
TCP_PORT = 50525 # pick something above 1024 as those are system reserved
BUFFER_SIZE = 20  # Normally 1024, but we want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.bind((TCP_IP, TCP_PORT))
s.bind(('',TCP_PORT))
s.listen(1)

conn, addr = s.accept()
print 'Connection address:', addr
while 1:
    data = conn.recv(BUFFER_SIZE)
    if not data: break
    print "received data:", data
    conn.send(data)  # echo
conn.close()
