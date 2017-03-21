print("hello and welcome")

print("importing libraries")

import sys
import os
import wiringpi
import time
import subprocess
import spidev

# Our owm code
from sftp import upload_file
    
REG_CMM = 0x0 #communication register 8 bit
REG_SETUP = 0x1 #setup register 8 bit
REG_CLOCK = 0x2 #clock register 8 bit
REG_DATA = 0x3 #data register 16 bit, contains conversion result
REG_TEST = 0x4 #test register 8 bit, POR 0x0
REG_NOP = 0x5 #no operation
REG_OFFSET = 0x6 #offset register 24 bit
REG_GAIN = 0x7 # gain register 24 bit

#channel selection for AD7706 (for AD7705 use the first two channel definitions)
#CH1 CH0
CHN_AIN1 = 0x0 #AIN1; calibration register pair 0
CHN_AIN2 = 0x1 #AIN2; calibration register pair 1
#CHN_COMM = 0x2 #common; calibration register pair 0
#CHN_AIN3 = 0x3 #AIN3; calibration register pair 2

#output update rate
#CLK FS1 FS0
UPDATE_RATE_20 = 0x0 # 20 Hz
UPDATE_RATE_25 = 0x1 # 25 Hz - Min for BioSensor project
UPDATE_RATE_100 = 0x2 # 100 Hz
UPDATE_RATE_200 = 0x3 # 200 Hz
UPDATE_RATE_50 = 0x4 # 50 Hz
UPDATE_RATE_60 = 0x5 # 60 Hz
UPDATE_RATE_250 = 0x6 # 250 Hz
UPDATE_RATE_500 = 0x7 # 500 Hz

#operating mode options
#MD1 MD0
MODE_NORMAL = 0x0 #normal mode
MODE_SELF_CAL = 0x1 #self-calibration
MODE_ZERO_SCALE_CAL = 0x2 #zero-scale system calibration, POR 0x1F4000, set FSYNC high before calibration, FSYNC low after calibration
MODE_FULL_SCALE_CAL = 0x3 #full-scale system calibration, POR 0x5761AB, set FSYNC high before calibration, FSYNC low after calibration

#gain setting
GAIN_1 = 0x0
GAIN_2 = 0x1
GAIN_4 = 0x2
GAIN_8 = 0x3
GAIN_16 = 0x4
GAIN_32 = 0x5
GAIN_64 = 0x6
GAIN_128 = 0x7

UNIPOLAR = 0x0
BIPOLAR = 0x1

CLK_DIV_0 = 0x0
CLK_DIV_1 = 0x1
CLK_DIV_2 = 0x2

MODE = 0b11 #SPI_CPHA | SPI_CPOL
BITS = 8
SPEED = 100000 # changed to 100MHz after adding Capacitors to circuit as 50kHz was no longer working
# SPEED = 50000 # Normal operational freq = 50kHz, AD7705 lists 2.4576MHz as spec
	# 1MHz and 500kHz were too fast	
	






