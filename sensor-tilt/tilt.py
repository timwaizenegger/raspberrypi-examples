"""
read state from tilt switch sensor using callback functions

"""
import RPi.GPIO as GPIO
import time

tiltPin = 15 # S connected to D15

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(tiltPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

lastState = GPIO.input(tiltPin)

def eventTiltSwitch(e):
	print("Tilted!")

GPIO.add_event_detect(tiltPin, GPIO.BOTH, bouncetime = 200, callback = eventTiltSwitch)

while(True):
	time.sleep(0.1)
	#print(GPIO.input(tiltPin))