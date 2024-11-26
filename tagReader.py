#!/usr/bin/env python
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
        print("Awaiting scan...")
        id = reader.read()[0]
        print("Tag Number:", id)
finally:
        print("Cleaning...")
        GPIO.cleanup()
