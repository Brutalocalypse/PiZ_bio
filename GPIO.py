# import wiringpi library to get pwm duty cycle range of 1-20xx for
    # 0-900mV at 1mV steps control
# wiringpi library
# wiringpi 2 library
# gpio library
print("hello and welcome")

print("importing libraries")

# import wiringpi2 as wiringpi
    #wiringpi2 has been deprecated
# import RPi.GPIO as GPIO
import wiringpi
    # help(wiringpi) to see functions and options

# variables
pin_num = 21
HIGH = 1
LOW = 0

# Pin Reference Setups with GPIO numbers
wiringpi.wiringPiSetupGpio() # must run with root privileges!
	# OR, using wiringpi numbers
		#wiringpi.wiringPiSetup()
	# OR, using P1 header pin numbers
		#wiringpi.wiringPiSetupPhys()

# wiringpi.pinMode(int pin_number, int mode)
	# 0 = Input, 1 = Output, 2 = Alt Function
# wiringpi.digitalWrite(int pin, int value)
	# Writes HIGH or LOW based on 1 or 0 given
		# HIGH can be as low as 1.3V and a LOW can be as high as 0.8V
		# according to GPIO-Pads-Control2 pdf over the BCM2835 Broadcom chip

# int = wiringpi.digitalRead(int pin)
	# reads	a HIGH (1) or LOW(0), technically a 3.3V or 0V though a

# set output pin to demo 3.3V HIGH
wiringpi.pinMode(pin_num, 1)
wiringpi.digitalWrite(pin_num, HIGH)
print ("pin %i set HIGH = 3.3V, next will be setting the pin LOW" % pin_num)
prompt = raw_input ("please proceed by pressing Enter")
# set output pin to demo 0V LOW
wiringpi.digitalWrite(pin_num, LOW)
print ("pin %i set LOW = 0V" % pin_num)
prompt = raw_input ("please proceed by pressing Enter")
print ("Goodbye")
