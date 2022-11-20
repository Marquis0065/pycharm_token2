import lxml
import requests
from lxml import etree
url = 'https://sz.lianjia.com/zufang/futianqu/rt200600000001l1/'
response = requests.get(url)
result = etree.HTML(response.text).xpath('//em/text()')
print(result)