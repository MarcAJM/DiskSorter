import RPi.GPIO as GPIO          
from time import sleep

in1 = 5 #input 1 pin
in2 = 6 #input 2 pin
en = 26 #enable pin
temp1= 1 #temporary variable (to alter the speed of the motor etc.)

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT) 
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(en,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
p=GPIO.PWM(en,1000)
p.start(25)
print("The default speed & direction of motor is LOW & Forward.....")
print("r-run s-stop f-forward b-backward l-low m-medium h-high vh-very high e-exit")
print("\n")    

while(1):

    x=input() #take input from keyboard 
    
    if x=='r':
        print("run")
        if(temp1==1): #(initial case)
         GPIO.output(in1,GPIO.HIGH)
         GPIO.output(in2,GPIO.LOW)
         print("forward")
         x='z'
        else: #run the motor backward (temp1 = 0 in this instance)
         GPIO.output(in1,GPIO.LOW)
         GPIO.output(in2,GPIO.HIGH)
         print("backward")
         x='z'

    elif x=='s':
        print("stop") #stop the belt 
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
        x='z'

    elif x=='f': #run motor forwards
        print("forward")
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        temp1=1 #alter temp1 accordingly
        x='z'

    elif x=='b': #run motor backwards
        print("backward")
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.HIGH)
        temp1=0 #alter temp1 accordingly
        x='z'

    elif x=='l':
        speed = 25
        print("low")
        p.ChangeDutyCycle(speed) #change speed of belt
        x='z'

    elif x=='m':
        speed = 50
        print("medium")
        p.ChangeDutyCycle(speed) #change speed of belt
        x='z'

    elif x=='h':
        speed = 75
        print("high")
        p.ChangeDutyCycle(speed) #change speed of belt
        x='z'

    elif x=='vh':
        speed = 100
        print("very high")
        p.ChangeDutyCycle(speed) #change speed of belt
        x='z'

    elif x=='e':
        GPIO.cleanup() #exit program 
        break

    else:
        print("<<<  wrong data  >>>")
        print("please enter the defined data to continue.....")
