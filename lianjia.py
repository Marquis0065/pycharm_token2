import lxml
import requests
from lxml import etree
# url = 'https://m.pinduoduo.net/brand_activity_subsidy.html?_pdd_tc=ffffff&access_from=home&refer_page_sn=10002&_pdd_fs=1&top_goods_list=335847881037%2C395820670867%2C415279791795%2C346670171320&_pdd_sbs=1&top_goods_sort=1_1&refer_page_el_sn=1110247'
url = 'https://sz.lianjia.com/zufang/futianqu/pg2rt200600000001l1/#contentList'
response = requests.get(url)
from bs4 import BeautifulSoup
soup = BeautifulSoup(response.text,'lxml')
price_list = soup.find_all('em')
for price in price_list:
    print(price.string)