class AD770X():
	def __init__(self,bus=0,device=0) :        
		self.spi = spidev.SpiDev()
		self.spi.open(bus, device)        
		self.spi.max_speed_hz = SPEED
		self.spi.mode = 0b11
		self.spi.bits_per_word = BITS        
		self.reset()

	def initChannel(self,channel,clkDivider=CLK_DIV_1,polarity=BIPOLAR,gain=GAIN_1,updRate=UPDATE_RATE_500) : #CLK_DIV=1 appears to work best
		self.setNextOperation(REG_CLOCK, channel, 0)
		self.writeClockRegister(0, clkDivider, updRate) #CLKDIS first argument, disabling bit (set to 1) boosts DRDY speed but data is unreliable

		self.setNextOperation(REG_SETUP, channel, 0)
		self.writeSetupRegister(MODE_SELF_CAL, gain, polarity, 0, 0)

		while not self.dataReady(channel) :
			pass

	def setNextOperation(self,reg,channel,readWrite) :
		r = reg << 4 | readWrite << 3 | channel
		self.spi.xfer([r])

	'''
	Clock Register
		7		6		5		4		3		2		1		0
	ZERO(0) ZERO(0) ZERO(0) CLKDIS(0) CLKDIV(0) CLK(1) FS1(0) FS0(1)

	CLKDIS: master clock disable bit
	CLKDIV: clock divider bit
	'''
	def writeClockRegister(self,CLKDIS,CLKDIV,outputUpdateRate) :
		r = CLKDIS << 4 | CLKDIV << 3 | outputUpdateRate

		r &= ~(1 << 2); # clear CLK
		self.spi.xfer([r])

	'''
	Setup Register
		7		6		5		4		3		2		1		0
	MD10) MD0(0) G2(0) G1(0) G0(0) B/U(0) BUF(0) FSYNC(1)
	'''
	def writeSetupRegister(self,operationMode,gain,unipolar,buffered,fsync) :
		r = operationMode << 6 | gain << 3 | unipolar << 2 | buffered << 1 | fsync
		self.spi.xfer([r])

	def readADResult(self) :
		b1 = self.spi.xfer([0x0])[0]
		b2 = self.spi.xfer([0x0])[0]

		r = int(b1 << 8 | b2)

		return r

	def readADResultRaw(self,channel) :
		while not self.dataReady(channel) :
			pass
		self.setNextOperation(REG_DATA, channel, 1)

		return self.readADResult()

	def readVoltage(self,channel,vref,factor=1) :    
		return float(self.readADResultRaw(channel)) / 65536.0 * vref * factor

	def dataReady(self,channel) :
		self.setNextOperation(REG_CMM, channel, 1)
		b1 = self.spi.xfer([0x0])[0]
		return (b1 & 0x80) == 0x0 # True = 0 Logic LOW

	def reset(self) :                        
		for i in range(100) :
			self.spi.xfer([0xff])        

def open_csv(sample_num):
	csv_fname = "adc_test_%s.csv" % (sample_num)
	#if os.path.exists("./%s" % csv_fname):
	#	print "Warning: test CSV already exists. HANDLE THIS JORDAN. Not overwriting."
	#	sys.exit(1)
	#else:
	csv_file = open("./%s" % csv_fname, "w")
	csv_file.write("iteration, input voltage, adc voltage, adc current\n")
	print "CSV file opened: %s" % csv_file
	return csv_fname,csv_file
			
