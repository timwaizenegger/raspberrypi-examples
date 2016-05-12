import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(14, GPIO.OUT) #red
GPIO.output(14,1)
GPIO.setup(13, GPIO.OUT) #green
GPIO.output(13,1)
GPIO.setup(12, GPIO.OUT) #blue
GPIO.output(12,1)

try:
    while(True):
        request = raw_input("RGB-->")
        if (len(request) == 3):
            GPIO.output(14, int(request[0]))
            GPIO.output(13, int(request[1]))
            GPIO.output(12, int(request[2]))
except KeyboardInterrupt:
    GPIO.cleanup()
