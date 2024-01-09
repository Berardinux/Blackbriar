# DC motor
import RPi.GPIO as GPIO
import time
# Controller
import evdev
import numpy as np

# Motor
GPIO.setmode(GPIO.BOARD)
GPIO.setup(29, GPIO.OUT)
GPIO.setup(31, GPIO.OUT)
pinOneMotor_pwm = GPIO.PWM(29, 1000)
pinTwoMotor_pwm = GPIO.PWM(31, 1000)  # PWM pin
pinOneMotor_pwm.start(0)
pinTwoMotor_pwm.start(0)

# Controller
def map_value(value, in_min, in_max, out_min, out_max):
    return np.interp(value, [in_min, in_max], [out_min, out_max])
device = evdev.InputDevice('/dev/input/event0')
print(device)

# Motor control methods
def forward(speed):
    print(f"Going Forward at {speed}%")
    GPIO.output(31, False)
    pinOneMotor_pwm.ChangeDutyCycle(speed)

def backward(speed):
    print(f"Going Backward at {speed}%")
    GPIO.output(29, False)
    pinTwoMotor_pwm.ChangeDutyCycle(speed)

def stop():
    print("Stopping")
    GPIO.output(29, False)  # IN1
    time.sleep(1)
    motor_pwm.ChangeDutyCycle(0)

# Event loop
for event in device.read_loop():
    if event.type == evdev.ecodes.EV_ABS:
        # Right Trigger
        if event.code == evdev.ecodes.ABS_GAS:
            speed = round(map_value(event.value, 0, 1023, 0, 100))
            print(f"Right Trigger: {event.value}")
            forward(speed)
        # Left Trigger
        elif event.code == evdev.ecodes.ABS_BRAKE:
            speed = round(map_value(event.value, 0, 1023, 0, 100))
            print(f"Left Trigger: {event.value}")
            backward(speed)
    # Right Bumper
    elif event.type == evdev.ecodes.EV_KEY and event.code == evdev.ecodes.BTN_TR and event.value == 1:
        stop()

