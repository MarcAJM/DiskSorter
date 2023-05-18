import os
import sys 
import time
import logging
import spidev as SPI
from lib import LCD_1inch3
from PIL import Image,ImageDraw,ImageFont

sys.path.append("..")

class Screen:
    
    # Constructor:
    def __init__(self):
        self.display = LCD_1inch3.LCD_1inch3()
        self.display.Init()     # Initialize library.
        self.display.clear()    # Clear display.

    # Everytime the screen needs to get an update call this method:
    def update_display(self, speed, white_disks, black_disks, error_message):
        try:
            image = Image.new("RGB", (self.display.width, self.display.height), "WHITE") 
            draw = ImageDraw.Draw(image)
            font = ImageFont.truetype("../fonts/font1.ttf", 50)

            # Change the text:
            draw.text((5, 5), 'Speed: ' + speed, fill = 'BLUE',font=font) 
            draw.text((5, 65), 'White disks: ' + white_disks, fill = 'BLUE',font=font) 
            draw.text((5, 125), 'Black disks: ' + black_disks, fill = 'BLUE',font=font) 
            draw.text((5, 185), error_message, fill = 'RED',font=font) 

            # Display the image and exit:
            self.display.ShowImage(image)
            self.display.module_exit()

        except IOError as e:
            logging.info(e)    

        except KeyboardInterrupt:
            self.display.module_exit()
            logging.info("quit:")
            exit()