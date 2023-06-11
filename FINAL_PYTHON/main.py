#imports
import os
import sys 
import time
import logging
import spidev as SPI
sys.path.append('') #add path and CHECK IMPORTS
import LCD_1inch54
import LCD_1inch3
from PIL import Image,ImageDraw,ImageFont
import RPi.GPIO as GPIO          
from time import sleep

#main code starts now
class Main:

    def run(self):

        #variable for the while loop to run the code
        z = True

        print("type 'r' to run the main code, type 'e' to end the program once main code is executed")

        while (z):

            x = input() #take keyboard input
            
            if x=='r':
                Helper.m1(self) #run helper class method
                x = 'z'
            
            if x == 'e':
                GPIO.cleanup() #cleanup pins
                z = False
                break

            if x != 'r' or x != 'e':
                print("type a valid input")
    
class Helper:

    def m1(self):

        #motor1 (Helper) --> runs the main belt
        #motor2 (Motor2) --> sorts the black disks
        #motor3 (Motor3) --> sorts the white disks

        #setup the motors so they operate
        SetupMotors.setupm1m2m3(self)

        #variable for while loop
        k = 0
        
        #while loop to run the belt
        while k < 100: 

            #run colorsensor class
            ColorSensor.cs(self)

            #retrieve rgb values from running colorsensor class
            r = ColorSensor.red
            g = ColorSensor.green
            b = ColorSensor.blue
            
            #print rgb values to check
            print("red value - ",r) #prints R value
            print("blue value - ",b) #prints B value
            print("green value - ",g, "/n") #prints G value
            
            #indefinitely run motor1 with motor2 and motor3 off
            Motor1.runm1f(self)
            Motor2.stopm2(self)
            Motor3.stopm3(self)
            time.sleep(0.01)
        
            #if black then jump to another part in the code
            if (18000 < r < 32000) and (22000 < b < 31000) and (21000 < g < 27000): #check this based on environment later
                
                Black.blackdetected(self)

            #if white then jump to another part in the code
            elif (18000 < r < 32000) and (22000 < b < 31000) and (21000 < g < 27000): #check this based on environment later
                
                White.whitedetected(self)

            else:
                #increment k for the while loop
                k = k + 1

class Motor1:

    #pins motor1 (belt)
    in1 = 5 #input 1 pin
    in2 = 6 #input 2 pin
    en = 26 #enable pin
    temp1= 1 #temporary variable (to alter the speed of the motor etc.)
    speed = 100 #speed of the motor

    #speed control motor1
    p1 = 0

    #run motor1 in forward direction
    def runm1f(self):

        #run the motor at maximum speed
        GPIO.output(Motor1.in1, GPIO.HIGH)
        GPIO.output(Motor1.in2, GPIO.LOW)
        Motor1.p1.start(100)
    
    #run motor1 in backward direction
    def runm1b(self):

        #run the motor at maximum speed
        GPIO.output(Motor1.in1, GPIO.LOW)
        GPIO.output(Motor1.in2, GPIO.HIGH)
        Motor1.p1.start(100)
    
    #stop motor1
    def stopm1(self):

        #stop the motor immediately
        Motor1.p1.stop()
        GPIO.output(Motor1.en, GPIO.LOW)
        GPIO.output(Motor1.in1, GPIO.LOW)
        GPIO.output(Motor1.in2, GPIO.LOW)

class Motor2:
    
    #pins motor2 (push black)
    in1 = 23 #input 1 pin
    in2 = 24 #input 2 pin
    en = 16 #enable pin
    temp1= 1 #temporary variable (to alter the speed of the motor etc.)
    speed = 100

    #speed control motor2
    p2 = 0

    #run motor2 in forward direction
    def runm2f(self):

        #run the motor at maximum speed
        GPIO.output(Motor2.in1, GPIO.HIGH)
        GPIO.output(Motor2.in2, GPIO.LOW)
        Motor2.p2.start(100)
    
    #run motor2 in backward direction
    def runm2b(self):

        #run the motor at maximum speed
        GPIO.output(Motor2.in1, GPIO.LOW)
        GPIO.output(Motor2.in2, GPIO.HIGH)
        Motor2.p2.start(100)
    
    #stop motor2
    def stopm2(self):

        #stop the motor immediately
        Motor2.p2.stop()
        GPIO.output(Motor2.en, GPIO.LOW)
        GPIO.output(Motor2.in1, GPIO.LOW)
        GPIO.output(Motor2.in2, GPIO.LOW)

