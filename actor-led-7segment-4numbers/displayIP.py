#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import tm1637
import socket

# Initialize the display (GND, VCC=3.3V, Example Pins are DIO-20 and CLK21)
Display = tm1637.TM1637(CLK=21, DIO=20, brightness=0.3)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("gmail.com", 80))
IP = s.getsockname()[0]

s.close()

print "IP of RasPi is"
print IP

# Separate on comma.
numbers = IP.split(".")

# Loop and print each city name.
loops = 3
while loops > 0:
    for number in numbers:
        Display.ShowInt(number)
        time.sleep(2)
    loops -= 1
    Display.Clear()
    time.sleep(2)

print('done.')
Display.cleanup()
