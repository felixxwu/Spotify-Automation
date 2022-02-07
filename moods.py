# set SPOTIPY_CLIENT_ID and SPOTIPY_CLIENT_SECRET environment variables

import time
import spotipy
from pprint import pprint
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
import json
import spotipy.util as util
from processPlaylist import processPlaylist
import sys

urban_mood        = {'id': '6QyPXogZHDElyNcXRf14oN', 'name': 'Beats and Vibes'}
upbeat_mood       = {'id': '6ip96AlGVRpb41U8cOudo6', 'name': 'Upbeat Grooves'}
funky_mood        = {'id': '3Xw80hGkazf4qOPIw30SpJ', 'name': 'Funky Fresh'}
clubby_mood       = {'id': '3o2U5B7cvlFspKuFEDJyhq', 'name': 'Heavy Hitters'}
breaks_mood       = {'id': '62RrxLSRtbJAhiQAPu0jEh', 'name': 'Rave Breaks'}
deep_mood         = {'id': '6mBSlC6XZHSL0UyWFAGUGO', 'name': 'Deep and Soulful'}
chill_mood        = {'id': '6dtETOTmLhXAZZZa2DH9Cb', 'name': 'Laid-back Chill'}
electronic_mood   = {'id': '0Y2InqMR3vNJeRvvttZfR9', 'name': 'Electronic Goodness'}
release_discovery = {'id': '1MEp4PrZZUdwUnEGvT7qYb', 'name': 'Release + Discovery'}

moods = [
    urban_mood,
    upbeat_mood,
    funky_mood,
    clubby_mood,
    breaks_mood,
    deep_mood,
    chill_mood,
    electronic_mood,
    release_discovery,
]

genres = [
    { 'name': 'Acid House',         'id': '2NzymlUWKrvI4htixiIs3C', 'moods': [deep_mood] },
    { 'name': 'Bass House',         'id': '1NPHecfqYaGA1WePqWokI0', 'moods': [clubby_mood] },
    { 'name': 'Breakbeat',          'id': '6PB0CoDn4povX33QpmQ02e', 'moods': [deep_mood, breaks_mood] },
    { 'name': 'Chill R&B / Soul',   'id': '0UtKErAsSYJUHTc2zdnDPX', 'moods': [chill_mood] },
    { 'name': 'Chill House',        'id': '67f5NnFFo2q3L5RYZta5w7', 'moods': [chill_mood] },
    { 'name': 'Chillhop / Beats',   'id': '4Nq24gCbtioyKjAKD1INIL', 'moods': [chill_mood] },
    { 'name': 'Deep House',         'id': '2qyLVxWBh4vQCF9DwCk902', 'moods': [deep_mood] },
    { 'name': 'Disco',              'id': '7dxDjILCeSVrjVpzvDv729', 'moods': [upbeat_mood] },
    { 'name': 'Disco House',        'id': '2E6LKDR37X50mjgS7pzXsT', 'moods': [upbeat_mood, funky_mood] },
    { 'name': 'Drum & Bass',        'id': '4UI4KdZo6nK3rvE2NJffR7', 'moods': [breaks_mood] },
    { 'name': 'Funky House',        'id': '6oT10NgHvsFLczeWgGgQxd', 'moods': [funky_mood] },
    { 'name': 'Future Bass',        'id': '00MdAHM17nugGL6n7vdJO8', 'moods': [electronic_mood] },
    { 'name': 'Future Beats',       'id': '5RucBBOskc1Hk4zTEeO0xR', 'moods': [urban_mood] },
    { 'name': 'Future House',       'id': '2WHhRbzPCHFr1MNCyLnfPl', 'moods': [electronic_mood] },
    { 'name': 'Groovy / Soul',      'id': '4vfmQDn8KcjFkitbsXTnx9', 'moods': [funky_mood, upbeat_mood] },
    { 'name': 'Halftime / Bass',    'id': '7Cx3FApTEjoAJy5gn3m25V', 'moods': [electronic_mood] },
    { 'name': 'Hip Hop / Grime',    'id': '5DNjq57hOo0HJ7oel2nMmI', 'moods': [urban_mood] },
    { 'name': 'Ibiza House',        'id': '6D8ZjY9YMfDqBTfAmkWOwj', 'moods': [clubby_mood] },
    { 'name': 'Jazz',               'id': '0rTmE7jxCO6ojsUue21SS5', 'moods': [chill_mood] },
    { 'name': 'Jazz Funk',          'id': '0KZY0HStJkmOtwkSapnLKj', 'moods': [funky_mood] },
    { 'name': 'Jungle',             'id': '2edrfJyokLxCWXPnmkHOoa', 'moods': [breaks_mood] },
    { 'name': 'Liquid Drum & Bass', 'id': '1onEsTGHFBsk7IZ5sGSoaE', 'moods': [breaks_mood] },
    { 'name': 'Lofi House',         'id': '67irKHtgNLMKLgEnWMS93K', 'moods': [deep_mood] },
    { 'name': 'Minimal Techno',     'id': '54LXniLpAy2UArsQH7i7tX', 'moods': [deep_mood] },
    { 'name': 'Nu Funk',            'id': '03GNMqql4MbNf8GwsbVFYn', 'moods': [funky_mood] },
    { 'name': 'Progressive House',  'id': '6BUxoJGWtllzMdejzgfvHJ', 'moods': [electronic_mood] },
    { 'name': 'Tech House',         'id': '2FGMn8inH33crqXNTWMdyS', 'moods': [clubby_mood] },
    { 'name': 'Techno',             'id': '12JxGTejUK5wOr7qZDTywX', 'moods': [clubby_mood] },
    { 'name': 'UK Garage',          'id': '6KSZa1AzLgKmrlCruKhmxR', 'moods': [urban_mood] },
    { 'name': 'Release Radar',      'id': '37i9dQZEVXbwcRCxi05N0l', 'moods': [release_discovery] },
    { 'name': 'Discover Weekly',    'id': '37i9dQZEVXcJVkLihw7Abc', 'moods': [release_discovery] },
]

def addToMood(id, tracks):
    if len(tracks) > 0:
        response = sp.playlist_add_items(id, tracks)

def exitIfRunTooFrequently():
    fileName = 'lastRun.txt'

    try:
        file = open(fileName, 'r')
        lastRun = float(file.read())
        file.close()
    except:
        lastRun = 0

    now = time.time()

    file = open(fileName, 'w')
    file.write(str(now))
    file.close()

    if now - lastRun < 86400: # less than a day
        exit()




# START ############################################################

if not (len(sys.argv) > 1 and sys.argv[1] == '-f'):
    exitIfRunTooFrequently()

# clear mood playlists
for mood in moods:
    scope = 'playlist-modify-public'
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
    sp.playlist_replace_items(mood['id'], [])

for genre in genres:

    for mood in genre['moods']:
        print(genre['name'] + ' -> ' + mood['name'])

        def callback(response, sp):
            tracks = []
            for track in response['items']:
                tracks.append(track['track']['id'])
            addToMood(mood['id'], tracks)

        processPlaylist(genre['id'], callback)
