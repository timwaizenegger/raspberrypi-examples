import threading
import signal
import sys
import time
import operator
from queue import Queue
from datetime import datetime

from temperature import TemperatureSensor
from flame import FlameSensor
from rotary import RotarySensor
from observer import Observer
from buzzer import ActorBuzzer


threads = []
sleeptime = 0.1
temperature_threshold = 60

def signal_handler(signal, frame):
    print ("Closing all threads...")
    for t in threads:
        if t.isAlive():
            t.stop()
    '''for t in threads:
        if t.isAlive():
            t.join()'''
    print ("Finished.")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

queue_ = Queue(100)
obs = Observer(queue_)

temp_sensor = TemperatureSensor("temp", queue_, sleeptime, pin = 0)
flame_sensor = FlameSensor("flame", queue_, sleeptime, pin = 27)
#rotary_sensor = RotarySensor(thread_id="rotary", queue_, sleeptime)

buzzer = ActorBuzzer(15)

def tempAlarm(*args, **kwargs):
    print ("HIGH TEMPERATURE: %s" % str(kwargs["value"]))
    buzzer.buzz()
obs.addSensor("temp", temperature_threshold, operator.ge, tempAlarm)

def flameAlarm(*args, **kwargs):
    print ("ON FIRE!!!")
    buzzer.buzz()
obs.addSensor("flame", 0,  operator.eq, flameAlarm)

#obs.addSensor(thread_id="rotary_sensor", -1, action) # -1 for any positive value (0 and 1 as binary)

threads.append(obs)
threads.append(temp_sensor)
threads.append(flame_sensor)
#threads.append(rotary_sensor)

for t in threads:
    t.start()

while (True):
    pass
