import os
import sys 
import time
import logging
import ui.potentiometer as potentiometer
import sensors.color_sensor as color_sensor
import error_detection
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

# This is for when the machine starts:
display = LCD_1inch3.LCD_1inch3()
display.Init()     # Initialize library.
display.clear()    # Clear display.

# Everytime the screen needs to get an update call this method:
def update_display(speed, white_disks, black_disks, error_message):
    try:
        image = Image.new("RGB", (display.width, display.height), "WHITE")    # Create blank image for drawing.
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype("../fonts/font1.ttf", 50)

        draw.text((5, 5), 'Speed: ' + speed, fill = 'BLUE',font=font) # Line for the speed of the conveyor belt
        draw.text((5, 65), 'White disks: ' + white_disks, fill = 'BLUE',font=font) # Line for the amount of white disks in bin
        draw.text((5, 125), 'Black disks: ' + black_disks, fill = 'BLUE',font=font) # Line for the amount of black disks in bin
        draw.text((5, 185), error_message, fill = 'RED',font=font) # Line for error description

        display.ShowImage(image)
        display.module_exit()

    except IOError as e:
        logging.info(e)    

    except KeyboardInterrupt:
        display.module_exit()
        logging.info("quit:")
        exit()

# Keep updating the display:
while True:
    update_display(potentiometer.speed, color_sensor.white_disks, color_sensor.black_disks, error_detection.error_message)
    time.sleep(1)