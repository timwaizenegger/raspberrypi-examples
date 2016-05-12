##KY-016 RGB 5mm LED / KY-009 RGB LED SMD 
![image](pic3.jpg)
![image](pic4.jpg)

Example code [here](rgb.py)

##Linker-Kit RGB Led

![image](rgbled.jpg)

* RGB
* 8mm
* Chipset WS2812
* Working voltage: 3 V  ~  5 V


## get it running

Connect the RGB led on pin 12:

![image](pic2.jpg)

Then:

    git clone https://github.com/jgarff/rpi_ws281x.git
    cd rpi_ws281x.git
    sudo scons
    cd python
    sudo python ez_setup.py
    sudo python setup.py install
    
    cd examples
    python strandtest.py



![image](pic1.jpg)
