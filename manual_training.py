import numpy as np
import cv2
import time
import os
from random import randint
from pynput import keyboard
from grab_screen import grab_screen

last_key = ''

def on_press(key):
    global last_key
    try: k = key.char # single-char keys
    except: k = key.name # other keys
    if key == keyboard.Key.esc: return False # stop listener
    if k in ['space', 'left', 'right', 'up']: # keys interested
        # self.keys.append(k) # store it in global-like variable
        last_key = k

def get_output():
    # left, right, up, space
    output = [0, 0, 0, 0]
    if last_key == 'left':
        output[0] = 1
    elif last_key == 'right':
        output[1] = 1
    elif last_key == 'up':
        output[2] = 1
    elif last_key == 'space':
        output[3] = 1
    return output

file_name = 'training_data.npy'
lis = keyboard.Listener(on_press=on_press)

if os.path.isfile(file_name):
    print('got zhe file')
    training_data = list(np.load(file_name))
else:
    print('not file :()')
    training_data = []

def main():

    for i in list(range(4))[::-1]:
        print(i+1)
        time.sleep(1)

    global last_key
    last_time = time.time()

    while(True):
        processed_screen = grab_screen()
        output = get_output(message)

        print(processed_screen)
        training_data.append([processed_screen, output])

        if len(training_data) % 250 == 0:
            print(len(training_data))
            np.save(file_name, training_data)

        print('loop took {} seconds got {} data'.format(time.time()-last_time, len(training_data)))
        # print(output)

        last_key = 'nothing'
        time.sleep(0.20)
        last_time = time.time()

if __name__ == '__main__':
    main()
