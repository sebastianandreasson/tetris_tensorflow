import numpy as np
import cv2
import os
from PIL import Image

X = 10 # 0
Y = 105 # 95
WIDTH = 215 # 356
HEIGHT = 440 # 440

def process_img(original_img):
    processed_img = cv2.cvtColor(original_img, cv2.COLOR_BGR2GRAY)
    processed_img = cv2.resize(processed_img, (10, 20))
    return processed_img

def grab_screen():
    if not os.path.isfile('./image_data/FIFO'):
        os.mkfifo('./image_data/FIFO')

    os.system('screencapture -x -tjpg -R{},{},{},{} ./image_data/FIFO'.format(X, Y, WIDTH, HEIGHT))

    with Image.open('./image_data/FIFO') as fifo:
        screen = fifo
        processed_screen = process_img(np.array(screen))

    return processed_screen
