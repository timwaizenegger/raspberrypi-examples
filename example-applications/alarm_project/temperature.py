import time
from datetime import datetime
from queue import Queue
import random as rd

import RPi.GPIO as GPIO
import spidev

from sensor import SensorBase
from sensor import readadc

def random_temp(midvalue=60):
    return rd.randint(midvalue - 20, midvalue + 10)


class TemperatureSensor (SensorBase):

    def __init__(self, thread_id, notification_queue, sleeptime, pin = 0):
        super().__init__(thread_id, notification_queue, sleeptime) # python 3 syntax only
        self.pin = pin
        self.spi = spidev.SpiDev()
        self.spi.open(0,0)

    def _getSensorValue(self):
        #return random_temp()
        value =  readadc(self.pin)
        volts = (value * 5.0) / 1024.0
        temp = (volts - 0.5) * 100
        return temp