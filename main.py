from components import motor, solenoid
# from components import error_button
from sensors import color_sensor
from ui import potentiometer, screen
from time import sleep

# Some important initial variables:
speed = 100
white_disks = 0
black_disks = 0
error_message = "Press the button to run error diagnostics."
status_message = ""
# error_boolean = False
# button_state = False

# Everything we need on the robot:
conv_motor = motor.Motor(5, 6, 26, speed)
solenoid_a = solenoid.Solenoid(4, 2)
solenoid_b = solenoid.Solenoid(5, 2)
color_sensor = color_sensor.Color_sensor()
potentiometer = potentiometer.Potentiometer(17)
screen = screen.Screen()
# TODO: change gpio pin error_button = error_button.Error_button(10)

# TODO: change gpio pin if GPIO.input(10) == GPIO.HIGH:
#    error_boolean = True


# if error_boolean:
#   error_check()

# def error_check():
#   error_message = 'Press the button once for 'no' and hold for 2 seconds for 'yes'. To continue, hold for 2 seconds. To exit error diagnostics, hold for 5 seconds'
#   screen.update_display(speed, white_disks, black_disks, error_message, status_message)
#   if GPIO.input(10) == GPIO.HIGH:
#       time.sleep(2)
#       if GPIO.input(10) == GPIO.HIGH:
#           time.sleep(3)
#               if GPIO.input(10) == GPIO.HIGH:
#                   return

# optimise the code below with a loop???
#   error_message = 'Are there any external obstructions?'    
#   screen.update_display(speed, white_disks, black_disks, error_message, status_message)
#   button_state = button_state()
#   if button_state == True:
#       error_message = 'Remove any external obstructions from the robot'
#       screen.update_display(speed, white_disks, black_disks, error_message, status_message)
#           return

#   error_message = 'Is the buzzer beeping?'
#   screen.update_display(speed, white_disks, black_disks, error_message, status_message)
#   button_state = button_state()
#   if button_state == True:
#       error_message = 'The robot has been lifted. Place it on the surface.'
#       screen.update_display(speed, white_disks, black_disks, error_message, status_message)
#           return
#   
#   error_message = 'Is the belt running?'
#   screen.update_display(speed, white_disks, black_disks, error_message, status_message)
#   button_state = button_state()
#   if button_state == True:
#       error_message = 'Turn the belt on and check if there are any motors that aren't turning.'
#       screen.update_display(speed, white_disks, black_disks, error_message, status_message)
#           return   
#                   
#           
# def button_state():
#   if GPIO.input(10) == GPIO.HIGH:
#       time.sleep(2)
#           if GPIO.input(10) == GPIO.HIGH:
#               return True
#           else:
#               return False
#               

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

    else:
        status_message = "UNKNOWN OBJECT"
        
    # TODO: We need to find the color that it will measure when there is no object in front of the sensor.
    #       This will be the normal situation and nothing will be done here.
        

    screen.update_display(speed, white_disks, black_disks, error_message, status_message)
    sleep(0.1) # Wait a little
