# #
print(['{}*{}={}'.format(i,j,i*j) for i in range(1,10) for j in range(1,i+1)])
for i in range(1,10):
    for j in range(1,i+1):
        print('%d*%d=%d '%(j,i,i*j),end='')
    print()

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
