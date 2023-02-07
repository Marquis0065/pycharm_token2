# #

# 邮件的标题,需要引入email库中header模块中的Header()函数。
# 邮件的内容,需要引入email库中mime模块下text模块中的MIMEText()函数。
# 邮件的发送者、接收者、服务器地址、端口号、账号、密码等，需要引入smtplib，使用SMTP_SSL()函数。
from email.header import Header
from email.mime.text import MIMEText
import smtplib #SMTP协议客户端

# 1定义邮箱服务器地址、端口、发件人账号、密码、收件人账号和邮件标题及邮件内容
host = 'smtp.qq.com'
port = 465
user = '1071255432@qq.com'
password = 'ebskndibyzbrbbfb'
receiver = ['fzh006591@hotmail.com','fzh006591@sohu.com']
title = 'pycharm邮件测式'
text = 'python自动化发送，无需回复'
# 2发送邮件，需要指定邮件正文，通过MIMEtext函数
message = MIMEText(text,'plain','utf-8')
#加入标题，及收件人
message['Subject'] = Header(title,'utf-8')
message['From'] = user
message['To'] = ';'.join(receiver)
#发送邮件
smtp = smtplib.SMTP_SSL(host)
smtp.connect(host,port)
smtp.login(user,password)
#发送，指定发件人账号，收件人账号，内容
smtp.sendmail(user,receiver,message.as_string())
# # 封闭函数
# def auto_picture(io_from, name, io_to, col):
#     '''
#     函数功能：汇总多个工作簿，并绘制拆线图
#     输出：含有拆线图的工作簿
#     io_from ：目标文件夹的地址
#     name:表中的列名，按哪个分组操作
#     io_to:导出工作薄的名称
#     col:
#
#
#     '''
#     import pandas as pd
#     import os
#     import matplotlib.pyplot as plt
#     import xlwings as xw
#
#     # 设置绘图风格
#     plt.style.use('seaborn')
#     # 设置字体为黑色
#     plt.rcParams['font.family'] = 'SimHei'
#     # 显示符号
#     plt.rcParams['axes.unicode_minus'] = False
#
#     df = pd.DataFrame()
#     for i in os.listdir(r'{}'.format(io_from)):
#
#         if i.startswith('~$'):
#             continue
#         data = pd.read_excel(r"{}\{}".format(io_from, i))
#         #         df1 = data.groupby('产品名称').agg({name:sum})
#         df1 = data.groupby(name).agg({col: sum})
#         df1.columns = [i.split('.')[0]]
#         df = pd.concat([df, df1], axis=1)
#     df.to_excel("半年{}.xlsx".format(io_to))
#     fig = plt.figure(figsize=(8, 5))
#     for i in df.index:
#         plt.plot(df.columns, df.loc[i], marker='v')
#     plt.title('产品半年统计表_{}'.format(io_to))
#     plt.xlabel('月份')
#     plt.ylabel(col)
#     plt.legend(df.index)
#
#     # 把图形插入到表格中
#
#     app = xw.App(visible=False, add_book=False)
#     book = app.books.open("半年{}.xlsx".format(io_to))
#     sheet = book.sheets[0]
#     # 插入图片，需要指定位置，left ,top
#     sheet.pictures.add(fig, left=0, top=89)
#     book.save()
#     book.close()
#     app.quit()
# auto_picture("C:\Data\Jupyter_file\Python数据清洗基础\办公自动化\汇总多个工作簿数据\销售统计",
#             '产品名称','利润表_4','销售利润（元）')
# from  requests_html import HTMLSession
# import pandas as pd
# s = HTMLSession()
# url = 'https://sz.lianjia.com/zufang/futianqu/pg1rt200600000001l1/#contentList'
#
# response = s.get(url)
# print(response.status_code)
# price = response.html.xpath('//em/text()')[:-2]
# print(price)
# s_price = pd.Series(price)
# price(s_price)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from pyecharts.charts import Bar
import seaborn as sns

