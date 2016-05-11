"""
read state from obstacle avoidance sensor using callback functions

"""
import RPi.GPIO as GPIO
import time

outPin = 15 # out connected to D15
enPin = 16 # EN connected to D16

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(outPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def eventObstacleSensor(e):
	print("Obstacle found!")
	print(e)

GPIO.add_event_detect(outPin, GPIO.FALLING, bouncetime = 200, callback = eventObstacleSensor)

while(True):
	time.sleep(0.1)