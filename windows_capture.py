import numpy as np
import cv2
import time
from PIL import ImageGrab
from win32gui import FindWindow, GetWindowRect
from directkeys import PressKey, ReleaseKey, W, A, S, D, AUP, ADOWN, ALEFT, ARIGHT

# for i in list(range(4))[::-1]:
#     print(i+1)
#     time.sleep(1)

# print('down')
# PressKey(AUP)
# time.sleep(10)
# print('up')
# ReleaseKey(AUP)

def roi(img, vertices):
    mask = np.zeros_like(img)
    cv2.fillPoly(mask, vertices, 255)
    masked = cv2.bitwise_and(img, mask)
    return masked

def process_img(original_image):
    processed_img = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    processed_img = cv2.Canny(processed_img, threshold1=200, threshold2=300)

    # vertices = np.array([[10, 500], [10, 300], [300, 200], [500, 200], [800, 300], [800, 500]])
    vertices = np.array([[132, 500], [132, 350], [300, 250], [500, 250], [655, 350], [655, 500]])
    processed_img = roi(processed_img, [vertices])
    return processed_img

t0 = time.time()
while True:
    # "Cyberpunk 2077 (C) 2020 by CD Projekt RED"
    window_name = "Need for Speed™ Payback"
    id = FindWindow(None, window_name)
    bbox = GetWindowRect(id)
    screen = np.array(ImageGrab.grab(bbox=bbox))
    screen = cv2.resize(screen, (800,600), interpolation=cv2.INTER_LINEAR)
    new_screen = process_img(screen)

    cv2.imshow('window', new_screen)
    print('Done. (%.3fs)' % (time.time() - t0))

    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break