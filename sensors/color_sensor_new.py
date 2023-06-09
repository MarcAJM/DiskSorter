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
  temp = 1
  while(1):  

    GPIO.output(s2,GPIO.LOW)
    GPIO.output(s3,GPIO.LOW)
    time.sleep(0.3)
    start = time.time()
    for impulse_count in range(NUM_CYCLES):
      GPIO.wait_for_edge(signal, GPIO.FALLING)
    duration = time.time() - start #seconds to run for loop
    red  = NUM_CYCLES / duration #in Hz
    print("red value - ",red) #prints R value

    GPIO.output(s2,GPIO.LOW)
    GPIO.output(s3,GPIO.HIGH)
    time.sleep(0.3)
    start = time.time()
    for impulse_count in range(NUM_CYCLES):
      GPIO.wait_for_edge(signal, GPIO.FALLING)
    duration = time.time() - start
    blue = NUM_CYCLES / duration #in Hz
    print("blue value - ",blue) #prints B value

    GPIO.output(s2,GPIO.HIGH)
    GPIO.output(s3,GPIO.HIGH)
    time.sleep(0.3)
    start = time.time()
    for impulse_count in range(NUM_CYCLES):
      GPIO.wait_for_edge(signal, GPIO.FALLING)
    duration = time.time() - start
    green = NUM_CYCLES / duration #in Hz
    print("green value - ",green) #prints G value
    time.sleep(2)  

def endprogram():
    GPIO.cleanup()

if __name__=='__main__':
    setup()

    try:
        loop()

    except KeyboardInterrupt:
        endprogram()
