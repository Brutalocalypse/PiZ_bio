#!/usr/bin/python

import sys
import os
import subprocess

from ABE_ADCDACPi import ADCDACPi
import time
import RPi.GPIO as GPIO

# custom library
from sftp import upload_file


# The ADCDAC Pi uses GPIO pin 22 to control the DAC.  
# This will need to be turned off for the DAC to operate correctly.
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(22, GPIO.OUT)
GPIO.output(22, False)

def open_csv(sample_num):
	csv_filename = "adc_test_%s.csv" %sample_num
	csv_file = open("./%s" %csv_filename, "w")
	csv_file.write("iteration, input voltage, adc voltage, adc current\n")
	print "CSV file opened: %s" %csv_file
	return csv_filename, csv_file

def main(args):
	user_input = sys.argv
	startV = float(user_input[1])
	maxV = float(user_input[2])
	# lowV = float(user_input[3])
	# endV = float(user_input[4])

	print("User has typed in : %s" %user_input)
	print("Test starts at %.3f volts" %startV)
	print("Test peaks at %.3f volts" %maxV)

	# initialize
	adcdac = ADCDACPi(1) # create an instance of the ADCDAC Pi with a DAC gain set to 1
	adcdac.set_adc_refvoltage(3.3) # powered off 3.3V GPIO rail

	# TODO: add in sample number
	csv_filename, test_csv = open_csv(1)

	# Hardware settings/references
	shunt_resistor = 10 # 10 Ohms
		# High-Side Current Monitor IC
	gain = 500
		# DAC Vref = 2.048v internal
		# ADC Vref = Vdd = 3.3v

	# start test
	raw_input("Press [Enter] to view Conditions")
	adcdac.set_dac_voltage(1, startV)  # set the voltage on channel 1
	voltage = startV
	# 1mV increments
		# init = int(startV*1000)
		# peak = int(maxV*1000)
	# 10mV increments
	init = int(startV*100)
	peak = int(maxV*100)
	count = 0
	print("START is %0.3f VOLTS" %voltage)
	print("HIGH is %0.3f VOLTS" %maxV)
	print("INIT is %0.3f UNITS" %init)
	print("PEAK is %0.3f UNITS" %peak)
	raw_input("Press [Enter] to begin the test")

	# ramp up
	for i in range (init, peak, 1):
		adcdac.set_dac_voltage(1, voltage)
		# read channel 1 in single ended mode
		voltage_reading = adcdac.read_adc_voltage(1, 0)
		#print("%0.3f counts" %i)
		# Vdrop @ shunt = voltage_reading/gain
		# Current = Vdrop/Rshunt
		calc_current = (voltage_reading/gain)/shunt_resistor
		print("%.3f volts driven, %.3f volts seen" %(voltage, voltage_reading))
		print("Calculated current is %.5f mA \n" %(calc_current*1000))
		#save test results
		count = count + 1
		test_csv.write("%d, %.3f, %.3f, %s\n" %(count, voltage, voltage_reading, calc_current))
		voltage = voltage+0.01
		time.sleep(0.040)
	# ramp down
	for i in range (peak, init-1, -1):
		adcdac.set_dac_voltage(1, voltage)
		# read channel 1 in single ended mode
		voltage_reading = adcdac.read_adc_voltage(1, 0)
		#print("%0.3f counts" %i)
		calc_current = (voltage_reading/gain)/shunt_resistor
		print("%.3f volts driven, %.3f volts seen" %(voltage, voltage_reading))
		print("Calculated current is %.5f mA \n" %(calc_current*1000))
		#save test results
		count = count + 1
		test_csv.write("%d, %.3f, %.3f, %s\n" %(count, voltage, voltage_reading, calc_current))
		voltage = voltage-0.01
		time.sleep(0.040)  

	raw_input("press [Enter] to set DAC to 0 volts")
	adcdac.set_dac_voltage(1, 0)    
	test_csv.close()
	upload_file(csv_filename)

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
