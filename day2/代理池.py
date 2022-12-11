# @Time: 2022/12/11 11:56
import urllib.request
import urllib.parse
import requests
url = 'https://www.kuaidaili.com/free/inha/1/'
header = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    #'Accept-Encoding':' gzip, deflate, br',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'Cache-Control':'max-age=0',
    'Connection':'keep-alive',
    'Cookie':'channelid=bdtg_a13_a13a1; sid=1670730812972429; _gcl_au=1.1.1072060240.1670730815; Hm_lvt_7ed65b1cc4b810e9fd37959c9bb51b31=1670730817; _ga=GA1.2.1764834749.1670730817; _gid=GA1.2.1772658481.1670730817; Hm_lpvt_7ed65b1cc4b810e9fd37959c9bb51b31=1670730863',
    'Host':'www.kuaidaili.com',
    'Referer': 'https://www.kuaidaili.com/?utm_source=bdtg&utm_campaign=a13a1&utm_medium=a13&bd_vid=7227809341127955209',
    'sec-ch-ua':'"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile':'?0',
    'sec-ch-ua-platform':'"Windows"',
    'Sec-Fetch-Dest':'document',
    'Sec-Fetch-Mode':'navigate',
    'Sec-Fetch-Site':'same-origin',
    'Sec-Fetch-User':'?1',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    }

s= requests.session()
response = s.get(url= url ,headers=header)
response.encoding='utf8'
content = response.text
from lxml import etree
ip_list = etree.HTML(content).xpath('//td[@data-title][1]/text()')
port_list= etree.HTML(content).xpath('//td[@data-title][2]/text()')
print(ip_list)
print(port_list)
proxy_list=[]
print(len(ip_list),len(port_list))
for i in range(len(ip_list)):
    proxy_list.append(ip_list[i]+":"+port_list[i])
print(proxy_list)
proxies_list=[]
for i in proxy_list:
    proxies_list.append('http'+":"+i)
print(proxies_list)