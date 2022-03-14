# create_training_data.py

import numpy as np
from PIL import ImageGrab
from win32gui import FindWindow, GetWindowRect
import cv2
import time
from getkeys import key_check
import os


def keys_to_output(keys):
    '''
    Convert keys to a ...multi-hot... array

    [A,W,D] boolean values.
    '''
    output = [0,0,0]
    
    if 'A' in keys:
        output[0] = 1
    elif 'D' in keys:
        output[2] = 1
    else:
        output[1] = 1
    return output

np_load_old = np.load
np.load = lambda *a, **k: np_load_old(*a, allow_pickle=True, **k)

file_name = 'training_data.npy'

if os.path.isfile(file_name):
    print('File exists, loading previous data!')
    training_data = list(np.load(file_name))
else:
    print('File does not exist, starting fresh!')
    training_data = []


def main():

    for i in list(range(4))[::-1]:
        print(i+1)
        time.sleep(1)


    paused = False
    while(True):

        if not paused:

            window_name = "Need for Speed™ Payback"
            id = FindWindow(None, window_name)
            bbox = GetWindowRect(id)
            screen = np.array(ImageGrab.grab(bbox=bbox))
            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
            # 160x120 windowed mode
            screen = cv2.resize(screen, (160,120), interpolation=cv2.INTER_LINEAR)
            last_time = time.time()
            print(last_time)

            # resize to something a bit more acceptable for a CNN
            keys = key_check()
            output = keys_to_output(keys)
            training_data.append([screen,output])
            
            if len(training_data) % 500 == 0:
                print(len(training_data))
                np.save(file_name,training_data)

        keys = key_check()
        if 'J' in keys:
            if paused:
                paused = False
                print('unpaused!')
                time.sleep(1)
            else:
                print('Pausing!')
                paused = True
                time.sleep(1)


main()