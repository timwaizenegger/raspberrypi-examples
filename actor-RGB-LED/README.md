##KY-016 RGB 5mm LED / KY-009 RGB LED SMD 
![image](pic3.jpg)
![image](pic4.jpg)

Example code [here](rgb.py)

### Code Colors
Based on the raspberry code of [sensorkit.joy-it.net](http://sensorkit.joy-it.net/index.php?title=KY-016_RGB_5mm_LED_Modul)

. |. | .
------------ | ------------- | -------
![red](images/1.jpg) | ![red](images/2.jpg) | ![red](images/3.jpg)
LED_Farbe(100,0,0,1) - **RED**  |    LED_Farbe(100,50,0,1) - **ORANGE**  |  LED_Farbe(100,100,0,1) - **YELLOW**
![red](images/4.jpg) | ![red](images/5.jpg) | ![red](images/6.jpg)
LED_Farbe(50,100,0,1) - **LIGHT GREEN**  |    LED_Farbe(0,100,0,1) - **GREEN**  |  LED_Farbe(0,100,50,1) - **AQUA**
![red](images/7.jpg) | ![red](images/8.jpg) | ![red](images/9.jpg)
LED_Farbe(0,100,100,1) - **CYAN**  |    LED_Farbe(0,50,100,1) - **LIGHT BLUE**  |  LED_Farbe(0,0,100,1) - **BLUE**
![red](images/10.jpg)| ![red](images/11.jpg) | ![red](images/12.jpg)
LED_Farbe(50,0,100,1) - **PURPLE**  |    LED_Farbe(100,0,100,1) - **MAGENTA**  |  LED_Farbe(100,0,50,1) - **PINK**

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
    sudo apt-get install scons swig
    sudo scons
    cd python
    sudo python ez_setup.py
    sudo python setup.py install
    
    cd examples
    python strandtest.py



![image](pic1.jpg)
