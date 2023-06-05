import RPi.GPIO as GPIO
import time

s2 = 23 #pins can change
s3 = 24 #pins can change
signal = 25 #pins can change
NUM_CYCLES = 10

#note this prints the RGB values in Hz

def setup():
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(signal,GPIO.IN, pull_up_down=GPIO.PUD_UP)
  GPIO.setup(s2,GPIO.OUT)
  GPIO.setup(s3,GPIO.OUT)
  print("\n")

def loop():
  y = True

  while(y):  

    print("type 'r' to retrive rgb values in hz, type 'e' ro end the program")
    x = input()

    if (x == 'r'):
      GPIO.output(s2,GPIO.LOW)
      GPIO.output(s3,GPIO.LOW)
      time.sleep(0.3)
      start = time.time()
      for impulse_count in range(NUM_CYCLES):
        GPIO.wait_for_edge(signal, GPIO.FALLING)
      duration = time.time() - start #seconds to run for loop
      red  = NUM_CYCLES / duration #in Hz

      GPIO.output(s2,GPIO.LOW)
      GPIO.output(s3,GPIO.HIGH)
      time.sleep(0.3)
      start = time.time()
      for impulse_count in range(NUM_CYCLES):
        GPIO.wait_for_edge(signal, GPIO.FALLING)
      duration = time.time() - start
      blue = NUM_CYCLES / duration #in Hz

      GPIO.output(s2,GPIO.HIGH)
      GPIO.output(s3,GPIO.HIGH)
      time.sleep(0.3)
      start = time.time()
      for impulse_count in range(NUM_CYCLES):
        GPIO.wait_for_edge(signal, GPIO.FALLING)
      duration = time.time() - start
      green = NUM_CYCLES / duration #in Hz

      print("red value - ",red) #prints R value
      print("blue value - ",blue) #prints B value
      print("green value - ",green) #prints G value
    
    if (x != ('r' or 'e')):
       print("type a valid input")

    if (x == 'e'):
       y = False

def endprogram():
    GPIO.cleanup()

if __name__=='__main__':
    setup()

    try:
        loop()

    except KeyboardInterrupt:
        endprogram()
