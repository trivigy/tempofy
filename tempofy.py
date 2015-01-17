#!/private/var/local/venv/tempofy/bin/python
import urllib2
import json

# given tempo, return song ID or name or something

# Your API Key: 6AR8ZBJDQ5QTT0KK0
# Your Consumer Key: 0ffcf57c715c85b2a0e00d4798f9999e
# Your Shared Secret: IapgevuYQ6a3RLqrg6CF4A


class Tempofy():
    def __init__(self):
        pass

    def get_songs(self, tempo=120):
        api_key = '6AR8ZBJDQ5QTT0KK0'
        format = 'json'
        mintempo = tempo - 10
        maxtempo = tempo + 10
        request = 'http://developer.echonest.com/api/v4/song/search?api_key=%s&format=%s&min_tempo=%s&max_tempo=%s&bucket=id:spotify&bucket=tracks' % \
            (api_key, format, str(mintempo), str(maxtempo))
        try:
            response = urllib2.urlopen(request).read()
        except (urllib2.URLError, urllib2.HTTPError):
            return None
        parsed_response = json.loads(response)
        song = parsed_response['response']['songs'][0]
        spotify_id = song['tracks'][0]['foreign_id'].split(':')[-1]
        return spotify_id

t = Tempofy()
t.get_songs()
