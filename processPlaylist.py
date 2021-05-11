import spotipy
from pprint import pprint
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
import json
import spotipy.util as util
import os

def processPlaylist(id, callback):

    pl_id = f'spotify:playlist:{id}'

    client_id = os.environ['SPOTIPY_CLIENT_ID']
    client_secret = os.environ['SPOTIPY_CLIENT_SECRET']
    redirect_uri = 'https://google.com'
    username = '11136558335'

    scope = 'playlist-modify-private'
    token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)

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
        print(offset, "/", response['total'])
        
        callback(response, sp)
