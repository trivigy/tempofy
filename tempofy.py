import urllib2
import json


def get_song(self, tempo=120):
    api_key = '6AR8ZBJDQ5QTT0KK0'
    response_format = 'json'
    mintempo = tempo - 5
    maxtempo = tempo + 5
    request = 'http://developer.echonest.com/api/v4/song/search?api_key=%s&format=%s&min_tempo=%s&max_tempo=%s&bucket=id:spotify&bucket=tracks' % \
        (api_key, response_format, str(mintempo), str(maxtempo))
    try:
        response = urllib2.urlopen(request).read()
    except (urllib2.URLError, urllib2.HTTPError):
        return None
    parsed_response = json.loads(response)
    song = parsed_response['response']['songs'][0]
    spotify_id = song['tracks'][0]['foreign_id'].split(':')[-1]
    return spotify_id
