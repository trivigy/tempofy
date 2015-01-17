#!/usr/bin/python
from flask import Flask, request, Response


app = Flask(__name__)

@app.route('/', methods=['POST'])
def index():
    if request.method == 'POST':
        print len(request.data)
        # if len(request.data) != 0:
        #     return Response(status = 201)
        #     # data = request.data
        # else:
        #     return Response(status = 400)

        return Response("BLAH\n", status = 200)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug = True)
