# Spotify Playlist Merger

Automatically merge playlists together.

## Configuring Playlists

Open `run.py` in a text editor and modify the `config` variable with Spotify links of playlists you want to merge.

![Config](/images/config.png "Config")

## Setup

To get started, create a new app at https://developer.spotify.com/dashboard, any app name will do.

In the app settings, set "Redirect URIs" to `https://google.com`, any valid URI will work here too.

![Spotify Redirect URI](/images/redirectURI.png "Spotify Redirect URI")

## First Run

The first run of the script will ask you for a bunch of information to connect your Spotify app and account. This will be saved locally for subsequent runs so this will only need to be done once.

1. Open a terminal and run `python run.py`.

2. When prompted, you will need to copy your "Client ID" and "Client Secret" from your Spotify dashboard into the terminal.

    ![Spotify Client Secrets](/images/clientSecrets.png "Spotify Client Secrets")

3. Copy your Spotify username into the terminal when prompted.

    ![Spotify Username](/images/spotifyUsername.png "Spotify Username")

4. The script will open up the Spotify permissions page to link your app to your account. Click "Agree"

    ![Spotify Permissions](/images/spotifyPermissions.png "Spotify Permissions")

5. You'll be redirected to Google with an authentication token in the URL. It will look something like `https://www.google.com/?code=AQCBDymSKeCEo_vA...` Copy the entire URL and paste it back into the terminal.

6. You'll be redirected one more time to Google with a second authentication token. Copy this into the terminal again.

7. You're all set! Subsequent runs will skip all of these steps as the information will be saved locally.

## Subsequent Runs

Run `python run.py` whenever you want to merge your playlists. By default the script will run only once every 24 hours, run `python run.py -f` to bypass this limit.

## Tips

To maximise automation, link running the script to something that happens relatively frequently. For example, you can add it to the startup process of your OS so that every time you boot up your PC, the script runs.

On Windows:
1. Create a `.bat` file like `spotifymerge.bat`, and write `python run.py` inside
2. Right click your `.bat` file and choose "Create shortcut"
3. Press Win+R and type `shell:startup` or go to `C:\Users\<User>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup`
4. Move the shortcut of the `.bat` file into this folder, and you're all set!