#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
import spidev

thumbPin1 = 0 # joystick connected to A0/A1
thumbPin2 = 1 # joystick connected to A0/A1

spi = spidev.SpiDev()
spi.open(0,0)

def readadc(adccnum):
	# read SPI data from MCP3004 chip, 4 possible adc’s (0 thru 3)
	if ((adcnum > 3) or (adcnum < 0)):
		return -1
	r = spi.xfer2([1,8 + adcnum << 4, 0])
	print(r)
	adcout = ((r[1] &3) << 8) + r[2]
	return adcout

while True:
	value = readadc(thumbPin1)
	volts = (value * 3.3) / 1024
	print("Pin 1: %4d/1023 => %5.3f V" % (value, volts))
	value = readadc(thumbPin2)
	volts = (value * 3.3) / 1024
	print("Pin 2: %4d/1023 => %5.3f V" % (value, volts))
	time.sleep(0.1)

print('done.')