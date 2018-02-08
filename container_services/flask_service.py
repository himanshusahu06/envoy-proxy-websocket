from flask import Flask
from flask import request
import socket
import os
import sys
import requests

app = Flask(__name__)

@app.route('/httpservice')
def hello():
    return ('Hello from behind Envoy http service ! hostname: {} resolved'
            'hostname: {}\n'.format(socket.gethostname(),
                                    socket.gethostbyname(socket.gethostname())))
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)