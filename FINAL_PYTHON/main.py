#imports
import RPi.GPIO as GPIO          
from time import sleep
import time

#main code starts now
class Main:

    def run(self):
        # Instantiate the subclasses
        motor1 = Motor1()
        motor2 = Motor2()
        motor3 = Motor3()
        colorsensor = ColorSensor()
        screen = Screen()
        potentiometer = Potentiometer()

        #actual code

        z = True

        #run main belt
        motor1.m1()

        while (z):
            colorsensor.cs() #run color sensor

            #rgb values retrieved
            red = colorsensor.red
            green = colorsensor.green()
            blue = colorsensor.blue()

            #if statement
            if red == 1000 & blue == 10 & green == 5: #CHANGE this based on testing
                red = 10 #CHANGE THIS TO INCOPERATE RUNNING THE OTHER MOTORS TO PUSH
            
            #ADD CODE TO UPDATE SCREEN

            #code to terminate belt if something happens
            GPIO.output(motor1.in1,GPIO.LOW)
            GPIO.output(motor1.in2,GPIO.LOW)
    
class Motor1:

    in1 = 5 #input 1 pin
    in2 = 6 #input 2 pin
    en = 26 #enable pin
    temp1= 1 #temporary variable (to alter the speed of the motor etc.)
    speed = 100 #speed of the motor

    def m1(self):

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(Motor1.in1,GPIO.OUT) 
        GPIO.setup(Motor1.in2,GPIO.OUT)
        GPIO.setup(Motor1.en,GPIO.OUT)
        GPIO.output(Motor1.in1,GPIO.LOW)
        GPIO.output(Motor1.in2,GPIO.LOW)
        p=GPIO.PWM(Motor1.en,1000)
        p.start(25)

        #start the motor
        GPIO.output(Motor1.in1,GPIO.HIGH)
        GPIO.output(Motor1.in2,GPIO.LOW)
        p.ChangeDutyCycle(Motor1.speed)

class Motor2:

    def m2(self):
        print("This is a method of Motor2")

class Motor3:

    def m3(self):
        print("This is method of Motor3")

class ColorSensor:
    red = 0
    blue = 0
    green = 0

    def cs(self):
        s2 = 23 #pins can change
        s3 = 24 #pins can change
        signal = 25 #pins can change
        NUM_CYCLES = 10

        #setup the pins and stuff
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(signal,GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(s2,GPIO.OUT)
        GPIO.setup(s3,GPIO.OUT)

        #get rgb values in Hz
        GPIO.output(s2,GPIO.LOW)
        GPIO.output(s3,GPIO.LOW)
        time.sleep(0.3)
        start = time.time()
        for impulse_count in range(NUM_CYCLES):
            GPIO.wait_for_edge(signal, GPIO.FALLING)
        duration = time.time() - start #seconds to run for loop
        ColorSensor.red  = NUM_CYCLES / duration #in Hz

        GPIO.output(s2,GPIO.LOW)
        GPIO.output(s3,GPIO.HIGH)
        time.sleep(0.3)
        start = time.time()
        for impulse_count in range(NUM_CYCLES):
            GPIO.wait_for_edge(signal, GPIO.FALLING)
        duration = time.time() - start
        ColorSensor.blue = NUM_CYCLES / duration #in Hz

        GPIO.output(s2,GPIO.HIGH)
        GPIO.output(s3,GPIO.HIGH)
        time.sleep(0.3)
        start = time.time()
        for impulse_count in range(NUM_CYCLES):
            GPIO.wait_for_edge(signal, GPIO.FALLING)
        duration = time.time() - start
        ColorSensor.green = NUM_CYCLES / duration #in Hz

class Screen:

    def sc(self):
        print("This is method of Screen")

class Potentiometer:

    def pot(self):
        print("This is method 2 of Potentiometer")

#run the code
if __name__ == "__main__":
    main = Main()
    main.run()