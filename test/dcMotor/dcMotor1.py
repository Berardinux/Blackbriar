import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

Pin16 = 16
Pin18 = 18
Pin22 = 22

GPIO.setup(Pin16, GPIO.OUT)
GPIO.setup(Pin18, GPIO.OUT)
GPIO.setup(Pin22, GPIO.OUT)

pwm_frequency = 1000
pwm_speed = GPIO.PWM(Pin22, pwm_frequency)
pwm_speed.start(0)

def forward(speed):
  print(f"Going Backward at {speed}%")
  GPIO.output(Pin16, True)
  GPIO.output(Pin18, False)
  pwm_speed.ChangeDutyCycle(speed)

def backward(speed):
  print(f"Going Backward at Speed {speed}%")
  GPIO.output(Pin16, False)
  GPIO.output(Pin18, True)
  pwm_speed.ChangeDutyCycle(speed)

def stop():
  print("Stopping")
  GPIO.output(Pin16, False)
  GPIO.output(Pin18, False)
  sleep(1)
  pwm_speed.ChangeDutyCycle(0)

try:
  forward(50)
  sleep(3)
  stop()
  backward(75)
  sleep(3)

finally:
  print("Turning Off DC Motors")
  pwm_speed.stop()
  GPIO.cleanup()
  print("DC Motors Turned Off")