#!/usr/bin/env python
from RPLCD.i2c import CharLCD

lcd=CharLCD('PCF8574', 0x27)
lcd.clear()