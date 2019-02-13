# Written for Python 3
# With love from Alex.
# Modified a bit by Jabbe.

# Requires pyserial and requests installed.
# To install run:
# pip3 install pyserial
# pip3 install requests

import serial
import sys
import requests

# Frequency used when communicating with serial device
DEVICE = "/dev/ttyACM0"
# Frequency used when communicating with serial device
BAUDRATE = 74880
# Timeout for serial connection
TIMEOUT = 1

def establish_connection(device=DEVICE, baudrate=BAUDRATE, timeout=TIMEOUT):
    """Establishes a connection to a serial device"""
    s = serial.Serial(device, baudrate, timeout=timeout)
    return s

def publish(s):
    url = 'http://ec2-18-195-248-134.eu-central-1.compute.amazonaws.com/publish'
    requests.post(url, data=s)

def readln(serial_device):
    """Reads one line from a serial port"""
    line = serial_device.readline().decode("utf-8")
    print(line)
    prefix = "Level completed "
    if line.startswith(prefix):
        publish(line[len(prefix):].strip())
    return line

def writeln(serial_device, message):
    """Writes one line to the serial port"""
    serial_device.write((message + '\n').encode('utf-8'))

def user_input():
    """Reads one line from stdin and returns it"""
    user_message = str(input("Enter your message: "))
    return user_message
