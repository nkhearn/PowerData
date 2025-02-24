#!/usr/bin/python
# -*- coding:utf-8 -*-

# reads analogue to digital converter
# retreiving sensor data

import smbus 
import time 
address = 0x48 
A0 = 0x40 
A1 = 0x41
A2 = 0x42
A3 = 0x43

def readv():
  bus = smbus.SMBus(1) 
  time.sleep(0.1)
  bus.write_byte(address, A2) 
  time.sleep(0.1)
  value = bus.read_byte(address)
  return value


# Calibrate reading as required.
# Loop until valid reading is received
# as some ADCs are slow or noisy.

while True:
  value = readv()
  if value > 127:
      print(value)
      time.sleep(0.1)
      break
