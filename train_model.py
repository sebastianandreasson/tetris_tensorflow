# train_model.py

import numpy as np
from alexnet import alexnet
WIDTH = 10
HEIGHT = 20
LR = 1e-3
EPOCHS = 10
MODEL_NAME = './models/py-tetris-fast-{}-{}-{}-epochs.model-auto-balanced-7672'.format(LR, 'alexnet', EPOCHS)

model = alexnet(WIDTH, HEIGHT, LR)

hm_data = 22
for i in range(EPOCHS):
    train_data = np.load('./training_data/training_data_balanced.npy')

    train = train_data[:-100]
    test = train_data[-100:]

    X = np.array([i[0] for i in train]).reshape(-1,WIDTH,HEIGHT,1)
    Y = [i[1] for i in train]

    test_x = np.array([i[0] for i in test]).reshape(-1,WIDTH,HEIGHT,1)
    test_y = [i[1] for i in test]

    model.fit({'input': X}, {'targets': Y}, n_epoch=1, validation_set=({'input': test_x}, {'targets': test_y}),
        snapshot_step=500, show_metric=True, run_id=MODEL_NAME)

    model.save(MODEL_NAME)

# tensorboard --logdir=foo:C:/path/to/log
