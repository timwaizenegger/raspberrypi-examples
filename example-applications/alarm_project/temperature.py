import time
from datetime import datetime
from queue import Queue

import random as rd

from sensor import SensorBase

def random_temp(midvalue=30):
    return rd.randint(midvalue - 20, midvalue + 10)


class TemperatureSensor (SensorBase):

    def __init__(self, thread_id, notification_queue, sleeptime, pin = 0):
        super().__init__(thread_id, notification_queue, sleeptime) # python 3 only
        self.__thread_id = thread_id
        self.__notification_queue = notification_queue
        self.__sleeptime = sleeptime

    def run(self):
        print ("Thread %s started!" % str(self.__thread_id))
        while (not self.stopped()):
            temp = random_temp(30) # this is a stub
            self.notify_observers(temp)
            time.sleep(self.__sleeptime)
    
    def notify_observers(self, value):
        dict_ = {
            "id": self.__thread_id,
            "time": datetime.now(),
            "value": value,
        }
        self.__notification_queue.put_nowait(dict_)