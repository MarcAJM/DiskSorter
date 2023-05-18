import board
import adafruit_tcs34725
from time import sleep

i2c = board.I2C()
sensor = adafruit_tcs34725.TCS34725(i2c)

white_disks = 0
black_disks = 0

# TODO: We have to check how accurate the sensor actually is 
# and based on that we need to make sort of a threshold like Alisha did in her code.

while True:
    # Color is black:
    if sensor.color_rgb_bytes == (0, 0, 0):
        black_disks += 1

    # Color is white
    elif sensor.color_rgb_bytes == (255, 255, 255):
        white_disks += 1

    sleep(0.2)