class Motor3:
    
    #pins motor3 (push white)
    in1 = 13 #input 1 pin
    in2 = 19 #input 2 pin
    en = 0 #enable pin
    temp1= 1 #temporary variable (to alter the speed of the motor etc.)
    speed = 100

    #speed control motor3
    p3 = 0

    #run motor3 in forward direction
    def runm3f(self):

        #run the motor at maximum speed
        GPIO.output(Motor3.in1, GPIO.HIGH)
        GPIO.output(Motor3.in2, GPIO.LOW)
        Motor3.p3.start(100)

    #run motor3 in backward direction
    def runm3b(self):

        #run the motor at maximum speed
        GPIO.output(Motor3.in1, GPIO.LOW)
        GPIO.output(Motor3.in2, GPIO.HIGH)
        Motor3.p3.start(100)
    
    #stop motor3 
    def stopm3(self):

        #stop the motor immediately
        Motor3.p3.stop()
        GPIO.output(Motor3.en, GPIO.LOW)
        GPIO.output(Motor3.in1, GPIO.LOW)
        GPIO.output(Motor3.in2, GPIO.LOW)

class Black:

    def blackdetected(self):
        
        #variable for while loop
        k = 0
        
        #while loop to run the belt
        while k < 50: #TIME THIS

            #run colorsensor class
            ColorSensor.cs(self)

            #retrieve rgb values from running colorsensor class
            r = ColorSensor.red
            g = ColorSensor.green
            b = ColorSensor.blue
            
            #print rgb values to check
            print("red value - ",r) #prints R value
            print("blue value - ",b) #prints B value
            print("green value - ",g, "/n") #prints G value
            
            #turn motor1 to slide disk into bin
            if k < 5: #time this

                Motor1.runm1f(self)
                Motor2.runm2f(self)
                Motor3.stopm3(self)
                time.sleep(0.01)

            if k > 45: #time this

                Motor1.runm1f(self)
                Motor2.runm2b(self)
                Motor3.stopm3(self)
                time.sleep(0.01)

            #if black then jump to another part in the code
            if (18000 < r < 32000) and (22000 < b < 31000) and (21000 < g < 27000): #check this based on environment later
                
                Black.blackdetected(self) #recurse the same code again

            #if white then jump to another part in the code
            elif (18000 < r < 32000) and (22000 < b < 31000) and (21000 < g < 27000): #check this based on environment later
                
                print("jump to another part in the code") #FINISH THIS LATER

            else:
                #increment k for the while loop
                k = k + 1

class White:

    def whitedetected(self):
        
        #variable for while loop
        k = 0
        
        #while loop to run the belt
        while k < 50: #TIME THIS

            #run colorsensor class
            ColorSensor.cs(self)

            #retrieve rgb values from running colorsensor class
            r = ColorSensor.red
            g = ColorSensor.green
            b = ColorSensor.blue
            
            #print rgb values to check
            print("red value - ",r) #prints R value
            print("blue value - ",b) #prints B value
            print("green value - ",g, "/n") #prints G value
            
            #turn motor1 to slide disk into bin
            if k < 5: #time this

                Motor1.runm1f(self)
                Motor2.stopm2(self)
                Motor3.runm3f(self)
                time.sleep(0.01)

            if k > 35: #time this

                Motor1.runm1f(self)
                Motor2.stopm2(self)
                Motor3.runm3b(self)
                time.sleep(0.01)

            #if black then jump to another part in the code
            if (18000 < r < 32000) and (22000 < b < 31000) and (21000 < g < 27000): #check this based on environment later
                
                print("jump to another part in the code") #FINISH THIS LATER

            #if white then jump to another part in the code
            elif (18000 < r < 32000) and (22000 < b < 31000) and (21000 < g < 27000): #check this based on environment later
                
                White.whitedetected(self) #recurse the same code again

            else:
                #increment k for the while loop
                k = k + 1

