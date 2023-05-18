import RPi.GPIO as GPIO

# Set the GPIO mode and channel
GPIO.setmode(GPIO.BCM)
pin = 17

# Set up the GPIO channel as an input
GPIO.setup(pin, GPIO.IN)

try:
    while True:
        # Read the analog input value
        potentiometer_value = GPIO.input(pin)

        # Calculate the speed based on the potentiometer value
        speed = potentiometer_value / 10.23 

finally:
    GPIO.cleanup()