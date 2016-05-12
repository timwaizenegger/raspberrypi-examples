"""
read state from vibration sensor using callback functions

"""
import RPi.GPIO as GPIO
import time

vibPin = 15 # S connected to D15

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(vibPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

lastState = GPIO.input(vibPin)

def eventVibration(e):
	print("Vibrated!")

GPIO.add_event_detect(vibPin, GPIO.RISING, bouncetime = 200, callback = eventVibration)

while(True):
	time.sleep(0.1)
	#print(GPIO.input(vibPin))