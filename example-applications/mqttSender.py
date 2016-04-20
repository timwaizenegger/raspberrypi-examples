#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import paho.mqtt.client as mqtt
import sys

mq_org = "xx"
mq_type = "xx"
mq_id = "xx"
mq_authtoken = "xx"


messages = dict()
# [(topic, message), ...]
messages['dt'] = [('iot-2/evt/switch_speakers/fmt/json', '{"channel_a":1, "channel_b":0}'),
					('iot-2/evt/switch_power1/fmt/json', '{"channel_a":0}'),
					('iot-2/evt/sendir/fmt/string', 'rcvr_pwr_toggle')]
messages['tv'] = [('iot-2/evt/switch_speakers/fmt/json', '{"channel_a":0, "channel_b":1}'),
					('iot-2/evt/switch_power1/fmt/json', '{"channel_a":1}'),
					('iot-2/evt/sendir/fmt/string', 'rcvr_pwr_toggle')]
messages['bm'] = [('iot-2/evt/switch_speakers/fmt/json', '{"channel_a":1, "channel_b":1}'),
					('iot-2/evt/switch_power1/fmt/json', '{"channel_a":0}'),
					('iot-2/evt/sendir/fmt/string', 'rcvr_pwr_toggle')]
					
message = []

if ('tv' == sys.argv[1]):
	message = messages['tv']
elif('dt' == sys.argv[1]):
	message = messages['dt']
elif('bm' == sys.argv[1]):
	message = messages['bm']


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
	print("Connected with result code "+str(rc))
	for m in message:
		client.publish(topic=m[0], payload=m[1], qos=1, retain=False)
	client.disconnect()
	

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    #client.subscribe("$SYS/#")
    
    
    

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
	print("message: ")
	print(msg.topic+" "+str(msg.payload))

mq_clientId = "d:"+mq_org+":"+mq_type+":"+mq_id

client = mqtt.Client(client_id=mq_clientId, clean_session=True, userdata=None, protocol=mqtt.MQTTv311)
client.username_pw_set(username="use-token-auth", password=mq_authtoken)

client.on_connect = on_connect
client.on_message = on_message

client.connect("qa64ya.messaging.internetofthings.ibmcloud.com", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
#m:publish("iot-2/evt/t1/fmt/string","hello",0,0, function(conn) print("sent") end) 

