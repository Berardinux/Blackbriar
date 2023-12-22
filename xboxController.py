import evdev

device = evdev.InputDevice('/dev/input/event0')

print(device)

for event in device.read_loop():
    if event.type == evdev.ecodes.EV_KEY:
        if event.value == 1:
            if event.code == evdev.ecodes.BTN_A:
                print("Button A pressed")
            elif event.code == evdev.ecodes.BTN_B:
                print("Button B pressed")
            elif event.code == evdev.ecodes.BTN_X:
                print("Button X pressed")
            elif event.code == evdev.ecodes.BTN_Y:
                print("Button Y pressed")
    elif event.type == evdev.ecodes.EV_ABS:
        if event.value == 3:
            # Left Analog Stick
            if event.code == evdev.ecodes.ABS_X:
                print(f"Joystick X: {event.value}")
            elif event.code == evdev.ecodes.ABS_Y:
                print(f"Joystick Y: {event.value}")
            # Right Trigger
            elif event.code == evdev.ecodes.ABS_GAS:
                print(f"Right Trigger: {event.value}")
            # Left Trigger
            elif event.code == evdev.ecodes.ABS_BRAKE:
                print(f"Left Trigger: {event.value}")
