from gpiozero import Motor
from time import sleep

motor = Motor(20, 16)

motor.forward()
sleep(2)
motor.forward(.5)
sleep(2)
motor.forward(.2)
sleep(2)
motor.forward()
sleep(2)
motor.stop()
