# serial comms

import wiringpi


# setup serial comms
    # int serialOpen(char device, int baud)

comms = serialOpen("/dev/ttyAMA0", 115200)
    # on-board/GPIO serial port at 115200 baud rate
    # GPIO 14 UART TXD, GPIO 15 UARD RXD pins

