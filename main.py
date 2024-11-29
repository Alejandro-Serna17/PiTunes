#!/usr/bin/env python
from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from time import sleep
import re

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
            id = reader.read()[0] # Tag id
            uri = reader.read()[1].strip() # Tag value(URI)
            print("Tag Id:", id)
            print("Tag Value:", uri)
            sp.transfer_playback(device_id=deviceId, force_play=False)

            # Play songs, albums, playlists
            if uri:
                if isSong(uri):  # If it's a track
                    sp.start_playback(device_id=deviceId, uris=[uri])  # Use uris for track
                elif isAlbum(uri):  # If it's an album
                    sp.start_playback(device_id=deviceId, context_uri=uri)  # Use context_uri for album
                elif isPlaylist(uri):  # If it's a playlist
                    sp.start_playback(device_id=deviceId, context_uri=uri)  # Use context_uri for playlist
                elif uri.strip(): # If there is no value yet
                    pass
                else:
                    print("Unknown URI format, check the tag's value.")
            sleep(2)

            # Basic Spotify controls, update with your own tag id's
            if (id==481439137621):# Skip Forward
                sp.next_track(device_id=deviceId)
                sp.start_playback(device_id=deviceId)
                sleep(2)
            elif (id==894108319680):# Backtrack
                sp.previous_track(device_id=deviceId)
                sp.previous_track(device_id=deviceId)
                sp.start_playback(device_id=deviceId)
                sleep(2)
            elif (id==825439240140):# Pause
                sp.pause_playback(device_id=deviceId)
                #print("Music is paused")
                sleep(2)
            elif (id==894544592811):# Resume
                sp.start_playback(device_id=deviceId)
                #print("Music is playing")
                sleep(2)
            elif (id==276472086309):# Shuffle On
                sp.shuffle(state=True, device_id=deviceId)
                sp.start_playback(device_id=deviceId)
                print("Shuffle On")
                sleep(2)
            elif (id==207718989654):# Shuffle Off
                sp.shuffle(state=False, device_id=deviceId)
                sp.start_playback(device_id=deviceId)
                print("Shuffle Off")
                sleep(2)

            playbackState = sp.current_playback()  # Check if there is any playback information
            if playbackState:
                songName = playbackState['item']['name']
                artist = playbackState['item']['artists'][0]['name']
                albumName = playbackState['item']['album']['name']

                print(f"Now Playing: {songName} - {albumName}")
                print(f"By {artist}")
            else:
                print("No playback information available.")

    except Exception as e:
        print(e)
        pass

    finally:
        print("Cleaning...")
        GPIO.cleanup()
