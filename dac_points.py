#!/usr/bin/python

from ABE_ADCDACPi import ADCDACPi
import time
import RPi.GPIO as GPIO

"""
================================================
ABElectronics ADCDAC Pi 2-Channel ADC, 2-Channel DAC | DAC Write Demo
Version 1.0 Created 17/05/2014
Version 1.1 16/11/2014 updated code and functions to PEP8 format
run with: python demo-dacwrite.py
================================================

"""

# The ADCDAC Pi uses GPIO pin 22 to control the DAC.  
# This will need to be turned off for the DAC to operate correctly.

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(22, GPIO.OUT)
GPIO.output(22, False)

adcdac = ADCDACPi(1) # create an instance of the ADCDAC Pi with a DAC gain set to 1
startV_flag = 1
maxV_flag = 1

# set voltage to X volts
start = float(raw_input("Enter a starting voltage below 0.4 volts, then press [Enter]"))
while startV_flag == 1:
	if start > 0.4:
		start = float(raw_input("Incorrect, please enter a starting voltage below 0.4 volts, then press [Enter]"))
	elif start < 0.0:
		start = float(raw_input("Incorrect, please enter a positive value, then press [Enter]")) 
	else:
		startV_flag = 0

high = float(raw_input("Enter a max voltage up to 0.4 volts, then press [Enter]"))
while maxV_flag == 1:
	if high > 0.4:
		high = float(raw_input("Incorrect, please enter a max voltage up to 0.4 volts, then press [Enter]"))
	elif high < 0.0:
		high = float(raw_input("Incorrect, please enter a positive value, then press [Enter]")) 
	else:
		maxV_flag = 0
# start test
raw_input("Press [Enter] to begin the test")
adcdac.set_dac_voltage(1, start)  # set the voltage on channel 1 to 1.5V
# set to max voltage
raw_input("press [Enter] to set DAC %0.3f volts" %high)
adcdac.set_dac_voltage(1, high)  # set the voltage on channel 1 to 1.5V
# back to start voltage
raw_input("press [Enter] to set DAC back to %0.3f volts" %start)
adcdac.set_dac_voltage(1, start)  # set the voltage on channel 1 to 1.5V
# set to Zero volts
raw_input("press [Enter] to set DAC to 0 volts")
adcdac.set_dac_voltage(1, 0)    
