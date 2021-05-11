# set SPOTIPY_CLIENT_ID and SPOTIPY_CLIENT_SECRET environment variables

import spotipy
from pprint import pprint
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
import json
import spotipy.util as util
from processPlaylist import processPlaylist

scope = 'playlist-modify-private'

liked_id = '4HHZrOpZ91HFgQ9ascBvve'

danceable_id = '7lSuuqKdKkQ0LAKICd6p2L'
undanceable_id = '0qQup6FIjpxpcntdwAOJ1O'
energetic_id = '1K0VJ9CFro5WeDAQn4QH9R'
chill_id = '40H1lQfdAO4G78WuyWjWXz'
happy_id = '0Nq8HLw8JFC88VMzDOwT0r'
sad_id = '2VKpTalgsNRvZkMWH64ffs'
instrumental_id = '0ggeMp2X433mF1CDMRS5Ig'
vocal_id = '43t2MF5stq2F6F8aw87aNR'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
sp.playlist_replace_items(danceable_id, [])
sp.playlist_replace_items(undanceable_id, [])
sp.playlist_replace_items(energetic_id, [])
sp.playlist_replace_items(chill_id, [])
sp.playlist_replace_items(happy_id, [])
sp.playlist_replace_items(sad_id, [])
sp.playlist_replace_items(instrumental_id, [])
sp.playlist_replace_items(vocal_id, [])

def addToPlaylist(id, tracks):
    if len(tracks) > 0:
        response = sp.playlist_add_items(id, tracks)
        print(response)

def callback(response, sp):
    ### get tracks
    trackIDs = []
    for track in response['items']:
        trackIDs.append(track['track']['id'])

    ### get features of tracks
    features = sp.audio_features(trackIDs)

    ### get dancable/undanceable
    danceable = []
    undanceable = []
    energetic = []
    chill = []
    happy = []
    sad = []
    instrumental = []
    vocal = []

    for feature in features:

        if feature['danceability'] > 0.5:
            danceable.append(feature['id'])
        else:
            undanceable.append(feature['id'])
        
        if feature['energy'] > 0.5:
            energetic.append(feature['id'])
        else:
            chill.append(feature['id'])
        
        if feature['valence'] > 0.5:
            happy.append(feature['id'])
        else:
            sad.append(feature['id'])
        
        if feature['instrumentalness'] > 0.5:
            instrumental.append(feature['id'])
        else:
            vocal.append(feature['id'])

    
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
    addToPlaylist(danceable_id, danceable)
    addToPlaylist(undanceable_id, undanceable)
    addToPlaylist(energetic_id, energetic)
    addToPlaylist(chill_id, chill)
    addToPlaylist(happy_id, happy)
    addToPlaylist(sad_id, sad)
    addToPlaylist(instrumental_id, instrumental)
    addToPlaylist(vocal_id, vocal)

processPlaylist(liked_id, callback)
