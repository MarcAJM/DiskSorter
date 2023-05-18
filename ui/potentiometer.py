import RPi.GPIO as GPIO

class Potentiometer:
    
    # Constructor:
    def __init__(self, pin):
        self.pin = pin

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.IN)
    
    # Get the input:
    def get_input(self):
        return GPIO.input(self.pin)