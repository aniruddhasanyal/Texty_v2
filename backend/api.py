import os
from flask import Flask, session, request
from flask_socketio import SocketIO, emit, rooms, join_room, leave_room, close_room, disconnect

async_mode = None

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socket_io = SocketIO(app, async_mode=async_mode)
thread = None

@socket_io.on('connect')
def test_connect():
    emit('my_response', {'data': 'Connected'})

if __name__ == '__main__':
    socket_io.run(app,host=os.getenv('IP', '0.0.0.0'), port =int(os.getenv('PORT', 8080)), debug=True)


