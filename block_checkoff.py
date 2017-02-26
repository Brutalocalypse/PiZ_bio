# import wiringpi library to get pwm duty cycle range of 1-20xx for
    # 0-900mV at 1mV steps control

print("program initialization")

print("importing libraries")

import wiringpi
    # help(wiringpi) to see functions and options

Range = 1024 # range of 0-1023 integers, 1024 appears to do nothing

##prompt = input("select a DutyCalc ")
##print("you typed", prompt)
##DutyCalc = prompt
DutyCalc = 205 # from 0 to 1024
    
DutyCycle = DutyCalc*100/Range # from 0 to 100
# Freq = base clock / (divisor x range)
# Base Clock = 19.2 MHz
Divisor = 2 # divisor for PWM
	# = 1 unstable (5Hz on Oscope)
	# = 2 -> Freq = 9.375 MHz
	# = 8 -> Freq = 2.343 MHz
	# = 9 -> Freq = 2.083 MHz
	# = 10 -> 1.875 MHz (circuit parts capped at 2MHz Frequency)
Frequency = 19200000/(Divisor*Range)
    #Freq of 18MHz (Divisor of 1) was unstable
##print("Range set to %i units" %Range)
##print("DutyCalc set to %i of %i" %(DutyCalc,Range))
print("DutyCycle set to %i Percent" %DutyCycle)
##print("Divisor set to %i" %Divisor)
print("Frequency set to %i Hz" %Frequency)

# Hardware setup
    # using BCM GPIO NUMBERS
wiringpi.wiringPiSetupGpio() # must run with root privileges!
wiringpi.pinMode(18, 2) # x = 2 declares alt function, pwm only works on GPIO port 18

# set PWM Mode
    # balanced (default, varies frequency with duty cycle for even pulses)
	# not wanted for general engineering applications
    # mark-space mode (traditional, up and down cycle matches duty cycle)
wiringpi.pwmSetMode(wiringpi.PWM_MODE_MS)
wiringpi.pwmSetRange(Range) # sets the range register for the PWM. Default is 1024.
wiringpi.pwmSetClock(Divisor) # sets divisor for the PWM clock
wiringpi.pwmWrite(18, DutyCalc) # duty cycle between 0 and 1024. 0 = off, 1024 = fully on

# GPIO pins support 0v-3.3v
Volts = 3.3*DutyCalc/Range
#Sensor = 0.9*DutyCalc/Range
print("Pin 18 is set to %g Volts" %Volts)

# Show 1.875 MHz frequency
prompt = raw_input ("Frequency will be now set to 1.875 MHz. Press Enter to proceed.")
Divisor = 10
Frequency = 19200000/(Divisor*Range)
print("Frequency now set to %i Hz" %Frequency)
wiringpi.pwmSetClock(Divisor)

# 100% Duty Cycle test
prompt = raw_input ("Duty Cycle will be now set to 100%. Press Enter to proceed.")
DutyCalc = 1024
DutyCycle = DutyCalc*100/Range
print("DutyCycle set to %i Percent" %DutyCycle)
wiringpi.pwmWrite(18, DutyCalc)

prompt = raw_input ("Duty Cycle will be now set to 0%. Press Enter to proceed.")
DutyCalc = 0
DutyCycle = DutyCalc*100/Range
print("DutyCycle set to %i Percent" %DutyCycle)
wiringpi.pwmWrite(18, DutyCalc)

prompt = raw_input ("Stop PWM by pressing Enter")
# turn off PWM
wiringpi.pwmWrite(18, 0)

print("terminating C drive")
