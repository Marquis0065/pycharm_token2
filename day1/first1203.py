#print('第一个程序')
#print("新增day1，测试github上的token更新")
import lxml
import wheel
import scrapy
import wheel
import requests
url = 'https://m.pinduoduo.net/brand_activity_subsidy.html?_pdd_tc=ffffff&access_from=home&refer_page_sn=10002&_pdd_fs=1&top_goods_list=335847881037%2C395820670867%2C415279791795%2C346670171320&_pdd_sbs=1&top_goods_sort=1_1&refer_page_el_sn=1110247'
header = {
 'User-Agent': '%E7%BE%8E%E5%9B%A2/103983 CFNetwork/1206 Darwin/20.1.0'
}
data ={

}
response = requests.get(url,headers=header)
print(response.status_code)
print(response.text)

