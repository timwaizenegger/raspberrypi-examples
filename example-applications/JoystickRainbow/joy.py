import RPi.GPIO as GPIO
import time
import spidev

xPin = 0 # joystick x connected to A0
yPin = 1 # joystick y connected to A1

tolerancevalue = 10
xZero = 512
yZero = 512

spi = spidev.SpiDev()
spi.open(0,0)

def readadc(adcnum):
        # read SPI data from MCP3004 chip, 4 possible adc’s (0 thru 3)
        if ((adcnum > 3) or (adcnum < 0)):
                return -1
        r = spi.xfer2([1,8 + adcnum << 4, 0])
        #print(r)
        adcout = ((r[1] &3) << 8) + r[2]
        return adcout

def position(adcnum, zerovalue):
        return readadc(adcnum) - zerovalue
#Colors setup
GPIO.setmode(GPIO.BCM)

LED_Rot = 14
LED_Gruen = 13
LED_Blau = 12

GPIO.setup(LED_Rot, GPIO.OUT)
GPIO.setup(LED_Gruen, GPIO.OUT)
GPIO.setup(LED_Blau, GPIO.OUT)

Freq = 100 #Hz


ROT = GPIO.PWM(LED_Rot, Freq)
GRUEN = GPIO.PWM(LED_Gruen, Freq)
BLAU = GPIO.PWM(LED_Blau, Freq)
ROT.start(0)
GRUEN.start(0)
BLAU.start(0)

def LED_Farbe(Rot, Gruen,Blau):
    ROT.ChangeDutyCycle(Rot)
    GRUEN.ChangeDutyCycle(Gruen)
    BLAU.ChangeDutyCycle(Blau)

select = 0
change = 0
red = 0
green = 0
blue = 0
increment = 10
c = 0
rainbow = [(100,0,0),(100,50,0),(100,100,0),(50,100,0),(0,100,0),(0,100,50),(0,100,100),(0$
try:
    while True:
        xPos = position(xPin, xZero)
        yPos = position(yPin, yZero)


        if (xPos > (500)) and (abs(yPos) < tolerancevalue): #change value
            change = change + 1
            print "change value"
        elif (xPos > 100) and (abs(yPos) < tolerancevalue) and select != 1: 
            c = 0
            print "Selected RED"
            print (xPos,yPos)
        elif (yPos > 100)and (abs(xPos) < tolerancevalue) and select != 2:
            select = 2
            c = 0
            print "Selected GREEN"
        elif (yPos < -100) and (abs(xPos) < tolerancevalue) and select != 3:
            select = 3
            c = 0
            print "Selected BLUE"
        elif (xPos < -100)and (abs(yPos) < tolerancevalue) and select != 4: 
            select = 4
            print "Selected RAINBOW"


       while change > 0:
            print select
            if select == 1 and change == 1:
                red = red + increment
                if red > 100:
                    red = 0
            elif select == 2 and change == 1:
                green = green + increment
                if green > 100:
                    green = 0
            elif select == 3 and change == 1:
                blue = blue + increment
                if blue > 100:
                    blue = 0
            elif select == 4 and change == 1:
                LED_Farbe(rainbow[c][0],rainbow[c][1],rainbow[c][2])
                c = c + 1
                if c > 11:
                    c = 0
                red = rainbow[c][0]
                green = rainbow[c][1]
                blue = rainbow[c][2]
                time.sleep(0.5)

            print (red,green,blue, increment)
            LED_Farbe(red,green,blue)
            time.sleep(0.5)
            change = 0

except KeyboardInterrupt:
        GPIO.cleanup()


