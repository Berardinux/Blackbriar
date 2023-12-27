# Connect xboxcontroller to bluetooth
bluetoothctl
scan on
pair XX:XX:XX:XX:XX:XX
trust XX:XX:XX:XX:XX:XX
connect XX:XX:XX:XX:XX:XX

# Look at Controller raw output
sudo evtest /dev/input/event0

# udev rules
sudo nano /etc/udev/rules.d/99-Blackbriar.rules {
SUBSYSTEM=="input", KERNELS=="event0", ACTION=="add", RUN+="/bin/systemctl start Blackbriar.service"
}
sudo udevadm control --reload-rules


# Systemd
sudo nano /etc/systemd/system/blackbriar-monitor.service {
[Unit]
Description=Blackbriar Monitor Service
After=udev.service

[Service]
Type=simple
ExecStart=/home/berardinux/Documents/Blackbriar/Blackbriar.sh

[Install]
WantedBy=multi-user.target
}
sudo systemctl daemon-reload
sudo systemctl status blackbriar-monitor.service
