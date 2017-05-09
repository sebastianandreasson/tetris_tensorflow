import numpy as np
import cv2
import time
import os
from PIL import Image
from random import randint
from pynput import keyboard


# X = 0
# Y = 95
# WIDTH = 356
# HEIGHT = 70

X = 0
Y = 105
WIDTH = 225
HEIGHT = 450

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

def process_img(original_img):
    processed_img = cv2.cvtColor(original_img, cv2.COLOR_BGR2GRAY)
    processed_img = cv2.resize(processed_img, (10, 20))
    return processed_img

def screen_record():
    global last_key
    last_time = time.time()
    # screen = np.array(ImageGrab.grab(bbox=(X,Y,WIDTH,HEIGHT)))
    # processed_screen = process_img(screen)
    # cv2.imwrite("image_processed.jpg", processed_screen)

    while(True):
        if not os.path.isfile('FIFO'):
            os.mkfifo('FIFO')

        os.system('screencapture -x -tjpg -R{},{},{},{} FIFO'.format(X, Y, WIDTH, HEIGHT))

        with Image.open('FIFO') as fifo:
            screen = fifo
            processed_screen = process_img(np.array(screen))

        print(processed_screen)
        #
        # output = get_output()
        #
        # training_data.append([processed_screen, output])
        #
        # if len(training_data) % 250 == 0:
        #     print(len(training_data))
        #     np.save(file_name, training_data)

        print('loop took {} seconds got {} data'.format(time.time()-last_time, len(training_data)))
        # print(output)

        # last_key = 'nothing'
        time.sleep(0.20)
        last_time = time.time()

# screen_record()

file_name = 'training_data.npy'
lis = keyboard.Listener(on_press=on_press)

if os.path.isfile(file_name):
    print('got zhe file')
    training_data = list(np.load(file_name))
else:
    print('not file :()')
    training_data = []

def main():

    # for i in list(range(4))[::-1]:
    #     print(i+1)
    #     time.sleep(1)

    # lis.start()
    screen_record()

if __name__ == '__main__':
    main()
