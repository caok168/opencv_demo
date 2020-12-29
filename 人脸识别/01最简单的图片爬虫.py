#'https://class.imooc.com/?c=ios&mc_marking=286b51b2a8e40915ea9023c821882e74&mc_channel=L5
# 爬虫 1 理解爬虫原理 2 实现一个的图片爬虫
# 1 http 2 html 3 正则 过滤条件 4 其它
# 知识点多
# 1 url 2 html src 3 img 4 img url
import urllib
import urllib3
import os
from bs4 import BeautifulSoup
# load url
html = urllib.request.urlopen('https://class.imooc.com/?c=ios&mc_marking=286b51b2a8e40915ea9023c821882e74&mc_channel=L5').read()
# parse url data 1 html 2 'html.parser' 3 'utf-8'
soup = BeautifulSoup(html,'html.parser',from_encoding='utf-8')
# img
images = soup.findAll('img')
print(images)
imageName = 0
for image in images:
    link = image.get('src')
    print('link=',link)
    link = 'http:'+link
    fileFormat = link[-3:]
    if fileFormat == 'png' or fileFormat == 'jpg':
        fileSavePath = '/Users/mac/Desktop/DL/'+str(imageName)+'.jpg'
        imageName = imageName +1
        urllib.request.urlretrieve(link,fileSavePath)