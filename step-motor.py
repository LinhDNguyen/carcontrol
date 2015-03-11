#/usr/bin/env python2.7

import RPi.GPIO as GPIO
from time import sleep
from stepper import Stepper

# Numbering by GPIO number, not header pin numberring
GPIO.setmode(GPIO.BCM)

# Use GPIO03 J8-05 |
#     GPIO04 J8-07 |
#     GPIO17 J8-11 |
#     GPIO27 J8-13 | to control stepper motor

# Config pins
step_pins = [3, 4, 17, 27]

for pin in step_pins:
	GPIO.setup(pin, GPIO.OUT, initial=0)
	GPIO.output(pin, 0)

def write(value):
	if value & 0x01:
		GPIO.output(step_pins[0], 1)
	else:
		GPIO.output(step_pins[0], 0)
	if value & 0x02:
		GPIO.output(step_pins[1], 1)
	else:
		GPIO.output(step_pins[1], 0)
	if value & 0x04:
		GPIO.output(step_pins[2], 1)
	else:
		GPIO.output(step_pins[2], 0)
	if value & 0x08:
		GPIO.output(step_pins[3], 1)
	else:
		GPIO.output(step_pins[3], 0)


s = Stepper(write=write, full_step=False)
s.single_step(1)
s.step_to(s.position + 2000)
s.step_relative(2000)
sleep(1)
s.single_step(-1)
s.step_to(s.position - 2000)
s.step_relative(-2000)
sleep(1)
# Clean
GPIO.cleanup()
