import RPi.GPIO as GPIO          
from time import sleep

in1 = 5
in2 = 6
en = 26
temp1= 1

speed = 25

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(en,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
p=GPIO.PWM(en,1000)
p.start(speed)
print("The default speed & direction of motor is LOW & Forward.....")
print("r-run s-stop f-forward b-backward l-low m-medium h-high vh-very high e-exit")
print("\n")    

while(1):

    x=input()
    
    if x=='r':
        print("run")
        if(temp1==1):
         GPIO.output(in1,GPIO.HIGH)
         GPIO.output(in2,GPIO.LOW)
         print("forward")
         x='z'
        else:
         GPIO.output(in1,GPIO.LOW)
         GPIO.output(in2,GPIO.HIGH)
         print("backward")
         x='z'

    elif x=='s':
        print("stop")
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
        x='z'

    elif x=='f':
        print("forward")
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        temp1=1
        x='z'

    elif x=='b':
        print("backward")
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.HIGH)
        temp1=0
        x='z'

    elif x=='l':
        speed = 25
        print("low")
        p.ChangeDutyCycle(speed)
        x='z'

    elif x=='m':
        speed = 50
        print("medium")
        p.ChangeDutyCycle(speed)
        x='z'

    elif x=='h':
        speed = 75
        print("high")
        p.ChangeDutyCycle(speed)
        x='z'

    elif x=='vh':
        speed = 100
        print("very high")
        p.ChangeDutyCycle(speed)
        x='z'

    elif x=='e':
        GPIO.cleanup()
        break

    else:
        print("<<<  wrong data  >>>")
        print("please enter the defined data to continue.....")