#-*- coding:utf-8 -*-
#!/usr/bin/env python
import urllib2
import re
import urllib
from bs4 import BeautifulSoup
#强制编码encode（‘utf-8')

def open_http(Url):
    request_1=urllib2.Request(Url)
    request_1.add_header("user-agent","Mozilla/5.0")
    opendz=urllib2.urlopen(request_1)
    read_sj=opendz.read()
    return read_sj

def http_date(date):#视频链接
    soup=BeautifulSoup(date,'html.parser',from_encoding='utf-8')
    soup_1=soup.encode("utf-8")
    links_1=re.findall(r'http://.+\.mp4',soup_1)
    return links_1
def http_fx(date_1):#视频下载
    i=1
    k=0
    for link in date_1:
        max_1=float(len(date_1)-1)
        urllib.urlretrieve(link,'%s.mp4' % i)
        
        k=int(k+10*(i/(max_1)))
        i+=1


def open_http(open):
    
    date_1=http_date(open)
    date_save=http_fx(date_1)
    return date_save
