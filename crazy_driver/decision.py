import time
import numpy as np

# use DX input
from directkeys import PressKey, ReleaseKey, W, A, S, D, AUP, ADOWN, ALEFT, ARIGHT

# use pynput
from pynput.keyboard import Key, Controller
keyboard = Controller()


def straight():
    ReleaseKey(ADOWN)
    PressKey(AUP)
    ReleaseKey(ALEFT)
    ReleaseKey(ARIGHT)

def left():
    PressKey(ALEFT)
    ReleaseKey(ADOWN)
    PressKey(AUP)
    ReleaseKey(ARIGHT)
    ReleaseKey(AUP)

def right():
    PressKey(ARIGHT)
    ReleaseKey(ADOWN)
    PressKey(AUP)
    ReleaseKey(ALEFT)
    ReleaseKey(AUP)

def releaseAll():
    ReleaseKey(AUP)
    ReleaseKey(ALEFT)
    ReleaseKey(ARIGHT)
    ReleaseKey(ADOWN)


def pynStraight():
    keyboard.release(Key.down)
    keyboard.press(Key.up)
    keyboard.release(Key.left)
    keyboard.release(Key.right)

def pynLeft():
    keyboard.press(Key.left)
    keyboard.release(Key.down)
    keyboard.press(Key.up)
    keyboard.release(Key.right)
    keyboard.release(Key.up)

def pynRight():
    keyboard.press(Key.right)
    keyboard.release(Key.down)
    keyboard.press(Key.up)
    keyboard.release(Key.left)
    keyboard.release(Key.up)

def pynReleaseAll():
    keyboard.release(Key.up)
    keyboard.release(Key.left)
    keyboard.release(Key.right)
    keyboard.release(Key.down)

def update(m1, m2, ldStuckCount, rdStuckCount, sStuckCount, dx = True):

    print(sStuckCount)

    if (sStuckCount >= 100):
        print('s stuck')

        if (dx): releaseAll() 
        else: pynReleaseAll()

        if (np.random.choice([0,1])):
            if (dx): PressKey(ARIGHT)
            else: keyboard.press(Key.right)
        else:
            if (dx): PressKey(ALEFT)
            else: keyboard.press(Key.left)


        if (dx): PressKey(ADOWN)
        else: keyboard.press(Key.down)
        time.sleep(4)
        sStuckCount = 0

    if (ldStuckCount >= 50):
        print('l stuck')

        if (dx): 
            releaseAll()
            PressKey(ARIGHT)
            PressKey(ADOWN)
        else: 
            pynReleaseAll()
            keyboard.press(Key.right)
            keyboard.press(Key.down)

        time.sleep(2)
        ldStuckCount = 0

    if (rdStuckCount >= 50):
        print('r stuck')

        if (dx): 
            releaseAll()
            PressKey(ALEFT)
            PressKey(ADOWN)
        else: 
            pynReleaseAll()
            keyboard.press(Key.left)
            keyboard.press(Key.down)

        time.sleep(2)
        rdStuckCount = 0


    if m1 < 0 and m2 < 0:
        rdStuckCount += 1
        sStuckCount = 0

        if (dx): right()
        else: pynRight()

    elif m1 > 0  and m2 > 0:
        ldStuckCount += 1
        sStuckCount = 0

        if (dx): left()
        else: pynLeft()
    
    else:
        sStuckCount += 1
        rdStuckCount = 0
        ldStuckCount = 0

        if (dx): straight()
        else: pynStraight()

    return ldStuckCount, rdStuckCount, sStuckCount