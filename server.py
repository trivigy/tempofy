#!/usr/bin/python
from flask import Flask, request, Response
from tempofy import get_song
import json

app = Flask(__name__)


@app.route('/', methods=['POST'])
def song():
    if request.method == 'POST':
        if request.headers['Content-Type'] == 'application/json':
            if len(request.data) != 0:
                data = json.loads(request.data)
            else:
                return Response(status = 400)
        # song_id = get_song(130)
        # return Response(song_id, status=200)
        return Response(json.dumps({"data":"WORKS"}), status=200)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
