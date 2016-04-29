# List of contents
* [Raspbian (OS) install](#install)
* [Updates](#update)
* [SSH Access](#ssh-access)
* [SD card reset](#sd-card-reset)
* [SO issue solving](#issue-solving)

## Install

This guide is also found [here](https://www.raspberrypi.org/documentation/installation/noobs.md).
* [Download NOOBS offline and network install](https://www.raspberrypi.org/downloads/noobs/)
* Format a microSD (at least 4GB) on **FAT32**
* Unzip the content of the downloaded file on the card. The card content should look like:
![SD card content](images/noobfiles.png)
* Plug the card and plug the power on the Raspberry (in that order)
* When the loading is complete, select the *Raspbian* option and click on Install
![RASPBIAN INSTALL](images/raspinstall.png)
* Wait until the installation is finished and the OS is ready

## Update

### SO Update
* Open the terminal (`ctrl + alt + T`)
* Do the following commands (type `y` for the incoming questions after each command):
 * `sudo apt-get update`
 * `sudo apt-get dist-upgrade`
 
### Firmware Update
* Open the terminal (`ctrl + alt + T`)
* Do the following commands (type `y` for the incoming questions after each command):
 * `sudo rpi-update`
 * `reboot`

## SSH Access

This guide is also found [here](https://www.raspberrypi.org/documentation/remote-access/ssh/).
SSH is already enabled on RaspberryPi by default.
To access, you will need to check the RaspberryPi IP. That can be done through the terminal with on of the following commands (`eth0` stands for your ethernet interface IP and`wlan0` for your wireless interface IP):
* `sudo ifconfig -a`
* `sudo ip addr show`
* `sudo hostname --ip-address`
The default *username* is `pi` and the default *password* is `raspberry`.
If the SSH is **not enabled**, you can enable through:
* Run `sudo raspi-config` on the terminal
* Navigate to `9 Advanced Options`
* Navigate to `A4 SSH`
* Select `Enable`

## SD card reset

This guide is also found [here](http://kb.sandisk.com/app/answers/detail/a_id/14827/~/using-sd-formatter-tool-to-restore-full-capacity-on-sdhc%2Fsdxc-cards).
* [Download SD Formatter Tool](https://www.sdcard.org/downloads/formatter_4/) (scroll to the bottom of the page)
* Install the application
* With the SD card plugged, open the application
* Go to *Option*, change *FORMAT SIZE ADJUSTMENT* to *ON*
![OPTION BUTTON](images/sdresetoption.png)
![FORMAT SIZE ADJUSTMENT](images/sdresetformatsize.png)
* Click on *Format*

## Issue Solving

### Display resolution problem

This resolution is also found [here](http://weblogs.asp.net/bleroy/getting-your-raspberry-pi-to-output-the-right-resolution).
* Open the terminal (`ctrl + alt + T`)
* Do the following commands (type `y` for the incoming questions after each command):
 * `tvservice -d edid`
 * `edidparser edid`
* Edit the file `/boot/config.txt`
 * `nano /boot/config.txt`
* Uncomment the following lines and put those values (If your mode description from the last command contains “DMT”, the group should be 2, and if it contains “CEA”, it should be 1):
  * `hdmi_group=2`
  * `hdmi_mode=82`
