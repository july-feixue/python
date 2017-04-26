#!/usr/bin/python2.7
# -*- coding:UTF-8 -*-

import urllib2
import urllib
import sys
from bs4 import BeautifulSoup 

#获取网页并得到网页源码
def h_s(urldz):
    
    request_1=urllib2.Request(urldz)
    request_1.add_header("user-agent","Mozilla/5.0")
    opendz=urllib2.urlopen(request_1)
    read_sj=opendz.read()
    
    return read_sj
#获取网页上的数据名称
def s_s(html_string):   
    soup=BeautifulSoup(html_string,'html.parser',from_encoding='utf-8')
    #soup_1=soup.encode("utf-8")
    links_1=soup.find_all('img')
    return links_1
#根据数据名称保存文件
def p_f(string_1):
    i=n
    for link in string_1:
        print 'Downloading pictures'
        print link.name,link['src'],link.get_text()
        urllib.urlretrieve(link['src'],'%s.jpg' % i)
        i+=1
        
           
#对以上函数整体调用
def dywj(http_):
    http_string=h_s(http_)
    soup_string=s_s(http_string)
    return soup_string
	
#选择下载图片方式	
#xuanze=int(raw_input('#选择根据输入网址：1\n#选择根据文件内网址:2\n#你的选择为：'))
def open_http(http_url):
    http_data=[]
    if http_url:
            url_http=str(http_url)
            http_11=dywj(url_http)
            for aa_11 in http_11:
                http_data.append(aa_11['src'])
	
    else:
	   
            wj=open('httpwz.txt','r')#网址文件名字
            while True:
                    wjh=(wj.readline())
                    if not wjh:break
                    a_lk=dywj(wjh)
                    for linkKK in a_lk:
                        http_data.append(linkKK['src'])
                    wj.close()
    return http_data

   
