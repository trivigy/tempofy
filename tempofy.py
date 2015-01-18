#!/private/var/local/venv/tempofy/bin/python
import urllib2
import json
import random
import time


def spotify(tempo=124):
    api_key = '6AR8ZBJDQ5QTT0KK0'
    response_format = 'json'
    mintempo = tempo - 1
    maxtempo = tempo + 1
    request = 'http://developer.echonest.com/api/v4/song/search?api_key=%s&format=%s&min_tempo=%s&max_tempo=%s&results=100&style=edm&rank_type=familiarity&sort=tempo-asc&bucket=id:spotify&bucket=tracks' % (api_key, response_format, str(mintempo), str(maxtempo))
    response = urllib2.urlopen(request).read()
    parsed_response = json.loads(response)
    songs = parsed_response['response']['songs']
    song = songs[0]
    song = random.choice(songs)
    while True:
        try:
            spotify_id = song['tracks'][0]['foreign_id'].split(':')[-1]
            break
        except:
            pass
    return spotify_id

while True:
    time.sleep(2)
    print spotify((random.random() * 30) + 100)
