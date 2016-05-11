"""
read state from flame sensor using callback functions

"""
import RPi.GPIO as GPIO
import time

flamePin = 15 # D0 connected to D15
flameInvPin = 16 # A0 connected to D16

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(flamePin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def eventFlameSensor(e):
	print("Flame detected!")
	print(e)

GPIO.add_event_detect(flamePin, GPIO.RISING, bouncetime = 200, callback = eventFlameSensor)

while(True):
	time.sleep(0.1)