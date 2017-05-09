# balance_data.py

import numpy as np
import pandas as pd
from collections import Counter
from random import shuffle

train_data = np.load('./training_data/training_data.npy')

df = pd.DataFrame(train_data)
print(df.head())
print(Counter(df[1].apply(str)))

lefts = []
rights = []
space = []
rotate_left = []
rotate_right = []

shuffle(train_data)

print(train_data[0][1])

for data in train_data:
    img = data[0]
    choice = data[1]

    ## left, right, rouptate, space, ignore no actions taken
    if choice == [1,0,0,0]:
        lefts.append([img,choice])
    elif choice == [0,1,0,0]:
        rights.append([img,choice])
    elif choice == [0,0,1,0]:
        space.append([img,choice])
    elif choice == [0,0,0,1]:
        rotate_right.append([img,choice])

print('lefts, {}'.format(len(lefts)))
print('rights, {}'.format(len(rights)))
print('space, {}'.format(len(space)))
# print('rotate_left, {}'.format(len(rotate_left)))
print('rotate_right, {}'.format(len(rotate_right)))

space = space[:len(rotate_right)]
lefts = lefts[:len(space)]
rights = rights[:len(space)]
#
#
print('lefts, {}'.format(len(lefts)))
print('rights, {}'.format(len(rights)))
print('space, {}'.format(len(space)))
print('rotate_right, {}'.format(len(rotate_right)))
#
final_data = lefts + rights + space + rotate_right
shuffle(final_data)
#
print('final_data, {}'.format(len(final_data)))
#
np.save('./training_data/training_data_balanced.npy', final_data)
