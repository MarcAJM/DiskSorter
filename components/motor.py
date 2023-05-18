import RPi.GPIO as GPIO  
from time import sleep

class Motor():
    
    # this is the constructor:
    def __init__(self, in1, in2, en, speed):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(in1, GPIO.OUT)
        GPIO.setup(in2, GPIO.OUT)
        GPIO.setup(en, GPIO.OUT) 

        GPIO.output(in1, GPIO.HIGH)
        GPIO.output(in2, GPIO.LOW)
        self.p=GPIO.PWM(en, 1000)
        self.p.start(speed) # Start at maximum speed
    
    # function to change the speed of the motor:
    def change_speed(self, new_speed):
        self.p.ChangeDutyCycle(new_speed)
    
