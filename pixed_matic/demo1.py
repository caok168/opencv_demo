# 灰度处理
# imread
# 方法1 imread
import cv2
# img0 = cv2.imread('../imgs/4.jpg', 0)
# img1 = cv2.imread('../imgs/4.jpg', 1)
# print(img0.shape)
# print(img1.shape)
# cv2.imshow('src', img0)
# cv2.imshow('src1', img1)
# cv2.waitKey(0)

img = cv2.imread('../imgs/4.jpg', 1)
dst = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('dst', dst)
cv2.waitKey(0)