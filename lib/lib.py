import spotipy
from pprint import pprint
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
import spotipy.util as util
import time
import sys
from urllib.parse import urlparse

def getPlayListId(url):
    parsed = urlparse(url)
    if parsed.netloc != 'open.spotify.com':
        print('This is not a Spotify link!', url)
        exit()
    if parsed.path.split('/')[1] != 'playlist':
        print('This is not a playlist link!', url)
        exit()
    return parsed.path.split('/')[2]

def readSecret(name, default, useInput, inputText):
    fileName = f'lib/{name}.secret'
    
    try:
        file = open(fileName, 'r')
        value = file.read()
        file.close()
    except:
        if useInput:
            value = input(inputText + '\n')
            writeSecret(name, value)
        else:
            value = default
            writeSecret(name, value)

    return value

def writeSecret(name, value):
    fileName = f'lib/{name}.secret'
    file = open(fileName, 'w')
    file.write(str(value))
    file.close()

def authenticate(): 
    client_id = readSecret('clientID', '', True, 'Enter your Spotify Client ID, find yours at https://developer.spotify.com/dashboard')
    client_secret = readSecret('clientSecret', '', True, 'Enter your Spotify Client Secret, find yours at https://developer.spotify.com/dashboard')
    redirect_uri = readSecret('redirect', '', True, 'Enter the redirect URL you set up your app with, you can use https://google.com')
    username = readSecret('username', '', True, 'Enter your Spotify Username, find yours at https://spotify.com/account/overview')

    scope = 'playlist-modify-public'
    util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)


def processPlaylist(id, callback):
    authenticate()
    
    pl_id = f'spotify:playlist:{id}'

    offset = 0
    while True:
        ### get response
        sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
        response = sp.playlist_items(pl_id,
                                    offset=offset,
                                    fields='items.track.id,total',
                                    additional_types=['track'])
        if len(response['items']) == 0:
            break
        offset = offset + len(response['items'])
        callback(response, sp)



def exitIfRunTooFrequently():
    lastRun = readSecret('lastRun', 0, False, '')
    now = time.time()
    if now - float(lastRun) < 86400: # less than a day
        print('Script already ran today, use the "-f" option to force the script to run.')
        exit()

    writeSecret('lastRun', str(now))

def transfer(fr, to):
    def callback(response, sp):
        tracks = []
        for track in response['items']:
            tracks.append(track['track']['id'])
        if len(tracks) > 0:
            response = sp.playlist_add_items(to, tracks)

    processPlaylist(fr, callback)

def clear(id):
    scope = 'playlist-modify-public'
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
    sp.playlist_replace_items(id, [])

def start(config):
    if not (len(sys.argv) > 1 and sys.argv[1] == '-f'):
        exitIfRunTooFrequently()

    paths = []
    for path in config:
        newPath = {'from': getPlayListId(path['from']), 'to': getPlayListId(path['to'])}
        paths.append(newPath)

    authenticate()

    destinationsSeen = []
    count = 0
    for path in paths:
        count += 1
        print(count, '/', len(config))
        if path['to'] not in destinationsSeen:
            destinationsSeen.append(path['to'])
            clear(path['to'])
        transfer(path['from'], path['to'])
