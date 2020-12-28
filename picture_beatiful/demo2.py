# 直方图均衡化

#灰度 直方图均衡化
import cv2
import numpy as np
img = cv2.imread('../imgs/4.jpg',1)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('src',gray)
dst = cv2.equalizeHist(gray)
cv2.imshow('dst',dst)
cv2.waitKey(0)

#彩色 直方图均衡化
import cv2
import numpy as np
img = cv2.imread('../imgs/4.jpg',1)
cv2.imshow('src',img)
(b,g,r) = cv2.split(img)#通道分解
bH = cv2.equalizeHist(b)
gH = cv2.equalizeHist(g)
rH = cv2.equalizeHist(r)
result = cv2.merge((bH,gH,rH))# 通道合成
cv2.imshow('dst',result)
cv2.waitKey(0)


#YUV 直方图均衡化
import cv2
import numpy as np
img = cv2.imread('../imgs/4.jpg',1)
imgYUV = cv2.cvtColor(img,cv2.COLOR_BGR2YCrCb)
cv2.imshow('src',img)
channelYUV = cv2.split(imgYUV)
channelYUV[0] = cv2.equalizeHist(channelYUV[0])
channels = cv2.merge(channelYUV)
result = cv2.cvtColor(channels,cv2.COLOR_YCrCb2BGR)
cv2.imshow('dst',result)
cv2.waitKey(0)