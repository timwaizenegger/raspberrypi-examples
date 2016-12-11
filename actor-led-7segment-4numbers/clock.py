#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import sleep
import tm1637

try:
    import thread
except ImportError:
    import _thread as thread

# Initialize the clock (GND, VCC=3.3V, Example Pins are DIO-20 and CLK21)
Display = tm1637.TM1637(CLK=21, DIO=20, brightness=1.0)

try:
    print "Starting clock in the background (press CTRL + C to stop):"
    Display.StartClock(military_time=False)
    print 'Continue Python script and tweak Display!'
    sleep(5)
    Display.ShowDoublepoint(False)
    sleep(5)
    loops = 3
    while loops > 0:
        for i in range(0, 10):
            Display.SetBrightness(i / 10.0)
            sleep(0.5)
        loops -= 1
    Display.StopClock()
    thread.interrupt_main()
except KeyboardInterrupt:
    print "Properly closing the clock and open GPIO pins"
    Display.cleanup()
