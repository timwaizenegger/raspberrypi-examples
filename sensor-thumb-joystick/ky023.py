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
swPin = 27 # sw connected to D27

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(swPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

tolerancevalue = 10
xZero = 512
yZero = 512

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

def position(adcnum, zerovalue):
	return readadc(adcnum) - zerovalue


def eventSWButton(e):
	print("SW from joystick pressed")
	print(e)

# using the callback is optional
GPIO.add_event_detect(swPin, GPIO.FALLING, bouncetime = 200, callback = eventSWButton)

while True:
	xPos = position(xPin, xZero)
	yPos = position(yPin, yZero)

	# in case you don't want to use the callback
	#if (GPIO.input(swPin) == 0):
	#	print("Button pressed!")
	
	if (abs(xPos) < tolerancevalue):
		print("Not moving in X.")
	elif (xPos > 0):
		print("Moving ahead.")
		print("X intensity: %5d" % abs(xPos))
	else:
		print("Moving backwards.")
		print("X intensity: %5d" % abs(xPos))

	if (abs(yPos) < tolerancevalue):
		print("Not moving in Y.")
	elif (yPos > 0):
		print("Moving left.")
		print("Y intensity: %5d" % abs(yPos))
	else:
		print("Moving right.")
		print("Y intensity: %5d" % abs(yPos))
		
	print("")
	time.sleep(0.5)

print('done.')