import time

import RPi.GPIO as GPIO
import spidev


class ActorBuzzer ():
    def __init__(pin=27, frequency=50, duration=10):
        self.pin = pin
        self.frequency = frequency
        self.duration = duration

        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    def buzz():
        p = GPIO.PWM(self.pin, self.frequency)
        p.start(50)
        time.sleep(float(self.duration)/1000)
        p.stop()
