# Connect xboxcontroller to bluetooth
bluetoothctl
scan on
pair XX:XX:XX:XX:XX:XX
trust XX:XX:XX:XX:XX:XX
connect XX:XX:XX:XX:XX:XX

# Look at controller raw output
sudo evtest /dev/input/event0

# udev rules
/etc/udev/rules.d/99-Blackbriar.rules
sudo udevadm control --reload-rules

# Systemd
/etc/systemd/system/blackbriar-monitor.service
sudo systemctl daemon-reload
sudo systemctl status blackbriar-monitor.service
