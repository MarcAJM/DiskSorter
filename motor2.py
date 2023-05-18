import RPi.GPIO as GPIO  
import potentiometer   
import color_sensor
from time import sleep

in1 = 5
in2 = 6
en = 26
temp1= 1

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(en,GPIO.OUT)

GPIO.output(in1,GPIO.HIGH)
GPIO.output(in2,GPIO.LOW)
p=GPIO.PWM(en,1000)
p.start(potentiometer.speed)

try:
    while True:
        p.ChangeDutyCycle(potentiometer.speed)
finally:
    GPIO.cleanup()