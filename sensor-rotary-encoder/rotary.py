"""
read state from rotary encoder using callback function

"""
import RPi.GPIO as GPIO
import time

aPin = 26  # CLK pin
bPin = 15  # DT pin
swPin = 16 # SW pin 

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(aPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(bPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(swPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def eventRotary(e):
	if (GPIO.input(bPin) != GPIO.input(aPin)): # a changed before b
		print('Rotating clockwise')
		#position -= 1
	else:
		print('Rotating counterclockwise')
		#position += 1

GPIO.add_event_detect(aPin, GPIO.BOTH, bouncetime = 200, callback = eventRotary)

position = 0
while(True):
	time.sleep(0.1)