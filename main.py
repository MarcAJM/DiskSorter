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


error_boolean = True

if error_boolean:
   error_check()

def error_check():

    module_message = [
        "1: Are you having a problem with the buzzer?",
        "2: Are you having a problem with the belt?",
        "3: Are you having problems with sorting?",
    ]

    buzzer_error = [
        "1.1: Is the buzzer beeping when the system is grounded?",
        "1.2: Is the buzzer not beeping when the system is midair?",
        "1.3: Is the buzzer not beeping continuously?",
        " ",
        "2.1: Is the belt struggling to move fast enough?",
        "2.2: Is the belt not moving continuously?",
        "2.3: Is the belt not in place and stretched on the gears?"
        " ",
        "3.1: Are the LEDs of the color sensor working?",
        "3.2: Is the color sensor dirty or obstructed?",
        "3.3: Are the pistons working at all?",
        " ",
        "0: It seems like there are external obstructions."
    ]

    solution_message = [
        "1.1: Check if the conductive part is stuck.",
        "1.2: Check the wiring and check if the conductive part is stuck.",
        "1.3: Check the wiring.",
        " ",
        "2.1: Turn up the speed dial as necessary; if the battery is low, replace it.",
        "2.2: Check the motor-belt connection and fix the wiring.",
        "2.3: Align the belt with the gears.",
        " ",
        "3.1: For more accuracy, temporarily use the flashlight of your phone from an appropriate distance.",
        "3.2: Clean the color sensor and remove any obstructions.",  
        "3.3: Check the connections with the pistons.",
        " ",
        "0: Remove any external obstructions, then restart/resume the system."
    ]


    error_message = "You have entered error diagnostics. 'no': press button once; 'yes': hold for 2 seconds. To exit error diagnostics, hold for 5 seconds. Wait 5 seconds to continue."
    screen.update_display(speed, white_disks, black_disks, error_message, status_message)
    if GPIO.input(10) == GPIO.HIGH:
        time.sleep(5)
        if GPIO.input(10) == GPIO.HIGH:
            return
        else: 

            #functionality is implemented in the following code
            error_message = "To continue, press once"
            screen.update_display(speed, white_disks, black_disks, error_message, status_message)
            #button_state()    

    for i in range(1, len(module_message)):
        if button_state():
            screen.update_display(speed, white_disks, black_disks, module_message[i - 1], status_message)
        else:
            startIndex = 0
            endIndex = 0

            #iterates through the specified problems of the selected module 
            for j in range(startIndex, endIndex):
                screen.update_display(speed, white_disks, black_disks, solution_message[j], status_message) #asks the first question

                #selects whether the next error message is displayed or the solution to the current error is displayed
                if button_state():
                    screen.update_display(speed, white_disks, black_disks, solution_message[j + 1], status_message)   
                else:
                    screen.update_display(speed, white_disks, black_disks, error_message[j], status_message)
                           
    def button_state():
        if GPIO.input(10) == GPIO.HIGH:
            time.sleep(2)
            if GPIO.input(10) == GPIO.HIGH:
                #button pressed for 2 seconds
                return True
            else:
                #button pressed momentarily
                return False
        time.sleep(0.05)
        button_state
        
       
       


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
