# Connect xboxcontroller to bluetooth
bluetoothctl
scan on
pair XX:XX:XX:XX:XX:XX
trust XX:XX:XX:XX:XX:XX
connect XX:XX:XX:XX:XX:XX

# Look at controller raw output
sudo evtest /dev/input/event0
