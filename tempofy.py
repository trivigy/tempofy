#!/private/var/local/venv/tempofy/bin/python
import urllib2
import json
import random


def get_song(tempo=124):
    api_key = '6AR8ZBJDQ5QTT0KK0'
    response_format = 'json'
    mintempo = tempo - 1
    maxtempo = tempo + 1
    request = 'http://developer.echonest.com/api/v4/song/search?api_key=%s&format=%s&min_tempo=%s&max_tempo=%s&results=100&style=edm&rank_type=familiarity&sort=tempo-asc&bucket=id:spotify&bucket=tracks' % \
        (api_key, response_format, str(mintempo), str(maxtempo))
    try:
        response = urllib2.urlopen(request).read()
    except (urllib2.URLError, urllib2.HTTPError):
        return None
    parsed_response = json.loads(response)
    songs = parsed_response['response']['songs']
    song = random.choice(songs)
    spotify_id = song['tracks'][0]['foreign_id'].split(':')[-1]
    return spotify_id

get_song()
