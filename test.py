#!/usr/bin/env python2.7

from mystepper import Stepper

def write(value):
	print "Write: %d" % value
	v = ''
	if value & 0x01:
		v += '1'
	else:
		v += '0'
	if value & 0x02:
		v += '1'
	else:
		v += '0'
	if value & 0x04:
		v += '1'
	else:
		v += '0'
	if value & 0x08:
		v += '1'
	else:
		v += '0'
	print v

s = Stepper(write=write, full_step=False)
s.single_step(1)
s.single_step(1)
s.single_step(1)
s.single_step(1)
s.single_step(1)
s.single_step(1)
s.single_step(1)
s.single_step(1)
