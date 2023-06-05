import os
import sys 
import time
import logging
import spidev as SPI
sys.path.append('') #add path and CHECK IMPORTS
import LCD_1inch54
import LCD_1inch3
from PIL import Image,ImageDraw,ImageFont

class Screen:
    
    # Constructor:
    def __init__(self):
        self.display = LCD_1inch3.LCD_1inch3()
        self.display.Init()     # Initialize library.
        self.display.clear()    # Clear display.

    # Everytime the screen needs to get an update call this method:
    def update_display(self, speed, white_disks, black_disks, error_message, status_message):
        try:
            image = Image.new("RGB", (self.display.width, self.display.height), "BLACK") 
            draw = ImageDraw.Draw(image)
            font = ImageFont.truetype("/home/marcajm/Desktop/DiskSorter/fonts/font1.ttf", 20)

            # Change the text:
            draw.text((5, 5), 'Speed: {}%'.format(speed), fill = 'WHITE',font=font) 
            draw.text((5, 35), 'White disks: {}'.format(white_disks), fill = 'WHITE',font=font) 
            draw.text((5, 65), 'Black disks: {}'.format(black_disks), fill = 'WHITE',font=font) 
            draw.text((5, 125), error_message, fill = 'RED',font=font)
            draw.text((5, 155), status_message, fill = 'RED', font=font)
            # Display the image and exit:
            self.display.ShowImage(image)
            self.display.module_exit()

        except IOError as e:
            logging.info(e)    

        except KeyboardInterrupt:
            self.display.module_exit()
            logging.info("quit:")
            exit()


        

