#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import time


import RPi.GPIO as GPIO


import tm1637
import socket


#CLK in 7-segment to GPIO23(pin16), and Di0 to GPIO24(pin18) in Raspberry Pi
Display = tm1637.TM1637(21,22,tm1637.BRIGHT_TYPICAL)

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("gmail.com",80))
IP = s.getsockname()[0]

s.close()

print "IP of RasPi is"
print IP

# Separate on comma.
numbers = IP.split(".")

# Loop and print each city name.
while True:
        for number in numbers:
                Display.ShowInt(number)
                time.sleep(2)
        Display.Clear()
        time.sleep(2)


print('done.')

