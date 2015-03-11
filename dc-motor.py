#/usr/bin/env python2.7

import RPi.GPIO as GPIO
from time import sleep

# Numbering by GPIO number, not header pin numberring
GPIO.setmode(GPIO.BCM)

# Use GPIO12 (PWM0) J8-32 to control speed of motor A
#	  GPIO13 (PWM1) J8-33 to control speed of motor B
# Use GPIO14 J8-8   |
#     GPIO15 J8-10  | to control direction of motor A
# Use GPIO18 J8-12  |
#     GPIO23 J8-16  | to control direction of motor B

# Config pins
# Motor A
GPIO.setup(12, GPIO.OUT)
GPIO.setup(14, GPIO.OUT, initial=0)
GPIO.setup(15, GPIO.OUT, initial=0)
motorA = GPIO.PWM(12, 1000)
# Motor B
GPIO.setup(13, GPIO.OUT)
GPIO.setup(18, GPIO.OUT, initial=0)
GPIO.setup(23, GPIO.OUT, initial=0)
motorB = GPIO.PWM(13, 1000)

# Motor A, fullspeed, right
motorA.start(100)
GPIO.output(14, 1)
GPIO.output(15, 0)


sleep(3)