# sns.set_theme(style="whitegrid")
#
# # Load the example planets dataset
# planets = sns.load_dataset("planets")
#
# cmap = sns.cubehelix_palette(rot=-.2, as_cmap=True)
# g = sns.relplot(
#     data=planets,
#     x="distance", y="orbital_period",
#     hue="year", size="mass",
#     palette=cmap, sizes=(10, 200),
# )
# g.set(xscale="log", yscale="log")
# g.ax.xaxis.grid(True, "minor", linewidth=.25)
# g.ax.yaxis.grid(True, "minor", linewidth=.25)
# g.despine(left=True, bottom=True)
# bar = Bar()
# bar.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
# bar.add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
# bar.add_yaxis("商家B", [7, 10, 46, 20, 65, 95])
# # bar.render_notebook()
# # bar.show_config()
# bar.render('bar.html')
# # np.random.seed(1)
# data1 = {"x":["201{}".format(i) for i in range(10)],
#         "y":np.random.randint(2000,5000,10)}
# np.random.seed(2)
# data2 = {"x":["201{}".format(i) for i in range(10)],
#         "y":np.random.randint(2000,5000,10)}
# plt.plot(data1['x'],data1['y'])
# plt.figure()
# plt.plot(data1['x'],data1['y'])
# plt.show()
# se1 = pd.Series([1,3,3,4,5],index=list('abcde'),dtype='int32',name='age')
# print(type(se1))
# print(se1)
# arr = np.array([i for i in range(10)])
# print(arr)
# print(['{}*{}={}'.format(i,j,i*j) for i in range(1,10) for j in range(1,i+1)])
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('%d*%d=%d '%(j,i,i*j),end='')
#     print()

# import pymysql
#
# con = pymysql.connect(host='127.0.0.1',user='root',password='1qaz@WSX',database='cda')
# cur = con.cursor()
# sql = 'select * from dept'
# result = cur.execute(sql)
# print(result)
# for i in cur.fetchall():
#     print(i)
# con.close()





# print(type(i for i in 'adfdfdfdafd'))
# print([i for i in 'afdfdfdfdf'])
# print((i for i in 'afdfd888fdfdf'))
# print(list(i for i in 'afdfdfdfdf'))



# def h():
#     print("你好")
#     yield 5
#     print("再见")
#     yield 6
#     yield 7
# g = h()
#
# print('----------------')
# for i in g:
#     print('111111111111111111111111')
#     print(i)
#     print('t',end='--')
#
# for i in g:
#     print('22222222222222222222222222')
#     print('ttst',end='==')
# print(g)
# print(list(g))









# print('abcd\\ef')
# print('abcd\bef')
# print('abcd\aef')
# print('abcd\vef')
# print('abcd\tef')
# print('abcd\ref')
# print('abcd'.split())


# print({i:j for i,j in enumerate('abcdef')})
# print(i for i in 'abcdefg')
# print(list(i for i in 'abcdef'))
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('{} * {} = {}'.format(i,j,i*j),end='  ')
#     print()
# print(1,2,3,end='\t')
# print(4,5,6,end='\n')
# print('asdfg\nss', end='\n')
# print('hello,world')






# def g():
#     a = 1
#     while True:
#         yield a
#         a += 1
# a = g()
# print(next(g()))
# print(next(g()))
# print(next(g()))
# print(next(a),next(a),next(a))
# print(next(g()),next(g()),next(g()),next(g()))




# print([lambda x:x*i for i in range(10)])
# print([i for i in range(5)])
# print({i for i in range(5)})
# fun_1 = [lambda x:i for i in range(5)]
# print(fun_1)
# print(fun_1)
# prices = {
#     'AAPL': 191.88,
#     'GOOG': 1186.96,
#     'IBM': 149.24,
#     'ORCL': 48.44,
#     'ACN': 166.89,
#     'FB': 208.09,
#     'SYMC': 21.29
# }
# print({key:prices[key] for key in prices if prices[key] > 100})
# for key,value in prices.items():
#     print(key,value)






# print({i:x for x,i in enumerate('12345')})
# print({i for i in enumerate('10')})
# generator_demo1 = (x*x for x in range(5))
# print(generator_demo1)
# print(list(generator_demo1))
#
# print(type([i for i in range(10)]))
# print(type(x for x in range(6)))
# print(type((x for x in range(6))))

