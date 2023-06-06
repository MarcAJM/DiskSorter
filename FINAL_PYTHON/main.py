#imports
import RPi.GPIO as GPIO          
from time import sleep
import time

#main code starts now
class Main:

    def run(self):
        # Instantiate the subclasses
        helper = Helper()
        #motor2 = Motor2()
        #motor3 = Motor3()
        #colorsensor = ColorSensor()
        #screen = Screen()
        #potentiometer = Potentiometer()

        #actual code

        z = True

        #run main belt
        #motor1.m1()

        while (z):
            x = input()
            
            if x=='r':
                helper.m1() 
                #motor2.m2()
                x = 'z'
            
            if x == 'e':
                z = False
                GPIO.cleanup() #exit program 
                break
            #colorsensor.cs() #run color sensor

            #rgb values retrieved
            #red = colorsensor.red
            #green = colorsensor.green()
            #blue = colorsensor.blue()

            #if statement
            #if red == 1000 & blue == 10 & green == 5: #CHANGE this based on testing
                #red = 10 #CHANGE THIS TO INCOPERATE RUNNING THE OTHER MOTORS TO PUSH
            
            #ADD CODE TO UPDATE SCREEN

            #code to terminate belt if something happens
            #GPIO.output(motor1.in1,GPIO.LOW)
            #GPIO.output(motor1.in2,GPIO.LOW)
    
class Helper:
    
    #pins motor1 (helper class)
    in1 = 5 #input 1 pin
    in2 = 6 #input 2 pin
    en = 26 #enable pin
    temp1= 1 #temporary variable (to alter the speed of the motor etc.)
    speed = 100 #speed of the motor
    
    
    #colorsensor
    #colorsensor = Colorsensor()
    

    def m1(self):

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(Helper.in1,GPIO.OUT) 
        GPIO.setup(Helper.in2,GPIO.OUT)
        GPIO.setup(Helper.en,GPIO.OUT)
        GPIO.setup(Motor2.in1, GPIO.OUT)
        GPIO.setup(Motor2.in2,GPIO.OUT)
        GPIO.setup(Motor2.en,GPIO.OUT)
        
        
        GPIO.output(Helper.in1,GPIO.LOW)
        GPIO.output(Helper.in2,GPIO.LOW)
        
        GPIO.output(Motor2.in1,GPIO.LOW)
        GPIO.output(Motor2.in2,GPIO.LOW)
        
        p1=GPIO.PWM(Helper.en,1000)
        p1.start(25)
        
        p2=GPIO.PWM(Motor2.en,1000)
        p2.start(25)
        
        kleur = ColorSensor()
        
        #run the colorsensor code
        #colorsensor.cs()

        #start the motor
        
        #r = ColorSensor.red
        #g = ColorSensor.green
        #b = Colorsensor.blue
        
        k = 0
        
        while k < 20:
            
            #colorsensor = ColorSensor()
        
            #run the colorsensor code
            kleur.cs()

            #start the motor
        
            r = ColorSensor.red
            g = ColorSensor.green
            b = ColorSensor.blue
            
            print(r)
            print(g)
            print(b)
            
            GPIO.output(Helper.in1,GPIO.HIGH)
            GPIO.output(Helper.in2,GPIO.LOW)
            GPIO.output(Motor2.in1,GPIO.LOW)
            GPIO.output(Motor2.in2,GPIO.LOW)
            p1.ChangeDutyCycle(Helper.speed)
            time.sleep(0.1)
        
            if (18000 < r < 32000) and (22000 < b < 31000) and (21000 < g < 27000):
                GPIO.output(Helper.in1,GPIO.HIGH)
                GPIO.output(Helper.in2,GPIO.LOW)
                GPIO.output(Motor2.in1,GPIO.HIGH)
                GPIO.output(Motor2.in2,GPIO.LOW)
                p2.ChangeDutyCycle(Motor2.speed)
                
                time.sleep(2)
                
            k = k + 1


class Motor2:
    
    in1 = 23 #input 1 pin
    in2 = 24 #input 2 pin
    en = 25 #enable pin
    temp1= 1 #temporary variable (to alter the speed of the motor etc.)
    speed = 100

    def m2(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(Motor2.in1,GPIO.OUT) 
        GPIO.setup(Motor2.in2,GPIO.OUT)
        GPIO.setup(Motor2.en,GPIO.OUT)
        GPIO.output(Motor2.in1,GPIO.LOW)
        GPIO.output(Motor2.in2,GPIO.LOW)
        p=GPIO.PWM(Motor2.en,1000)
        p.start(25)

        #start the motor
        GPIO.output(Motor2.in1,GPIO.HIGH)
        GPIO.output(Motor2.in2,GPIO.LOW)
        p.ChangeDutyCycle(Motor2.speed)
        time.sleep(10)

class ColorSensor:
    red = 0
    blue = 0
    green = 0

    def cs(self):
        s2 = 17 #pins can change
        s3 = 27 #pins can change
        signal = 22 #pins can change
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
