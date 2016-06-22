import operator

from stoppable import StoppableThread

class Observer (StoppableThread): # Observer pattern (observer)

    def __init__(self, notification_queue, thread_id="observer"):
        super(Observer, self).__init__()
        self.__notification_queue = notification_queue
        self.__thread_id = thread_id
        self.sensors = {}

    def run(self):
        print ("Thread %s started!" % str(self.__thread_id))
        while (not self.stopped()):
            recv = self.__notification_queue.get(block=True)
            print (recv)
            id_ = recv["id"]
            if id_ in self.sensors:
                sensor = self.sensors[id_]

                if (sensor["operator"](recv["value"], sensor["threshold"])):
                    sensor["action"](value = recv["value"], recv = recv)

    def addSensor(self, sensor_id, threshold, operator=operator.ge, action=None):
        self.sensors[sensor_id] = {
            "threshold": threshold,
            "operator": operator,
            "action": action,
        }

def defaultAction():
    raise NotImplementedError("Needs an action attributed to the sensor.")