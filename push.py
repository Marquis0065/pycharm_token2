print('push test test')
import requests
from lxml import etree
# url = https://sz.lianjia.com/zufang/nanshanqu/pg2rt200600000001l1/#contentList
base_url = 'https://sz.lianjia.com/zufang/nanshanqu/pg'
fp = open('price1219.text','w',encoding='utf8')
for i in range(2):
    url = base_url+str(i)+'rt200600000001l1/#contentList'
    response = requests.get(url)
    price = etree.HTML(response.text).xpath('//em/text()')
    fp.write(str(price))
    fp.write('\n')
fp.close()