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



pd = 0 #Analog in (on linker-base ADC)
  

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


while True:
	value=readadc(pd)
	volts=(value*3.3)/1024
	print("%4d/1023 => %5.3f V" % (value, volts))
	#temp = (((value * 1000) - 500)/10)
	#print temp
	time.sleep(0.1)


print('done.')

