## Sensor KY-032: Obstacle avoidance sensor

![ky032](images/ky032.jpg)

The *pins need to be remaped* for the extension board, where (`sensor: board`) - following the [example code](obstacle.py):
* GND:	G
* +:	V
* out:	D15
* EN:	D16

* GND – should be connected to ground
* + – should be connected to 5V power supply
* out – obstacle signal
* EN – no use found
