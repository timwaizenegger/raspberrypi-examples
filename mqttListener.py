#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import paho.mqtt.client as mqtt
import sys, json
import subprocess


mq_org = "xx"
mq_type = "xx"
mq_id = "xx"
mq_authtoken = "xx"


topic = "iot-2/cmd/media_output/fmt/json"

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
	print("Connected with result code "+str(rc))
	
	#client.publish(topic="iot-2/evt/switch_speakers/fmt/json", payload=msg, qos=1, retain=False)
	#client.disconnect()
	

	# Subscribing in on_connect() means that if we lose the connection and
	# reconnect then subscriptions will be renewed.
	client.subscribe(topic)
	
	
	
	
	

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
	print("message: ")
	print(msg.topic+" - "+str(msg.payload))
	if (msg.topic == topic):
		pl = json.loads(msg.payload.decode(encoding='utf-8', errors='strict'))
		print(json.dumps(pl))
		if(pl['media_output'] in ('tv', 'dt', 'bm')):
			print("switching output")
			subprocess.Popen(["/home/tim/bin/enigma_display-control.sh", pl['media_output']])
			subprocess.Popen(["/home/tim/bin/enigma_sound-control.sh", pl['media_output']])
		

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

