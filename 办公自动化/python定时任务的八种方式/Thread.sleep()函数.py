# @Time: 2023/7/31 21:35
# _*_coding : utf-8 _*_
# @Authon : 
# @File : Thread.sleep()函数
import datetime
import time
import threading
import telebot

bot = telebot.TeleBot("6377312623:AAGz3ZSMVswWq0QVlihRPklw8b7skSBP16Y")


def job():
    bot.send_message(-677235937, 'thread.sleep():实现定时任务{}'.format(datetime.datetime.now().strftime('%H:%M')))

while True:
    threading.Thread(target=job).start()
    time.sleep(180)  # 等待10秒后继续执行下一次任务