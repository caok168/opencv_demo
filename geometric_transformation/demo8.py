# 仿射变换
import cv2
import numpy as np
img = cv2.imread('../imgs/4.jpg')
cv2.imshow('src', img)
imgInfo = img.shape
heitht = imgInfo[0]
width = imgInfo[1]
# src 3->dst 3 (左上角 左下角 右上角)
matSrc = np.float32([[0,0], [0, heitht-1], [width-1,0]])
matDst = np.float32([[50, 50], [300, heitht-200], [width-300, 100]])
# 组合
matAffine = cv2.getAffineTransform(matSrc, matDst)
dst = cv2.warpAffine(img, matAffine, (width,heitht))
cv2.imshow('dst', dst)
cv2.waitKey(0)