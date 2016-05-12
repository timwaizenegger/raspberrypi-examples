"""
read state from touch sensor using callback functions

"""
import RPi.GPIO as GPIO
import time

touchPin = 26 # D0 connected to D26
touchInvPin = 27 # A0 connected to D27

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(touchPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def eventTouchSensor(e):
	print("Sensor touched!")
	print(e)

GPIO.add_event_detect(touchPin, GPIO.RISING, bouncetime = 200, callback = eventTouchSensor)

while(True):
	time.sleep(0.1)