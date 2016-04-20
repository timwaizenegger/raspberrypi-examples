#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys


import RPi.GPIO as GPIO
import time
import spidev

import tm1637


pd = 2 #Analog in (on linker-base ADC)
  

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
 
Display = tm1637.TM1637(23,24,tm1637.BRIGHT_TYPICAL)

while True:
	value=readadc(pd)
	volts=(value*3.3)/1024
	#print("%4d/1023 => %5.3f V" % (value, volts))
	Display.ShowInt(value)
	time.sleep(0.1)


print('done.')

