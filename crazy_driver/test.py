import matplotlib.pyplot as plt
import numpy as np
import cv2
from draw_lanes import draw_lanes


file = "C:\\Users\\Ming\\Desktop\\1.jpg"
img = cv2.imread(file)
# print(img)
# 灰度化
img_gary = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 边缘检测
img_can = cv2.Canny(img_gary, threshold1=100, threshold2=200)
# 高斯除噪
img_G = cv2.GaussianBlur(img_can, (5, 5), 0)

lines = cv2.HoughLinesP(img_G, 1, np.pi / 180, 180, 100, 5)
# for line in lines:
#     x1, y1, x2, y2 = line[0]
#     cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

m1 = 0
m2 = 0
try:
    l1, l2, m1, m2 = draw_lanes(img, lines)
    cv2.line(img, (l1[0], l1[1]), (l1[2], l1[3]), [0, 255, 0], 30)
    cv2.line(img, (l2[0], l2[1]), (l2[2], l2[3]), [0, 255, 0], 30)
except Exception as e:
    pass
try:
    for coords in lines:
        coords = coords[0]
        try:
            cv2.line(img, (coords[0], coords[1]), (coords[2], coords[3]), [255, 0, 0], 3)
        except Exception as e:
                        pass
except Exception as e:
    pass

cv2.namedWindow("img_1", cv2.WINDOW_NORMAL)
# cv2.resizeWindow("img_1", 800, 600)
# cv2.imshow("img_1", img)
# cv2.imshow("img_1", img_gary)
# cv2.imshow("img_1", img_can)
# cv2.imshow("img_1", img_G)
cv2.imshow("img_1", img)
cv2.waitKey(0)










# fig = plt.figure(figsize=(8, 6))
# fig.add_subplot(1,1,1)

# vertices = np.array([[132, 500], [132, 350], [300, 250], [500, 250], [655, 350], [655, 500]],
#                         np.int32)
# plt.plot(vertices)
# plt.show()