#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys


import RPi.GPIO as GPIO
import time


ptrig = 17
pecho = 18

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
	
	
	GPIO.wait_for_edge(pecho,GPIO.RISING)
	start = time.time()
	GPIO.wait_for_edge(pecho,GPIO.FALLING)
	delay = (time.time() - start) * 1000 * 1000
	time.sleep(0.1)
	print("distance: %0.1f cm" % (delay / 58.0))


setup()
while(True):
	getValue()
print('done.')

