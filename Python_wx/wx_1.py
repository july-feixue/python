#coding=utf-8
import re
import wx
import time
import save_data #自定义模块
import dow_data
import pc_1
import urllib2
import urllib
from bs4 import BeautifulSoup

def py_wx():
    global shuru_#申明全局变量
    global prin_t
    prin_t=''
    app=wx.App()
    win=wx.Frame(None,title=u"GPS纸飞机  ",size=(500,400))

    zujian=wx.Panel(win)#win的组件
    button_1=wx.Button(zujian,label=u'开始')
    button_2=wx.Button(zujian,label=u'保存')
    http_1=wx.TextCtrl(zujian)
    data_time=wx.Gauge(zujian, -1, 100, (100, 50), (200, 25), style = wx.GA_PROGRESSBAR)
    count = 0    
    data_time.SetBezelFace(3)  
    data_time.SetShadowWidth(3)
    def aaa(self):#触发进度条和开始按钮事件函数
        
        shuru_=http_1.GetValue()#得到输入后的字符串的变量
        prin_t='aaaaaaaaaaaaaaaaaaaaaaaa'
        #print_file.SetValue(prin_t)#更新输入框的内容
        asd="1111111111111111111"
        print_file.WriteText(str(asd))
        for a in range(0,101):
            time.sleep(0.01)
            
            data_time.SetValue(a)
        data_time.Center(True)
    def aa(self):
        n=0
        global link_mp4
        global link_jpg
        link_m_1=[]
        link_j_1=[]
        pd1=re.compile(r'http://.+\.mp4$',re.I)
        pd2=re.compile(r'http://.+\.jpg$',re.I)
        shuru_=http_1.GetValue()#得到输入后的字符串的变量
        #all_link_string=pc_1.open_http(shuru_)
        link_ss_1=pc_1.open_http(shuru_)
        link_ss_2=dow_data.open_http(shuru_)
        
        for aaaa in link_ss_2:
            link_ss_1.apend(str(aaaa))

        for link4 in link_ss_1:
            print_file.WriteText(str(link4))
            print_file.WriteText('\n')
            ys1=pd1.match(link4)
            ys2=pd2.match(link4)
            
            if ys1:
                link_m_1.append(str(link4))
            elif ys2:
                link_j_1.append(str(link4))
            len_1=int(100/(len(all_link_string)))
            n=n+len_1
            data_time.SetValue(n)
        n=100
        data_time.SetValue(n)
        link_jpg=link_j_1
        link_mp4=link_m_1
        
    
    #触发保存文件函数（根据网页地址下载数据），调用保存数据模块函数
    def aa_2(self):
        
        if link_mp4:#下载视频
            save_data.dow_video(link_mp4)
        elif link_jpg:#下载图片
            save_data.dow_pic(link_jpg)

                
        #根据数组长度设置周期，进度：data_video或data_pic以及完成：ov
    

            

       
        
        
        
    
    button_1.Bind(wx.EVT_BUTTON,aa)
    button_2.Bind(wx.EVT_BUTTON,aa_2)
    
    #print_file=wx.TextCtrl(zujian,style=wx.TE_MULTILINE|wx.HSCROLL,prin_t)
    print_file=wx.TextCtrl(zujian,style=wx.TE_MULTILINE | wx.HSCROLL)
    hbox=wx.BoxSizer()#尺寸器参数默认水平
    hbox.Add(http_1,proportion=2,flag=wx.EXPAND)#可扩大可获取空间
    hbox.Add(button_1,proportion=0,flag=wx.LEFT,border=5)#靠左宽度
    hbox.Add(button_2,proportion=0,flag=wx.LEFT,border=5)
    
    #hbox.Add(button_3,proportion=0,flag=wx.LEFT,border=5)
    
    vbox=wx.BoxSizer(wx.VERTICAL)#尺寸器参数垂直
    vbox.Add(hbox,proportion=0,flag=wx.EXPAND|wx.ALL,border=5)#vbox中的尺寸器hbox整体可扩大
    vbox.Add(print_file,proportion=1,flag=wx.EXPAND|wx.LEFT|wx.BOTTOM|wx.RIGHT,border=5)
    vbox.Add(data_time,proportion=0,flag=wx.LEFT,border=10)

    
    
    zujian.SetSizer(vbox)
    win.Show()
    app.MainLoop()


#事件处理器(处理函数)
#button_1.Bind(wx.EVT_BUTTON,hanshuming)

py_wx()

