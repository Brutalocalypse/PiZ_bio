print("hello and welcome")

print("importing libraries")

import sys
import wiringpi
import time
    # help(wiringpi) to see functions and options
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
Sensor = 0.4*DutyCalc/Range
print("Pin 18 is set to %g Volts" %Volts)
print("Past the Op Amp, sensor voltage calculates to %g Volts" %Sensor)

raw_input("Press [Enter] to begin test.")
# Prep for test
begin = int(start*1000)
finish = int(end*1000)
DutyCalc = (start*Range)/(0.4)# has range of Range
print DutyCalc
print "start %0.3f volts" %start
# Test
for i in range(begin, finish+1):
	print "i %i in loop" %i
	print "DutyCalc %i of 1024" %DutyCalc
	DutyCalc = ((start+(i*0.001))*Range)/(0.4)# has range of Range
	voltage = DutyCalc*0.4/Range
	# pass in variable for time delay from GUI
	time.sleep(0.040)
	wiringpi.pwmWrite(18,int(DutyCalc))
	print "voltage is %0.3f" %voltage

raw_input("Press [Enter] to stop PWM.")
wiringpi.pwmWrite(18,0) # duty cycle between 0 and 1024. 0 = off, 1024 = fully on
