# @Time: 2022/12/17 19:54
import requests
import json
def getjson(loc,page_num=0):
    header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
        }
    pa = {
        'query':'公园',
        'region':loc,
        'scope':'1',
        'output':'json',
        'page_size':'20',
        'page_num':page_num,
        'ak':'KLWlIOmkhGUc58vieyfQyvfeVtdmMKU2'
    }
    url = 'https://api.map.baidu.com/place/v2/search'
    r = requests.get(url = url,params=pa,headers=header)
    decodejson = json.loads(r.text)
    return decodejson


province_list = [
    '河北省','山西省','吉林省','辽宁省','黑龙江省','陕西省','甘肃省','青海省','山东省',
    '福建省','浙江省','台湾','河南省','湖北省','湖南省','江西省','江苏省','安徽省','广东省','海南省','四川省',
    '贵州省','云南省'
]
# for province in province_list:
#     decodejson = getjson(province)
#     print(decodejson)
#     for result in decodejson['results']:
#         city = result['name']
#         num = result['num']
#         output = '\t'.join([city,str(num)])+'\r\n'
#         print(output)
#         with open('cities.txt','a',encoding='utf8')as f:
#             f.write(output)
#             f.close()
print(getjson('广东'))
park = getjson('深圳')
print(park)
print(park['results'])
# for res in park['results']:
#     name = res['name']
#     lat = res['location']['lat']
#     lng = res['location']['lng']
#     output = '\t'.join([name, str(lat),str(lng)]) + '\r\n'
#     print(output)
#     with open('local.txt','a',encoding='utf8')as f:
#         f.write(output)
import pymysql
conn = pymysql.connect(
    host='192.168.52.99',
    user='root',
    password='123456',
    db='fri',
    charset='utf8'
)
cur = conn.cursor()
# sql = '''create table city3(id int(11) primary key auto_increment,
#                          name varchar(200),
#                          lat int(100),
#                          lng int(100))charset = '''
# cur.execute(sql)
# cur.close()
# conn.commit()
# conn.close()
for res in park['results']:
    name = res['name']
    lat = res['location']['lat']
    lng = res['location']['lng']
    sql = 'insert into city5(name,lat,lng)values("{}","{}","{}")'.format(name,lat,lng)
    cur.execute(sql)
    conn.commit()
cur.close()
conn.close()