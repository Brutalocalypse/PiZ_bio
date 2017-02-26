# saves data collected into cvs format file
    # save data
    # set GPIO pin as input

import RPi.GPIO as GPIO
import sys
import csv
import time

# use GPIO pin numbering
GPIO.setmode(GPIO.BOARD)

# pin setup for INPUT
##GPIO.setup(pin_number, GPIO.IN)
    # return either a 0/LOW or 1/HIGH
    # LOW is 0v - about .4v
    # HIGH IS 3.3v - about 1.8v

# pin setup for OUTPUT
##GPIO.setup(pin_number, GPIO.OUT)

# multiple pin setup
##pin_list = [11,12]
##GPIO.setup(pin_list, GPIO.IN)

# GPIO software PWM
##pwm = GPIO.PWM(pin_number, frequency)
##pwm.start(duty_cycle)
##pwm.ChangeDutyCycle(duty_cycle)
##pwm.ChangeFrequency(frequency)
##pwm.stop()

# writing csv file
##with open('data.csv','ab') as csvfile:
##    spamwriter = csv.writer(csvfile, dialect = 'excel')
##    spamwriter.writenow([])

# cleanup
GPIO.cleanup()
