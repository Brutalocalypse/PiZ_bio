# import wiringpi library to get pwm duty cycle range of 1-20xx for
    # 0-900mV at 1mV steps control

print("hello and welcome")

print("importing libraries")

import wiringpi
    # help(wiringpi) to see functions and options

Range = 1024 # range of 0-1023 integers, 1024 appears to do nothing

DutyCalc = 777 # from 0 to 1024
    
DutyCycle = DutyCalc*100/Range
# Freq = base clock / (divisor x range)
# Base Clock = 19.2MHz
Divisor = 16 # divisor for PWM
Frequency = 19200000/(Divisor*Range)
    #Freq of 18MHz (Divisor of 1) was unstable or too high for multimeter
print("Range set to %i units" %Range)
print("DutyCalc set to %i of %i" %(DutyCalc,Range))
print("DutyCycle set to %i Percent" %DutyCycle)
print("Divisor set to %i" %Divisor)
print("Frequency set to %i Hz" %Frequency)

# Hardware setup
    # using BCM GPIO NUMBERS
wiringpi.wiringPiSetupGpio() # must run with root privileges!
wiringpi.pinMode(18,2) # x = 2 declares alt function, pwm only works on GPIO port 18
wiringpi.pullUpDnControl(24, wiringpi.PUD_DOWN) # PUD_OFF allows to float
        # PUD_DOWN enables internal pull down resistor, pulling to GND
        # PUD_UP enables internal pull up resistor, pulling to 3.3V

wiringpi.pinMode(24,0) # x = 0 sets pin to input
    # according to GPIO PADS CONTROL2 PDF...
    # maximum low level voltage = 0.8V
    # minimum high level voltage = 1.3V

# set PWM Mode
    # balanced (default, varies frequency with duty cycle for even pulses)
    # mark-space mode (traditional)
wiringpi.pwmSetMode(wiringpi.PWM_MODE_MS)
wiringpi.pwmSetRange(Range) # sets the range register for the PWM. Default is 1024.
wiringpi.pwmSetClock(Divisor) # sets divisor for the PWM clock
wiringpi.pwmWrite(18,DutyCalc) # duty cycle between 0 and 1024. 0 = off, 1024 = fully on

# GPIO pins support 0v-3.3v
Volts = 3.3*DutyCalc/Range
#Sensor = 0.9*DutyCalc/Range
print("Pin 18 is set to %g Volts" %Volts)
#print("Past the Op Amp, sensor voltage calculates to %g Volts" %Sensor)
prompt = raw_input("please proceed, press ENTER ")
# attempt to insert pause so pin voltage is read correctly
    # forum suggests GPIO library can only read at 1MHz max
        # tested at above and below 1MHz, misreading still occurs about
            # 1 out of 10 trials
# the sampling period is variable and will not be accurate for such
    # an attempt without implementing an interrupt
            
pin24 = wiringpi.digitalRead(24) # Reads voltage as a 1 or 0
print("%i volts" %pin24)
print("reading input pin 24")
if pin24 == 1: # Logic HIGH
    print("Pin 24 reads as %i volt, therefore it is HIGH" %pin24)
else:
    print("Pin 24 reads as %i volts, therefore it is LOW" %pin24)
    


