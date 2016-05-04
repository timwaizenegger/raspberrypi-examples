#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
reads position from thumb-joystick
needs spidev installed
http://www.raspberrypi-spy.co.uk/2014/08/enabling-the-spi-interface-on-the-raspberry-pi/
"""
import RPi.GPIO as GPIO
import time
import spidev

xPin = 0 # joystick x connected to A0
yPin = 1 # joystick y connected to A1

xzero = 512
yzero = 512

spi = spidev.SpiDev()
spi.open(0,0)

def readadc(adcnum):
	# read SPI data from MCP3004 chip, 4 possible adc’s (0 thru 3)
	if ((adcnum > 3) or (adcnum < 0)):
		return -1
	r = spi.xfer2([1,8 + adcnum << 4, 0])
	print(r)
	adcout = ((r[1] &3) << 8) + r[2]
	return adcout

def position(value, zerovalue):
	return value - zerovalue

while True:
	value = readadc(xPin)
	posx = position(value, xzero)
	print("x: %4d/1023 => %5d" % (value, posx))
	value = readadc(yPin)
	posy = position(value, yzero)
	print("y: %4d/1023 => %5d" % (value, posy))

	if (posx > (1023 * 3/4)):
		print("Button pressed!")
	print("")
	time.sleep(0.5)



print('done.')