#!/usr/bin/python
import urllib2
import json
import random
import time

def spotify(tempo=124):
    api_key = '6AR8ZBJDQ5QTT0KK0'
    response_format = 'json'
    style = 'pop'
    rank_type = 'familiarity'
    sort = 'tempo-asc'
    if tempo > 200: tempo = 200
    mintempo = int(tempo - 1)
    maxtempo = int(tempo + 1)
    request = 'http://developer.echonest.com/api/v4/song/search?api_key=%s&format=%s&min_tempo=%s&max_tempo=%s&results=100&style=%s&rank_type=%s&sort=%s&bucket=id:spotify&bucket=tracks' % (api_key, response_format, str(mintempo), str(maxtempo), style, rank_type, sort)

    response = urllib2.urlopen(request).read()
    parsed_response = json.loads(response)
    songs = parsed_response['response']['songs']
    
    i = random.random(len(songs))
    try: 
        song = songs[i]
        spotify_id = song['tracks'][0]['foreign_id'].split(':')[-1]
    except Exception as err:
        print err
        return None

    return spotify_id

# testing code
# while True:
#    time.sleep(2)                                                                                                      
#    print spotify((random.random() * 30) + 100)
