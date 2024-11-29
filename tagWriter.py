#!/usr/bin/env python
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from time import sleep

while True:
    reader = SimpleMFRC522()
    try:
        uri = input("\nEnter the Spotify URI (ex. spotify:track:7KA4W4McWYRpgf0fWsJZWB): ")
        print("Double check Spotify URI:", uri)
        print("Place RFID tag on reader now.")
        reader.write(uri)
        print("Successfully wrote to RFID tag!")
    except Exception as e:
        print("Error writing to RFID tag:", e)
    finally:
        print("Cleaning...")
        GPIO.cleanup()
        sleep(2)

