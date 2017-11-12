# -*- coding: utf-8 -*-
from selenium import webdriver
from bs4 import BeautifulSoup
import re
import os
import requests
from geturl import urll  #把链接导入
from page import m    #把漫画页数导入


def geturl(url):
    try:
        browser=webdriver.PhantomJS()
        browser.implicitly_wait(10)
        browser.get(url)
        html=browser.page_source
        browser.quit()     #渲染获取动态加载后的网页源代码
        return html
    except:
        print u'图片链接获取失败'


def saveimag(html,k):
    soup=BeautifulSoup(html,'html.parser')
    r=soup.find_all('img',id="mhpic")
    p=str(r)
    po=re.compile('src="(.*?)"/>')   #提取漫画图片的链接
    lianjie=re.findall(po,p)
    try:
        with open(str(k)+'.jpg','wb') as file:
            file.write(requests.get(lianjie[0]).content)   #把图片写入文件夹中
        print u'第'+str(k)+u'图片保存成功'
    except:
        print u'第'+str(k)+u'图片保存失败'

class main():
    for k in range(0,m):
        url=urll+str(k)+'.html'
        html=geturl(url)
        saveimag(html,k)
