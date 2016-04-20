"""
read state from buttons using callback functions

"""
import RPi.GPIO as GPIO


btnPin1 = 27
btnPin2 = 22


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(btnPin1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(btnPin2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)




def eventB1(e):
	print("Button 1 pressed")
	print(e)

def eventB2(e):
	print("Button 1 pressed")
	print(e)
	
	
	
GPIO.add_event_detect(btnPin1, GPIO.RISING, bouncetime=200, callback=eventB1)
GPIO.add_event_detect(btnPin2, GPIO.RISING, bouncetime=200, callback=eventB2)
	
	

while(True):
	time.sleep(0.1)


