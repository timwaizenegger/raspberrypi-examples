import RPi.GPIO as GPIO
import time
import binascii as ba
import sys

sendPin = 16
bittime = 1

GPIO.setmode(GPIO.BCM)
GPIO.setup(sendPin, GPIO.OUT)

while True:
	GPIO.output(sendPin, GPIO.HIGH)
	time.sleep(bittime)
	GPIO.output(sendPin, GPIO.LOW)
	time.sleep(bittime)