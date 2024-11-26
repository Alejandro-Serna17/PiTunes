# PiTunes<br />
With the use of a Python script, this Raspberry Pi makes API calls to Spotify which are controlled with RFIDs<br />

## Setup<br />
- A Raspberry Pi 3+
### Make sure Pi is updated:
`sudo apt-get update`<br/>
`sudo apt-get upgrade`
### Enable SPI on the Pi:
`sudo raspi-config`
- Select SPI and click 'Yes'
- Reboot the Pi<br/>

`sudo reboot`
### Install Python & Libraries:
`sudo apt-get install python3-dev python3-pip`<br/>
`sudo pip3 install spidev`<br/>
`sudo pip3 install mfrc522`
### Test current setup with reader.py:
- RFID Scanner will be able to pick up scans now.
### Make the Raspberry Pi a connect device
- Download the library Raspotify<br/>

`sudo apt-get -y install curl && curl -sL https://dtcooper.github.io/raspotify/install.sh | sh`

### Create an app on Spotify:
- Visit `https://developer.spotify.com/dashboard`<br/>
- Create an app and add these callback URIs:<br/>

`http://localhost:8888/callback`<br/>
`http://localhost:8080`
- Write down the Client ID and the Client Secret

### Get the device ID:
- Connect to Raspotify with any device ex. Phone<br/>
- Visit `https://developer.spotify.com/console/get-users-available-devices/`<br/>
- Click "Try it"
- Take note of the Raspberry Pi's device ID

### Install spotipy:
- The spotipy library is what will allow us to communicate with the Spotify API using Python.<br/>

`sudo pip install spotipy`

### Open testSpotify.py:
- Update the device ID, client ID, and client Secret with the data we got before.<br/>
- save and run the script:  `python3 testSpotify.py `
- Authenticate on the Spotify window
- Close the window

### Open UPDATE.py:
- Update the device ID, client ID, and client Secret with the data we got before.<br/>
- save and run the script:  `python3 UPDATEEEEE.py `
- And that's it!
### Notes:
- Since the program runs on an infinite loop, it can be killed using: `Ctrl + C`
- If there is a device not found error, re-connect to Raspotify using another device ex. Phone
- To add songs or albums, you must get the link Spotify provides when you click share. This link will look similar to this: `https://open.spotify.com/track/7KA4W4McWYRpgf0fWsJZWB?si=7b7946d4a5394cd0` We want the part that is between the forward slash `/` and `?`, so for the given example it would be `7KA4W4McWYRpgf0fWsJZWB`.
