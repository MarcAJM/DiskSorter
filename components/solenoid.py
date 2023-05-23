import RPi.GPIO as GPIO
from time import sleep

class Solenoid:
    
    # Constructor:
    def __init__(self, in1, en):
        self.in1 = in1

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.in1, GPIO.OUT)
        GPIO.setup(en, GPIO.OUT)
        
        GPIO.output(self.in1, GPIO.HIGH)
        GPIO.output(en, GPIO.HIGH)

    # TODO: May not be correct.
    # Push solenoid:
    def push(self, delay):
        sleep(delay)
        GPIO.output(self.in1, GPIO.LOW)
        sleep(0.05)
        GPIO.output(self.in1, GPIO.HIGH)
