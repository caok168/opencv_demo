# 图片缩放1

import cv2
img = cv2.imread('../imgs/1.jpg', 1)
imgInfo = img.shape
print(imgInfo)
cv2.imshow('origin', img)
cv2.waitKey(100)

height = imgInfo[0]
width = imgInfo[1]
mode = imgInfo[2]

# 1、放大 缩小 2 等比例 非 2:3
dstHeight = int(height * 0.5)
dstWidth = int(width * 0.5)

dst = cv2.resize(img, (dstWidth, dstHeight))
cv2.imshow('image', dst)
cv2.waitKey(0)
