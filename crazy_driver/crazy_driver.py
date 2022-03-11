from turtle import up
import numpy as np
import cv2
import time
from PIL import ImageGrab
from win32gui import FindWindow, GetWindowRect
from draw_lanes import draw_lanes
from decision import update

def roi(img, vertices):
    
    #blank mask:
    mask = np.zeros_like(img)   
    
    #filling pixels inside the polygon defined by "vertices" with the fill color    
    cv2.fillPoly(mask, vertices, 255)
    
    #returning the image only where mask pixels are nonzero
    masked = cv2.bitwise_and(img, mask)
    return masked


def process_img(image):
    original_image = image
    # convert to gray
    processed_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # edge detection
    processed_img =  cv2.Canny(processed_img, threshold1 = 200, threshold2=300)
    
    processed_img = cv2.GaussianBlur(processed_img,(5,5),0)
    
    vertices = np.array([[132, 500], [132, 350], [300, 250], [500, 250], [655, 350], [655, 500]], np.int32) # Need for Speed 20 bumper view

    processed_img = roi(processed_img, [vertices])

    # more info: http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_houghlines/py_houghlines.html
    #                                     rho   theta   thresh  min length, max gap:        
    lines = cv2.HoughLinesP(processed_img, 1, np.pi/180, 180,      100,       5)
    m1 = 0
    m2 = 0
    try:
        l1, l2, m1,m2 = draw_lanes(original_image,lines)
        cv2.line(original_image, (l1[0], l1[1]), (l1[2], l1[3]), [0,255,0], 30)
        cv2.line(original_image, (l2[0], l2[1]), (l2[2], l2[3]), [0,255,0], 30)
    except Exception as e:
        pass
    try:
        for coords in lines:
            coords = coords[0]
            try:
                cv2.line(processed_img, (coords[0], coords[1]), (coords[2], coords[3]), [255,0,0], 3)
                
                
            except Exception as e:
                pass
    except Exception as e:
        pass

    return processed_img,original_image, m1, m2


for i in list(range(4))[::-1]:
    print(i+1)
    time.sleep(1)


t0 = time.time()
ldStuckCount = 0
rdStuckCount = 0
sStuckCount = 0
while True:

    # "Cyberpunk 2077 (C) 2020 by CD Projekt RED"
    # "Need for Speed™ Payback"
    window_name = "Forza Horizon 4"
    id = FindWindow(None, window_name)
    bbox = GetWindowRect(id)
    screen = np.array(ImageGrab.grab(bbox=bbox))
    screen = cv2.resize(screen, (800,600), interpolation=cv2.INTER_LINEAR)

    new_screen, original_image, m1, m2 = process_img(screen)
    cv2.imshow('window2',cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB))

    ldStuckCount, rdStuckCount, sStuckCount = update(m1, m2, ldStuckCount, rdStuckCount, sStuckCount, False)

    # print('Done. (%.3fs)' % (time.time() - t0))
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
