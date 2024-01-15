import evdev
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
servo = GPIO.PWM(11,50)
servo.start(0)

controllerInput = evdev.InputDevice("/dev/input/event0")

try:
    for event in controllerInput.read_loop():
        if event.type == evdev.ecodes.EV_ABS:
            if event.code == evdev.ecodes.ABS_X:
                angle = 5.7 + (event.value / 21845)
                servo.ChangeDutyCycle(angle)
                print(angle)

except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
