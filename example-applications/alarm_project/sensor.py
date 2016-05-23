import abc
import time
from datetime import datetime
from queue import Queue

import spidev

from stoppable import StoppableThread

def readadc(adcnum):
    spi = spidev.SpiDev()
    spi.open(0,0)
    # read SPI data from MCP3004 chip, 4 possible adc’s (0 thru 3)
    if ((adcnum > 3) or (adcnum < 0)):
        return-1
    r = spi.xfer2([1,8+adcnum <<4,0])
    #print(r)
    adcout = ((r[1] &3) <<8)+r[2]
    return adcout


class SensorBase (StoppableThread): # Observer pattern (observable)
    __metaclass__ = abc.ABCMeta
    
    def __init__(self, thread_id, notification_queue, sleeptime):
        super().__init__() # python 3 only
        self.__thread_id = thread_id
        self.__notification_queue = notification_queue
        self.__sleeptime = sleeptime
        
    def run(self):
        ''' reads sensor value and adds to queue '''
        while (not self.stopped()):
            value = self._getSensorValue()
            self.notify_observers(value)
            time.sleep(self.__sleeptime)
    
    @abc.abstractmethod
    def _getSensorValue(self):
        # CODE TO GET SENSOR VALUE
        return

    def notify_observers(self, value):
        ''' adds value to the queue '''
        dict_ = {
            "id": self.__thread_id,
            "time": datetime.now(),
            "value": value,
        }
        self.__notification_queue.put_nowait(dict_)