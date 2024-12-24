#!/usr/bin/env python
from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from time import sleep
import re

GPIO.setwarnings(False)

deviceId=""
clientId=""
clientSecret=""

def isSong(uri): # Check if uri is for a song
    return uri.startswith("spotify:track:")

def isAlbum(uri): # Check if uri is for an album
    return uri.startswith("spotify:album:")

def isPlaylist(uri): # Check if uri is for a playlist
    return uri.startswith("spotify:playlist:")

while True:
    try:
        reader = SimpleMFRC522()
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=clientId, client_secret=clientSecret, redirect_uri="http://localhost:8080", scope="user-read-playback-state,user-modify-playback-state"))
        
        while True:
            print("\n\nAwaiting for scan...")
            id=reader.read()[0]  # Reads the ID of the scanned tag
            uri=reader.read()[1].strip()  # Read the URI written on the tag
            print("Tag Id:", id)
            print("Tag Value:", uri)
                
            sp.transfer_playback(device_id=deviceId, force_play=False)

            if isSong(uri):  # If it's a track
                sp.start_playback(device_id=deviceId, uris=[uri])  # Use uris for track
            elif isAlbum(uri) or isPlaylist(uri):  # If it's an album or a playlist
                sp.start_playback(device_id=deviceId, context_uri=uri)  # Use context_uri for album/playlist
            elif uri.strip(): # If there is no value yet
                pass
            else:
                print("Unknown URI format, check the tag's value.")

            # Basic Spotify controls, update with your own tag id's
            if (id==481439137621):# Skip Forward
                sp.next_track(device_id=deviceId)
                sp.start_playback(device_id=deviceId)
            elif (id==894108319680):# Backtrack
                sp.previous_track(device_id=deviceId)
                sp.previous_track(device_id=deviceId)
                sp.start_playback(device_id=deviceId)
            elif (id==825439240140):# Pause
                sp.pause_playback(device_id=deviceId)
                continue # Make sure we don't reach the next start playback 
            elif (id==894544592811):# Resume
                sp.start_playback(device_id=deviceId)
            elif (id==276472086309):# Shuffle On
                sp.shuffle(state=True, device_id=deviceId)
                sp.start_playback(device_id=deviceId)
                print("Shuffle On")
            elif (id==207718989654):# Shuffle Off
                sp.shuffle(state=False, device_id=deviceId)
                sp.start_playback(device_id=deviceId)
                print("Shuffle Off")
                
            sleep(1.5)
            sp.start_playback(device_id=deviceId) # Continue playing songs when in an album

    except Exception as e:
        print(e)
        pass

    finally:
        print("Cleaning...")
        GPIO.cleanup()
