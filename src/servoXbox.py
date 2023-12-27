# Servo
import RPi.GPIO as GPIO
import time
# Controller
import evdev
import numpy as np

# Servo
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
servo = GPIO.PWM(11,50)
servo.start(89)

# Controller
def map_value(value, in_min, in_max, out_min, out_max):
    return np.interp(value, [in_min, in_max], [out_min, out_max])
device = evdev.InputDevice('/dev/input/event0')
print(device)

for event in device.read_loop():
    if event.type == evdev.ecodes.EV_ABS:
        # Left Analog Stick
        if event.code == evdev.ecodes.ABS_X:
            angle = round(map_value(event.value, 0, 65536, 0, 179))
            print(angle)
            # Servo
            duty_cycle = 2 + (angle / 18)
            print(duty_cycle)
            servo.ChangeDutyCycle(duty_cycle)
