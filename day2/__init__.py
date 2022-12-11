url = 'https://sz.lianjia.com/zufang/futianqu/rt200600000001l1/'
import requests
result = requests.get(url)
from lxml import etree
price = etree.HTML(result.content).xpath('//em/text()')
print(price)
type(result)
import numpy as nu
arr = [1,2,4,4,5]
array=nu.array([1,2,3,4])
print(type(array))