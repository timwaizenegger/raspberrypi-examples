"""
this script uses XAutomation, i.e. the xte command. install it with:
>sudo apt-get install xautomation

"""
import RPi.GPIO as GPIO
import subprocess
import time


btnPin1 = 27
btnPin2 = 22


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(btnPin1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(btnPin2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)




def sendKey(key):
	subprocess.Popen(['xte', 'key %s' % (key)])


def eventRight(e):
	print("Right")
	print(e)
	sendKey("Right")

def eventLeft(e):
	print("Left")
	print(e)
	sendKey("Left")
	
	
	
GPIO.add_event_detect(btnPin1, GPIO.RISING, bouncetime=200, callback=eventRight)
GPIO.add_event_detect(btnPin2, GPIO.RISING, bouncetime=200, callback=eventLeft)
	
	

while(True):
	time.sleep(0.1)


