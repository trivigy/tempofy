#!/private/var/local/venv/tempofy/bin/python
from flask import Flask, request, Response
from tempofy import get_song

app = Flask(__name__)


@app.route('/song', methods=['GET'])
def song():
    if request.method == 'GET':
        song_id = get_song(130)
        return Response(song_id, status=200)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
