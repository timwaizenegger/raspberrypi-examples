import time
from datetime import datetime
from queue import Queue

import random as rd

from sensor import SensorBase

def random_bin():
    return rd.randint(0, 1)


class TemperatureSensor (SensorBase):

   def __init__(self, thread_id, notification_queue, sleeptime, pin = 27):
        super().__init__(thread_id, notification_queue, sleeptime) # python 3 syntax only
        self.pin = pin

    def _getSensorValue(self):
    	return random_bin
        '''value =  readadc(pd)
        volts = (value * 5.0)/1024.0
        temp = (volts - 0.5) * 100
        return temp'''