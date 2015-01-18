#!/usr/bin/python
from flask import Flask, request, Response
from tempofy import get_song
import json
import numpy as np

app = Flask(__name__)


@app.route('/', methods=['POST'])
def song():
    if request.method == 'POST':
        if request.headers['Content-Type'] == 'application/json':
            if len(request.data) != 0:
                data = json.loads(request.data)
                bpm1 = find_bpm(data['y'])
                bpm2 = find_bpm([-a for a in data['y']])
                print  min(bpm1, bpm2)
                # print find_bpm(data['x']), find_bpm(data['y']), find_bpm(data['z'])
            else:
                return Response(status = 400)
        # song_id = get_song(130)
        # return Response(song_id, status=200)
        return Response(json.dumps({"data":"WORKS"}), status=200)

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
