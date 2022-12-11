# @Time: 2022/12/11 9:14
import urllib.request
import urllib.parse
#      http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname


#data2 = urllib.parse.urlencode(data).encode('utf8')
url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'
header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    }


def create_respect(data):
   respect = urllib.request.Request(url=url ,data = data ,headers=header)
   return respect

def create_content(respect):
    response = urllib.request.urlopen(respect)
    content = response.read().decode('utf8')
    return content
#with open('douban1211.json', 'w', encoding='utf8') as fp:
def down_load(content):
    fp.write(content)






if __name__ == '__main__':
    fp = open('kfc.json','w',encoding='utf8')
    page_start = int(input('请输入起始页：'))
    page_end = int (input('请输入结束页：'))

    for page in range(page_start,page_end+1):
        data = {
            'cname': '深圳',
            'pid': '',
            'pageIndex': page,
            'pageSize': 10
        }
        data = urllib.parse.urlencode(data).encode('utf8')
        respect = create_respect(data)
        content = create_content(respect)
        down_load(content)

