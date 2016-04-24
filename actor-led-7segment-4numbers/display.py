#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import time


import RPi.GPIO as GPIO


import tm1637


#CLK in 7-segment to GPIO23(pin16), and Di0 to GPIO24(pin18) in Raspberry Pi
Display = tm1637.TM1637(23,24,tm1637.BRIGHT_TYPICAL)

while True:
	for i in range(0,9999):
		Display.ShowInt(i)
		time.sleep(0.2)


print('done.')

