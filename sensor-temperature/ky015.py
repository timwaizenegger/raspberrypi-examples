#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
read temperature and humidity from KY-015

"""
import RPi.GPIO as GPIO
import time

def bin2dec(string_num):
    return str(int(string_num, 2))

tempPin = 14 # S connected to D14

def read_data(pin):
    data = 0
    for i in range(8):
        if (GPIO.input(pin) == GPIO.LOW):
            while (GPIO.input(pin) == GPIO.LOW): # wait for 50us
                pass
            time.sleep(30 * 1e-6) # determine the duration of the high level to determine the data is '0 'or '1'
            if (GPIO.input(pin) == GPIO.HIGH):
                data |= (1 << (7-i)) # high front and low in the post
            while (GPIO.input(pin) == GPIO.HIGH): # data '1 ', wait for the next one receiver
                pass
    return data

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(tempPin, GPIO.OUT)

while True:
    GPIO.output(tempPin, GPIO.LOW); # bus down, send start signal
    time.sleep(30 * 1e-6); # delay greater than 18ms, so DHT11 start signal can be detected

    GPIO.output(tempPin, GPIO.HIGH);
    time.sleep(40 * 1e-6); # Wait for DHT11 response

    GPIO.setup(tempPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    while (GPIO.input(tempPin) == GPIO.HIGH):
        pass
    time.sleep(80 * 1e-6) # DHT11 response, pulled the bus 80us
    if (GPIO.input(tempPin) == GPIO.LOW): # copied from C version (???)
        pass
    time.sleep(80 * 1e-6); # DHT11 80us after the bus pulled to start sending data

    dat = []
    for i in range(4): # receive temperature and humidity data, the parity bit is not considered
        dat[i] = read_data(tempPin)

    GPIO.setup(tempPin, GPIO.OUT)
    GPIO.output(tempPin, GPIO.HIGH); # send data once after releasing the bus, wait for the host to open the next Start signal
    
    # print results
    print('Current humidity: %3d.%d' % (dat[0], dat[1]))
    print('Current temperature: %3d.%dC' % (dat[2], dat[3]))
    time.sleep(1)