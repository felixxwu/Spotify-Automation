# set SPOTIPY_CLIENT_ID and SPOTIPY_CLIENT_SECRET environment variables

import spotipy
from pprint import pprint
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
import json
import spotipy.util as util
from processPlaylist import processPlaylist

urban_playlist = '6QyPXogZHDElyNcXRf14oN'
upbeat_playlist = '6ip96AlGVRpb41U8cOudo6'
funky_playlist = '3Xw80hGkazf4qOPIw30SpJ'
clubby_playlist = '3o2U5B7cvlFspKuFEDJyhq'
breaks_playlist = '62RrxLSRtbJAhiQAPu0jEh'
deep_playlist = '6mBSlC6XZHSL0UyWFAGUGO'
chill_playlist = '6dtETOTmLhXAZZZa2DH9Cb'

acid_playlist = '2NzymlUWKrvI4htixiIs3C' #
bass_playlist = '1NPHecfqYaGA1WePqWokI0' #
chill_rnb_playlist = '0UtKErAsSYJUHTc2zdnDPX' #
chillhop_playlist = '4Nq24gCbtioyKjAKD1INIL' #
deep_house_playlist = '2qyLVxWBh4vQCF9DwCk902' #
disco_playlist = '7dxDjILCeSVrjVpzvDv729' #
disco_house_playlist = '2E6LKDR37X50mjgS7pzXsT' #
dnb_playlist = '4UI4KdZo6nK3rvE2NJffR7' #
edm_playlist = '6D8ZjY9YMfDqBTfAmkWOwj' #
funky_house_playlist = '6oT10NgHvsFLczeWgGgQxd' #
future_bass_playlist = '00MdAHM17nugGL6n7vdJO8' #
future_beats_playlist = '5RucBBOskc1Hk4zTEeO0xR' #
groovy_playlist = '4vfmQDn8KcjFkitbsXTnx9' #
hiphop_playlist = '5DNjq57hOo0HJ7oel2nMmI' #
jazz_playlist = '0rTmE7jxCO6ojsUue21SS5' #
jungle_playlist = '2edrfJyokLxCWXPnmkHOoa' #
liquid_playlist = '1onEsTGHFBsk7IZ5sGSoaE' #
lofi_house = '67irKHtgNLMKLgEnWMS93K' #
nu_funk_playlist = '03GNMqql4MbNf8GwsbVFYn' #
tech_house_playlist = '2FGMn8inH33crqXNTWMdyS' #
ukg_playlist = '6KSZa1AzLgKmrlCruKhmxR' #

def addToPlaylist(id, tracks):
    if len(tracks) > 0:
        response = sp.playlist_add_items(id, tracks)
        print(response)

mappings = [
    {
        'mood': urban_playlist,
        'genres': [hiphop_playlist, ukg_playlist, future_beats_playlist]
    },
    {
        'mood': upbeat_playlist,
        'genres': [disco_house_playlist, disco_playlist, future_bass_playlist, edm_playlist]
    },
    {
        'mood': funky_playlist,
        'genres': [funky_house_playlist, groovy_playlist, nu_funk_playlist]
    },
    {
        'mood': clubby_playlist,
        'genres': [tech_house_playlist, dnb_playlist, bass_playlist]
    },
    {
        'mood': breaks_playlist,
        'genres': [jungle_playlist, liquid_playlist]
    },
    {
        'mood': deep_playlist,
        'genres': [deep_house_playlist, lofi_house, acid_playlist]
    },
    {
        'mood': chill_playlist,
        'genres': [chill_playlist, chillhop_playlist, jazz_playlist]
    },
]

for mapping in mappings:
    scope = 'playlist-modify-private'
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
    sp.playlist_replace_items(mapping['mood'], [])

    for genre in mapping['genres']:

        def callback(response, sp):
            tracks = []
            for track in response['items']:
                tracks.append(track['track']['id'])
            addToPlaylist(mapping['mood'], tracks)

        processPlaylist(genre, callback)
