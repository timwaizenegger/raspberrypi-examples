#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
needs spidev installed
http://www.raspberrypi-spy.co.uk/2014/08/enabling-the-spi-interface-on-the-raspberry-pi/
'''
import sys

import RPi.GPIO as GPIO
import time
import spidev

pd = 0 # S connected to A0
  
spi = spidev.SpiDev()
spi.open(0,0)
 
def readadc(adcnum):
	# read SPI data from MCP3004 chip, 4 possible adc’s (0 thru 3)
	if ((adcnum > 3) or (adcnum < 0)):
		return-1
	r = spi.xfer2([1,8+adcnum <<4,0])
	#print(r)
	adcout = ((r[1] &3) <<8)+r[2]
	return adcout

tolerance = 0.5 # degrees
value = readadc(pd)
# calibrate the formula with a termometer
lasttemp = 125.315 - 0.175529 * value # temperature formula made through Wolfram Alpha: 'linear function (0,125);(720,0);(1023,-55)', where (readvalue, temperature)
print('Temperature: %5.2fC (input: %3d)' % (lasttemp, value))
while True:
	value = readadc(pd)
	temp = 125.315 - 0.175529 * value # temperature formula
	if ((temp > lasttemp + tolerance) or (temp < lasttemp - tolerance)): # if temperature changed more than the tolerance
		print('New temperature: %5.2fC (input: %3d)' % (temp, value))
		lasttemp = temp
	time.sleep(0.1)

print('done.')