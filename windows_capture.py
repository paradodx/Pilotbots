import numpy as np
import cv2
import time
from PIL import ImageGrab
from win32gui import FindWindow, GetWindowRect
from directkeys import PressKey, ReleaseKey, W, A, S, D, AUP, ADOWN, ALEFT, ARIGHT

for i in list(range(4))[::-1]:
    print(i+1)
    time.sleep(1)

print('down')
PressKey(AUP)
time.sleep(3)
print('up')
ReleaseKey(AUP)

def process_img(original_image):
    processed_img = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    processed_img = cv2.Canny(processed_img, threshold1=200, threshold2=300)
    return processed_img

t0 = time.time()
while True:
    window_name = "Need for Speed™ Payback"
    id = FindWindow(None, window_name)
    bbox = GetWindowRect(id)
    screen = np.array(ImageGrab.grab(bbox=bbox))
    # screen = cv2.resize(screen, (1280,720), interpolation=cv2.INTER_LINEAR)
    new_screen = process_img(screen)

    cv2.imshow('window', new_screen)
    print('Done. (%.3fs)' % (time.time() - t0))

    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break