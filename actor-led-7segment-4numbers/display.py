#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import sleep
import tm1637

# Initialize the display (GND, VCC=3.3V, Example Pins are DIO-20 and CLK21)
Display = tm1637.TM1637(CLK=21, DIO=20, brightness=1.0)

# Basic Display Update:
digits = [1, 2, 3, 4]
Display.Show(digits)
print "1234  - Working? (Press Key)"
scrap = raw_input()

# Update Individual Digits:
print "Updating one digit at a time:"
Display.Clear()
Display.Show1(1, 3)
sleep(0.5)
Display.Show1(2, 2)
sleep(0.5)
Display.Show1(3, 1)
sleep(0.5)
Display.Show1(0, 4)
print "4321  - (Press Key)"
scrap = raw_input()

# The ":"
print "Add double point\n"
Display.ShowDoublepoint(True)
sleep(0.2)

# Vary the brightness:
print "Brightness Off"
Display.SetBrightness(0)
sleep(0.5)
print "Full Brightness"
Display.SetBrightness(1)
sleep(0.5)
print "30% Brightness"
Display.SetBrightness(0.3)
sleep(0.3)

print('done.')
Display.cleanup()
