#!/usr/bin/python
# -*- coding: UTF-8 -*-
#import chardet

import os
import sys 
import time
import logging
import spidev as SPI
sys.path.append("..")
from lib import LCD_1inch54
from lib import LCD_1inch3
from PIL import Image,ImageDraw,ImageFont

# Raspberry Pi pin configuration:
RST = 27
DC = 25
BL = 18
bus = 0 
device = 0 

try:
    # disp = LCD_1inch3.LCD_1inch3(spi=SPI.SpiDev(bus, device),spi_freq=10000000,rst=RST,dc=DC,bl=BL)
    disp = LCD_1inch3.LCD_1inch3()
    # Initialize library.
    disp.Init()
    # Clear display.
    disp.clear()
    # Create blank image for drawing.
    image = Image.new("RGB", (disp.width, disp.height), "WHITE")
    draw = ImageDraw.Draw(image)
    Font3 = ImageFont.truetype("../Font/Font02.ttf", 32)
    draw.text((5, 5), 'Speed: Maximum', fill = "#6C3483",font=Font3)

    disp.ShowImage(image)
    time.sleep(10)
    disp.clear()
    disp.module_exit()

except IOError as e:
    logging.info(e)    

except KeyboardInterrupt:
    disp.module_exit()
    logging.info("quit:")
    exit()