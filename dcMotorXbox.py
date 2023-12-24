import RPi.GPIO as GPIO
import time
import evdev
import numpy as np

Pin16 = 16
Pin18 = 18
Pin22 = 22

GPIO.setmode(GPIO.BOARD)
GPIO.setup(Pin16, GPIO.OUT)
GPIO.setup(Pin18, GPIO.OUT)
GPIO.setup(Pin22, GPIO.OUT)

pwm_frequency = 1000
pwm_speed = GPIO.PWM(Pin22, pwm_frequency)
pwm_speed.start(0)

# Controller
def map_value(value, in_min, in_max, out_min, out_max):
    return np.interp(value, [in_min, in_max], [out_min, out_max])

def forward(speed):
    print(f"Going Forward at {speed}%")
    GPIO.output(Pin16, True)
    GPIO.output(Pin18, False)
    pwm_speed.ChangeDutyCycle(speed)

def backward(speed):
    print(f"Going Backward at {speed}%")
    GPIO.output(Pin16, False)
    GPIO.output(Pin18, True)
    pwm_speed.ChangeDutyCycle(speed)

def stop():
    print("Stopping")
    GPIO.output(Pin16, False)
    GPIO.output(Pin18, False)
    time.sleep(1)
    pwm_speed.ChangeDutyCycle(0)

# Controller
device = evdev.InputDevice('/dev/input/event0')
print(device)

for event in device.read_loop():
    if event.type == evdev.ecodes.EV_ABS:
        if event.code == evdev.ecodes.ABS_GAS:
            speed = round(map_value(event.value, 0, 1023, 0, 100))
            print(f"Right Trigger: {event.value}")
            forward(speed)
        elif event.code == evdev.ecodes.ABS_BRAKE:
            speed = round(map_value(event.value, 0, 1023, 0, 100))
            print(f"Left Trigger: {event.value}")
            backward(speed)
    elif event.type == evdev.ecodes.EV_KEY and event.code == evdev.ecodes.BTN_A and event.value == 0:
        stop()
