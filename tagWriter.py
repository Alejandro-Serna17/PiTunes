#!/usr/bin/env python
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from time import sleep

GPIO.setwarnings(False)

while True:
    reader = SimpleMFRC522()
    try:
        uri = input("\nEnter the Spotify URI (e.g., spotify:track:7KA4W4McWYRpgf0fWsJZWB): ")
        print("Double check Spotify URI:", uri)
        print("Place RFID tag on reader now.")
        reader.write(uri)
        print("Successfully wrote to RFID tag!")
    except Exception as e:
        print("Error writing to RFID tag:", e)
    finally:
        print("\nCleaning...")
        GPIO.cleanup()
        sleep(2)
