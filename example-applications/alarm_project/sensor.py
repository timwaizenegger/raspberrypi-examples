import abc
import time
from datetime import datetime
from queue import Queue

from stoppable import StoppableThread

class SensorBase (StoppableThread): # Observer pattern (observable)
    __metaclass__ = abc.ABCMeta
    
    @abc.abstractmethod
    def __init__(self, thread_id, notification_queue, sleeptime):
        super().__init__() # python 3 only
        self.__thread_id = thread_id
        self.__notification_queue = notification_queue
        self.__sleeptime = sleeptime
        
    @abc.abstractmethod
    def run(self):
        ''' reads sensor value and adds to queue '''
        while (not self.stopped()):
            value = get_sensor_value() # stub - CHANGE THIS LINE
            self.notify_observers(value)
            time.sleep(self.__sleeptime)
    
    @abc.abstractmethod
    def notify_observers(self, value):
        ''' adds value to the queue '''
        dict_ = {
            "id": self.__thread_id,
            "time": datetime.now(),
            "value": value,
        }
        self.__notification_queue.put_nowait(dict_)