# -*- coding: utf-8 -*-
import requests
from geturl import urll   #从geturl模块中把链接导入

for k in range(0,60):
    url=urll+str(k)+'.html'
    r=requests.get(url)
    t=r.status_code
    if t==500:
        print u'共有'+str(k)+u'页'  #通过循环测试得到漫画总共有多少页
        m=k
        break
    else:
        continue

    
    
