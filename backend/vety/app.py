"""Creates and exports the backend app object
TODO add more detailed description
"""

from flask import Flask
from flask_socketio import SocketIO


app: Flask = Flask(__name__)
socketio = SocketIO(app, path="socket.io")
app.config.from_prefixed_env()

@app.route("/ping")
def ping():
    return "pong"
