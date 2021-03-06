# 灰度处理2
import cv2
import numpy as np
# img = cv2.imread('../imgs/4.jpg', 1)
# imgInfo = img.shape
# height = imgInfo[0]
# width = imgInfo[1]
# # RGB  R=G=B = gray (R+G+B)/3
# dst = np.zeros((height, width, 3), np.uint8)
# for i in range(0, height):
#     for j in range(0, width):
#         (b, g, r) = img[i, j]
#         gray = (int(b) + int(g) + int(r)) / 3
#         dst[i, j] = np.uint8(gray)
#
# cv2.imshow('dst', dst)
# cv2.waitKey(0)

# 方法4 gray = r*0.299+g*0.587+b*0.114
import cv2
import numpy as np
img = cv2.imread('../imgs/4.jpg', 1)
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
dst = np.zeros((height, width, 3), np.uint8)
for i in range(0, height):
    for j in range(0, width):
        (b, g, r) = img[i,j]
        b = int(b)
        g = int(g)
        r = int(r)
        gray = r*0.299+g*0.587+b*0.114
        dst[i,j] = np.uint8(gray)
cv2.imshow('dst', dst)
cv2.waitKey(0)