class SetupMotors:

    #setup all the motors simultaneously
    def setupm1m2m3(self):
        
        #to setup pins
        GPIO.setmode(GPIO.BCM)

        #set pins to OUTPUT pins motor1
        GPIO.setup(Motor1.in1,GPIO.OUT) 
        GPIO.setup(Motor1.in2,GPIO.OUT)
        GPIO.setup(Motor1.en,GPIO.OUT)

        #set pins to OUTPUT pins motor2
        GPIO.setup(Motor2.in1,GPIO.OUT) 
        GPIO.setup(Motor2.in2,GPIO.OUT)
        GPIO.setup(Motor2.en,GPIO.OUT)

        #set pins to OUTPUT pins motor3
        GPIO.setup(Motor3.in1,GPIO.OUT) 
        GPIO.setup(Motor3.in2,GPIO.OUT)
        GPIO.setup(Motor3.en,GPIO.OUT)

        #initial state LOW (so motor is off) motor1
        GPIO.output(Motor1.in1,GPIO.LOW)
        GPIO.output(Motor1.in2,GPIO.LOW)

        #initial state LOW (so motor is off) motor2
        GPIO.output(Motor2.in1,GPIO.LOW)
        GPIO.output(Motor2.in2,GPIO.LOW)

        #initial state LOW (so motor is off) motor3
        GPIO.output(Motor3.in1,GPIO.LOW)
        GPIO.output(Motor3.in2,GPIO.LOW)

        #speed control setup motor1
        Motor1.p1=GPIO.PWM(Motor1.en, 100)
        Motor1.p1.start(25)

        #speed control setup motor2
        Motor2.p2=GPIO.PWM(Motor2.en, 100)
        Motor2.p2.start(25)

        #speed control setup motor3
        Motor3.p3=GPIO.PWM(Motor3.en, 100)
        Motor3.p3.start(25)

class ColorSensor:
    red = 0
    blue = 0
    green = 0

    def cs(self):
        s2 = 2 #pins can change
        s3 = 3 #pins can change
        signal = 4 #pins can change
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
    
    # Constructor:
    def __init__(self):
        self.display = LCD_1inch3.LCD_1inch3()
        self.display.Init()     # Initialize library.
        self.display.clear()    # Clear display.

    # Everytime the screen needs to get an update call this method:
    def update_display(self, speed, white_disks, black_disks, error_message, status_message):
        try:
            image = Image.new("RGB", (self.display.width, self.display.height), "BLACK") 
            draw = ImageDraw.Draw(image)
            font = ImageFont.truetype("/home/marcajm/Desktop/DiskSorter/fonts/font1.ttf", 20)

            # Change the text:
            draw.text((5, 5), 'Speed: {}%'.format(speed), fill = 'WHITE',font=font) 
            draw.text((5, 35), 'White disks: {}'.format(white_disks), fill = 'WHITE',font=font) 
            draw.text((5, 65), 'Black disks: {}'.format(black_disks), fill = 'WHITE',font=font) 
            draw.text((5, 125), error_message, fill = 'RED',font=font)
            draw.text((5, 155), status_message, fill = 'RED', font=font)
            # Display the image and exit:
            self.display.ShowImage(image)
            self.display.module_exit()

        except IOError as e:
            logging.info(e)    

        except KeyboardInterrupt:
            self.display.module_exit()
            logging.info("quit:")
            exit()

#run the code
if __name__ == "__main__":
    main = Main()
    main.run()
