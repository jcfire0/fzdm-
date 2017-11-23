*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re

url='http://www.fzdm.com/'
r=requests.get(url)
r.encoding='utf-8'
page=r.text
soup=BeautifulSoup(page,'html.parser')
lis=str(soup.find_all('div',id="mhnew"))  #获取风之动漫网站的最新漫画列表
p=re.compile('target="_blank">(.*?)</a>')
pi=re.findall(p,lis)
po=re.compile('href="(.*?)"\s')    #获取列表中的漫画对应的首页链接
poo=re.findall(po,lis)
k=len(pi)
t=1
for i in range(0,k):
    print (str(t)+':'+'    '+pi[i].decode('unicode_escape'))  #给漫画编序号
    t=t+1
m=input(u'请输入你想要的漫画序号:')   #通过交互平台实现输入漫画序号爬对应漫画的给能
urll='http:'+poo[m]+'index_'    #得到最终链接

