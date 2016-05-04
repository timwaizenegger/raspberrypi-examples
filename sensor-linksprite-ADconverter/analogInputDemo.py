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
 
 
def buildBar(num):
	b = int((float(num)*20.0)/1024)
	s = b*"#" + (20-b)*"_"
	return s


while True:
	v0=readadc(0)
	v1=readadc(1)
	v2=readadc(2)
	v3=readadc(3)
	
	print("%s(%i) \t %s(%i) \t %s(%i) \t %s(%i)" % (buildBar(v0), v0, buildBar(v1), v1, buildBar(v2), v2, buildBar(v3), v3))
	
	
	#volts=(value*3.3)/1024
	#print("%4d/1023 => %5.3f V" % (value, volts))
	
	time.sleep(0.05)


print('done.')