def main(args):
	import time
	ad7705 = AD770X()    
	ad7705.initChannel(CHN_AIN1)
	
	user_input = sys.argv
	start = float(user_input[1])
	high = float(user_input[2])
	low = float(user_input[3])
	end = float(user_input[4])

	print("user has typed in: %s" %user_input)
	print("test starts at %.3f volts" %start)
	print("test high is %.3f volts" %high)
	print("test low is %.3f volts" %low)
	print("test end at %.3f volts" %end)

	# TODO: add in the sample number
	csv_fname, test_csv = open_csv(1)
	
	# Range = 2048 # sets the range of the duty cycle, 2^n bits
		# Over a voltage range of 0-900mV, this grants 0.44mV steps.
	Range = 1024 # range of 0-1023 integers, 1024 appears to do nothing
		# Default is 1024
		# Don't need a higher range bc I will use the 1024 steps to control the
			# 900mV coming out of the Op Amp to get 0.88mV steps.
	DutyCalc = 221 # from 0 to 1024

	DutyCycle = DutyCalc*100/Range # from 0 to 100
	# Freq = base clock / (divisor x range)
	# Base Clock = 19.2MHz
	Divisor = 4 # divisor for PWM
	Frequency = 19200000/(Divisor*Range)
		#Freq of 18MHz (Divisor of 1) was unstable or too high for multimeter
	shunt_resistor = 1500 # 1.5kOhmn
	Vref = 0.9 # volts
	print("Range set to %i units" %Range)
	print("DutyCalc set to %i of %i" %(DutyCalc,Range))
	print("DutyCycle set to %i Percent" %DutyCycle)
	print("Divisor set to %i" %Divisor)
	print("Frequency set to %i Hz" %Frequency)

	# Hardware PWM setups

	# Elevate Privileges
	# If using BCM GPIO NUMBERS
	wiringpi.wiringPiSetupGpio() # must run with root privileges!

	wiringpi.pinMode(18,2) # X = 2 declares alt function, pwm only works on GPIO port 18
	# set PWM Mode
		# balanced (default, varies frequency with duty cycle for even pulses)
		# mark-space mode (traditional)

	wiringpi.pwmSetMode(wiringpi.PWM_MODE_MS)
	wiringpi.pwmSetRange(Range) # sets the range register for the PWM. Default is 1024.
	wiringpi.pwmSetClock(Divisor) # sets divisor for the PWM clock
	wiringpi.pwmWrite(18,DutyCalc) # duty cycle between 0 and 1024. 0 = off, 1024 = fully on

	Volts = 3.3*DutyCalc/Range
	Sensor = Vref*DutyCalc/Range
	print("Pin 18 is set to %g Volts" %Volts)
	print("Past the Op Amp, sensor voltage calculates to %g Volts" %Sensor)

	raw_input("Press [Enter] to begin test.")
	# Prep for test
	begin = int(start*1000)
	max = int(high*1000)
	min = int(low*1000)
	finish = int(end*1000)
	
	DutyCalc = (start*Range)/(Vref)# has range of Range
	print DutyCalc
	print "start %0.3f volts" %start
	# Test
	for i in range(begin, max):
		print "i is %i in loop" %i
		print "DutyCalc is %i of 1024" %DutyCalc
		DutyCalc = ((start+(i*0.001))*Range)/(Vref)# has range of Range
		voltage = DutyCalc*Vref/Range
		# pass in variable for time delay from GUI
		time.sleep(0.040)
		wiringpi.pwmWrite(18,int(DutyCalc))
		print "supplied voltage is calculated to be %0.3f volts" %voltage
		# call ADC
		#time.sleep(0.02)

		raw_value = ad7705.readADResultRaw(CHN_AIN1) 
		voltage_reading = ad7705.readVoltage(CHN_AIN1,2.5)
		print "ADC raw %s bits" % raw_value
		print "ADC voltage %s volts" % voltage_reading
		# calculate current
		#import shunt resistor value
		calc_current = voltage_reading/shunt_resistor
		print "calculated current is %s Amps" %calc_current
		print "  "
		
		# Save the test results
		test_csv.write("%d, %0.3f, %0.3f, %0.3f\n" % (i, voltage, voltage_reading, calc_current))
		
	for i in range(max, finish-1, -1):
		print "i is %i in loop" %i
		print "DutyCalc is %i of 1024" %DutyCalc
		DutyCalc = ((i*0.001)*Range)/(Vref)# has range of Range
		voltage = DutyCalc*Vref/Range
		# pass in variable for time delay from GUI
		time.sleep(0.040)
		wiringpi.pwmWrite(18,int(DutyCalc))
		print "supplied voltage is calculated to be %0.3f volts" %voltage
		# call ADC
		#time.sleep(0.02)

		raw_value = ad7705.readADResultRaw(CHN_AIN1) 
		voltage_reading = ad7705.readVoltage(CHN_AIN1,2.5)
		print "ADC raw %s bits" % raw_value
		print "ADC voltage %s volts" % voltage_reading
		# calculate current
		#import shunt resistor value
		calc_current = voltage_reading/shunt_resistor
		print "calculated current is %s Amps" %calc_current
		print "  "
		
		# Save the test results
		test_csv.write("%d, %0.3f, %0.3f, %0.3f\n" % (i, voltage, voltage_reading, calc_current))

	raw_input("Press [Enter] to stop PWM.")
	wiringpi.pwmWrite(18,0) # duty cycle between 0 and 1024. 0 = off, 1024 = fully on
	test_csv.close()
	upload_file(csv_fname)

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
