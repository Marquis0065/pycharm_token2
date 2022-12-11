# @Time: 2022/12/10 20:38
import urllib.request
import urllib.parse
from lxml import etree
url_base = 'https://movie.douban.com/j/chart/top_list?type=13&interval_id=100%3A90&action=&start='
header = {
    'Cookie': 'bid=jZrKwBcLGh0; douban-fav-remind=1; ll="118282"; Hm_lvt_16a14f3002af32bf3a75dfe352478639=1670585457; __yadk_uid=JDpDumfKixRF98BsXewkqYi7SPKRjNJI; __gads=ID=5a3c107d6f37899b-22b816a1fdd800ed:T=1670585529:RT=1670585529:S=ALNI_MZt1B0KBQDvH8ZV9EIGedqBahXNWQ; _vwo_uuid_v2=D98C85F759E1EFFE754C5B38FCEC3D86F|fe14ed8c3a602b9746390b714920fd1f; ap_v=0,6.0; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1670674983%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3Dni6BXrVsE7hrj79JEOZI2DH-SVqTdnVvHeN5E1IM1kux8ISCS6nwzPhfSM6er8MG%26wd%3D%26eqid%3Dd127204a001f19000000000663947a1e%22%5D; _pk_ses.100001.4cf6=*; __utma=30149280.647547874.1670331178.1670589449.1670674984.4; __utmb=30149280.0.10.1670674984; __utmc=30149280; __utmz=30149280.1670674984.4.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utma=223695111.1999152548.1670585434.1670589449.1670674984.3; __utmb=223695111.0.10.1670674984; __utmc=223695111; __utmz=223695111.1670674984.3.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __gpi=UID=000008c88e2d1832:T=1670585529:RT=1670674984:S=ALNI_MYx5Jy9sIZPrLCymJc8QqapY5NNWw; _pk_id.100001.4cf6=cc67e2a88ff30e09.1670585434.3.1670675056.1670589449.',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}
fp = open('douban.json','w',encoding='utf8')
for i in range(20):
    if i == 0:
        url = url_base+str(i)+'&limit=20'
    else:
        url = url_base+str(i*20)+'&limit=20'
    respect = urllib.request.Request(url=url,headers=header)
    response = urllib.request.urlopen(respect)
    content = response.read().decode('utf8')
    fp.write(content)




import requests



