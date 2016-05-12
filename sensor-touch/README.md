## Sensor KY-036: Touch sensor

![ky036](images/ky036.jpg)

The *pins need to be remaped* for the extension board, where (`sensor: board`) - following the [example code](touch.py):
* A0:	D27
* G:	G
* +:	V
* D0:	D26


* A0 – inverted signal
* G – should be connected to ground
* + – should be connected to 5V power supply
* D0 – touch signal
