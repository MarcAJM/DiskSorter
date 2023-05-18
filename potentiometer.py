import RPi.GPIO as GPIO

# Set the GPIO mode and channel
GPIO.setmode(GPIO.BCM)
channel = 17

# Set up the GPIO channel as an input
GPIO.setup(channel, GPIO.IN)

try:
    while True:
        # Read the analog input value
        potentiometer_value = GPIO.input(channel)

        # Calculate the speed based on the potentiometer value
        speed = potentiometer_value / 1023.0  # Adjust this scaling factor if needed

finally:
    GPIO.cleanup()