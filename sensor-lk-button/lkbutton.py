"""
read state from button using callback functions

"""
import RPi.GPIO as GPIO
import time

lkbuttonPin = 27 # button connected to D26/D27

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(lkbuttonPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def eventLKButton(e):
	print("LK-Button pressed")
	print(e)

GPIO.add_event_detect(lkbuttonPin, GPIO.RISING, bouncetime = 200, callback = eventLKButton)

while(True):
	time.sleep(0.1)