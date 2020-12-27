# 1 info 2 空白模板 3 xy
import cv2
import numpy as np
img = cv2.imread('../imgs/1.jpg', 1)
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
dstHeight = int(height/2)
dstWidth = int(width/2)
dstImage = np.zeros((dstHeight, dstWidth, 3), np.uint8)
for i in range(0, dstHeight):
    for j in range(0, dstWidth):
        iNew = int(i*(height*1.0/dstHeight))
        jNew = int(j*(width*1.0/dstWidth))
        dstImage[i, j] = img[iNew, jNew]
cv2.imshow('dst', dstImage)
cv2.waitKey(0)
cv2.destroyAllWindows()