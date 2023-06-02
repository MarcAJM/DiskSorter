import RPI.GPIO as GPIO

class Button():

    def __init__(self, in1):
        self.in1 = in1

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.in1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)