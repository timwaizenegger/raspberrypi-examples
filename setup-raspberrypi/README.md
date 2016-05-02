# List of contents
* [Raspbian (OS) install](#install)
* [Updates](#update)
* [SD card reset](#sd-card-reset)
* [SO issue solving](#issue-solving)
* [Eduroam wlan config](#eduroam)

## Install

This guide is also found [here](https://www.raspberrypi.org/documentation/installation/noobs.md).
* [Download NOOBS offline and network install] (https://www.raspberrypi.org/downloads/noobs/)
* Format a microSD (at least 4GB) on **FAT32**
* Unzip the content of the downloaded file on the card. The card content should look like:
![SD card content](http://puu.sh/oxzVl/5d7b1abb67.png)
* Plug the card and plug the power on the Raspberry (in that order)
* When the loading is complete, select the *Raspbian* option and click on Install
![RASPBIAN INSTALL](http://puu.sh/oxBd5/41d7f3c3cf.png)
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

## SD card reset

This guide is also found [here](http://kb.sandisk.com/app/answers/detail/a_id/14827/~/using-sd-formatter-tool-to-restore-full-capacity-on-sdhc%2Fsdxc-cards).
* [Download SD Formatter Tool] (https://www.sdcard.org/downloads/formatter_4/) (scroll to the bottom of the page)
* Install the application
* With the SD card plugged, open the application
* Go to *Option*, change *FORMAT SIZE ADJUSTMENT* to *ON*
![OPTION BUTTON](http://kb.sandisk.com/euf/assets/images/faqs/14827/kb14827_1.png)
![FORMAT SIZE ADJUSTMENT](http://kb.sandisk.com/euf/assets/images/faqs/14827/kb14827_2.png)
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

## Eduroam
This resolution is based on this [link](http://www.willprice.org/2014/03/17/eduroam-on-the-raspberry-pi.html)
* Open the terminal (`ctrl + alt + T`)
* Do the following command to stop the network on Raspberry: 
 * `sudo service networking stop`
* Now acces the file `wpa_supplicant.conf` as administrator: 
 * You can open it on terminal with the command `sudo leafpad /etc/wpa_supplicant/wpa_supplicant.conf`
 * Or you go to the folder `/etc/wpa_supplicant/`, right click on `wpa_supplicant.conf` and choose `Open With`. Change the tab from `Installed Applications` to `Custom Command Line` and write `sudo leafpad`:
  
   ![Right Click](right_click.png) 

* Then you will find the reference to the eduroam network:
   ![select](select.png) 
* And change the identity and the password:
   ![change](change.png) 
* If your not in University of Stuttgart you should change the first block following your university configurarion.
* Do NOT change the information in the second block.
* After that save the file and run `sudo wpa_supplicant -i wlan0 -c /etc/wpa_supplicant/wpa_supplicant.conf -B`
* Your connection should work!
 
 
