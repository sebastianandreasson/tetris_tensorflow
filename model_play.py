# model_play.py

import numpy as np
import cv2
import time
from PIL import ImageGrab
from alexnet import alexnet
from pynput.keyboard import Key, Controller
from grab_screen import grab_screen

keyboard = Controller()

WIDTH = 10
HEIGHT = 20
LR = 1e-3
EPOCHS = 10
MODEL_NAME = './models/py-tetris-fast-{}-{}-{}-epochs.model-auto-balanced-7672'.format(LR, 'alexnet', EPOCHS)

model = alexnet(WIDTH, HEIGHT, LR)
model.load(MODEL_NAME)

def main():
    last_time = time.time()
    for i in list(range(4))[::-1]:
        print(i+1)
        time.sleep(1)

    paused = False
    while(True):
        processed_screen = grab_screen()
        print(processed_screen)

        prediction = model.predict([processed_screen.reshape(WIDTH,HEIGHT,1)])[0]
        print(prediction)

        index_max = np.argmax(prediction)
        print(index_max)

        # left, right, space, up
        if index_max == 0:
            print('left')
            keyboard.press(Key.left)
            keyboard.release(Key.left)
        elif index_max == 1:
            print('right')
            keyboard.press(Key.right)
            keyboard.release(Key.right)
        elif index_max == 2:
            print('space')
            keyboard.press(Key.space)
            keyboard.release(Key.space)
        elif index_max == 3:
            print('rotate')
            keyboard.press(Key.up)
            keyboard.release(Key.up)

        time.sleep(0.5)



main()
