#!/usr/bin/env python
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from time import sleep

GPIO.setwarnings(False)

while True:
    reader = SimpleMFRC522()
    try:
            print("\nAwaiting for scan...")
            tagId = reader.read()[0] # Tag Id
            tagValue = reader.read()[1] # Tag Value
            print("RFID tag id:", tagId)
            print("RFID tag value:", tagValue)
    except Exception as e:
        print("\nError reading:", e)
    finally:
            print("\nCleaning...")
            GPIO.cleanup()
            sleep(2)
