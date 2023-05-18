from components import motor, solenoid
from sensors import color_sensor
from ui import potentiometer, screen
from time import sleep

# Some important initial variables:
speed = 100
white_disks = 0
black_disks = 0
error_message = ""

# Everything we need on the robot:
conv_motor = motor.Motor(5, 6, 26, speed)
solenoid_a = solenoid.Solenoid(4)
solenoid_b = solenoid.Solenoid()
color_sensor = color_sensor.Color_sensor()
potentiometer = potentiometer.Potentiometer(17)
screen = screen.Screen()

# This while loop updates everything of the robot:
while True:

    # This is for obtaining and updating the speed:
    potentiometer_value = potentiometer.get_input
    speed = potentiometer_value / 10.23     # TODO: May not be precise
    conv_motor.change_speed(speed) # Change the speed of the motor
    
    # This is for sensoring the color and updating the amount of disks:
    rgb = color_sensor.get_rgb()
    if rgb < (50, 50, 50):  # Color is black
        black_disks += 1
        solenoid_a.push(0.2)

    elif rgb > (205, 205, 205):  # Color is white
        white_disks += 1
        solenoid_a.push(0.2)
        
    # TODO: We need to find the color that it will measure when there is no object in front of the sensor.
    #       This will be the normal situation and nothing will be done here.
        
    screen.update_display(speed, white_disks, black_disks, error_message)
    sleep(0.1) # Wait a little