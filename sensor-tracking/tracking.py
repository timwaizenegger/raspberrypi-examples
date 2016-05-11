#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys


import RPi.GPIO as GPIO
import time

trackingPin = 27

def setup():
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(trackingPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def eventTracking(e):
	print("Tracking triggered!")
	print(e)

#GPIO.add_event_detect(trackingPin, GPIO.RISING, bouncetime = 200, callback = eventTracking)

setup()

while(True):
	GPIO.input(trackingPin)
	time.sleep(0.1)