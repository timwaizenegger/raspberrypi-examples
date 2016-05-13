import RPi.GPIO as GPIO
import time
import binascii as ba
import sys

recvPin = 27
bittime = 1

GPIO.setmode(GPIO.BCM)
GPIO.setup(recvPin, GPIO.IN)

while True:
	value = GPIO.input(recvPin)
	print ('Received: ' + str(value))
	time.sleep(bittime)