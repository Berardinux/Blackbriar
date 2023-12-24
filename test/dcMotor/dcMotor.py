import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

# first motor | left on the fritzing diagram
motor1_endpoint1 = 16  # endpoint 1 of motor 1
motor1_endpoint2 = 18  # endpoint 2 of motor 1
motor1_enable = 22     # first motor enable pin

GPIO.setup(motor1_endpoint1, GPIO.OUT)
GPIO.setup(motor1_endpoint2, GPIO.OUT)
GPIO.setup(motor1_enable, GPIO.OUT)


print("Going Forward")

GPIO.output(motor1_endpoint1, True)
GPIO.output(motor1_endpoint2, False)
GPIO.output(motor1_enable, True)

sleep(3)
GPIO.output(motor1_enable,False)
GPIO.output(motor1_endpoint1, False)
GPIO.output(motor1_endpoint2, False)
sleep(3)
GPIO.output(motor1_enable, True)

print("Going Backward")

GPIO.output(motor1_endpoint1, False)
GPIO.output(motor1_endpoint2, True)

print("Turning Off DC Motors")

GPIO.output(motor1_enable, False)

print("DC Motors Turned Off")