from bs4 import *
# def add(x,y):
#     return x+y
# print(add(1,2))
# import sum_
# print(sum_.sum_(1,2,3))
#
#
# tup = (1,2,3,4,5,6)
# a,b,c,d,e,f = tup
# print(a,b)














# import tkinter as tk
# class GameOjbect(object):
#     def __init__(self,canvas,item):
#         self.canvas = canvas
#         self.item= item
#     #删除方法
#     def delete(self):
#         self.canvas.delete(self.item)
#     #得到对象的坐标
#     def get_coords(self):
#         return self.canvas.coords(self.item)
#     #对象移动
#     def move(self,x,y):
#         self.canvas.move(self.item,x,y)
#
#
# class Racket(GameOjbect):
#     def __init__(self,canvas,x,y):
#         item = canvas.create_rectangle(x,y,x+90,y+10,fill= 'green')
#         super().__init__(canvas,item)
#
#     def draw(self,offset):
#         pos = self.get_coords()
#         width = self.canvas.winfo_width()
#         #当弹板在画布内时，按给定偏移量移动
#         if pos[0]+offset >= 0 and pos[2]+offset <= width:
#             super().move(offset,0)
#
# class Ball(GameOjbect):
#     def __init__(self,canvas,x,y):
#         self.direction = [1,-1]
#         self.speed = 10
#         item = canvas.create_oval(x,y,x+20,y+20,fill = 'blue')
#         super().__init__(canvas,item)
#
#     #绘制弹球
#     def draw(self):
#         pos = self.get_coords()
#         self.canvas_width= self.canvas.winfo_width()
#         #方向判断
#         if pos[1] <= 0:
#             self.direction[1] *= -1
#         if game.hit_racket():
#             self.direction[1] *= -1
#         if pos[0] <= 0 and pos[2] >= self.canvas_width:
#             self.direction[0] *= -1
#         #偏移量
#         x = self.direction[0] * self.speed
#         y = self.direction[1] * self.speed
#         self.move(x,y)
#
# #游戏类,定义完整过程
# class Game(tk.Frame):
#     def __init__(self,master):
#         super().__init__(master)
#         self.lives = 3
#         self.scores = 0
#         self.width = 800
#         self.height = 600
#         #设置画版放置
#         self.canvas = tk.Canvas(self,bg='#f8c26c',width=self.width,height= self.height)
#         self.canvas.pack()
#         self.pack()
#         self.ball = None
#         self.lives_text = None
#         self.scores_text = None
#         #初始化弹版
#         self.racket = Racket(self.canvas,self.width/2-45,480)
#         self.setup_game()
#         #将键盘焦点转移到画布组件上
#         self.canvas.focus_set()
#         #将键盘左右键与弹版左右移动函数绑定在一起
#         self.canvas.bind('<KeyPress-Left>',lambda turn_left:self.racket.draw(-20))
#         self.canvas.bind('<KeyPress-Right>',lambda turn_right:self.racket.draw(20))
#     #加载游戏
#     def setup_game(self):
#         #将球设置在弹板中间的位置的上方
#         self.reset_ball()
#         self.update_lives_text()
#         self.update_scores_text()
#         self.text = self.canvas.create_text(400,200,text='单击左键开始游戏',font=('Helvetica',36))
#         self.canvas.bind('<Button-1>',lambda start_game:self.start_game())
#     #在游戏预置时添加弹球，弹球在弹板中间位置上方
#     def reset_ball(self):
#         if self.ball != None:
#             self.ball.delete()
#         racket_pos = self.racket.get_coords()
#         x = (racket_pos[0]+racket_pos[2]) * 0.5-10
#         self.ball = Ball(self.canvas,x,350)
#
#     #更新生命的数字
#     def update_lives_text(self):
#         text = '生命:%s'% self.lives
#         if self.lives_text is None:
#             self.lives_text = self.canvas.create_text(60,30,text = text,
#                                                       font = ('Helvetica',16),fill= 'green')
#         else:
#             self.canvas.itemconfig(self.lives_text,text=text)
#     #更新得分数字
#     def update_scores_text(self):
#         text = '得分:%s'% self.scores
#         if self.scores_text is None:
#             self.scores_text = self.canvas.create_text(60, 60, text=text,
#                                                       font=('Helvetica', 16), fill='green')
#         else:
#             self.scores = self.scores +1
#             text = '得分:%s'% self.scores
#             self.canvas.itemconfig(self.scores_text, text=text)
#     #开始游戏
#     def start_game(self):
#        self.canvas.unbind('<Button-1>')
#        self.reset_score()
#        self.canvas.delete(self.text)
#        self.game_loop()
#
#     #重置得分为零
#     def reset_score(self):
#         self.scores = 0
#         text =  '得分:%s'% self.scores
#         self.canvas.itemconfig(self.scores_text, text=text)
#     #游戏循环
#     def game_loop(self):
#         if self.ball.get_coords()[3] >= self.height:
#             self.ball.speed = 0
#             self.lives -= 1
#             #小于零 ,游戏结束
#             if self.lives < 0:
#                 self.canvas.create_text(400,200,text='游戏结束',
#                 font = ('Helvetica',36),fill='red')
#             else:
#                 self.scores = self.scores -1
#                 self.after(1000,self.setup_game)
#         else:
#             self.ball.draw()
#             self.after(50,self.game_loop())
#
#     #每碰撞一次，更新一次得分
#     def hit_racket(self):
#         ball_pos = self.ball.get_coords()
#         racket_pos = self.racket.get_coords()
#         if ball_pos[2] >= racket_pos[0] and ball_pos[0] <= racket_pos[2]:
#             if ball_pos[3] >= racket_pos[1] and ball_pos[3] <= racket_pos[3]:
#                 self.update_scores_text()
#                 return True
#         return False
#
# if __name__=='__main__':
#     root = tk.Tk()
#     root.title('弹球游戏')
#     #窗口大小不可改变
#     root.resizable(0,0)
#     #窗口总是显示在最前面
#     root.wm_attributes("-topmost",1)
#     game = Game(root)
#     game.mainloop()
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# # import random
# # ran = random.randint(1,100)
# # print(ran)
# # # cho = random.choice([1,3,2,2,5,5])
# # # print(cho)
# # # while True:
# # #     throw_1 = random.randint(1,6)
# # #     throw_2 = random.randint(1,6)
# # #     total = throw_1+throw_2
# # #     print(total)
# # #     if throw_2 == 6 and  throw_1 ==6:
# # #         break
# # # print('两个六')
# #
# # ls = [1,3,2,2,5,5]
# # print(ls[1:3])
# # print(ls+ls)
# # ls.sort()
# # print(ls)
# # print(ls[-6])
# # def get_guess(word):
# #     return 'a'
# #
# # def process_guess(guess,work):
# #     global lives_remaining
# #     lives_remaining = lives_remaining - 1
# #     return False
# #
# # x = 'abc'.center(10,'-')
# # print(x)
# # x2 = x.splitlines()
# # print(x2)
# # y = ['1','2','3']
# # # y2 = int(y)
# # print(y)
# # # print(y2)
# # import lianjia
# # print(lianjia.result)
# # import pygame
# # print(type('abc'))
# # cc = str(3333)
# import requests
# import urllib.request
# # url = 'https://pic.rmb.bdstatic.com/bjh/down/336fadf70477f381057be1fe137cf938.jpeg'
# # con = requests.get(url)
# # con.encoding = 'utf8'
# # print(con.text)
# # urllib.request.urlretrieve(url,'pic.jpg')
# from    PIL import Image
# import pytesseract
# import re
# import os
# # image = Image.open(r'pic.jpg')
# # text = pytesseract.image_to_string(Image,lang='chi_sim')
# # file = open('./imag_test.txt',mode='w')
# # file.writelines(text)
# # file.close()
#
# # file = './pic.jpg'
# # image = Image.open(file)
# # result = pytesseract.image_to_string(image,lang='chi_sim')
#
#
#
# # from cnocr import CnOcr
# # file = './pic.jpg'
# # ocr = CnOcr()
# # result = ocr.ocr(file)
# # print(f'Predicted Chars:{result}')
