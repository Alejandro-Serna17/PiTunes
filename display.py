#!/usr/bin/env python
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from time import sleep
from RPLCD.i2c import CharLCD

deviceId = "98bb0735e28656bac098d927d410c3138a4b5bca"
clientId = "461faaead1ac4dd79c15e71b136c3cb9"
clientSecret = "5556e041f54544d9a35934a5c2a3a440"
lcd = CharLCD('PCF8574', 0x27)
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=clientId, client_secret=clientSecret, redirect_uri="http://localhost:8080", scope="user-read-playback-state,user-modify-playback-state"))

def playback():
    playbackState = sp.current_playback()  # Check if there is any playback information
    if playbackState:
        songName = playbackState['item']['name']
        return songName
    else:
        return "No playback information available."
    
hold = None
while True:
    try:        
        while True:
            check = playback()
            if check != hold:
                playbackState = sp.current_playback()  # Check if there is any playback information
                songName = playbackState['item']['name']
                artist = playbackState['item']['artists'][0]['name']
                albumName = playbackState['item']['album']['name']
                lcd.clear()
                sleep(0.5)
                lcd.cursor_pos=(0,0)
                lcd.write_string(songName)
                sleep(0.5)
                lcd.cursor_pos=(1,0)
                lcd.write_string(albumName)
                sleep(0.5)
                lcd.cursor_pos=(2,0)
                lcd.write_string(artist)
                sleep(0.5)
                lcd.cursor_pos=(3,0)
                lcd.write_string("Powered by PiTunes")
                hold = check
            
        sleep(1)

    except Exception as e:
        print(e)
        pass

    finally:
        print("Cleaning...")
        lcd.clear()

