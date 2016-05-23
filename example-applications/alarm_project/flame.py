import time
from datetime import datetime
from queue import Queue
import random as rd

import RPi.GPIO as GPIO
import spidev

from sensor import SensorBase

def random_bin():
    return rd.randint(0, 1)


class FlameSensor (SensorBase):

    def __init__(self, thread_id, notification_queue, sleeptime, pin = 27):
        super().__init__(thread_id, notification_queue, sleeptime) # python 3 syntax only
        self.pin = pin
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    def _getSensorValue(self):
        #return random_bin()
        return GPIO.input(self.pin)
        
