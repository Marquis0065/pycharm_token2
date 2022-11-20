import scrapy
url = 'http://baidu.com'
import requests
response = requests.get(url)
print(response.status_code)