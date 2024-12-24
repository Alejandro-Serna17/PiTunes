#!/usr/bin/env python
from time import sleep
from RPLCD.i2c import CharLCD

try:
    lcd = CharLCD('PCF8574', 0x27)
    lcd.clear()
    sleep(0.5)
    lcd.cursor_pos=(0,0)
    lcd.write_string("Welcome to PiTunes!")
    sleep(0.5)
    lcd.cursor_pos=(1,0)
    lcd.write_string("Testing 123...")
    sleep(0.5)
    lcd.cursor_pos=(2,0)
    lcd.write_string("More testing...")
    sleep(0.5)
    lcd.cursor_pos=(3,0)
    lcd.write_string("Powered by PiTunes")
except Exception as e:
    print(e)
finally:
    print("Cleaning...")
    lcd.clear()
