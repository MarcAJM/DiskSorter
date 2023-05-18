import board
import adafruit_tcs34725
from time import sleep

class Color_sensor:
    
    # Constructor:
    def __init__(self):
        i2c = board.I2C()
        self.sensor = adafruit_tcs34725.TCS34725(i2c)
    
    # Get the rgb values:
    def get_rgb(self):
        return self.sensor.color_rgb_bytes