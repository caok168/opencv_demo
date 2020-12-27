# 图片剪切
# 100 > 200 x
# 100 > 300 y

import cv2
img = cv2.imread('../imgs/4.jpg', 1)
imgInfo = img.shape
cv2.imshow('origin', img)
dst = img[0:200, 0:300]
cv2.imshow('image', dst)
cv2.waitKey(0)
