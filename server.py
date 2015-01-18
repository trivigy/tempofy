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
                bpm1 = find_bpm(data['y'])
                bpm2 = find_bpm([-a for a in data['y']])
                final_bpm = min(bpm1, bpm2) - 20
                song_id = get_song(final_bpm)
                return Response(json.dumps({"song_id": song_id}), status=200)
    else:
        return Response(status=400)


def find_bpm(accels):
    baseline = sum(accels)/len(accels)
    peaks = []
    side = 1
    for i in range(side, len(accels)-side):
        if accels[i-side] < accels[i] > accels[i+side]:
            peaks.append(i)
    total = 0
    peaks = [p for p in peaks if accels[p] > baseline]
    if len(peaks) > 1:
        total = peaks[-1]-peaks[0]
        average = total/float(len(peaks)-1)
        seconds = average*1/60
        bpm = 60/seconds
    else:
        bpm = 0
    return bpm

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
