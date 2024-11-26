#!/usr/bin/env python
from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from time import sleep

# Replace with your own
deviceId=""
clientId=""
clientSecret=""

while True:
    try:
        reader=SimpleMFRC522()
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=clientId, client_secret=clientSecret,redirect_uri="http://localhost:8080",scope="user-read-playback-state,user-modify-playback-state"))

        while True:
            print("\n\nAwaiting for scan...")
            id=reader.read()[0]
            print("Card Value is:",id)
            sp.transfer_playback(device_id=deviceId, force_play=False)

            if (id==841043396814) # Play a song
                sp.start_playback(device_id=deviceId, uris=['spotify:track:7KA4W4McWYRpgf0fWsJZWB'])
                sleep(2)
            elif (id==117456696): # Play an album
                sp.start_playback(device_id=deviceId, context_uri='spotify:album:0qmyud8qe8LqaVQ1YQ7S5G')
                sleep(2)
            elif (id==201408306): # Play a playlist
                sp.start_playback(device_id=deviceId, context_uri='spotify:playlist:7z9Af7AnTmSCLQUjtOHImN')
                sleep(2)
            elif (id==481439137621): # Skip Forward
                sp.next_track(device_id=deviceId)
                sp.start_playback(device_id=deviceId)
                sleep(2)
            elif (id==894108319680): # Backtrack
                sp.previous_track(device_id=deviceId)
                sp.previous_track(device_id=deviceId)
                sp.start_playback(device_id=deviceId)
                sleep(2)
            elif (id==825439240140): # Pause
                sp.pause_playback(device_id=deviceId)
                print("Music is paused")
                sleep(2)
            elif (id==894544592811): # Resume
                sp.start_playback(device_id=deviceId)
                print("Music is playing")
                sleep(2)
            elif (id==276472086309): # Shuffle On
                sp.shuffle(state=True, device_id=deviceId)
                sp.start_playback(device_id=deviceId)
                print("Shuffle On")
                sleep(2)
            elif (id==207718989654): # Shuffle Off
                sp.shuffle(state=False, device_id=deviceId)
                sp.start_playback(device_id=deviceId)
                print("Shuffle Off")
                sleep(2)

            playbackState = sp.current_playback() # Check if there is any playback information
            if playbackState:
                songName=playback_state['item']['name']
                artist=playback_state['item']['artists'][0]['name']
                albumName=playback_state['item']['album']['name']

                print(f"Now Playing: {songName} - {albumName}")
                print(f"By {artist}")
            else:
                print("No playback information available.")

    # if there is an error (ex. no device error, timeour issue, etc), skip iteration to try again.
    except Exception as e:
        print(e)
        pass

    finally:
        print("Cleaning...")
        GPIO.cleanup()
