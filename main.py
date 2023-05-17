from gpiozero import OutputDevice
from time import sleep

motor = OutputDevice(2)

motor.on()
sleep(4)
motor.close()