#!/usr/bin/env python3

# Import functions that should be used when communicating
# with the device.
# Note that pyserial is needed to use the library.
# See utils.py for more details about this and how to use the functions.
from utils import establish_connection, readln, writeln, user_input
from time import sleep

# Establish a connection
# Edit name of device                        v v v   
serial_device = establish_connection(device="COM15")
sleep(0.5)

# Reset the device to start from the beginning
writeln(serial_device, 'reset')

# Read and print until no further input
while True:
    line = readln(serial_device)
    if not line:
        break

# Write one line of user input to device
writeln(serial_device, user_input())

# Read and print until no further input
while True:
    line = readln(serial_device)
    if not line:
        break

print("Done")
