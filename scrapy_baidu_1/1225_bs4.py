# @Time: 2022/12/25 11:01
from bs4 import BeautifulSoup
import requests
url = 'http://www.baidu.com'
response = requests.get(url)
print(response.status_code)
# with open('baidu.html','w',encoding='utf8')as f:
#     f.write(response.text)
soup = BeautifulSoup(open('baidu.html',encoding='utf8'),'lxml')
print(soup)
#第一个标签a
print(soup.a)
#标签属性和属性值
print(soup.a.attts)

# print('push test test')
# import requests
# from lxml import etree
#
# # url = https://sz.lianjia.com/zufang/nanshanqu/pg2rt200600000001l1/#contentList
# base_url = 'https://sz.lianjia.com/zufang/nanshanqu/pg'
# fp = open('price1219.text', 'w', encoding='utf8')
# for i in range(2):
#     url = base_url + str(i) + 'rt200600000001l1/#contentList'
#     response = requests.get(url)
#     price = etree.HTML(response.text).xpath('//em/text()')
#     fp.write(str(price))
#     fp.write('\n')
# fp.close()

# response = requests.get(url)
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(response.text,'lxml')
# price_list = soup.find_all('em')
#bs4的一些函数
# 1,find
#     print(soup.find('a')) #返回每一个符合条件的数据
#     print(soup.find('a',title='t2'))
# 2,find_all #返回所有的标签 ,多个标签需放在列表内
#     print(soup.find_all(['a','span']))
#     print(soup.find_all('li',limit=2)) #查找前几个标签数据
# 3,select
#     一,print(soup.select('a')) #返回多个标签内容，返回一个列表
#     二,print(soup.select('.a1')) #找类标签 class='a1',类选择器
#     三,print(soup.select('#l1'))#id 选择器，id='l1'
#     四,print(soup.select('li[id]')) #查找li中有id的属性，属性选择器
#         print(soup.select('li[id='l2']'))
#     五，层级选择器
#         print(soup.select('div li'))#后代选择器，div 中全部li
#         print(soup.select('div > ul > li'))#子代选择器，标签的第一级子标签,其它语言空格中必需的
#         print(soup.select('a li'))#所有a,li标签
# 节点信息：
#     1,获取节点内容，适用于标签中嵌套结构
#     obj = soup.select('#d1')
#     #如果标签对象中只有内容 ，string 和get_test()用法相同
#     如果内容中还有其它标签，只能用get_text()
#     print(soup.select('#d1')[0].string)
#     print(soup.select('#d1')[0].get_text())
#     2,节点属性
#     print(soup.select(#p1)[0].name) #name是标签的名字
#     print(soup.select(#p1)[0].attrs)#将属性值作为字典返回
#     3,获取节点属性
#         print(soup.select('#p1')[0].attrs.get('class'))#获取字典的数据
#         print(obj.get('class'))
#         print(obj['class'])三种方式都可以











