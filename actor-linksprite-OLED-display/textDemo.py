# -*- coding: utf-8 -*-
import math
import time

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


# Raspberry Pi pin configuration:
RST = 24
# Note the following are only used with SPI:
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)


# Initialize library.
disp.begin()


# Get display width and height.
width = disp.width
height = disp.height

# Clear display.
disp.clear()
disp.display()

# Create image buffer.
# Make sure to create image with mode '1' for 1-bit color.
image = Image.new('1', (width, height))

# Load default font.
#font = ImageFont.load_default(fontsize=100)
font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeSans.ttf", 50)

# Create drawing object.
draw = ImageDraw.Draw(image)


text= "Juhuu!"


# draw the text
draw.rectangle((0,0,width,height), outline=0, fill=0)

draw.text((0, 0), text, font=font, fill=255)

disp.image(image)
disp.display()




