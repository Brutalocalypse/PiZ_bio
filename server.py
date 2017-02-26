#!/usr/bin/env python

import socket
import os
import sys

# For Windows Machines, must enable IPv4 Ping Response in Advanced Firewall Settings

# TCP_IP = '127.0.0.1'
#TCP_IP = 'localhost'
TCP_PORT = 50525 # pick something above 1024 as those are system reserved
BUFFER_SIZE = 20  # Normally 1024, but we want fast response

# Pulls data on byte at a time from a socket until a command
#   delimiter is received.
# Delimiter must be a single character, if supplied
def get_msg(s, delimiter_char='\n'):
    msg = ""
    try:
        c = s.recv(1)
        while delimiter_char not in c:
            #print "Received: ", c,
            msg += c
            c = s.recv(1)
    except KeyboardInterrupt:
        print "Received stop signal. Terminating."
        return None

    return msg

def perform_command(command, args):
    if command == "pwm":
        print "Received 'pwm' command. Starting pwm"
        os.system("./pwm.py %s" % args)
    else:
        print "Received unidentified command: '%s'. Terminating" % command
        sys.exit(1)



if __name__ == "__main__":
    print "PiZ Server online!"

    # Open up a passive socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('',TCP_PORT))
    s.listen(1)

    conn, addr = s.accept()
    print 'Connection address:', addr
    while True:
        print "About to wait for next message."
        msg = get_msg(conn)
        if msg == None:
            break

        print "Received message:", msg
        command = msg.split(":")
        perform_command(command[0], command[1])

        #conn.send(msg)  # echo
    print "Releasing sockets."
    conn.close()
    s.close()
