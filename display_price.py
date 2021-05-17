# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import busio
import board
from digitalio import DigitalInOut, Direction

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from adafruit_epd.epd import Adafruit_EPD
from adafruit_epd.ssd1675b import Adafruit_SSD1675B  # pylint: disable=unused-import

from get_price import get_price

# create two buttons
switch1 = DigitalInOut(board.D6)
switch2 = DigitalInOut(board.D5)
switch1.direction = Direction.INPUT
switch2.direction = Direction.INPUT

# create the spi device and pins we will need
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
ecs = DigitalInOut(board.D8)
dc = DigitalInOut(board.D22)
rst = DigitalInOut(board.D27)
busy = DigitalInOut(board.D17)

# give them all to our driver
display = Adafruit_SSD1675B(
    122,
    250,
    spi,  # 2.13" HD mono display (rev B)
    cs_pin=ecs,
    dc_pin=dc,
    sramcs_pin=None,
    rst_pin=rst,
    busy_pin=busy,
)
display.rotation = 1

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = display.width
height = display.height
image = Image.new("RGB", (width, height))

WHITE = (0xFF, 0xFF, 0xFF)
BLACK = (0x00, 0x00, 0x00)

# clear the buffer
display.fill(Adafruit_EPD.WHITE)
# clear it out
display.display()

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw an outline box
draw.rectangle((1, 1, width - 2, height - 2), outline=BLACK, fill=WHITE)

# Load default font.
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)

# Alternatively load a TTF font.  Make sure the .ttf font
# file is in the same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
# font = ImageFont.truetype('Minecraftia.ttf', 8)

data = get_price()["data"]
btc = data["BTC"]["quote"]["USD"]["price"]
eth = data["ETH"]["quote"]["USD"]["price"]
btc_price = "%.2f" % btc
eth_price = "%.2f" % eth

# Write two lines of text.
draw.text((10, 10), "BTC", font=font, fill=BLACK)
draw.text((10, 35), "$" + str(btc_price), font=font, fill=BLACK)

draw.text((10, 60), "ETH", font=font, fill=BLACK)
draw.text((10, 85), "$" + str(eth_price), font=font, fill=BLACK)

while True:
    if not switch1.value:
        print("Switch 1")
        display.image(image)
        display.display()
        while not switch1.value:
            time.sleep(0.01)
    if not switch2.value:
        print("Switch 2")
        display.fill(Adafruit_EPD.WHITE)
        display.display()
        while not switch2.value:
            time.sleep(0.01)
    time.sleep(0.01)
