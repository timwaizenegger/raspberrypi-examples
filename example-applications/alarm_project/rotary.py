import time
from datetime import datetime
from queue import Queue

import random as rd

from sensor import SensorBase

def random_bin():
    return rd.randint(0, 1)


class RotarySensor (SensorBase):

    def __init__(self, thread_id, notification_queue, sleeptime, aPin = 1, bPin = 1):
        super().__init__(thread_id, notification_queue, sleeptime) # python 3 only
        self.__thread_id = thread_id
        self.__notification_queue = notification_queue
        self.__sleeptime = sleeptime
        # GPIO.add_event_detect(aPin, GPIO.BOTH, bouncetime = 200, callback = __eventRotary)

    def run(self):
        print ("Thread %s started!" % str(self.__thread_id))
        while (not self.stopped()):
            time.sleep(self.__sleeptime)

    def __eventRotary(self):
        #if (GPIO.input(bPin) != GPIO.input(aPin)): # a changed before b
        #    self.notify_observers(0) # Rotating clockwise
        #else:
        #    self.notify_observers(1) # Rotating counterclockwise
        return
    
    def notify_observers(self, value):
        dict_ = {
            "id": self.__thread_id,
            "time": datetime.now(),
            "value": value,
        }
        self.__notification_queue.put_nowait(dict_)