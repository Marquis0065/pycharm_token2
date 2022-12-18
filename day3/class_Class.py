# @Time: 2022/12/16 13:40

class SclaleConverter:
    def __init__(self,unfrom ,unto,factor):
        self.unfrom = unfrom
        self.unto = unto
        self.factor = factor
    def describe(self):
        return 'Convert'+self.unfrom+'to'+self.unto
    def convert(self,value):
        return value * self.factor

c1 = SclaleConverter('inches','mm',25)
print(c1.describe())
print('converting 2 inches')
print(str(c1.convert(2))+c1.unto)
f =open('C:\\Users\\fzh00\\PycharmProjects\\pythonProject1\\day3\\dangdang\\dangdang\\spiders\\book.json',encoding='utf8')
f.close()
import glob
glob.glob('*.txt')
from tkinter import *
root = Tk()
Label(root,text='hello,world').pack()
root.mainloop()
