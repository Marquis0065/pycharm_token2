# @Time: 2023/7/18 18:00
# _*_coding : utf-8 _*_
# @Authon : 
# @File : 星巴客
from bs4 import BeautifulSoup
import urllib.request

url = 'https://www.starbucks.com.cn/menu/'
header = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': 'ZHh6ku4z=A0Yn8meJAQAATdwojAAAtiVTdXm6mv5IkC41QVRUxo0rw9vqF1o8YC0PtRGUAXddKgCuchRAwH8AAEB3AAAAAA|1|1|03794da821c6b231b0e8965826050a2a482b81db',
    'Host': 'www.starbucks.com.cn',
    'Referer':'https://www.starbucks.com.cn/',
    'Sec-Ch-Ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': 'Windows',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}

request = urllib.request.Request(url=url,headers=header)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
soup = BeautifulSoup(content,'lxml')

base_url='https://www.starbucks.com.cn'
name = soup.select('a[class="thumbnail"] strong')
for k,v in zip(soup.select('a[class="thumbnail"] div'),name):
    try:
        urllib.request.urlretrieve(base_url+k['style'].split('\"')[1],'C:/Users/fzh00/PycharmProjects/pythonProject1/办公自动化/星巴图片/{}.jpg'.format(v.string))
    except FileNotFoundError:
        urllib.request.urlretrieve(base_url+k['style'].split('\"')[1],'C:/Users/fzh00/PycharmProjects/pythonProject1/办公自动化/星巴图片/{}.jpg'.format(v.string.replace('/','or')))

    # print(base_url+i['style'].split('\"')[1])



    # request2=urllib.request.Request(url = (base_url+i['href']),headers=header)
    # response2= urllib.request.urlopen(request2)
    # soup2 = BeautifulSoup(response2.read().decode('utf-8'),'lxml')
    # for j in soup2.select('div[class=" section--background background--lightpink  "] img'):
    #     print(base_url+j['src'])

        # urllib.request.urlretrieve(base_url+j['src'],"星巴克图片/{}.jpg".format(i.find('strong').string))