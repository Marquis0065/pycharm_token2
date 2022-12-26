# import random
# ran = random.randint(1,100)
# print(ran)
# # cho = random.choice([1,3,2,2,5,5])
# # print(cho)
# # while True:
# #     throw_1 = random.randint(1,6)
# #     throw_2 = random.randint(1,6)
# #     total = throw_1+throw_2
# #     print(total)
# #     if throw_2 == 6 and  throw_1 ==6:
# #         break
# # print('两个六')
#
# ls = [1,3,2,2,5,5]
# print(ls[1:3])
# print(ls+ls)
# ls.sort()
# print(ls)
# print(ls[-6])
# def get_guess(word):
#     return 'a'
#
# def process_guess(guess,work):
#     global lives_remaining
#     lives_remaining = lives_remaining - 1
#     return False
#
# x = 'abc'.center(10,'-')
# print(x)
# x2 = x.splitlines()
# print(x2)
# y = ['1','2','3']
# # y2 = int(y)
# print(y)
# # print(y2)
# import lianjia
# print(lianjia.result)
# import pygame
# print(type('abc'))
# cc = str(3333)
import requests
import urllib.request
# url = 'https://pic.rmb.bdstatic.com/bjh/down/336fadf70477f381057be1fe137cf938.jpeg'
# con = requests.get(url)
# con.encoding = 'utf8'
# print(con.text)
# urllib.request.urlretrieve(url,'pic.jpg')
from    PIL import Image
import pytesseract
import re
import os
# image = Image.open(r'pic.jpg')
# text = pytesseract.image_to_string(Image,lang='chi_sim')
# file = open('./imag_test.txt',mode='w')
# file.writelines(text)
# file.close()

file = './pic.jpg'
image = Image.open(file)
result = pytesseract.image_to_string(image,lang='chi_sim')



# from cnocr import CnOcr
# file = './pic.jpg'
# ocr = CnOcr()
# result = ocr.ocr(file)
# print(f'Predicted Chars:{result}')
