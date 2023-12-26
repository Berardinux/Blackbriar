#!/bin/bash

# Run the command and capture the output
output=$(ls /dev/input | grep event0)

# Check if the output is not empty
if [ -n "$output" ]; then
  echo "Command produced output: $output"
else
  echo "Command did not produce any output."
  python3 dcMotorXbox.py
  python3 servoXbox.py
fi