# Check if SPI is enabled
	# ls /dev/*spi*
	# should respond with /dev/spidev0.0 /dev/spidev0.1

# run in python2.7
	# #!python2
# run in python3 - has Byte type
	# #!python3
# SPI comms
# CE0 - GPIO 8
# CE1 - GPIO 7
# MOSI - GPIO 10
# MISO - GPIO 9
# SCLK - GPIO 11

import wiringpi
import time

delay = 0.01
SPIchannel = 0 # SPI Channel (CE0)
SPIspeed = 50000 # Clock Speed in Hz, online example for AD7705 had 50kHz
#SPIspeed = 2457600 # Clock Speed in Hz
	# ADC AD7705B Datasheet - fCLKIN = 2.4576 MHz 
# setup GPIO
wiringpi.wiringPiSetupGpio() # need to run with root privileges
print("SPI Setup")
wiringpi.wiringPiSPISetup(SPIchannel, SPIspeed)

# AD7705B ADC chip

# read 16bit data register between AIN1+ and AIN1- 0x0011 1000
#sendData = chr(56)
	# chr turns 0-255 value into ASCII character

# read 8bit comms register 0x0000 1000
#sendData = chr(8)
# read comms with channel 2+ and 2-
#sendData = chr(9)
# read clock register 0x0010 1000
#sendData = chr(40)
# write to clock register 0x0010 0000 500Hz update rate clock settings 0x0000 0111 	
	# sendData = str(32,7) ?
	# sendData = str(chr(32)7)
		# chr(32) = ?? not printable
# read 8bit setup register 0x0001 1000
#sendData = chr(24)

# Initialize ADC registers

# Check Comms Register
sendData = chr(8)
time.sleep(delay)
recvData = wiringpi.wiringPiSPIDataRW(SPIchannel, sendData)
time.sleep(delay)
print("Comms reads %s" % recvData)

# Write to Comms Register to select Clock Register 0010 0000
	# Active Analog Channels set to Ain1(+) and Ain1(-)
sendData = chr(32)
time.sleep(delay)
recvData = wiringpi.wiringPiSPIDataRW(SPIchannel, sendData)
time.sleep(delay)
print("wrote to Comms l%sl no read yet %s" % (sendData, recvData))
time.sleep(delay)

# Write to Clock Register to set update rate to 50Hz, clk freq = 2.4576MHz 0000 0100
#sendData = chr(4)
# attempt 500Hz
sendData = chr(7)
time.sleep(delay)
recvData = wiringpi.wiringPiSPIDataRW(SPIchannel, sendData)

# Write to Comms Register to select Setup Register 0001 0000
sendData = chr(16)
time.sleep(delay)
recvData = wiringpi.wiringPiSPIDataRW(SPIchannel, sendData)

# Write to Setup Register to:
	# Self-Calibrate, Gain=1, unipolar, buffer off, no filter sync 0100 0000
sendData = chr(68)
time.sleep(delay)
recvData = wiringpi.wiringPiSPIDataRW(SPIchannel, sendData)

# Wait for DRDY bit to go LOW/new word available. HIGH = completion of a read.
time.sleep(delay)

print("preloop")
time.sleep(delay)

while(True):
	# Check DRDY bit, highest bit, on Comms Register
	time.sleep(delay)
	sendData = chr(8)
	time.sleep(delay)
	recvData = wiringpi.wiringPiSPIDataRW(SPIchannel, sendData)
	time.sleep(delay)
	print("%s" % recvData)
	if sendData == "8": # DRDY 
		# read 16bit Data Register
		time.sleep(delay)
		sendData = chr(56)
		time.sleep(delay)
		recvData = wiringpi.wiringPiSPIDataRW(SPIchannel, sendData)
		time.sleep(delay)
		print("data received %s" % recvData)
	elif sendData == "128" or "136": # when DRDY bit is HIGH
		time.sleep(delay)
		print("reading..")
	# read clock register
	time.sleep(delay)
	sendData = chr(40)
	time.sleep(delay)
	recvData = wiringpi.wiringPiSPIDataRW(SPIchannel, sendData)
	time.sleep(delay)
	print("%s" % recvData)
	# read setup register
	time.sleep(delay)
	sendData = chr(24)
	time.sleep(delay)
	recvData = wiringpi.wiringPiSPIDataRW(SPIchannel, sendData)
	time.sleep(delay)
	print("%s" % recvData)
	#time.sleep(0.001)

#recvData = wiringpi.wiringPiSPIDataRW(SPIchannel, sendData)
	# recvData now holds a list [NumOfByte, recvDataStr] = [2, '\x9A\xCD']
# alternative send single byte
	# sendData = chr(42) # sends a single byte containing 42
	# recvData = wiringpi.wiringPiSPIDataRW(SPIchannel, sendData)
		# recvData now holds a list [NumOfByte, recvDataStr] = [1, '\x9A']

# other functions
	# wiringPiSPIDataRW()
	# wiringPiSPIGetFd()
		# get File Descriptor
	# wiringPiSPISetup()
	# wiringPiSPISetupMode()
		# see 3 SPI modes on wiki
