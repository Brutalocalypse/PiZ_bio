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

### Pin Reference Setups
##wiringpi.wiringPiSetupGpio()
##wiringpi.wiringPiSetup()
##wiringpi.wiringPiSetupPhys()

# Port Setup
# wiringpi.pinMode(port_or_pin_number, X)
    # port_or_pin_number depends on Reference Setup
    # X defines Port Function
        # 0 = input, 1 = output, 2 = alternative function
        # in this case, alt function for GPIO pin 18 is hardware PWM

# Hardware PWM setups
print "0"
# Elevate Privileges
# If using BCM GPIO NUMBERS
wiringpi.wiringPiSetupGpio() # must run with root privileges!
print "0.5"
wiringpi.pinMode(18,2) # X = 2 declares alt function, pwm only works on GPIO port 18
# set PWM Mode
    # balanced (default, varies frequency with duty cycle for even pulses)
    # mark-space mode (traditional)
print "1"
wiringpi.pwmSetMode(wiringpi.PWM_MODE_MS)
wiringpi.pwmSetRange(Range) # sets the range register for the PWM. Default is 1024.
wiringpi.pwmSetClock(Divisor) # sets divisor for the PWM clock
wiringpi.pwmWrite(18,DutyCalc) # duty cycle between 0 and 1024. 0 = off, 1024 = fully on
print "2"
Volts = 3.3*DutyCalc/Range
Sensor = 0.9*DutyCalc/Range
print("Pin 18 is set to %g Volts" %Volts)
print("Past the Op Amp, sensor voltage calculates to %g Volts" %Sensor)

### OR, using wiringpi numbers
##wiringpi.wiringPiSetup()
##wiringpi.pinMode(1,2) # pwm only works on wiringpi pin 1
##wiringpi.pwmWrite(1,0) # duty cycle between 0 and 1024. 0 = off, 1024 = fully on  # duty 
##
### OR, using P1 header pin numbers
##wiringpi.wiringPiSetupPhys()
##wiringpi.pinMode(12,2) # pwm only works on P1 header pin 12
##wiringpi.pwmWrite(12,0) # duty cycle between 0 and 1024. 0 = off, 1024 = fully on

#stop PWM by changing pin to input or output
##wiringpi.pinMode(18,0)

