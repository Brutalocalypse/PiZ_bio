# i2c interface comms

print("Loading WiringPi library")

import wiringpi
import smbus
import time

bus = smbus.SMBus(0)
address = 0x60 # result from running i2cdetect -y 0
pin_base = 65
i2c_addr = 0x20

wiringpi.wiringPiSetupGpio() # need to run with root privileges
print("PP")
wiringpi.wiringPiI2CSetup(pin_base,i2c_addr)

def write(value):
    bus.write_byte_data(address, 0, value)
    return -1
def read(value):
    var = bus.read_byte_data(address, 1)
    return var

# print("Detecting I2C devices on bus")

# run i2cdetect -y 1 in terminal to detect devices on bus
print ("run i2cdetect -y 1 in terminal to detect devices on bus")

# default baud rate is 100kbps


# read and write to registers
# i2cget, i2cset, i2cdump
