
# coding: utf-8

# In[1]:

import urllib2
import json
import string


# In[8]:

# given tempo, return song ID or name or something

# Your API Key: 6AR8ZBJDQ5QTT0KK0 
# Your Consumer Key: 0ffcf57c715c85b2a0e00d4798f9999e 
# Your Shared Secret: IapgevuYQ6a3RLqrg6CF4A

class Tempofy():
    def __init__(self):
        pass
    
    def get_songs(self, tempo = 120):
        api_key = '6AR8ZBJDQ5QTT0KK0'
        format = 'json'
        mintempo = tempo - 10;
        maxtempo = tempo + 10;
        request = 'http://developer.echonest.com/api/v4/song/search?api_key=%s&format=%s&min_tempo=%s&max_tempo=%s' % (api_key, format, str(mintempo), str(maxtempo))
        print request
        test = 'test'
        print test


t = Tempofy()
t.get_songs()


# In[ ]:



