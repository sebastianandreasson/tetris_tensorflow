from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import numpy as np
import time
import os
from grab_screen import grab_screen

# last_move = ''
last_screen = []
thread = None

def get_output(message):
    # left, right, up, space
    output = [0, 0, 0, 0]
    if message == 'left':
        output[0] = 1
    elif message == 'right':
        output[1] = 1
    elif message == 'space':
        output[2] = 1
    elif message == 'rotate-right':
        output[3] = 1
    return output

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@socketio.on('connection')
def connection(conn):
    print('connection ' + conn)

@socketio.on('move')
def test_message(message):
    global last_screen
    print('make move ' + message)
    processed_screen = grab_screen()
    output = get_output(message)
    print(last_screen)
    print(output)

    if len(last_screen) != 0:
        training_data.append([processed_screen, output])
        if len(training_data) % 250 == 0:
            print(len(training_data))
            np.save(file_name, training_data)

    last_screen = processed_screen

file_name = './training_data/training_data.npy'

if os.path.isfile(file_name):
    print('got an incomplete training file')
    training_data = list(np.load(file_name))
else:
    print('not file, creating new training data')
    training_data = []

def main():
    socketio.run(app)

    # for i in list(range(4))[::-1]:
    #     print(i+1)
    #     time.sleep(1)
    # screen_record()

if __name__ == '__main__':
    main()
