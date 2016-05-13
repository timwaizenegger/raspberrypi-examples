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

analogPin = 0 # A0 connected to A0
digitalPin = 27 # D0 connected to A1 - not needed

spi = spidev.SpiDev()
spi.open(0,0)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(digitalPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def readadc(adcnum):
	# read SPI data from MCP3004 chip, 4 possible adc’s (0 thru 3)
	if ((adcnum > 3) or (adcnum < 0)):
		return-1
	r = spi.xfer2([1,8+adcnum <<4,0])
	#print(r)
	adcout = ((r[1] &3) <<8)+r[2]
	return adcout

tolerance = 0.5 # degrees
value = readadc(analogPin)
# calibrate the formula with a termometer
lasttemp = 125.315 - 0.175529 * value # formula made through Wolfram Alpha: 'linear function (0,125);(720,0);(1023,-55)', where (readvalue, temperature)
print('Temperature: %5.2f' % lasttemp)
while True:
	value = readadc(analogPin)
	digital = GPIO.input(digitalPin)
	temp = 125.315 - 0.175529 * value
	if ((temp > lasttemp + tolerance) or (temp < lasttemp - tolerance)): # if temperature changed more than the tolerance
		print('New temperature: %5.2fC (input: a: %3d, d: %3d)' % (temp, value, digital))
		lasttemp = temp
	time.sleep(0.1)

print('done.')