import time

import RPi.GPIO as GPIO
import spidev


class ActorBuzzer ():
    def __init__(self, pin=27, frequency=1000, duration=100):
        self.pin = pin
        self.frequency = frequency
        self.duration = duration

        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.OUT)

    def buzz(self):
        p = GPIO.PWM(self.pin, self.frequency)
        p.start(50)
        time.sleep(float(self.duration)/1000)
        p.stop()
