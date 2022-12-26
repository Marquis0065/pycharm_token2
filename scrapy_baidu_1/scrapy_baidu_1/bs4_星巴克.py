# @Time: 2022/12/25 11:52
from bs4 import BeautifulSoup
import requests
import urllib

url = 'https://sz.lianjia.com/zufang/futianqu/l1/'
response = requests.get(url)
soup = BeautifulSoup(response.text,'lxml')

obj = soup.select('em')
data=[]
for i in obj:
    d=i.string
    data.append(d)

print(data)
import numpy as np
arr = np.array(data)
# arr2 = ''.join(arr)
# print(arr2)
int_list = [i for i in data ]
print(int_list)
s = 'a29ffee1702b41dba5e31ed39688e52c'
print(s.encode(s))

