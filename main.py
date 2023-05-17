from gpiozero import Motor
from time import sleep

motor = Motor(2)

time = input("Sleep time: ")

while True:
    motor.forward()
    sleep(float(time))
    motor.stop()
    sleep(float(time))
    motor.backward
    sleep(float(time))
    motor.stop()
    sleep(float(time))