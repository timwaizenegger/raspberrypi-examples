"""
read state from button using callback functions

"""
import RPi.GPIO as GPIO
import time

trackPin = 27 # button connected to D26/D27

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(trackPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def eventTrack(e):
	print("Tracked!")
	while(GPIO.input(e) == GPIO.HIGH): # waits until signal is off
		pass

GPIO.add_event_detect(trackPin, GPIO.RISING, bouncetime = 200, callback = eventTrack)

while(True):
	time.sleep(0.1)