#!/usr/bin/env python
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests
from PIL import Image, ImageTk
import tkinter as tk
from io import BytesIO

deviceId=""
clientId=""
clientSecret=""
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=clientId, client_secret=clientSecret, redirect_uri="http://localhost:8080", scope="user-read-playback-state,user-modify-playback-state"))
albumLabel = songLabel = artistLabel = piTunesLabel = None

def info():
    global albumLabel, songLabel, artistLabel, piTunesLabel
    
    playbackState = sp.current_playback()
    albumName = playbackState['item']['album']['name']
    songName = playbackState['item']['name']
    artist = playbackState['item']['artists'][0]['name']
    if songLabel:
        albumLabel.destroy()
        songLabel.destroy()
        artistLabel.destroy()

    albumLabel = tk.Label(root, text=albumName, font=("Manrope", 24))
    songLabel = tk.Label(root, text=songName, font=("Manrope", 24))
    artistLabel = tk.Label(root, text=artist, font=("Manrope", 24))
    albumLabel.place(relx=0.5, rely=.8, anchor="s")
    songLabel.place(relx=0.5, rely=.84, anchor="s")
    artistLabel.place(relx=0.5, rely=.88, anchor="s")

def getAlbumURL():
    playbackState = sp.current_playback()
    if playbackState:
        albumImages = playbackState['item']['album']['images']
        return albumImages[0]['url']
    return None

def updateImage():
    global currentAlbumURL, tkImage, label
    albumURL = getAlbumURL()

    if albumURL and albumURL != currentAlbumURL:
        try:
            response = requests.get(albumURL)
            response.raise_for_status()
            image = Image.open(BytesIO(response.content))
            tkImage = ImageTk.PhotoImage(image)
            label.config(image=tkImage)
            currentAlbumURL = albumURL
            info()

        except requests.exceptions.RequestException as e:
            print("Error fetching the image:", e)
        except Exception as e:
            print("Error updating the image:", e)

    root.after(500, updateImage)  # Update every 0.5 seconds

def cleanup():
    with open("/tmp/exit_signal", "w") as f:
        f.write("exit")
    root.quit()

root = tk.Tk()
root.attributes("-fullscreen", True)
root.bind("<Escape>", lambda e: root.quit())
root.bind("<Control-c>", lambda e: cleanup())

tkImage = None
currentAlbumURL = None
label = tk.Label(root)
piTunesLabel = tk.Label(root, text="Powered by PiTunes", font=("Manrope Bold", 24))
label.place(relx=0.5, rely=.75, anchor="s")
piTunesLabel.place(relx=0.5, rely=.92, anchor="s")

updateImage()
root.mainloop()
