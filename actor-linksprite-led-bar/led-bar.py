#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys


import RPi.GPIO as GPIO
import time




pd = 17 #DATA IN
pc = 18 #CLK IN
  
CmdMode = 0x0000  # Work on 8-bit mode
ON = 0x00ff       # 8-bit 1 data
OFF = 0x0000     # 8-bit 0 data


def isBitSet(x, n):
	return (x & n**2) != 0

def sendData(d):
	clk = True
	GPIO.output(pc,0)
	time.sleep(0.0005)
	for i in range(1,17):
		GPIO.output(pc,clk)
		GPIO.output(pd,isBitSet(d,i))
		clk = not clk
		time.sleep(0.00001)
	GPIO.output(pc,0)
	time.sleep(0.0005)
	
def latchData():
	l = False
	GPIO.output(pd,0)
	time.sleep(0.0005)
	for i in range(1,9):
		GPIO.output(pd,l)
		l = not l
	time.sleep(0.0005)	
	



def setup():
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(pd, GPIO.OUT)
	GPIO.setup(pc, GPIO.OUT)
	GPIO.output(pd,0)
	GPIO.output(pc,0)
	#sendData(CmdMode)
	for i in range(1,13):
		sendData(OFF)
	latchData()

def sendLedArray(l):
	#sendData(CmdMode)
	for i in l:
		if i:
			sendData(ON)
		else:
			sendData(OFF)
	latchData()



def pattern_countUp():
	sendLedArray([1,0,0,0,0,0,0,0,0,0,0,0])
	time.sleep(0.1)
	sendLedArray([1,1,0,0,0,0,0,0,0,0,0,0])
	time.sleep(0.1)
	sendLedArray([1,1,1,0,0,0,0,0,0,0,0,0])
	time.sleep(0.1)
	sendLedArray([1,1,1,1,0,0,0,0,0,0,0,0])
	time.sleep(0.1)
	sendLedArray([1,1,1,1,1,0,0,0,0,0,0,0])
	time.sleep(0.1)
	sendLedArray([1,1,1,1,1,1,0,0,0,0,0,0])
	time.sleep(0.1)
	sendLedArray([1,1,1,1,1,1,1,0,0,0,0,0])
	time.sleep(0.1)
	sendLedArray([1,1,1,1,1,1,1,1,0,0,0,0])
	time.sleep(0.1)
	sendLedArray([1,1,1,1,1,1,1,1,1,0,0,0])
	time.sleep(0.1)
	sendLedArray([1,1,1,1,1,1,1,1,1,1,0,0])
	
	
def pattern_Kitt():
	sendLedArray([1,0,0,0,0,0,0,0,0,0,0,0])
	time.sleep(0.1)
	sendLedArray([0,1,0,0,0,0,0,0,0,0,0,0])
	time.sleep(0.1)
	sendLedArray([0,0,1,0,0,0,0,0,0,0,0,0])
	time.sleep(0.1)
	sendLedArray([0,0,0,1,0,0,0,0,0,0,0,0])
	time.sleep(0.1)
	sendLedArray([0,0,0,0,1,0,0,0,0,0,0,0])
	time.sleep(0.1)
	sendLedArray([0,0,0,0,0,1,0,0,0,0,0,0])
	time.sleep(0.1)
	sendLedArray([0,0,0,0,0,0,1,0,0,0,0,0])
	time.sleep(0.1)
	sendLedArray([0,0,0,0,0,0,0,1,0,0,0,0])
	time.sleep(0.1)
	sendLedArray([0,0,0,0,0,0,0,0,1,0,0,0])
	time.sleep(0.1)
	sendLedArray([0,0,0,0,0,0,0,0,0,1,0,0])
	time.sleep(0.1)
	sendLedArray([0,0,0,0,0,0,0,0,1,0,0,0])
	time.sleep(0.1)
	sendLedArray([0,0,0,0,0,0,0,1,0,0,0,0])
	time.sleep(0.1)
	sendLedArray([0,0,0,0,0,0,1,0,0,0,0,0])
	time.sleep(0.1)
	sendLedArray([0,0,0,0,0,1,0,0,0,0,0,0])
	time.sleep(0.1)
	sendLedArray([0,0,0,0,1,0,0,0,0,0,0,0])
	time.sleep(0.1)
	sendLedArray([0,0,0,1,0,0,0,0,0,0,0,0])
	time.sleep(0.1)
	sendLedArray([0,0,1,0,0,0,0,0,0,0,0,0])
	time.sleep(0.1)
	sendLedArray([0,1,0,0,0,0,0,0,0,0,0,0])
	
	
	
	
	
setup()
while(True):
	#pattern_Kitt()
	pattern_countUp()
	
	
	
	
	
	
	
	
	
	
	
	

print('done.')

