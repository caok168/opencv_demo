# 05Hog特征

# 【3780】hog svm line训练【3780】
#。hog*svm = 值
# 值》T 目标obj


#整体hog cell复用
# 3780
# 3780 《-win（block cell bin）
# 1《-bin
# cell0 cell3 bin0-bin8
# cell0: bin0 bin1 。。。bin8
# cell1: bin0 bin1 。。。bin8
# cell2: bin0 bin1 。。。bin8
# cell3: bin0 bin1 。。。bin8
#ij cell0 bin0=《f0，
#i+1 j cell0 bin0 = f1
#ij。。。。
# sumbin0（f0+f1.。）= bin0
# 权重累加
#ij bin0 bin1

# cell复用

# block 4个cell
# 【0】【】【】【3】
# cell0 bin0-bin9
# cellx0 cellx2 cellx4
# cellx0:ij-》bin bin+1
# cellx2：ij -》 cell2 cell3 -》bin bin+1 bin bin+1
# cellx4：ij

# 【cell 9】【4cell】【105】 = 3780


# bin 投影 梯度
# bin 0-360 9bin 0-40
# bin1 0-20 180-200
# ij f a = 10
# 0-20 center bin1 a=190 180 200 bin1
# f
# 25 bin1 bin2
# f1 = f*f（夹角） f2 = f*（1-f（夹角））  f（夹角）  0-1.0
# +1 hog


#2·2 梯度 方向 模版
# 像素都有一个梯度 》hog== win
# 特征模版-》haar类似
# 【1 0 -1】【【1】【0】【-1】】
# a = p1*1+p2*0+p3*(-1) = 相邻像素之差
# b = 上下像素之差
# f = 根号下（a方+b方）
# angle = arctan（a/b）


#7 cell bin 梯度：运算
# 每个像素-》梯度 ：大小 f 方向 angle
# 0-360 /40 = 9块 = 9bin
# 1bin = 40 cell-》360-〉9bin
# hog特征维度：
# haar 值 hog 向量 （维度）-》完全描述 一个obj info all
# 维度 = 105*4*9=3780


#1 什么是hog》？特征 某个像素 某种运算
#2 2·1 模块划分 2·2 梯度 方向 模版 2·3 bin 投影 2·4 每个模块hog
#2·1 模块划分
# image（ppt） win（蓝色） block（红色） cell （绿色）（size）
#image》win〉block》cell
#block setp  win step cell bin
#win 特征计算最顶层单元 -》obj
# 1 win size 50*100 20*50    64*128
# 2 2.1 block 《win 2.2 win size w h / block （wh） 16*16
# 3 block step  如何win下滑动 8*8
# 4 计算block cout = （（64-16）/8+1）*（（128-16）/8+1）= 105 block
# 5 cell size 8*8
# 6 block = ？cell 16*16 = 2*2 = 》4cell  cell1-cell4
# 7 bin？