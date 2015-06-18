#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import json

import paho.mqtt.client as mqtt

import RPi.GPIO as GPIO
import time
import spidev

"""
mqtt connection data
"""

mq_org = ""
mq_type = "RPi"
mq_id = "sensor1"
mq_authtoken = ""
mq_topic = "iot-2/evt/sensordata/fmt/json"

mq_clientId = "d:"+mq_org+":"+mq_type+":"+mq_id
client = mqtt.Client(client_id=mq_clientId, clean_session=True, userdata=None, protocol=mqtt.MQTTv311)
client.username_pw_set(username="use-token-auth", password=mq_authtoken)


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
	print("Connected with result code "+str(rc))
	isConnected = True
	
	#client.disconnect()


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
	print("message: ")
	print(msg.topic+" "+str(msg.payload))


def sendMessage(msg):
	client.publish(topic=mq_topic, payload=msg, qos=1, retain=False)



client.on_connect = on_connect
client.on_message = on_message

client.connect("qa64ya.messaging.internetofthings.ibmcloud.com", 1883, 60)
client.loop_start()


"""
Analog in (on linker-base ADC)
0: JP1 connector,
2: JP2 connector
"""
pd = 0
  

spi = spidev.SpiDev()
spi.open(0,0)
 
def readadc(adPin):
	# read SPI data from MCP3004 chip, 4 possible adc’s (0 thru 3)
	if ((adPin > 3) or (adPin < 0)):
		return-1
	r = spi.xfer2([1,8+adPin <<4,0])
	#print(r)
	adcout = ((r[1] &3) <<8)+r[2]
	return adcout
 
def getLevel(adPin):
	value=readadc(adPin)
	volts=(value*3.3)/1024
	
	return (volts, value)
	

while True:
	v0 = getLevel(0)
	v1 = getLevel(2)
	
	light = v1[1]
	temp = (((v0[0] * 1000) - 500)/10)
	print(light, temp)
	msg = { 'light': light,
			'temp':temp}
	sendMessage(json.dumps(msg))
	time.sleep(60)


client.loop_stop()
client.disconnect()
print('done.')

