# @Time: 2022/12/10 18:53
import urllib.request
import urllib.parse
#quote方法，把汉字变成正确的编码

url_base = 'https://www.baidu.com/s?wd='
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}
name = urllib.parse.quote('周杰伦')

data={
    'wd':'周杰伦',
    'sex':'男',
    'location':'中国台湾'
}
new_data = urllib.parse.urlencode(data)
url=url_base+new_data
request = urllib.request.Request(url=url,headers=header)
response = urllib.request.urlopen(request)
print(response.read().decode('utf8'))
#https://movie.douban.com/j/chart/top_list?type=13&interval_id=100%3A90&action=&start=0&limit=20
#https://movie.douban.com/j/chart/top_list?type=13&interval_id=100%3A90&action=&start=20&limit=20
#https://movie.douban.com/j/chart/top_list?type=13&interval_id=100%3A90&action=&start=40&limit=20