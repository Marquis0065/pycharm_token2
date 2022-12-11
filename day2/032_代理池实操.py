# @Time: 2022/12/11 15:06
import random
import urllib.request

import requests

praxies_list=[
    {'http':'183.236.232.160:8080'},
    {'http':'27.42.168.46:55481'},
    {'http':'222.74.73.202:42055'},
    {'http':'210.5.10.87:53281'},
    {'http':'27.42.168.46:55481'},
    {'http':'121.13.252.60:41564'},
    {'http':'120.24.76.81:8123'},
    {'http':'120.24.76.81:8123'},
    {'http':'120.24.76.81:8123'}
]
header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    }
#url = https://sz.lianjia.com/zufang/futianqu/pg2rt200600000001l1/#contentList
url_base = 'https://sz.lianjia.com/zufang/yantianqu/pg'
fp = open('luohu.txt','w',encoding='utf8')
from lxml import etree
for i in range(2,50):
    proxy=random.choice(praxies_list)
    print(proxy)
    url = url_base+str(i)+'rt200600000001l1/#contentList'
    request = urllib.request.Request(url= url,headers=header)
    handler = urllib.request.ProxyHandler(proxies=proxy)
    opener = urllib.request.build_opener(handler)
    response = opener.open(request)
    content = response.read().decode('utf8')

    response.encoding= 'utf8'
    price= etree.HTML(content).xpath('//em/text()')
    for i in price:
        fp.write(i+',')

