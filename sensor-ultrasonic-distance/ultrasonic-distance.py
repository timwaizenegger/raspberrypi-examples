#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys


import RPi.GPIO as GPIO
import time


ptrig = 26
pecho = 27

def setup():
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(pecho, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	GPIO.setup(ptrig, GPIO.OUT)
	GPIO.output(ptrig, 0)
		


def getValue():
	GPIO.output(ptrig, 0)
	time.sleep(0.1)
	GPIO.output(ptrig, 1)
	time.sleep(0.00001)
	GPIO.output(ptrig, 0)
	
	
	while(0 == GPIO.input(pecho)):
		start = time.time()
	while(1 == GPIO.input(pecho)):
		end = time.time()
		

	delay = (end - start) * 1000 * 1000
	time.sleep(0.1)
	distance = (delay / 58.0)
	if 2 < distance < 400: # working interval
		print("distance: %0.1f cm" % distance)


setup()
while(True):
	getValue()
print('done.')

