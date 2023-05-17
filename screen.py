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
    display = LCD_1inch3.LCD_1inch3()
    display.Init()     # Initialize library.
    display.clear()    # Clear display.

    image = Image.new("RGB", (display.width, display.height), "WHITE")    # Create blank image for drawing.
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("../Font/Font02.ttf", 32)
    draw.text((5, 5), 'Speed: Maximum', fill = 'BLUE',font=font)

    display.ShowImage(image)
    display.module_exit()

except IOError as e:
    logging.info(e)    

except KeyboardInterrupt:
    display.module_exit()
    logging.info("quit:")
    exit()