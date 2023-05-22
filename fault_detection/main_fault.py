print("main fault has occurred")

#function go brrrr
def troubleshoot(manual):
    if manual != default_manual: troubleshoot(default_manual)
    
    for x in manual:
        print(x)
        #wait for button press
    print("Final: If none of the previous instructions worked, replace the part with a new one.")

#example: troubleshoot(buzzer_manual)

#step 1, step 2, step 3...
default_manual = [
    "1: Check that there are no external obstructions"
    "2: Check that the component is mechanically secured on the robot",
    "3: Check that the component is electrically connected to its corresponding parts"
]

buzzer_manual = [
    "4: If the buzzer is beeping, the robot has been lifted. Place the robot on a solid surface."
]

sensor_manual = [
    "4: Check that the sensor isn't dirty"
    "5: Check that the light level isn't too high or too low"
]

belt_manual = [ 
    "4: Turn the belt on and check if there are any motors that aren't turning"
]

rpi_manual = [
    "4: Check that the RPi has power",
    "5: Check that code runs on the RPi",
]

pistons_manual = [
    "4: Push the piston manually and let it go. It should fully push in and return to its original position upon release"
]

buttons_manual = [
    "4: Check that the buttons are in the correct order"
]