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
all_daily_mixes   = {'id': '1QacCtP1WONJMnLEKY1Bbq', 'name': 'All Daily Mixes'}
favs              = {'id': '1gL61UZJBSaoRRiLpHpwhR', 'name': 'Favs'}

destinations = [
    urban_mood,
    upbeat_mood,
    funky_mood,
    clubby_mood,
    breaks_mood,
    deep_mood,
    chill_mood,
    electronic_mood,
    release_discovery,
    all_daily_mixes,
    favs,
]

sources = [
    { 'name': 'Acid House',         'id': '2NzymlUWKrvI4htixiIs3C', 'destinations': [deep_mood] },
    { 'name': 'Bass House',         'id': '1NPHecfqYaGA1WePqWokI0', 'destinations': [clubby_mood] },
    { 'name': 'Breakbeat',          'id': '6PB0CoDn4povX33QpmQ02e', 'destinations': [deep_mood, breaks_mood] },
    { 'name': 'Chill R&B / Soul',   'id': '0UtKErAsSYJUHTc2zdnDPX', 'destinations': [chill_mood] },
    { 'name': 'Chill House',        'id': '67f5NnFFo2q3L5RYZta5w7', 'destinations': [chill_mood] },
    { 'name': 'Chillhop / Beats',   'id': '4Nq24gCbtioyKjAKD1INIL', 'destinations': [chill_mood] },
    { 'name': 'Deep House',         'id': '2qyLVxWBh4vQCF9DwCk902', 'destinations': [deep_mood] },
    { 'name': 'Disco',              'id': '7dxDjILCeSVrjVpzvDv729', 'destinations': [upbeat_mood] },
    { 'name': 'Disco House',        'id': '2E6LKDR37X50mjgS7pzXsT', 'destinations': [upbeat_mood, funky_mood] },
    { 'name': 'Drum & Bass',        'id': '4UI4KdZo6nK3rvE2NJffR7', 'destinations': [breaks_mood] },
    { 'name': 'Float House',        'id': '54LXniLpAy2UArsQH7i7tX', 'destinations': [deep_mood] },
    { 'name': 'Funky House',        'id': '6oT10NgHvsFLczeWgGgQxd', 'destinations': [funky_mood] },
    { 'name': 'Future Bass',        'id': '00MdAHM17nugGL6n7vdJO8', 'destinations': [electronic_mood] },
    { 'name': 'Future Beats',       'id': '5RucBBOskc1Hk4zTEeO0xR', 'destinations': [urban_mood] },
    { 'name': 'Future House',       'id': '2WHhRbzPCHFr1MNCyLnfPl', 'destinations': [electronic_mood] },
    { 'name': 'Groovy / Soul',      'id': '4vfmQDn8KcjFkitbsXTnx9', 'destinations': [funky_mood, upbeat_mood] },
    { 'name': 'Halftime / Bass',    'id': '7Cx3FApTEjoAJy5gn3m25V', 'destinations': [electronic_mood] },
    { 'name': 'Hip Hop / Grime',    'id': '5DNjq57hOo0HJ7oel2nMmI', 'destinations': [urban_mood] },
    { 'name': 'Ibiza House',        'id': '6D8ZjY9YMfDqBTfAmkWOwj', 'destinations': [clubby_mood] },
    { 'name': 'Jazz',               'id': '0rTmE7jxCO6ojsUue21SS5', 'destinations': [chill_mood] },
    { 'name': 'Jazz Funk',          'id': '0KZY0HStJkmOtwkSapnLKj', 'destinations': [funky_mood] },
    { 'name': 'Jungle',             'id': '2edrfJyokLxCWXPnmkHOoa', 'destinations': [breaks_mood] },
    { 'name': 'Liquid Drum & Bass', 'id': '1onEsTGHFBsk7IZ5sGSoaE', 'destinations': [breaks_mood] },
    { 'name': 'Lofi House',         'id': '67irKHtgNLMKLgEnWMS93K', 'destinations': [deep_mood] },
    { 'name': 'Nu Funk',            'id': '03GNMqql4MbNf8GwsbVFYn', 'destinations': [funky_mood] },
    { 'name': 'Progressive House',  'id': '6BUxoJGWtllzMdejzgfvHJ', 'destinations': [electronic_mood] },
    { 'name': 'Tech House',         'id': '2FGMn8inH33crqXNTWMdyS', 'destinations': [clubby_mood] },
    { 'name': 'Techno',             'id': '12JxGTejUK5wOr7qZDTywX', 'destinations': [clubby_mood] },
    { 'name': 'UK Garage',          'id': '6KSZa1AzLgKmrlCruKhmxR', 'destinations': [urban_mood] },



    { 'name': 'Drum & Bass Favs',        'id': '1ygT1VOEKgZjzuhrh6CDXB', 'destinations': [favs] },
    { 'name': 'Jungle Favs',             'id': '68vNpnlIYpNZQwWG8q6Owc', 'destinations': [favs] },
    { 'name': 'Liquid Drum & Bass Favs', 'id': '2gwDNAq63WDUnqhd8lB3XB', 'destinations': [favs] },
    { 'name': 'Halftime / Bass Favs',    'id': '2ZQXMeR2KnpPfeZABkMWvQ', 'destinations': [favs] },

    { 'name': 'Tech House Favs',         'id': '4eTR1fDylaA1cmxboyHvFi', 'destinations': [favs] },
    { 'name': 'Bass House Favs',         'id': '0PbEKyrsS02IgsNwwmJufP', 'destinations': [favs] },
    { 'name': 'Deep House Favs',         'id': '4Q1P934932QR8vy9xj4rhr', 'destinations': [favs] },
    { 'name': 'Acid House Favs',         'id': '3dNr4pN9sO3FS1ipcItsFT', 'destinations': [favs] },

    { 'name': 'Ibiza House Favs',        'id': '0Lp9Tm5WpZFKRvarL6qNtd', 'destinations': [favs] },
    { 'name': 'Disco House Favs',        'id': '105MPwNzym9UetKNoYljUG', 'destinations': [favs] },
    { 'name': 'Funky House Favs',        'id': '7dRmcCQcYxJYn7anrPZnrW', 'destinations': [favs] },
    
    { 'name': 'Float House Favs',        'id': '3NJAJkhSjwkMV719YwVR19', 'destinations': [favs] },
    { 'name': 'Lofi House Favs',         'id': '4zd6RUBMoOcvljMKxJDlLs', 'destinations': [favs] },
    { 'name': 'Chill House Favs',        'id': '3NIcjGeoe523EgwFref8ra', 'destinations': [favs] },

    { 'name': 'Future House Favs',       'id': '0faX1DXvp4VmY97NT0Uv2F', 'destinations': [favs] },
    { 'name': 'Progressive House Favs',  'id': '3j6IkQNR7EUZPZj8uvuwya', 'destinations': [favs] },
    { 'name': 'Future Bass Favs',        'id': '2RooblzkBz9y7T1uDUi046', 'destinations': [favs] },

    { 'name': 'Breakbeat Favs',          'id': '5SO30bU406ejFVOHUcRaaf', 'destinations': [favs] },
    { 'name': 'UK Garage Favs',          'id': '27XBSE3WxBWmll9lGTwJFx', 'destinations': [favs] },
    { 'name': 'Hip Hop / Grime Favs',    'id': '4LLs77ShlJW9365YtVY868', 'destinations': [favs] },
    { 'name': 'Future Beats Favs',       'id': '47PpzzJNVTKb5UBIbFWG1j', 'destinations': [favs] },

    { 'name': 'Groovy / Soul Favs',      'id': '7wuKBNdYd306OTDvKa5RPc', 'destinations': [favs] },
    { 'name': 'Chill R&B / Soul Favs',   'id': '5Z3OkNGtSSsHdhN0S9SPKD', 'destinations': [favs] },
    { 'name': 'Disco Favs',              'id': '3Q14GKIjGkqs7SpSJN5ts3', 'destinations': [favs] },
    { 'name': 'Chillhop / Beats Favs',   'id': '1dnNccPZTcTLfQzxrUmLGB', 'destinations': [favs] },

    { 'name': 'Jazz Favs',               'id': '7LN7s4SL4ZWOC5fA08n2Cm', 'destinations': [favs] },
    { 'name': 'Jazz Funk Favs',          'id': '333oE61YVycXCALSw6iyhF', 'destinations': [favs] },
    { 'name': 'Nu Funk Favs',            'id': '54hDW0y41irql0Lx0vTDgT', 'destinations': [favs] },



    { 'name': 'Release Radar',      'id': '37i9dQZEVXbwcRCxi05N0l', 'destinations': [release_discovery] },
    { 'name': 'Discover Weekly',    'id': '37i9dQZEVXcJVkLihw7Abc', 'destinations': [release_discovery] },
    { 'name': 'Daily Mix 1',        'id': '37i9dQZF1E36zB6IBvTA1Z', 'destinations': [all_daily_mixes] },
    { 'name': 'Daily Mix 2',        'id': '37i9dQZF1E35FNp3AjwoD1', 'destinations': [all_daily_mixes] },
    { 'name': 'Daily Mix 3',        'id': '37i9dQZF1E38m7THoFLkuH', 'destinations': [all_daily_mixes] },
    { 'name': 'Daily Mix 4',        'id': '37i9dQZF1E3711IypgUARZ', 'destinations': [all_daily_mixes] },
    { 'name': 'Daily Mix 5',        'id': '37i9dQZF1E39Ehtni1Mgnb', 'destinations': [all_daily_mixes] },
    { 'name': 'Daily Mix 6',        'id': '37i9dQZF1E39ZTGCFZcqaE', 'destinations': [all_daily_mixes] },
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

    if now - lastRun < 86400: # less than a day
        exit()

    file = open(fileName, 'w')
    file.write(str(now))
    file.close()




# START ############################################################

if not (len(sys.argv) > 1 and sys.argv[1] == '-f'):
    exitIfRunTooFrequently()

# clear mood playlists
for destination in destinations:
    scope = 'playlist-modify-public'
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
    sp.playlist_replace_items(destination['id'], [])

for source in sources:

    for destination in source['destinations']:
        print(source['name'] + ' -> ' + destination['name'])

        def callback(response, sp):
            tracks = []
            for track in response['items']:
                tracks.append(track['track']['id'])
            addToMood(destination['id'], tracks)

        processPlaylist(source['id'], callback)
