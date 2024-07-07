from flask import Flask, request, jsonify
from flask_socketio import SocketIO, join_room, leave_room, send, emit
from pymongo import MongoClient
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app)

client = MongoClient("mongo uri")
db = client.wordle_game

@app.route("/start", methods=["POST"])
def start_game():
    # Implement game start logic
    return jsonify({"message": "Game started"})

@socketio.on('join')
def on_join(data):
    username = data['username']
    room = data['room']
    join_room(room)
    emit('message', {'msg': f'{username} has entered the room.'}, room=room)

@socketio.on('leave')
def on_leave(data):
    username = data['username']
    room = data['room']
    leave_room(room)
    emit('message', {'msg': f'{username} has left the room.'}, room=room)

@socketio.on('guess')
def on_guess(data):
    room = data['room']
    guess = data['guess']
    # Implement guess checking logic
    emit('guess_response', {'guess': guess, 'result': 'result'}, room=room)

if __name__ == "__main__":
    socketio.run(app, debug=True)
