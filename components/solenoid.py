import RPi.GPIO as GPIO
from time import sleep

class Solenoid:
    
    # Constructor:
    def __init__(self, pin):
        self.pin = pin

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)

    # TODO: May not be correct.
    # Push solenoid:
    def push(self, delay):
        sleep(delay)
        GPIO.output(self.pin, GPIO.LOW)
        sleep(0.05)
        GPIO.output(self.pin, GPIO.HIGH)