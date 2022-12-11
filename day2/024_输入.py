# @Time: 2022/12/10 16:37
#输入 input函数
import urllib
import urllib.request
import urllib.parse


url = 'http://www.baidu.com'
response = urllib.request.urlopen(url)
print(response.status)
content = response.read().decode('utf8')
print(type(response))
print(response.read(15))
print(response.getcode())
print(response.geturl())
print(response.getheaders())


