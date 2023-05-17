import board
import adafruit_tcs34725
import screen
from time import sleep

i2c = board.I2C()
sensor = adafruit_tcs34725.TCS34725(i2c)

while True:
    # Color is black:
    if sensor.color_rgb_bytes == (0, 0, 0):
        screen.update_display()

    # Color is white
    elif sensor.color_rgb_bytes == (255, 255, 255):
        screen.update_display()

    # Not black nor white:
    else:
        screen.update_display()


    sleep(0.2)