# List of contents
* [Raspbian (OS) install](#install)
* [Updates](#update)
* [SD card reset](#sd-card-reset)
* [SO issue solving](#issue-solving)

## [Install] (https://www.raspberrypi.org/documentation/installation/noobs.md)

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

## [SD card reset] (http://kb.sandisk.com/app/answers/detail/a_id/14827/~/using-sd-formatter-tool-to-restore-full-capacity-on-sdhc%2Fsdxc-cards)

* [Download SD Formatter Tool] (https://www.sdcard.org/downloads/formatter_4/) (scroll to the bottom of the page)
* Install the application
* With the SD card plugged, open the application
* Go to *Option*, change *FORMAT SIZE ADJUSTMENT* to *ON*
![OPTION BUTTON](http://kb.sandisk.com/euf/assets/images/faqs/14827/kb14827_1.png)
![FORMAT SIZE ADJUSTMENT](http://kb.sandisk.com/euf/assets/images/faqs/14827/kb14827_2.png)
* Click on *Format*

## Issue Solving

### [Resolution problem](http://weblogs.asp.net/bleroy/getting-your-raspberry-pi-to-output-the-right-resolution)
* Open the terminal (`ctrl + alt + T`)
* Do the following commands (type `y` for the incoming questions after each command):
 * `tvservice -d edid`
 * `edidparser edid`
* Edit the file `/boot/config.txt`
 * `nano /boot/config.txt`
* Uncomment the following lines and put those values (If your mode description from the last command contains “DMT”, the group should be 2, and if it contains “CEA”, it should be 1):
  * `hdmi_group=2`
  * `hdmi_mode=82`
