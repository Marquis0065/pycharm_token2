import requests
from lxml import etree
url = 'https://sz.fang.lianjia.com/loupan/yantianqu/#yantianqu'
      #https://sz.fang.lianjia.com/loupan/yantianqu/pg2/#yantianqu

#print(resp.text)
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}
resp = requests.get(url,headers=header)
print(etree.HTML(resp.text).xpath('//em/text()'))
from multiprocessing.dummy import Pool

