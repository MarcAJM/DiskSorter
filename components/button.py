
# The initialization code looks as follows:
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
# TODO: change gpio pin number
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)

# The pull_up_down parameter in the GPIO.setup call tells the Raspberry Pi which state the pin should be in
#    when there is nothing connected to the pin.
# This is important since we want our program to read a low state when the button is not pushed
#    and a high state when the button is pushed.
#  With the port initialized we can write the code that continuously reads the port and outputs a message
#    when the button is pressed. We use the GPIO.input function to read the state of the port.

while True: # Run forever
    if GPIO.input(10) == GPIO.HIGH:
        print("Button was pushed")

# Now it is just a matter of executing the program. 