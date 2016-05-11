"""
write state for relay

"""
import RPi.GPIO as GPIO
import time

relayPin = 27 # relay connected to D27

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(relayPin, GPIO.OUT)

while(True):
	GPIO.output(relayPin, GPIO.HIGH)
	time.sleep(1)
	GPIO.output(relayPin, GPIO.LOW)
	time.sleep(1)