from lib.lib import start

# destination playlists
all_daily_mixes       = 'https://open.spotify.com/playlist/1QacCtP1WONJMnLEKY1Bbq'
# add more playlists here, make sure to create an empty spotify playlist and grab the link

# source playlists
daily_mix_1           = 'https://open.spotify.com/playlist/37i9dQZF1E36zB6IBvTA1Z'
daily_mix_2           = 'https://open.spotify.com/playlist/37i9dQZF1E35FNp3AjwoD1'
daily_mix_3           = 'https://open.spotify.com/playlist/37i9dQZF1E38m7THoFLkuH'
daily_mix_4           = 'https://open.spotify.com/playlist/37i9dQZF1E3711IypgUARZ'
daily_mix_5           = 'https://open.spotify.com/playlist/37i9dQZF1E39Ehtni1Mgnb'
daily_mix_6           = 'https://open.spotify.com/playlist/37i9dQZF1E39ZTGCFZcqaE'

config = [
    { 'from': daily_mix_1, 'to': all_daily_mixes},
    { 'from': daily_mix_2, 'to': all_daily_mixes},
    { 'from': daily_mix_3, 'to': all_daily_mixes},
    { 'from': daily_mix_4, 'to': all_daily_mixes},
    { 'from': daily_mix_5, 'to': all_daily_mixes},
    { 'from': daily_mix_6, 'to': all_daily_mixes},
    # add more merges here
]

start(config)
