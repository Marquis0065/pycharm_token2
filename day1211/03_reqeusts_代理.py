# @Time: 2022/12/13 17:06
import requests
header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'

}
url = 'https://www.baidu.com/s?'
data = {
    'wd':'ip'
}
proxy = {
    'http':'117.114.149.66:55443'
}
response = requests.get(url=url,params=data,headers=header,proxies=proxy)
response.encoding = 'utf8'
content = response.text
with open('daili2.html','w',encoding='utf8')as fp:
    fp.write(content)