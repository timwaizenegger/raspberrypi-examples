#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

import RPi.GPIO as GPIO
import time




pd = 27 #DATA PIN
  



# freq in Hz
def buzz(duration, freq):
	GPIO.output(pd, 0)
	for i in range(1,duration):
		GPIO.output(pd, 1)
		time.sleep(0.001)
		GPIO.output(pd, 0)
		time.sleep(1.0/freq)

	GPIO.output(pd, 0)



def setup():
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(pd, GPIO.OUT)
	GPIO.output(pd, 0)



def buzzPwm(duration, freq):
	p = GPIO.PWM(pd,freq)
	p.start(50)
	time.sleep(float(duration)/1000)
	p.stop()
	













setup()
while(True):
	for i in range(100,10000,100):
		buzz(10,i)
	#for i in reversed(range(100,10000,100)):
	#	buzz(10,i)	
	
	


	
	

print('done.')

