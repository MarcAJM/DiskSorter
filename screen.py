import os
import sys 
import time
import logging
import spidev as SPI
from lib import LCD_1inch3
from PIL import Image,ImageDraw,ImageFont

sys.path.append("..")

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
    font = ImageFont.truetype("../fonts/font1.ttf", 50)

    draw.text((5, 5), 'Speed: High', fill = 'BLUE',font=font) # Line for the speed of the conveyor belt
    draw.text((5, 65), 'White disks: 5', fill = 'BLUE',font=font) # Line for the amount of white disks in bin
    draw.text((5, 125), 'Black disks: 10', fill = 'BLUE',font=font) # Line for the amount of black disks in bin
    draw.text((5, 185), 'Error', fill = 'RED',font=font) # Line for error description

    display.ShowImage(image)
    display.module_exit()

except IOError as e:
    logging.info(e)    

except KeyboardInterrupt:
    display.module_exit()
    logging.info("quit:")
    exit()