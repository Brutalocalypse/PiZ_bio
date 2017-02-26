# Check if SPI is enabled
	# ls /dev/*spi*
	# should respond with /dev/spidev0.0 /dev/spidev0.1

# SPI comms
# CE0 - GPIO 8
# CE1 - GPIO 7
# MOSI - GPIO 10
# MISO - GPIO 9
# SCLK - GPIO 11

import RPi.GPIO as GPIO
import time
import sys

# variables
CLKpin = 11
MISOpin = 9
MOSIpin = 10
CSpin = 0


SPIchannel = 0 # SPI Channel (CE0)
SPIspeed = 2457600 # Clock Speed in Hz
	# ADC AD7705B Datasheet - fCLKIN = 2.4576 MHz 

# setup GPIO - may need to run with root privileges
GPIO.setmode(GPIO.BCM) # Uses GPIO numbering
print("SPI Setup")

def setupSPIpins(CLKpin, MISOpin, MOSIpin, CSpin)
	# set all but MISO as output
	GPIO.setup(CLKpin, GPIO.OUT)
	GPIO.setup(MISOpin, GPIO.IN)
	GPIO.setup(MOSIpin, GPIO.OUT)
	GPIO.setup(CSpin, GPIO.OUT)

def readADC(CLKpin, MISOpin, MOSIpin, CSpin):
	# CS (Chip Select) pin is Active Low, recommended by datasheet to just
		# hardwire to ground
	# start to read
	# GPIO.output(CSpin, GPIO.LOW) # needed if not hardwired to GND
	GPIO.output(CLKpin, SPIspeed)

	# read Comms Register 0x0000 1000
	read_command = 0x08

	sendBits(read_command,5, CLKpin, MOSIpin)

	adcValue = recvBits(12, CLKpin, MISOpin)

	return adcValue

# example code from github
def sendBits(data, numBits, CLKpin, MOSIpin):
	# sends 1 Byte of data or less
	data <<= (8 - numBits)

	for bit in range(numBits):
		# set RPi's output bit high or low depending on hgihest bit of data field
		if data & ox80:
			GPIO.output(MOSIpin, GPIO.HIGH)
		else:
			GPIO.output(MOSIpin, GPIO.LOW)

		# Advance data to the next bit
		data <<= 1

		# Pulse the clock pin HIGH then immediately LOW
		GPIO.output(CLKpin, GPIO.HIGH)
		GPIO.output(CLKpin, GPIO.LOW)

def recvBits(numBits, CLKpin, MISOpin):
	# gets arbitrary number of bits
	retVal = 0

	for bit in range(numBits)
		# Pulse clock pin
		GPIO.output(CLKpin, GPIO.HIGH)
		gpio.output(CLKpin, GPIO.LOW)

		# Read 1 data bit in
		if GPIO.input(MISOpin):
			retVal |= 0x1

		# Advance input to next bit
		retVal <<= 1
	# Divide by two to drop the NULL bit
	return (retVal/2)



# AD7705B ADC chip
	# comms register 8 bit
	# data register 16 bit


# read 16bit data register between AIN1+ and AIN1- 0x0011 1000
sendData = chr(56)
	# chr turns 0-255 value into ASCII character

# read 8bit comms register 0x0000 1000
sendData = chr(8)
# read comms with channel 2+ and 2-
sendData = chr(9)
# read clock register 0x0010 1000
sendData = chr(40)
# write to clock register 0x0010 0000 500Hz update rate clock settings 0x0000 0111 	
	# sendData = str(32,7) ?
	# sendData = str(chr(32)7)
		# chr(32) = ?? not printable
# read 8bit setup register 0x0001 1000
sendData = chr(24)
