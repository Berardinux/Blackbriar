#!/bin/bash

# Is the Xbox Controller connected?
isControllerConnected=$(ls /dev/input | grep event0)

# Check if the Xbox Controller is connected.
if [ -n "$isControllerConnected" ]; then
  echo "Command produced isControllerConnected: $isControllerConnected"
  /usr/bin/python3 /home/berardinux/Documents/Blackbriar/src/dcMotorXbox.py &
  /usr/bin/python3 /home/berardinux/Documents/Blackbriar/src/servoXbox.py &
  while [ -n "$isControllerConnected" ]; do
    isControllerConnected=$(ls /dev/input | grep event0)
    echo "The Xbox Controller is still connected"
    sleep 1
  done
  echo "The Xbox Controller is no longer connected."
else
  echo "The Xbox Controller is not connected."
fi
