#-*- coding:utf-8 -*-
#!/usr/bin/env python
import urllib2
import re
import urllib
from bs4 import BeautifulSoup
#强制编码encode（‘utf-8')


def dow_video(date_1):#视频下载
    i=1
    k=0
    for link in date_1:
        #max_1=float(len(date_1)-1)
        urllib.urlretrieve(link,'%s.mp4' % i)
        #k=int(k+(i/(max_1)))*10
        i+=1


	#根据数据名称保存图片文件
def dow_pic(string_1):
    i=1
    k=0
    for link in string_1:
        #max_1=float(len(date_1)-1)
        #k=int(k+(i/(max_1)))*10
        urllib.urlretrieve(link,'%s.jpg' % i)
        i+=1

		
	
