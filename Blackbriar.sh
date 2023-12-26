#!/bin/bash

# Run the command and capture the output
output=$(ls /dev/input | grep event0)

# Check if the output is not empty
if [ -n "$output" ]; then
  echo "Command produced output: $output"
  python3 /home/berardinux/Documents/Blackbriar/dcMotorXbox.py &
  python3 /home/berardinux/Documents/Blackbriar/servoXbox.py &
  while [ -n "$output" ]; do
    output=$(ls /dev/input | grep event0)
    echo "Still connected"
    sleep 1
  done
  
else
  echo "Command did not produce any output."
fi