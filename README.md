# PiTunes<br />
[PiTunes.webm](https://github.com/user-attachments/assets/e8f6b6e7-256a-42f8-a316-02c364c0be55)

PiTunes is a music player powered by Raspberry Pi and Raspotify, controlled through RFID tags. Using a Python script with Spotipy API calls, PiTunes lets you pause, skip, or play specific songs and albums with just a tap. Enjoy a personalized music experience where each tag brings up something new.

---

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Setup](#setup)
   - [Hardware Setup](#hardware-setup)
   - [Software Installation](#software-installation)
3. [Testing Setup](#testing-setup)
4. [Using PiTunes](#using-pitunes)
   - [Assign Music to RFID Tags](#assign-music-to-rfid-tags)
   - [Configure and Run PiTunes](#configure-and-run-pitunes)

---

## Prerequisites<br />
- A Raspberry Pi 3 or newer.
- An RFID reader.
- RFID tags/stickers to control playback.
- (Optional) An LCD display for live data.
- (Optional) A small monitor for live data + album artwork.
- A Spotify Premium account.
### Setup
#### Hardware Setup
1. Enable SPI and I2c on the Raspberry Pi:
     ```bash
     sudo raspi-config
     ```
- Select Interface Options:
- Select SPI and click 'Yes'
- Select I2c and click 'Yes' (if using an LCD display)
- Reboot the Pi<br/>
  ```bash
  sudo reboot
  ```
2. Connect the RFID Reader:
  - Use this diagram to connect the RFID reader to the Raspberry Pi's GPIO ports:
    ```
    https://alejandrocodes.dev/guides/mfrc522ToGPIO.webp
    ```
3. (Optional) Connect the LCD Display:
  - Use this diagram to connect the LCD Display to the Raspberry Pi's GPIO ports:
    ```
    https://alejandrocodes.dev/guides/i2c2400ToGPIO.webp
    ```
#### Software Installation
1. Make sure Pi is updated:
     ```bash
     sudo apt-get update
     sudo apt-get upgrade
     ```
2. Install Python & Libraries:
     ```bash
     sudo apt-get install python3-dev python3-pip
     sudo pip3 install spidev
     sudo pip3 install mfrc522
     sudo pip3 install spotipy
     ```
  - (Optional) For LCD Display:
    ```bash
    sudo pip install RPLCD
    ```
   - (Optional) For GUI Display:
     ```bash
     sudo pip install requests pillow
     ```
    
3. Install Raspotify:
   ```bash
   sudo apt-get -y install curl && curl -sL https://dtcooper.github.io/raspotify/install.sh | sh
   ```

5. Create a Spotify App:
- Visit Spotify for Developers:
  ```
  https://developer.spotify.com/dashboard
  ```
- Create an app and add these callback URIs:<br/>
   ```
  http://localhost:8888/callback
  http://localhost:8080
   ```
- Write down the Client ID and the Client Secret for later use.

#### Get the device ID:
- Connect to Raspotify with any device ex. Phone<br/>
- Visit this site:
  ```
  https://developer.spotify.com/console/get-users-available-devices/
  ```
- Click "Try it"
- Take note of the Raspberry Pi's device ID for later use.

### Testing Setup
#### Test RFID Reader
1. Run the test script:
     ```bash
     python3 tagReader.py
     ```
  >[!NOTE]
  > A new tag doesn't usually have a value, just an ID so the Value may be blank at first.

#### (Optional) Test LCD Display
1. Find your I2C address:
  - Install i2c-tools:
     ```bash
     sudo apt-get install -y i2c-tools
     ```
  - Scan for I2C devices:
     ```bash
     i2cdetect -y 1
     ```
  - The output will be a grid showing addresses (in hexadecimal) where devices are detected.
2. Update the I2C address: 
  - Update this line: `lcd=CharLCD('PCF8574', 0x27)` where the 0x27 will be replaced by 0x followed by the number obtained from this command: `i2cdetect -y 1` (e.g. 0x42 if the number was 42)
3. Save and run the display test:
     ```bash
     python3 testLCD.py
     ```
#### Test Spotify Integration
1. Update `testSpotify.py` with your device ID, client ID, and client Secret with the data we got before.
2. Save and run the script:
     ```bash
     python3 testSpotify.py
     ```
     - Authenticate on the Spotify window
     - Close the window

#### (Optional) Test GUI Display
1. Update `display.py` with your device ID, client ID, and client Secret with the data we got before.
2. Save and run the script:
     ```bash
     python3 display.py
     ```
     - On a device connected to your Spotify account, play a song.
     - Once a song is being played, album artwork as well as playback information will be displayed.
3. Once done, press `esc` to exit the program.

### Using PiTunes
#### Assign Music to RFID Tags
1. We want to assign songs, albums, and playlists to our RFID tags, to do that we need to first find out the URI.
  - In Spotify, select a song, album, or playlist and click share to get the link. This link will look similar to this: `https://open.spotify.com/track/7KA4W4McWYRpgf0fWsJZWB?si=7b7946d4a5394cd0` We want the part that is between the forward slash `/` and the question mark `?`, so for the given example it would be `7KA4W4McWYRpgf0fWsJZWB`.
2. Now we want to write to the tags. Run tagWriter.py
     ```bash
     python3 tagWriter.py
     ```
  - It will prompt to enter the Spotify URI. Now, this part depends on wheter you are writing this tag for a song, album, or playlist. The URI will look like this: `spotify:FIRST:SECOND` where FIRST is track, album, or playlist and SECOND will be the string we got before that was between `/` and `?`. All put together should look something like this: `spotify:track:7KA4W4McWYRpgf0fWsJZWB` or `spotify:album:7KA4W4McWYRpgf0fWsJZWB` or `spotify:playlist:7KA4W4McWYRpgf0fWsJZWB`
  - You can test that the values(URI) were written correctly by running `tagReader.py` as in the earlier step.

#### Configure and Run PiTunes
1. Update `main.py`:
     - Update the device ID, client ID, and client Secret with the data we got before.<br/>
     - Update the id's for the basic Spotify controls using your own tags. You may use `tagReader.py` once again to check the tag id's.
2. Save and Run the main script:
  `python3 main.py`

(Optional) For use with LCD Display
  1. Update `lcd.py` with:
    - device ID, client ID, and client Secret with the data we got before.
    - I2C address with the one we got before in case it was different than 0x27.
      - Also do this step for clear.py
  2. Execute `run_lcd.sh`, this will execute both  `main.py` and `lcd.py` in the background
      ```bash
      ./run_lcd.sh
      ```
   3. Once done, use `ctrl + C` to kill both programs.

(Optional) For use with GUI Display
1. Execute `run.sh`, this will execute both `main.py` and `display.py` in the background
   ```bash
   ./run.sh
   ```
2. Once done, use `ctrl + C` to kill both programs.
- And that's it, you can now enjoy a personalized music experience where each tag brings up something new!

>[!NOTE]
> - PiTunes is fully functional on its own, but you may have noticed some instructions have "Optional". What this means is that you have the option to use: 1. An LCD display for live playback info, or 2. A GUI that displays album artwork as well as live playback info. Either one of these can be used as a simple additional feature for PiTunes!
> - Since most programs run on indefinately, they can always be killed using: `ctrl + C`
> - If there is a device not found error, re-connect to Raspotify using another device ex. Phone
> - If using a Raspberry Pi 5, the RPi.GPIO library won't be compatible. Use gpiozero instead: `pip install gpiozero`
