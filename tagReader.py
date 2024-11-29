#!/usr/bin/env python
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from time import sleep

while True:
    reader = SimpleMFRC522()
    try:
            print("\nAwaiting for scan...")
            tagId = reader.read()[0] # Tag Id
            tagValue = reader.read()[1] # Tag Value
            print("RFID tag id:", tagId)
            print("RFID tag value:", tagValue)
    finally:
            print("Cleaning...")
            GPIO.cleanup()
            sleep(2)
