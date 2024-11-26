#!/usr/bin/env python
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Replace with your own
deviceId=""
clientId=""
clientSecret=""

# Authenticate on Spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=clientId, client_secret=clientSecret, redirect_uri="http://localhost:8080", scope="user-read-playback-state,user-modify-playback-state"))

# Set playback to the Raspberry Pi, in case it is set to another decvice
sp.transfer_playback(device_id=deviceId, force_play=False)

# Test playing a song
sp.start_playback(device_id=deviceId, uris=['spotify:track:45vW6Apg3QwawKzBi03rgD'])
