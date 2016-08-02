This contains info about:
* [Shield w/ ADC Interface](#shield)
* [List of analog sensors](#analog-sensors)
* [AD converter](ky053)
* [Level shifter](ky051)

## Shield

To read analog values, you need to enable SPI.

You can find how to in [this README](../setup-raspberrypi/README.md).

Two version of the board have been used:
* [First version](#first-used-board-version)
* [Second version](#second-used-board-version)

## First used board version

![image of device](images/boardv1.JPG)

The linksprite board has a 4-channel analog-to-digital converter. You need to use this to read values from analog sensors since the RaspberryPi doesn't have analog inputs.

*Note* that the board has a jumper to set VCC to 3.3V or 5V. Some devices will not work if it's the wrong setting...

## Second used board version
![boardv2](images/boardv2.jpg)

![schema](images/schema.jpg)

The numbers disposed in the schema above are needed to inform to a given program where the sensor/actor is connected.

![schema](images/schema2.jpg)
![schema](images/description.png)

## Analog Sensors
* [temperature](../sensor-temperature)
* light (see [linksprite documentation](http://linksprite.com/wiki/index.php5?title=LDR_Module))
* noise level
* 3-axis accelerometer
* Rotary Potentiometer
* Magnet modul
* Heartbeat
* Magic light cup
* knock
* photocell

For the temperature sensor, use this python code to convert raw values to degrees celsius:

    temp = (((value * 1000) - 500)/10)
    

* [`analogIn.py`](analogIn.py) shows how to read the values
* [`analogInputDemo`](analogInputDemo.py) display all 4 values in real time; useful for test/debug

![image of device](images/sensor1.JPG)
![image of device](images/sensor2.JPG)
![image of device](images/sensor3.JPG)
![image of device](images/sensor4.JPG)
![image of device](images/sensor6.jpg)
![image of device](images/sensor7.jpg)
![image of device](images/sensor5.jpg)
![image of device](images/sensor8.jpg)
![image of device](images/sensor9.jpg)
![image of device](images/sensor10.jpg)
![image of device](images/sensor11.jpg)
![image of device](images/sensor12.jpg)
![image of device](images/sensor13.jpg)
![image of device](images/sensor14.jpg)
![image of device](images/sensor16.jpg)
![image of device](images/sensor15.jpg)
