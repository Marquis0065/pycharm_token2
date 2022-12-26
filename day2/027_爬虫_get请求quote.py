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
#https://www.baidu.com/s?wd=%E5%91%A8%E6%9D%B0%E4%BB%B3&rsv_spt=1&rsv_iqid=0xa7cea4ff0007f613&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&rqlang=cn&tn=baiduhome_pg&rsv_dl=tb&rsv_enter=0&oq=%2526lt%253B846a50745a74faca0fae09870%2526lt%253B645b%2526lt%253B%25E8%25A7%25A3%25E7%25A0%2581&rsv_btype=t&rsv_t=6a38poZ4Bvn5I5lE5yXHTxoa6JV51nVn6zlFkIKlyKS3Bk9r2RQm9NaTp3hqr%2FEJtLas&rsv_pq=d61a894f00048902&inputT=4239&rsv_sug3=167&rsv_sug1=120&rsv_sug7=100&rsv_sug2=0&rsv_sug4=4239