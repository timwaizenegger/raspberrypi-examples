![ky053](../images/ky053.JPG)

This is based on [this guide](http://sensorkit.joy-it.net/index.php?title=KY-053_Analog_Digital_Converter).

Use the board in *3,3V*.

The connections should be (`ky053: board`):
* VDD 	:	V (3,3V) 	[Pin 01]
* GND 	: 	G
* SCL 	: 	SCL (top left of the board)
* SDA 	: 	SDA (top left of the board)
* ADDR 	: 	N.C. 	[-]
* ALRT 	: 	N.C. 	[-]
* A0 	: 	Any Analog Input
* A1 	: 	Any Analog Input
* A2 	: 	Any Analog Input
* A3 	: 	Any Analog Input

You need to uncomment the line:
```
dtparam=i2c_arm=on
```

Through the command
```
sudo nano /boot/config.txt
```

and then install
```
sudo apt-get install python-smbus i2c-tools -y
```

at last you can run the [example code](KY-053_RPi_AnalogDigitalConverter.py) (needs the other files from the folder also).
```
sudo python KY-053_RPi_AnalogDigitalConverter.py
```