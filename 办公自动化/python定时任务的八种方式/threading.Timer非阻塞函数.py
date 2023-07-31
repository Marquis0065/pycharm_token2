# @Time: 2023/7/30 21:02
# _*_coding : utf-8 _*_
# @Authon : 
# @File : threading.Timer非阻塞函数
import datetime
import time
from threading import Timer
import threading
import telebot

bot = telebot.TeleBot("6377312623:AAGz3ZSMVswWq0QVlihRPklw8b7skSBP16Y")
def job():
    bot.send_message(-677235937, '利用threading.Timer实现定时任务{}'.format(datetime.datetime.now().strftime('%H:%M')))
    # now = datetime.datetime.now()
    # ts = now.strftime('%H:%M')
    # return ts

while True:
    t = threading.Timer(120, job)
    t.start()
    t.join()
    time.sleep(60)


# def loop_moitor():
#     t = Timer(120,time_printer)
#     t.start()
#
# while 1:
#     loop_moitor()
#     time.sleep(300)