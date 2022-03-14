import time
import numpy as np

# use DX input
from directkeys import PressKey, ReleaseKey, W, A, S, D, AUP, ADOWN, ALEFT, ARIGHT

# use pynput
from pynput.keyboard import Key, Controller
keyboard = Controller()


def straight():
    ReleaseKey(S)
    PressKey(W)
    ReleaseKey(A)
    ReleaseKey(D)

def left():
    PressKey(A)
    ReleaseKey(S)
    PressKey(W)
    ReleaseKey(D)
    ReleaseKey(W)

def right():
    PressKey(D)
    ReleaseKey(S)
    PressKey(W)
    ReleaseKey(A)
    ReleaseKey(W)

def releaseAll():
    ReleaseKey(W)
    ReleaseKey(A)
    ReleaseKey(D)
    ReleaseKey(S)


def pynStraight():
    keyboard.release('s')
    keyboard.press('w')
    keyboard.release('a')
    keyboard.release('d')

def pynLeft():
    keyboard.press('a')
    keyboard.release('s')
    keyboard.press('w')
    keyboard.release('d')
    keyboard.release('w')

def pynRight():
    keyboard.press('d')
    keyboard.release('s')
    keyboard.press('w')
    keyboard.release('a')
    keyboard.release('w')

def pynReleaseAll():
    keyboard.release('w')
    keyboard.release('a')
    keyboard.release('d')
    keyboard.release('s')

def update(m1, m2, ldStuckCount, rdStuckCount, sStuckCount, dx = True):

    if (sStuckCount >= 50):
        print('s stuck')

        if (dx): releaseAll() 
        else: pynReleaseAll()

        if (np.random.choice([0,1])):
            if (dx): PressKey(D)
            else: keyboard.press('d')
        else:
            if (dx): PressKey(A)
            else: keyboard.press('a')


        if (dx): PressKey(S)
        else: keyboard.press('s')
        time.sleep(4)
        sStuckCount = 0

    if (ldStuckCount >= 20):
        print('l stuck')

        if (dx): 
            releaseAll()
            PressKey(A)
            PressKey(S)
        else: 
            pynReleaseAll()
            keyboard.press('a')
            keyboard.press('s')

        time.sleep(2)
        ldStuckCount = 0

    if (rdStuckCount >= 20):
        print('r stuck')

        if (dx): 
            releaseAll()
            PressKey(D)
            PressKey(S)            
        else: 
            pynReleaseAll()
            keyboard.press('d')
            keyboard.press('s')

        time.sleep(2)
        rdStuckCount = 0


    if m1 < 0 and m2 < 0:
        rdStuckCount += 1
        sStuckCount = 0

        if (dx): right()
        else: pynRight()

    elif m1 > 0 and m2 > 0:
        ldStuckCount += 1
        sStuckCount = 0

        if (dx): left()
        else: pynLeft()
    
    elif m1 > 0 and m2 < 0 :
        sStuckCount += 1
        rdStuckCount = 0
        ldStuckCount = 0
        if (dx): straight()
        else: pynStraight()

    else:
        sStuckCount += 1
        if (dx): straight()
        else: pynStraight()

    return ldStuckCount, rdStuckCount, sStuckCount