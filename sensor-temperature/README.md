This contains info about several temperature sensors:
* [KY-013 Temperature (analog)](#ky-013)
* [KY-028 Temperature (analog and digital)](#ky-028)
* [KY-015 Temperature and Humidity (digital)](#ky-015)
* [KY-015 Temperature and Pressure (analog)](#ky-052)

## KY-013

![ky013](images/ky013.JPG)

The value-temperature formula used in this sensor code might need to be calibrated.
To do that, just use the [example code](ky013.py) and read the real values, relating them to the temperature witha a thermometer.
The pins for the extension board, where (`sensor: board`) - following the [example code](ky013.py):
* -:	G
* (middle pin):	V
* S:	A0


## KY-028

![ky028](images/ky028.JPG)

The value-temperature formula used in this sensor code might need to be calibrated.
To do that, just use the [example code](ky013.py) and read the real values, relating them to the temperature witha a thermometer.
The pins for the extension board, where (`sensor: board`) - following the [example code](ky028.py):
* -:	G
* +:	V
* A0:	A0
* D0: 	D27

## KY-015

![ky015](images/ky015.JPG)

There is a library build for this sensor. It already contains an example of use. Get it here:

[github.com/szazo/DHT11_Python](https://github.com/szazo/DHT11_Python)


You can also try this code  without the library (not recommended):

ky015.py(ky015/ky015.py)

* -:	G
* (middle pin):	V
* S:	D14

## KY-052

![ky052](images/ky052.JPG)