# @Time: 2022/12/10 19:26
import urllib.request
import urllib.parse
url = 'https://fanyi.baidu.com/sug'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}
data = {
    'kw':'spider'
}
#post的请求的参数,必须进行编码，urllib.parse.urlencode
data = urllib.parse.urlencode(data).encode('utf8')
#post请求的参数，必须上面再编码一次
request = urllib.request.Request(url=url,data=data,headers=header)
#post的请求参数不会拼接在url里
print(request)
response = urllib.request.urlopen(request)
print(response.status)
content=response.read().decode('utf8')
import json
obj=json.loads(content)
print(content)
print(obj)
