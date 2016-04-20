#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys


import RPi.GPIO as GPIO


import tm1637



Display = tm1637.TM1637(23,24,tm1637.BRIGHT_TYPICAL)

while True:
	for i in range(0,9999):
		Display.ShowInt(i)
		time.sleep(0.2)


print('done.')

